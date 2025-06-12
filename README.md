# Concept Extraction from Competitive Exam Questions

A Python program that analyzes competitive exam questions and extracts the underlying concepts being tested. This tool helps in understanding conceptual distribution of past questions and aids in curriculum mapping or study analytics.

## 🎯 Objective

This project aims to build a program that:

* Analyzes questions from competitive exams (like UPSC).
* Identifies and extracts underlying concepts from each question.
* Works seamlessly across different domains/subjects.
* Is designed for easy integration with large language model (LLM) APIs for enhanced extraction capabilities in the future.

## Folder Structure

```
.
├── main.py                 # Entry point, handles CLI and user code
├── llm_api.py              # Handles Anthropic API calls, loads API key from .env
├── csv_reader.py           # Reads CSV from resources/ and returns data
├── resources/              # Folder containing subject CSVs (ancient_history.csv, math.csv, etc.)
├── .env                    # Stores Anthropic API key
├── requirements.txt        # Python dependencies
├── Makefile                # Run commands
└── README.md               # Instructions
```

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Yuvraj010203/interns-test-ai-data_22B0725
    cd interns-test-ai-data_22B0725
    ```

2.  **Install dependencies:**
    This command sets up a virtual environment and installs all necessary Python libraries.
    ```bash
    make install
    ```
    *Alternatively, if `make` isn't available or preferred:*
    ```bash
    python3 -m venv venv
    . ./venv/bin/activate && pip install -r requirements.txt
    ```
## Usage

Run the program with your desired subject:

```
make run SUBJECT=math
```
Or directly:
```
python main.py --subject=math
```

## 📊 Example Output

When you run the program, you'll see a clear summary in your terminal, and a new CSV file (e.g., ancient_history_output_concepts.csv) will be created in your project's root directory with the extracted concepts.

### Command Line Output

```bash
$ python main.py --subject ancient_history
Loaded 27 questions for subject: ancient_history
Using extraction method: keyword
--------------------------------------------------
Question 1: Archaeological Sites and Artifacts
Question 2: Revenue and Land Systems; Temple-based Education; Brahmadeya and Village Institutions
Question 3: History of Indian Science; Chronological Reasoning
...
--------------------------------------------------
Extracted concepts written to ancient_history_output_concepts.csv
Total questions processed: 27

Concept Distribution:
  Ancient Indian History General: 12 questions
  Gupta Period: 6 questions
  Harappan Civilization: 3 questions
  Mauryan Empire: 3 questions
  ...
```
## 🧠 Extraction Methods

This program supports different ways to pull out concepts, giving you flexibility based on your needs.

### 1. Keyword-Based Extraction

* **Method Flag:** `--method keyword` (this is the default if no method is specified)
* **Description:** This method uses predefined keyword dictionaries for each subject to identify relevant concepts. It's like having a very smart search-and-match system.
* **Pros:** It's super fast, highly reliable for known patterns, and doesn't incur any API costs.
* **Cons:** Its effectiveness is limited to the keywords already defined. It might miss more subtle concepts.

### 2. Simulated LLM Extraction

* **Method Flag:** `--method simulated_llm`
* **Description:** This method simulates how an advanced Large Language Model (LLM) would analyze and extract concepts. It uses enhanced contextual awareness to provide more nuanced insights, mimicking AI capabilities without an actual API call.
* **Pros:** Offers a glimpse into more nuanced understanding and can suggest better relationships between concepts.
* **Cons:** It's still based on pre-programmed rules, not true AI reasoning.

### 3. Actual LLM Integration (Template Ready)

* **Description:** The `llm_api.py` module is built with a template to easily integrate with real LLM APIs (like Anthropic's Claude, Google's Gemini, or OpenAI's GPT) when an API key is provided and the necessary client is uncommented. This allows for genuine AI-powered concept extraction in the future!



