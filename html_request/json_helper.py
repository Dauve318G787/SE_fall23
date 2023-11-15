import json

def read_json(in_file):
    try:
        with open(in_file, 'r', encoding='UTF-8') as file:
            json_dat = json.load(file)

            if isinstance(json_dat, list):
                return json_dat
            elif isinstance(json_dat, dict):
                return json_dat
            else:
                print("Invalid JSON format")
                return None

    except FileNotFoundError:
        print(f"Error: File '{in_file}' not found")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{in_file}' JSON decode error")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def write_json(in_file, out_file):
    try:
        with open(in_file, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file]
            
        with open(out_file, 'w', encoding='utf-8') as json_file:
            json.dump(urls, json_file, indent=2)
            
        print(f"JSON URL List: {out_file}")
        return out_file
        
    except Exception as e:
        print(f"Error: {e}")
        return None
