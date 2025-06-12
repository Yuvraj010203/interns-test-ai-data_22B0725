.PHONY: all install run clean

# Default target: sets up the environment.
all: install

# Sets up the virtual environment and installs Python dependencies.
install:
	@echo "Setting up environment and installing dependencies..."
	python3 -m venv venv
	. ./venv/bin/activate && pip install -r requirements.txt
	@echo "Installation complete."

# Runs concept extraction for Ancient History using the keyword method.
run-ancient:
	@echo "Running Ancient History (keyword method)..."
	. ./venv/bin/activate && python main.py --subject ancient_history --method keyword

# Runs concept extraction for Mathematics using the keyword method.
run-math:
	@echo "Running Mathematics (keyword method)..."
	. ./venv/bin/activate && python main.py --subject math --method keyword

# Runs concept extraction for Physics using the keyword method.
run-physics:
	@echo "Running Physics (keyword method)..."
	. ./venv/bin/activate && python main.py --subject physics --method keyword

# Runs concept extraction for Economics using the keyword method.
run-economics:
	@echo "Running Economics (keyword method)..."
	. ./venv/bin/activate && python main.py --subject economics --method keyword

# Runs keyword-based concept extraction for all subjects.
run-all-keyword: run-ancient run-math run-physics run-economics
	@echo "All subjects processed with keyword method."

# Runs simulated LLM-based concept extraction for all subjects.
run-all-llm:
	@echo "Running Ancient History (simulated LLM method)..."
	. ./venv/bin/activate && python main.py --subject ancient_history --method simulated_llm
	@echo "Running Mathematics (simulated LLM method)..."
	. ./venv/bin/activate && python main.py --subject math --method simulated_llm
	@echo "Running Physics (simulated LLM method)..."
	. ./venv/bin/activate && python main.py --subject physics --method simulated_llm
	@echo "Running Economics (simulated LLM method)..."
	. ./venv/bin/activate && python main.py --subject economics --method simulated_llm
	@echo "All subjects processed with simulated LLM method."

# Cleans up generated output files and the virtual environment.
clean:
	@echo "Cleaning up generated files..."
	@rm -f *_output_concepts.csv output_concepts.csv
	@rm -rf __pycache__ venv
	@echo "Cleanup complete."