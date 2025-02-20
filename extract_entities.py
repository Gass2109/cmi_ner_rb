import os
import sys
import json
from utils import load_config, validate_input_file, extract_entities_from_docx

def main():
    """Main function to process a given .docx file."""
    if len(sys.argv) != 2:
        print("[ERROR] Usage: python extract_entities.py <filename.docx>")
        sys.exit(1)

    # Load configuration
    config = load_config("config.yaml")
    input_folder = config["INPUT_FOLDER"]
    output_folder = config["OUTPUT_FOLDER"]

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    file_name = sys.argv[1]
    file_path = os.path.join(input_folder, file_name)

    # Validate input file
    validate_input_file(file_path)

    print(f"[INFO] Processing: {file_name}")

    # Extract entities
    extracted_entities = extract_entities_from_docx(file_path, config)

    print("\nExtracted Named Entities:")
    for key, value in extracted_entities.items():
        print(f"{key}: {value}")

    # Define output file path (remove .docx from filename)
    output_filename = f"parsed_{os.path.splitext(file_name)[0]}.json"
    output_path = os.path.join(output_folder, output_filename)

    # Save results to JSON
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(extracted_entities, json_file, indent=4)

    print(f"\n[INFO] Extraction complete. Results saved to: {output_path}")

if __name__ == "__main__":
    main()
