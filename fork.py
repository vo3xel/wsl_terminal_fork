import logging
import os
import subprocess

logging.basicConfig(level=logging.DEBUG)

CURRENT_SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))

logging.debug("main script")
for i in range(1,3):
    logging.debug(f"start demo{i}.py script")
    subprocess.Popen(f"cmd.exe /c start cmd.exe /c wsl.exe python3 {CURRENT_SCRIPT_PATH}/demo{i}.py", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
logging.debug("main script ended.")
