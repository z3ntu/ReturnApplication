from __future__ import print_function
from time import sleep

import sys
import os
import requests
import subprocess
import logging

if sys.version_info >= (3, 0):
    print("Python 3")
    import configparser
else:
    print("Python 2")
    import ConfigParser

def works_again(batch_success_again):
    print("Works again.")
    logging.warning("Works again.")
    if os.path.isfile(batch_success_again):
        subprocess.call(batch_success_again)
    else:
        print("Not calling binary because it was not found: " + batch_success_again)

def fail(batch_fail):
    if last_status != "1":
        print("Fail!")
        logging.error("Failed!")
        if os.path.isfile(batch_fail):
            subprocess.call(batch_fail)
        else:
            print("Not calling binary because it was not found: " + batch_fail)
    else:
        print("Fail but not calling script")

def main():
    if sys.version_info >= (3, 0):
        # Python 3
        config = configparser.ConfigParser()
        config.read('config.ini')
        delay = int(config['DEFAULT']['delay'])
        batch_success_again = config['DEFAULT']['batch_success_again']
        url = config['DEFAULT']['url']
        batch_fail = config['DEFAULT']['batch_fail']
    else:
        # Python 2
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        delay = int(config.get("DEFAULT", "delay"))
        batch_success_again = config.get("DEFAULT", "batch_success_again")
        url = config.get("DEFAULT", "url")
        batch_fail = config.get("DEFAULT", "batch_fail")
    last_status = "0"
    logging.warning("Started.")
    if os.path.isfile(batch_success_again):
        subprocess.call(batch_success_again)
    else:
        print("Not calling binary because it was not found: " + batch_success_again)

    # Main loop
    while True:
        try:
            # get status
            response = requests.get(url)
            # trim output
            status = response.text.replace("\n", "")
        except Exception as e:
            print("Exception while getting the status. Treating as fail.")
            print(e)
            status = 1
        # check current status
        if status == "1":  # fail
            fail(batch_fail)
        elif last_status == "1":  # success again
            works_again(batch_success_again)
        else:
            print("Works.")
        # save current status for next iteration
        last_status = status
        # sleep for specificed duration
        sleep(delay)


if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.WARNING, format='%(asctime)s %(message)s')
    main()
