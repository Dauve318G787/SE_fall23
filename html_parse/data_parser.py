#--------------------------------------
# This module accepts two files. It reads from the input_file which is created by module_1.
# Then parses the contents of the file using bs4. After it writes the desired content from the input file to a new file
# specified in this file
#------------------------------------

import os
import lxml
import chardet
import json
from bs4 import BeautifulSoup

def get_html_tags(json_dict, tag_path):
    try:
        tag_buffer = {}
        for url, content in json_dict.items():
            soup = BeautifulSoup(content, 'lxml')
            body_tag = soup.find("body")
            comments = body_tag.find_all("div", class_="md")

            comment_texts = [comment.get_text() for comment in comments[2:]] if comments else None
            tag_buffer[url] = comment_texts
            
        with open(tag_path, 'w', encoding='utf-8') as tag_file:
            json.dump(tag_buffer, tag_file, indent=2)

        
        return tag_path

    except Exception as e:
        print("Error: ", str(e))
        return None
