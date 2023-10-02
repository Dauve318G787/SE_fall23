import lxml
import chardet
from bs4 import BeautifulSoup

def parse_file(input_file, output_file):

    try:
        with open(input_file, 'r', encoding='utf-8') as data_file:
            data_buffer = data_file.read()
            soup = BeautifulSoup(data_buffer, 'lxml')

            # div_tags = soup.find_all('div', class_="md")
            # comment_tags = [div for div in div_tags if div.find('p')]     
            comment_tags = soup.find_all('form', class_="usertext")
            
            with open(output_file, 'w', encoding='utf-8') as results_file:
                for comment in comment_tags:
                    results_file.write(comment.text + "\n")

            print("Written to", output_file)        

    except Exception as e:
        print("Error: ", str(e))
        return 1
