import json
from get_html_content import download_url

def read_url_list(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            json_file = json.load(file)

            if isinstance(json_file, list):
                # GET HTML CONTENT
                for entry in json_file:
                    print(entry)
            elif isinstance(json_file, dict):
                # GET HTML CONTENT
                for key, value in json_file.items():
                    print(f"{key}: {value}")

            else:
                print("Invalid JSON format")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' JSON decode error")
    except Exception as e:
        print(f"Error: {e}")
