import requests
import time

def download_text(url, max_retries, retry_delay):
    for attempt in range(max_retries):
        try:
            # Send HTTP GET request
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
    
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occured: {str(e)}")
        
        except Exception as e:
            print(f"An error occured: {str(e)}")

        if attempt < max_retries -1:
            time.sleep(retry_delay)

    return None
