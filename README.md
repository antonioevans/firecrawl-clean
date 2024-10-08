# FireCrawl JSON Cleaner

This Python script is designed to clean and process JSON files generated by FireCrawl. It extracts specific fields from the JSON structure and removes unnecessary characters, resulting in a cleaner and more compact output.

## Features

- Process JSON files from a specified location or from the `/process` folder
- Clean text by removing newlines, extra spaces, and special characters
- Extract specific fields from JSON: markdown, title, sourceURL, and ogDescription
- Handle multiple file encodings (UTF-8, UTF-16, Latin-1, CP1252)
- Fallback to text processing if JSON processing fails
- Output processed files to the `/done` folder

## Requirements

- Python 3.6+

## Usage

1. Clone this repository:
git clone https://github.com/antonioevans/firecrawl-clean.git
cd firecrawl-json-cleaner
Copy
2. Run the script:
python clean_json_firecrawl.py
Copy
3. When prompted, either:
- Enter the full path to the file you want to process, or
- Press Enter to process the first .json file in the `/process` folder

The script will process the file and save the cleaned output in the `/done` folder.

## File Structure

- `clean_json_firecrawl.py`: The main Python script
- `/process/`: Folder containing input files to be processed
- `process_example.json`: An example input file
- `/done/`: Folder where processed files are saved
- `done_example.json`: An example output file

## Example

Input (`/process/process_example.json`):
```json
[
{
 "markdown": "## Example Markdown\n\nThis is some example content with newlines and special characters!",
 "metadata": {
   "title": "Example Title",
   "sourceURL": "https://example.com",
   "ogDescription": "This is an example description."
 }
}
]
```
Output (/done/processed_process_example.json):

```json[
  {
    "markdown": "Example Markdown This is some example content with newlines and special characters",
    "title": "Example Title",
    "sourceURL": "https://example.com",
    "ogDescription": "This is an example description."
  }
```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
License

This project is MIT licensed.
