#------------------------------
# This module accepts some data and a file name.
# It writes the data to the file name given to the directory specified in this file
#-------------------------------------------------

import os

def write_text_file(text_data, output_file):
    cur_dir = os.getcwd()
    lf_dir = "Data/raw"
    file_path = os.path.join(cur_dir, lf_dir, output_file)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_data)
        print(f"Text download and saved to file {output_file}")
    
    except Exception as e:
        print(f"An error occured: {str(e)}")
