#!/usr/bin/env python3

import base64
import json
import re
import subprocess

import requests

imds_server_base_url = "http://169.254.169.254"

instance_api_version = "2021-02-01"
instance_endpoint = imds_server_base_url + \
    "/metadata/instance?api-version=" + instance_api_version

attested_api_version = "2021-02-01"
attested_nonce = "1234576"
attested_endpoint = imds_server_base_url + "/metadata/attested/document?api-version=" + \
    attested_api_version + "&nonce=" + attested_nonce

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


def pretty_print_json_obj_to_terminal(json_obj):
    print(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': ')))


if __name__ == "__main__":
    main()
