import napalm
from custom_napalm.ios import customIOSDriver


def main():
    driver = napalm.get_network_driver("ios")
    device = driver(
        hostname= "192.168.99.158",
        username= "admin",
        password= "admin"
    )
    print('Session Opening...')
    device.open()

    print(customIOSDriver.delete_old_keys(device))

    # device.load_merge_candidate(filename="config_file.conf")
    print(device.compare_config())
    device.commit_config()


    print('Session Closing...')
    device.close()

main()