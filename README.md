# Financial Document Parser using Rule-based Parser 🏦📄

This Python project is designed to extract financial named entities from `.docx` documents containing tables and save the results as JSON files for further analysis. The documents are processed using a rule-based parser (based on regular expression operations "re" Python module).

---

## Features
✅ Reads `.docx` files from the `input/` folder.  
✅ Extracts named entities such as **Counterparty**, **Notional**, **Valuation Date**, etc.  
✅ Saves extracted results in the `output/` folder with a `parsed_` prefix.  
✅ Uses a customizable `config.yaml` file for rule-based entity extraction.  


---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your_username/cmi_ner_rb.git
cd cmi_ner_rb
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Folder Structure
```bash
cmi_ner_rb/
│── input/ # Folder for input documents
│── output/ # Folder for extracted entity results
│── config.yaml # Config file for rule-based entity extraction
│── requirements.txt # Dependencies
│── README.md # Instructions to run the project
│── utils.py # Utility functions
│── extract_entities.py # Main script for entity extraction
```

---

## Usage

1. Place your `.docx` files inside the `input/` folder.
2. Run the script with the document name:
```bash
python extract_entities.py sample_input_document.docx
```
3. The output will be saved in the `output/` folder with the prefix `parsed_`.
```bash
output/
└── parsed_sample_input_document.json
```
---

## Example Output
Below is an example of the JSON output generated by the parser:

```json
{
"Counterparty": "BANK ABC",
"Initial Valuation Date": "31 January 2025",
"Notional": "EUR 1 million",
"Valuation Date": "31 July 2026",
"Maturity": "07 August 2026",
"Underlying": "Allianz SE (ISIN DE0008404005, Reuters: ALVG.DE)",
"Coupon": "0%",
"Barrier": "75.00% of Shareini",
"Calendar": "TARGET"
}
```

---

## 🛠️ Next Steps

✅ Improve regex for more formats.

✅ Add NLP-based entity extraction.

✅ Support more documents extentions (e.g. PDF).