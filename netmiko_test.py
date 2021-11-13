from netmiko import *
from datetime import *
from custom_netmiko.ios import CustomNetmiko
device = {
    'device_type' : 'cisco_ios',
    'host' : '192.168.99.158',
    'username' : 'admin',
    'password' : 'admin'
}

CustomNetmiko.Delete_Wan_Keys(device)
