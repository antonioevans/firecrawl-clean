import json
import re
import os
from pathlib import Path

def clean_text(text):
    # Remove newlines and extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove special characters
    text = re.sub(r'[^\w\s.,;:!?-]', '', text)
    return text

def process_json_file(input_file, output_file):
    encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                data = json.load(f)
            
            processed_data = []

            for item in data:
                if 'markdown' in item and 'metadata' in item:
                    processed_item = {
                        'markdown': clean_text(item['markdown']),
                        'title': item['metadata'].get('title', ''),
                        'sourceURL': item['metadata'].get('sourceURL', ''),
                        'ogDescription': item['metadata'].get('ogDescription', '')
                    }
                    processed_data.append(processed_item)

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully processed using {encoding} encoding.")
            return
        except UnicodeDecodeError:
            continue
        except json.JSONDecodeError:
            print(f"Invalid JSON using {encoding} encoding. Trying next encoding...")
            continue
    
    print("Failed to process the file with any of the attempted encodings.")

def process_text_file(input_file, output_file):
    encodings = ['utf-8', 'utf-16', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(input_file, 'r', encoding=encoding) as f:
                content = f.read()
            
            cleaned_content = clean_text(content)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            print(f"Successfully processed using {encoding} encoding.")
            return
        except UnicodeDecodeError:
            continue
    
    print("Failed to process the file with any of the attempted encodings.")

def main():
    # Ask for file location or skip
    file_location = input("Enter the file location to process (or press Enter to skip): ")

    if file_location:
        input_file = Path(file_location)
    else:
        # Check /process folder for .json files
        process_folder = Path('process')
        json_files = list(process_folder.glob('*.json'))
        
        if not json_files:
            print("No JSON files found in the /process folder.")
            return
        
        input_file = json_files[0]

    # Create /done folder if it doesn't exist
    done_folder = Path('done')
    done_folder.mkdir(exist_ok=True)

    output_file = done_folder / f"processed_{input_file.name}"

    # Process the file
    if input_file.suffix.lower() == '.json':
        try:
            process_json_file(input_file, output_file)
        except Exception as e:
            print(f"Error processing JSON file: {e}")
            print("Processing as text file instead.")
            process_text_file(input_file, output_file)
    else:
        process_text_file(input_file, output_file)

if __name__ == "__main__":
    main()