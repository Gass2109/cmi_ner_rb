import os
import sys
import re
import yaml
from docx import Document



def load_config(config_file):
    """Load configuration from config.yaml."""
    try:
        with open(config_file, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"[ERROR] Failed to load config file: {e}")
        sys.exit(1)

def validate_input_file(file_path):
    """Check if the file exists and is a valid .docx file."""
    if not os.path.isfile(file_path):
        print(f"[ERROR] File '{os.path.basename(file_path)}' not found in the input folder.")
        sys.exit(1)

    if not file_path.lower().endswith(".docx"):
        print("[ERROR] Invalid file format. Please provide a .docx file.")
        sys.exit(1)

def extract_entities_from_docx(file_path, config):
    """Extract named entities from a .docx document."""
    try:
        doc = Document(file_path)
    except Exception as e:
        print(f"[ERROR] Failed to read {file_path}: {e}")
        sys.exit(1)

    extracted_data = {}
    entity_mapping = config["ENTITY_MAPPING"]
    entity_patterns = config["ENTITY_PATTERNS"]

    for table in doc.tables:
        for row in table.rows:
            if len(row.cells) >= 2:  # Ensure the row has at least two columns
                key = row.cells[0].text.strip()
                value = row.cells[1].text.strip()

                # Map known entity names
                if key in entity_mapping:
                    entity_name = entity_mapping[key]

                    # Apply regex patterns if available
                    if entity_name in entity_patterns:
                        match = re.search(entity_patterns[entity_name], value)
                        extracted_data[entity_name] = match.group(0) if match else value
                    else:
                        extracted_data[entity_name] = value

    return extracted_data
