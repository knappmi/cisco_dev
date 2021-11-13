from datetime import *
from netmiko import ConnectHandler

class CustomNetmiko:
    def Delete_Wan_Keys(self):
        
        # Dictionary for month to int conversion
        mon_dict = {
            'Jan' : '01',
            'Feb' : '02',
            'Mar' : '03',
            'Apr' : '04',
            'May' : '05',
            'Jun' : '06',
            'Jul' : '07',
            'Aug' : '08',
            'Sep' : '09',
            'Oct' : '10',
            'Nov' : '11',
            'Dec' : '12'
        }
        
        # Specify Netmiko connection with kwargs unpacked
        ssh = ConnectHandler(**self)
        ssh.enable()

        # Show the key chain we want to delete from
        output = ssh.send_command('Sh key chain TEST')

        # collect the keys from the output and break it down to the individual keys.
        keys = output.splitlines()
        key1 = keys[1:5]

        # Define todays date for later comparsion
        todaysDate = datetime.now()

        # Take the accepted date from the key we pulled
        acceptDate = key1[2]

        # Parse the parts of the key to get just the date
        parseDate = acceptDate.split()
        testDate = parseDate[10:13]

        # Take the string and assign the corresponsing int to variable 'month'
        mon_str = testDate[0]
        month = mon_dict[mon_str]

        # Assign day and year to variables
        day = testDate[1]
        year = testDate[2].split(')')

        # Conditional to check if the key is older than today's date (i.e end date of the accept date has passed)
        keyDate = datetime(month=int(month), day=int(day), year=int(year[0]))
        if keyDate < todaysDate:
            key_list = key1[0]
            key_string = str(key1[0])
            key_strip = key_string.split('--')
            print(f'deleting {key_strip[0]}')
            ssh.send_command(f'no {key_strip[0]}')
            print('success')