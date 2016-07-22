from time import sleep

import requests
import subprocess
import config
import logging


def main():
    last_status = "0"
    logging.warning("Started.")
    # subprocess.call(config.batch_success_again)
    while True:
        response = requests.get(config.url)
        status = response.text.replace("\n", "")
        if status == "1":  # fail
            if last_status != "1":
                print("Fail!")
                logging.error("Failed!")
                # subprocess.call(config.batch_fail)
            else:
                print("Fail but not calling script")
        elif last_status == "1":  # success again
            print("Works again.")
            logging.warning("Works again.")
            # subprocess.call(config.batch_success_again)
        else:
            print("Works.")
        last_status = status
        sleep(config.delay)


if __name__ == '__main__':
    logging.basicConfig(filename='logging.log', level=logging.WARNING, format='%(asctime)s %(message)s')
    main()
