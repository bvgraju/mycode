#!/usr/bin/env python3

""" This makes the call to http://api.open-notify.org/astros.json
    to get list of astronauts in space in JSON format and coverts 
    it to list and prints
"""
import requests

astro_api = "http://api.open-notify.org/astros.json"

def main():
    astro_json = requests.get(astro_api)
    print("No of People in Space: ", astro_json.json()["number"])
    for x in astro_json.json()["people"]:
        print(x["name"], " is on the space station ", x["craft"])

if __name__ == "__main__":
    main()

