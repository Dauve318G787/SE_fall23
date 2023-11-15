#--------------------------------------
# This module accepts a URL, number of requests to make, and a delay timer.
# If the response from the GET request is succesfull, this module returns the response text
#-------------------------------------

import requests
import time
import json
from . import json_helper

def url_content_dict(url_dict, json_dict):
    with open(json_dict, 'w', encoding='utf-8') as json_file:
        json.dump(url_dict, json_file, indent=2)

    print(f"JSON URL Dict: {json_dict}")
    return json_dict

def download_text(url, max_retries, retry_delay):
    for attempt in range(max_retries):
        try:
            # Send HTTP GET request
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
    
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occured: {str(e)}")
            return None
        
        except Exception as e:
            print(f"An error occured: {str(e)}")
            return None

        if attempt < max_retries -1:
            time.sleep(retry_delay)

    return None

def process_url(url_in, url_out):
    HTML_dict = {}
    try:
        url_json = json_helper.write_json(url_in, url_out)

        if url_json:
            url_dat = json_helper.read_json(url_json)

        if url_dat:
            if isinstance(url_dat, list):
                for entry in url_dat:
                    HTML_dict[entry] = download_text(entry, 20, 0.1)
                    
                return HTML_dict
            
            elif isinstance(url_dat, dict):
                for key, value in url_dat.items():
                    print(f"{key}: {value}")
                    #entry_dict_raw = download_text(entry, 20, 0.1)
                return url_dat
            
            else:
                print("Invalid json")
                return None

    except Exception as e:
        print(f"Error: {e}")
        return None
