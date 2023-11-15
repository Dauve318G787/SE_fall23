#----------------------------
# The start of the program, expects a URL specifically to reddit but will
# work with other HTML files. Behavior unpredictable although if not used
# in a reddit website
#-------------------------------------

# Need sys for reading from command line

import sys
from html_request.get_html_content import process_url
from html_request.get_html_content import url_content_dict
from html_request.json_helper import read_json
from html_parse.data_parser import get_html_tags
from gpt_sentiment.gpt_wrapper import write_sentiment

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <URL_FILE>")
        sys.exit(1)

    ufile = sys.argv[1]
    url_file = "data/raw/url_list.json"
    dict_file = "data/raw/url_dict.json"
    tag_file = "data/processed/tag_dump.json"
    sentiment_file = "data/sentiments/sentiment_dump.txt"

    raw_dat = process_url(ufile, url_file) # takes file and converts it to json list
    url_content_dict(raw_dat, dict_file) # takes json list, gets content from url, makes json dict

    # takes json dict, gets tags with BS4, makes json dict
    get_html_tags(read_json(dict_file), tag_file)
    
if __name__ == "__main__":
    main()
