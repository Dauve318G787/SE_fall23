def write_text_file(text_data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text_data)
        print(f"Text download and saved to file {output_file}")
    
    except Exception as e:
        print(f"An error occured: {str(e)}")
