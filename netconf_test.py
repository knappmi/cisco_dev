from ncclient import manager
from ncclient.devices import csr
from pprint import pprint
import logging
import sys

# with manager.connect(host='10.10.20.175', port = 830, username='cisco', password = 'cisco', hostkey_verify=False, device_params = {"name":"csr"}) as m:
#     c = m.get_config(source='running').data_xml
#     with open("%s.xml" % '10.10.20.175', 'w') as f:
#         f.write(c)

# DELETE_WAN_KEYS = """
# <config xmlns='urn:ietf:params:xml:ns:netconf:base:1.0'>
#         <cli-config-data>
#             <cmd>key chain test</cmd>
#             <cmd>no key %s</cmd>
#         </cli-config-data>
# </config>
# """
DELETE_WAN_KEYS = """
<rpc message-id="netconf.mini.edit.3">
   <edit-config>
      <target>
         <running/>
      </target>
      <config>
         <cli-config-data-block>
            key chain test
            no key 1
         </cli-config-data-block>
      </config>
   </edit-config>
</rpc>]]>]]>
"""
#YANG-EXPLORER
def csr_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           device_params={'name': "csr"},
                           timeout=30
            )

def delete_wan_keys(conn, key_num):
    confstr = DELETE_WAN_KEYS % key_num
    rpc_obj = conn.edit_config(target='running', config=confstr)
    _check_response(rpc_obj, "DELETE_WAN_KEYS")

def _check_response(rpc_obj, snippet_name):
    logging.debug("RPCReply for %s is %s" % (snippet_name, rpc_obj.xml))
    xml_str = rpc_obj.xml
    if "<ok />" in xml_str:
        logging.info("%s successful" % snippet_name)
    else:
        logging.error("Cannot successfully execute: %s" % snippet_name)

def my_test(host, user, password):
    with csr_connect(host, port=830, user=user, password=password) as m:
        delete_wan_keys(m, '1')


my_test('10.10.20.175', 'cisco', 'cisco')