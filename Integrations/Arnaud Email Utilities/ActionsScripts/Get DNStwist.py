from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import unix_now, convert_unixtime_to_datetime, output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED,EXECUTION_STATE_TIMEDOUT
import dnstwist


@output_handler
def main():
    siemplify = SiemplifyAction()

    param = siemplify.extract_action_param("parameter", print_value=True)

    status = EXECUTION_STATE_COMPLETED  # used to flag back to siemplify system, the action final status
    output_message = "output message :"  # human readable message, showed in UI as the action result
    result_value = None  # Set a simple result value, used for playbook if\else and placeholders.

    #fuzz = dnstwist.Fuzzer("google.com")
    #fuzz.generate()
    #print(fuzz.domains)
    
    url = dnstwist.UrlParser("google.com") # Returns an object with 'domain', 'fragment', 'full_uri', 'password', 'path', 'port', 'query', 'scheme', 'username'
    #attributes = dir(url)
    #print(attributes)
    print(url.full_uri)
    
    
    
    worker = dnstwist.Scanner(1)
    #worker.setDaemon(True)

    #kill_received = False
    #debug = False

    worker.option_extdns = True
    worker.option_geoip = False
    worker.option_ssdeep = True
    worker.option_banners = True
    worker.option_mxcheck = True

    worker.nameservers = ["1.1.1.1"]
    useragent = "'Mozilla/5.0 dnsrazzle/%s'"

    worker.uri_scheme = url.scheme
    worker.uri_path = url.path
    worker.uri_query = url.query

    worker.domain_init = url.domain
    worker.run()
    #threads.append(worker)


    #siemplify.LOGGER.info("\n  status: {}\n  result_value: {}\n  output_message: {}".format(status,result_value, output_message))
    siemplify.end(output_message, result_value, status)


if __name__ == "__main__":
    main()



