
from SiemplifyAction import SiemplifyAction
from SiemplifyDataModel import EntityTypes
from SiemplifyUtils import unix_now, convert_unixtime_to_datetime, output_handler
from ScriptResult import EXECUTION_STATE_COMPLETED, EXECUTION_STATE_FAILED,EXECUTION_STATE_TIMEDOUT
from SiemplifyDataModel import EntityTypes
from OpenSSL import SSL
from cryptography import x509
from cryptography.x509.oid import NameOID
import idna
import json
from socket import socket
from collections import namedtuple
from datetime import datetime
from urllib.parse import urlparse

INTEGRATION_NAME = u"Tools"
SCRIPT_NAME = u"Cert Handler"
HostInfo = namedtuple(field_names='cert hostname peername', typename='HostInfo')
json_output = {'results': []}

def get_entity_original_identifier(entity):
    return entity.additional_properties.get('OriginalIdentifier', entity.identifier)
    
def get_certificate(hostname, port):
    hostname_idna = idna.encode(hostname)
    sock = socket()

    sock.connect((hostname, port))
    peername = sock.getpeername()
    ctx = SSL.Context(SSL.SSLv23_METHOD) # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(hostname_idna)
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()

    return HostInfo(cert=crypto_cert, peername=peername, hostname=hostname)

def  get_alt_names(cert):
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName)
        return ext.value.get_values_for_type(x509.DNSName)
    except x509.ExtensionNotFound:
        return None

def get_common_name(cert):
    try:
        names = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        return names[0].value
    except x509.ExtensionNotFound:
        return None

def get_issuer(cert):
    try:
        names = cert.issuer.get_attributes_for_oid(NameOID.COMMON_NAME)
        #cmp = cert.issuer.get_components()
        return names[0].value
    except x509.ExtensionNotFound:
        return None


def get_json_result(hostinfo):
    common_name = get_common_name(hostinfo.cert)
    san =get_alt_names(hostinfo.cert),
    issuer = get_issuer(hostinfo.cert)

    now  = datetime.now()
    delta = hostinfo.cert.not_valid_after - now   
    days_to_expiration = delta.days
    is_expired = days_to_expiration < 0 
    is_self_signed = common_name == issuer
    date_time = hostinfo.cert.not_valid_before.strftime("%m/%d/%Y")

    cert_details = {
        'hostname': hostinfo.hostname,
        'ip': hostinfo.peername[0],
        'commonName':common_name,
        'is_self_signed':is_self_signed,
        'SAN': san,
        'is_expired': is_expired,
        'issuer': issuer,
        'not_valid_before': hostinfo.cert.not_valid_before.strftime("%m/%d/%Y"),
        'not_valid_after': hostinfo.cert.not_valid_after.strftime("%m/%d/%Y"),
        'days_to_expiration': days_to_expiration
    }

    return cert_details

@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SCRIPT_NAME
    
    output_message = "Error occurred"
    result_value = "Failure"
    
    suitable_entities = [entity for entity in siemplify.target_entities if entity.entity_type == EntityTypes.URL]

    
    for entity in suitable_entities:
        siemplify.LOGGER.info("Started processing URL: {}".format(get_entity_original_identifier(entity)))
        try:
            host = get_entity_original_identifier(entity)
            host_domain = urlparse(host).netloc
            hostinfo = get_certificate(host_domain, 443)
            json_res = get_json_result(hostinfo)
            output_message = "Url Certificate  was successfully analyzed."
            siemplify.LOGGER.info("Cert for Domain {} retrieved".format(host_domain))
            json_output["results"].append(json_res)
            
        except Exception as e:
            siemplify.LOGGER.error("Error: {}".format(e))        
                
        
        
    siemplify.result.add_result_json(json_output)
    siemplify.end(output_message, result_value)

if __name__ == "__main__":
    main()
