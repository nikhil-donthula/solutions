#!/usr/bin/env python3

import base64
import json
import re
import subprocess
import sys

import requests

imds_server_base_url = "http://169.254.169.254"

instance_api_version = "2021-02-01"
instance_endpoint = imds_server_base_url + \
    "/metadata/instance?api-version=" + instance_api_version


# Proxies must be bypassed when calling Azure IMDS
proxies = {
    "http": None,
    "https": None
}


def api_call(endpoint):
    headers = {'Metadata': 'True'}
    json_obj = requests.get(endpoint, headers=headers, proxies=proxies).json()
    return json_obj


def main():
    # Instance provider API call
    instance_json = api_call(instance_endpoint)
    print("Instance provider data:")
    pretty_print_json_obj_to_terminal(instance_json)

    key = sys.argv[1] #"sample_key_for_now"
    value =  get_value(instance_json, key)
    if value is not None:
        print(f"The value for key '{key}' is: {value}")
    else:
         print(f"Key '{key}' not found in the JSON data.")


def pretty_print_json_obj_to_terminal(json_obj):
    print(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': ')))


def get_value(json_data, key):
  if isinstance(json_data, dict):    
    if key in json_data:
      return json_data[key]
    
    for value in json_data.values():
      
      result = get_value(value, key)
      if result is not None:
        return result
  elif isinstance(json_data, list):  
    for item in json_data: 
      result = get_value(item, key)
      if result is not None:
        return result
  return None

if __name__ == "__main__":
    main()




#sample command : python3 sam.py location