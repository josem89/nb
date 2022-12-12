from SiemplifyUtils import output_handler, unix_now
from SiemplifyConnectors import SiemplifyConnectorExecution
from TIPCommon import extract_connector_param
from constants import DEFAULT_TIME_FRAME, DEFAULT_LIMIT, EVENTS_DEFAULT_LIMIT
from UtilsManager import read_ids, write_ids, get_last_success_time, is_approaching_timeout, \
    get_environment_common, is_overflowed, save_timestamp, pass_whitelist_filter, UNIX_FORMAT
from VirusTotalManager import VirusTotalManager
from SiemplifyConnectorsDataModel import AlertInfo
import sys

connector_starting_time = unix_now()
CONNECTOR_NAME = "Livehunt Notifications Connector"


@output_handler
def main(is_test_run):
    siemplify = SiemplifyConnectorExecution()
    siemplify.script_name = CONNECTOR_NAME
    processed_alerts = []

    if is_test_run:
        siemplify.LOGGER.info("***** This is an \"IDE Play Button\"\\\"Run Connector once\" test run ******")

    siemplify.LOGGER.info("------------------- Main - Param Init -------------------")

    api_key = extract_connector_param(siemplify, param_name="API Key", is_mandatory=True)
    verify_ssl = extract_connector_param(siemplify, param_name="Verify SSL", input_type=bool, print_value=True)

    environment_field_name = extract_connector_param(siemplify, param_name="Environment Field Name", print_value=True)
    environment_regex_pattern = extract_connector_param(siemplify, param_name="Environment Regex Pattern",
                                                        print_value=True)

    script_timeout = extract_connector_param(siemplify, param_name="PythonProcessTimeout", is_mandatory=True,
                                             input_type=int, print_value=True)

    hours_backwards = extract_connector_param(siemplify, param_name="Max Hours Backwards", input_type=int,
                                              default_value=DEFAULT_TIME_FRAME, print_value=True)
    fetch_limit = extract_connector_param(siemplify, param_name="Max Alerts Per Cycle", input_type=int,
                                          is_mandatory=True, default_value=DEFAULT_LIMIT, print_value=True)

    whitelist_as_a_blacklist = extract_connector_param(siemplify, "Use whitelist as a blacklist", is_mandatory=True,
                                                       input_type=bool, print_value=True)
    device_product_field = extract_connector_param(siemplify, "DeviceProductField", is_mandatory=True)

    try:
        siemplify.LOGGER.info("------------------- Main - Started -------------------")

        if fetch_limit < 0:
            siemplify.LOGGER.info(f"\"Max Alerts Per Cycle\" must be non-negative. The default value "
                                  f"{DEFAULT_LIMIT} will be used")
            fetch_limit = DEFAULT_LIMIT

        if hours_backwards < 0:
            siemplify.LOGGER.info(f"\"Max Hours Backwards\" must be non-negative. The default value "
                                  f"{DEFAULT_TIME_FRAME} will be used")
            hours_backwards = DEFAULT_TIME_FRAME

        # Read already existing alerts ids
        existing_ids = read_ids(siemplify)
        siemplify.LOGGER.info(f"Successfully loaded {len(existing_ids)} existing ids")

        manager = VirusTotalManager(api_key=api_key, verify_ssl=verify_ssl, siemplify_logger=siemplify.LOGGER)

        fetched_alerts = []
        filtered_alerts = manager.get_livehunt_notifications(
            existing_ids=existing_ids,
            limit=fetch_limit,
            start_timestamp=int(
                get_last_success_time(siemplify=siemplify, offset_with_metric={"hours": hours_backwards},
                                      time_format=UNIX_FORMAT) / 1000)
        )

        siemplify.LOGGER.info(f"Fetched {len(filtered_alerts)} alerts")

        if is_test_run:
            siemplify.LOGGER.info("This is a TEST run. Only 1 alert will be processed.")
            filtered_alerts = filtered_alerts[:1]

        for alert in filtered_alerts:
            try:
                if is_approaching_timeout(script_timeout, connector_starting_time):
                    siemplify.LOGGER.info("Timeout is approaching. Connector will gracefully exit")
                    break

                if len(processed_alerts) >= fetch_limit:
                    # Provide slicing for the alerts amount.
                    siemplify.LOGGER.info(
                        "Reached max number of alerts cycle. No more alerts will be processed in this cycle."
                    )
                    break

                siemplify.LOGGER.info(f"Started processing alert {alert.notification_id}")

                # Update existing alerts
                existing_ids.append(alert.notification_id)
                fetched_alerts.append(alert)

                if not pass_filters(siemplify, whitelist_as_a_blacklist, alert, "rule_name"):
                    continue

                # Update existing alerts
                alert_info = alert.get_alert_info(
                    AlertInfo(),
                    get_environment_common(siemplify, environment_field_name, environment_regex_pattern)
                )

                if is_overflowed(siemplify, alert_info, is_test_run):
                    siemplify.LOGGER.info(
                        f"{alert_info.rule_generator}-{alert_info.ticket_id}-{alert_info.environment}"
                        f"-{alert_info.device_product} found as overflow alert. Skipping...")
                    # If is overflowed we should skip
                    continue

                processed_alerts.append(alert_info)
                siemplify.LOGGER.info(f"Alert {alert.notification_id} was created with date {alert.date}.")

            except Exception as e:
                siemplify.LOGGER.error(f"Failed to process alert {alert.notification_id}")
                siemplify.LOGGER.exception(e)

                if is_test_run:
                    raise

            siemplify.LOGGER.info(f"Finished processing alert {alert.notification_id}")

        if not is_test_run:
            siemplify.LOGGER.info("Saving existing ids.")
            write_ids(siemplify, existing_ids)
            save_timestamp(siemplify=siemplify, alerts=fetched_alerts, timestamp_key="date")

        siemplify.LOGGER.info(f"Alerts processed: {len(processed_alerts)} out of {len(fetched_alerts)}")

    except Exception as e:
        siemplify.LOGGER.error(f"Got exception on main handler. Error: {e}")
        siemplify.LOGGER.exception(e)

        if is_test_run:
            raise

    siemplify.LOGGER.info(f"Created total of {len(processed_alerts)} cases")
    siemplify.LOGGER.info("------------------- Main - Finished -------------------")
    siemplify.return_package(processed_alerts)


def pass_filters(siemplify, whitelist_as_a_blacklist, alert, model_key, organization_filter_key=None,
                 target_organizations=None, severity_filter_key=None, min_severity=None):
    # All alert filters should be checked here
    return True


if __name__ == "__main__":
    # Connectors are run in iterations. The interval is configurable from the ConnectorsScreen UI.
    is_test = not (len(sys.argv) < 2 or sys.argv[1] == "True")
    main(is_test)
