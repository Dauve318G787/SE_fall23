#----------------------------
# The start of the program, expects a URL specifically to reddit but will
# work with other HTML files. Behavior unpredictable although if not used
# in a reddit website
#-------------------------------------

# Need sys for reading from command line

import sys
from module_2.download_text_data import download_text
from module_1.write_to_file import write_text_file
from module_3.data_parser import parse_file
from module_4.gpt_wrapper import write_sentiment

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    raw_file = "data_dump.txt"
    tag_file = "tag_dump.txt"
    sentiment_file = "sentiment_dump.txt"
    text_data = download_text(url, 20, 1)
    
    if text_data:
        write_text_file(text_data, "raw", raw_file)
        parse_file(raw_file, tag_file)
        write_sentiment()

if __name__ == "__main__":
    main()
