import time
import json
import math
from random import random

import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    with open('cpu.jsonl', 'r') as file:
        lines = file.readlines()

    with open('cpu2.jsonl', 'r') as file:
        for count, line in enumerate(file):
            pass

    cpu_list = []

    c = 0

    # Loop through each line and process it
    driver = webdriver.Chrome()
    driver.get("https://www.techpowerup.com/cpu-specs/")
    time.sleep(5)
    for line in lines:
        c = c + 1

        if c < count + 2:
            continue
        json_data = json.loads(line)
        name = json_data["name"]
        if name.startswith("AMD "):
            name = name[4:]  # Remove "AMD"
        elif name.startswith("INTEL "):
            name = name[6:]  # Remove "INTEL"
        driver.find_element(By.XPATH, "//*[@id=\"quicksearch\"]").clear()
        driver.find_element(By.XPATH, "//*[@id=\"quicksearch\"]").send_keys(name)
        time.sleep(0.5)
        socket = "";
        while True:
            try:
                socket = driver.find_element(By.XPATH, "//*[@id=\"ajaxresults\"]/table/tbody/tr/td[5]").text
                break;
            except:
                try:
                    time.sleep(3)
                    if driver.find_element(By.XPATH, "//*[@id=\"ajaxresults\"]").text == "Nothing found.":
                        print("NOOOOOO")
                        socket = ""
                        break
                except:
                    socket = ""
                    break
                socket = ""
        if socket.startswith("Socket "):
            socket = socket[7:]  # Remove Socket
        modified_json_data = line[:-2] + ',"socket":\"' + socket + '\"}\n'
        with open('cpu2.jsonl', 'a') as file:
            # Append data to the file
            print(modified_json_data)
            file.write(modified_json_data)
        time.sleep(random()*20 + 25)
    print("Operation complete")

