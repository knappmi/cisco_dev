from jinja2.environment import Template
from napalm.ios.ios import IOSDriver
import jinja2
from datetime import datetime

class customIOSDriver(IOSDriver):
    
    def get_eigrp_keys(self):
        command = "Show key chain"
        output = self._send_command(command)
        return output
    
    def delete_old_keys(self):
        output = self.get_config()
        command = ''
        for line in output:
            if "accept-lifetime " < str(datetime.now()):
                print(line)
                command = f'key-chain TEST \r no key {line}'
                print(command)
        returned_line = self._send_command(command)
        return returned_line
        
