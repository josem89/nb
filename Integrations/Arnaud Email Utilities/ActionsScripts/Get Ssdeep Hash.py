from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import unix_now, convert_unixtime_to_datetime, output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED,EXECUTION_STATE_TIMEDOUT
import pyssdeep

@output_handler
def main():
    siemplify = SiemplifyAction()

    string_to_hash = siemplify.extract_action_param("String to Hash", print_value=True)

    status = EXECUTION_STATE_COMPLETED  # used to flag back to siemplify system, the action final status
    output_message = "Failed to create hash"
    result_value = "Failure"

    try:
        result = pyssdeep.get_hash_buffer(string_to_hash)
    except pyssdeep.FuzzyHashError as err:
        siemplify.LOGGER.error(err)
    except TypeError as err:
        siemplify.LOGGER.error(err)
    siemplify.LOGGER.info("Hash: {}".format(result))
    
    result_value = "Success"
    output_message = "Successfully created hash {}".format(result)

    siemplify.end(output_message, result_value, status)

if __name__ == "__main__":
    main()
