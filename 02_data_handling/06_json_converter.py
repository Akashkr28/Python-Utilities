import json
import csv
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "api_data.json")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "converted_data.csv")

def load_json_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    
    with open(filename, 'r', encoding="utf-8-sig") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")
        return
    
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)

    print(f"Converted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV.....")
    data = load_json_data(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()