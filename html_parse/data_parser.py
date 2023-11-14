#--------------------------------------
# This module accepts two files. It reads from the input_file which is created by module_1.
# Then parses the contents of the file using bs4. After it writes the desired content from the input file to a new file
# specified in this file
#------------------------------------

import os
import lxml
import chardet
from bs4 import BeautifulSoup

def parse_file(input_file, output_file):

    cur_dir = os.getcwd()
    lf_dir = "data/processed"
    infile_dir = "data/raw"
    file_path = os.path.join(cur_dir, lf_dir, output_file)
    input_path = os.path.join(cur_dir, infile_dir, input_file)
    
    try:
        with open(input_path, 'r', encoding='utf-8') as data_file:

            data_buffer = data_file.read()
            soup = BeautifulSoup(data_buffer, 'lxml')
            body_tag = soup.find("body")
            comments = body_tag.find_all("div", class_="md")
            
            with open(file_path, 'w', encoding='utf-8') as results_file:
                for comment in comments[2:]:
                    results_file.write(comment.text + "\n")

            print("Written to", output_file)        

    except Exception as e:
        print("Error: ", str(e))
        return 1
