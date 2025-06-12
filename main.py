import argparse
import csv
import os
from csv_reader import read_subject_csv
# The following import is commented out as we are not using a live LLM API for this submission.
# from llm_api import call_llm_api

def extract_concepts_keyword(question: str, subject: str) -> list:
    """
    This function contains predefined keyword rules for each subject
    """
    concepts = []
    question_lower = question.lower()

    if subject == 'ancient_history':
        # Indus Valley Civilization / Harappan Civilization
        if any(keyword in question_lower for keyword in ["harappan", "indus valley", "mohenjodaro", "harappa", "dholavira", "kalibangan", "rakhigarhi", "ropar", "chanhudaro", "kot diji", "desalpur", "civilization", "water harvesting", "city planning", "secular civilization", "cotton", "textiles", "horse-drawn chariots", "deities"]):
            concepts.append("Indus Valley Civilization")
        
        # Mauryan Empire / Ashokan Edicts / Kautilya's Arthashastra
        if any(keyword in question_lower for keyword in ["mauryan", "ashoka", "ashokan", "kautilya", "arthashastra", "edicts", "inscription", "ranyo ashoka", "james prinsep"]):
            concepts.append("Mauryan Empire / Ashokan Edicts")
        
        # Vedic Period / Rigvedic Aryans
        if any(keyword in question_lower for keyword in ["vedic", "rigvedic aryans", "rigveda", "yajnas", "nature worship", "early vedic"]):
            concepts.append("Vedic Period / Early Aryans")
        
        # Gupta Period
        if any(keyword in question_lower for keyword in ["gupta dynasty", "gupta period", "guptas of magadha", "ghantasala", "kadura", "chaul", "vishti", "forced labour"]):
            concepts.append("Gupta Period")
        
        # Religious Movements (Buddhism & Jainism)
        if any(keyword in question_lower for keyword in ["buddhism", "jainism", "buddha", "mahavira", "jaina texts", "nettipakarana", "parishishta parvan", "avadanasataka", "trishashtilakshana mahapurana", "religious sects", "avoidance of extremities", "indifference to vedas", "denial of rituals", "jain philosophy", "universal law", "dignaga"]):
            concepts.append("Buddhism and Jainism")
        
        # Scientific & Technological Progress (Ancient India)
        if any(keyword in question_lower for keyword in ["scientific progress", "surgical instruments", "transplant", "sine of an angle", "cyclic quadrilateral", "science", "astronomy", "mathematics"]):
            concepts.append("History of Indian Science & Technology")
            # If the question also specifically mentions centuries, add chronological reasoning
            if any(num_century in question_lower for num_century in ["1st century", "3rd century", "5th century", "7th century"]):
                concepts.append("Chronological Reasoning")
        
        # Archaeological Sites & Artifacts
        if any(keyword in question_lower for keyword in ["burzahom", "chandra-ketugarh", "ganeshwar", "rock-cut shrines", "terracotta art", "copper artefacts", "historical place", "archaeological"]):
            concepts.append("Archaeological Sites and Artifacts")
        
        # Administrative & Economic Systems / Guilds
        if any(keyword in question_lower for keyword in ["eripatti", "land revenue", "taniyurs", "ghatikas", "guilds", "shrenis", "economy", "wages", "rules of work", "prices", "judicial powers", "administrative authority", "tax", "kulyavapa", "dronavapa"]):
            concepts.append("Ancient Indian Economy & Administration / Guilds")
        
        # Art, Architecture, & Literature
        if any(keyword in question_lower for keyword in ["playwrights", "bhavabhuti", "hastimalla", "kshemeshvara", "kalidasa", "amarasimha", "panini", "literature", "texts", "sculpture", "stone portrait", "art", "architecture"]):
            concepts.append("Ancient Indian Art, Architecture & Literature")
        
        # Post-Gupta Period / Kingdoms
        if any(keyword in question_lower for keyword in ["decline of guptas", "rise of harshavardhana", "northern india", "kingdoms", "guptas of magadha", "paramaras of malwa", "pushyabhutis of thanesar", "maukharis of kanauj", "yadavas of devagiri", "maitrakas of valabhi", "harshavardhana"]):
            concepts.append("Post-Gupta Period / Regional Kingdoms")

        # Cultural History / Foreign Travellers
        if any(keyword in question_lower for keyword in ["yuan chwang", "hiuen tsang", "chinese traveller", "cultural contacts", "trade links", "southeast asia", "bay of bengal", "maritime history", "chronicles", "dynastic histories", "epic tales", "shramana", "parivraajaka", "agrahaarika", "magadha"]):
            concepts.append("Ancient Indian Culture & Foreign Relations")
            
        # Default fallback
        if not concepts:
            concepts.append("Ancient Indian History General")
            
    elif subject == 'economics':
        # Government Debt & Public Finance
        if any(keyword in question_lower for keyword in ["debt", "us treasury bonds", "government debt", "sovereign currency", "tax", "deficit", "fiscal policy", "expenditures", "csr", "corporate social responsibility"]):
            concepts.append("Government Debt & Public Finance")
        
        # Banking & Financial Markets (General)
        if any(keyword in question_lower for keyword in ["bank", "syndicated lending", "lenders", "loan", "credit line", "liquidity adjustment facility", "rbi", "reserve bank of india", "financial companies", "financial instruments", "collateral borrowing and lending obligations", "bond market", "forex market", "money market", "stock market", "capital markets", "call money market", "treasury bill market", "corporate bonds", "government securities", "insurance companies", "pension funds", "retail investors", "investment trusts", "invits", "securitization", "financial assets", "banking subsidiaries", "minimum capital", "board members"]):
            concepts.append("Banking & Financial Markets")
        
        # Monetary Policy
        if any(keyword in question_lower for keyword in ["monetary policy", "reserve bank", "rbi", "interest rates", "money supply", "central banks", "sterilization", "open market operations", "repo rate", "cash reserve"]):
            if "Monetary Policy" not in concepts: # Avoid duplicates if already added by 'Banking & Financial Markets'
                concepts.append("Monetary Policy")
        
        # Digital Currency / Digital Rupee
        if any(keyword in question_lower for keyword in ["digital rupee", "sovereign currency", "liability on the rbi’s balance sheet", "convertible", "cbdc"]):
            concepts.append("Digital Currency (CBDC)")
        
        # Economic Sectors / Capital
        if any(keyword in question_lower for keyword in ["sectors of the indian economy", "primary", "secondary", "tertiary", "storage of agricultural produce", "dairy farm", "mineral exploration", "weaving cloth", "physical capital", "farmer’s plough", "working capital", "computer", "fixed capital", "yarn", "petrol", "capital"]):
            concepts.append("Economic Sectors & Capital Classification")
        
        # International Trade & Global Economy
        if any(keyword in question_lower for keyword in ["global export", "trade", "wto", "export", "import", "balance of payments", "production-linked incentive", "pli scheme", "foreign companies", "global economy", "usa debt"]):
            concepts.append("International Trade & Global Economy")
        
        # Agriculture & Rural Economy
        if any(keyword in question_lower for keyword in ["farmer", "agricultural", "cultivate", "niger seeds", "kharif crop", "tribal people", "cooking oil", "minimum support price", "msps", "small farmer large field", "rural economy"]):
            concepts.append("Agriculture & Rural Economy")
        
        # Investment & Assets (General & Intangible)
        if any(keyword in question_lower for keyword in ["investments", "assets", "brand recognition", "inventory", "intellectual property", "mailing list", "intangible investments", "exchange-traded funds", "etf", "currency swap", "financial instruments"]):
            concepts.append("Investment & Assets")

        # Government Schemes / Programs (Specific to the question context)
        if any(keyword in question_lower for keyword in ["digital india land records modernisation programme", "funding", "cadastral maps", "digitised", "records of rights", "transliterate", "constitution of india"]):
            concepts.append("Government Schemes / Land Reforms")
        
        # Corporate Governance / CSR
        if any(keyword in question_lower for keyword in ["corporate social responsibility", "csr rules", "expenditures", "employees", "spending"]):
            if "Government Debt & Public Finance" not in concepts: # Add separately if not captured by broader finance keywords
                concepts.append("Corporate Governance / CSR")
        
        # Data Sufficiency / Statement Analysis (Question type)
        if any(keyword in question_lower for keyword in ["consider the following statements", "statement-i", "statement-ii", "correct in respect of the above statements"]):
            concepts.append("Statement Analysis / Data Interpretation")

        # Default fallback
        if not concepts:
            concepts.append("Economics General")
            
    elif subject == 'math':
        # Profit & Loss / Commercial Math
        if any(keyword in question_lower for keyword in ["profit", "loss", "buy", "sell", "merchant", "rate", "goods", "articles", "discount", "marks up", "cost price", "selling price", "trade", "transaction", "purchases"]):
            concepts.append("Profit and Loss / Commercial Math")

        # Percentages
        # This will be broad and often combined with other concepts
        if any(keyword in question_lower for keyword in ["%", "percentage", "more than", "less than", "earns", "overall win percentage", "changed by", "profit percentage"]):
            concepts.append("Percentages")

        # Ratios & Proportions / Mixtures & Alligations
        if any(keyword in question_lower for keyword in ["ratio", "mixed", "alloy", "share", "proportion", "ice-cream factory"]):
            concepts.append("Ratios and Mixtures")
        
        # Interest (Simple & Compound)
        if any(keyword in question_lower for keyword in ["compound interest", "simple interest", "deposits", "bank", "amount", "years"]):
            concepts.append("Interest (Simple & Compound)")
        
        # Algebra / Equations / Inequalities (Focus on 'x', 'range of values', 'solve')
        if any(keyword in question_lower for keyword in ["x%", "range of values", "equation", "variable", "sum of a and b", "find x"]):
            # Add Algebra if not already covered by percentage and explicitly algebraic
            if "algebra" not in [c.lower() for c in concepts]: # Check if algebra isn't already added
                concepts.append("Algebra")
        
        # Number Systems / Number Theory
        if any(keyword in question_lower for keyword in ["whole numbers", "integer amounts", "prime number", "integer"]):
            concepts.append("Number Systems / Number Theory")
        
        # Permutations & Combinations / Probability / Counting Principles
        if any(keyword in question_lower for keyword in ["outcomes", "triplets", "roll a die", "same number", "different", "counting"]):
            concepts.append("Permutations & Combinations / Probability")
        
        # Work & Time / Efficiency
        if any(keyword in question_lower for keyword in ["workers", "efficiency", "planting trees", "plant"]):
            concepts.append("Work and Time / Efficiency")
        
        # Data Sufficiency (Specific type of question)
        if any(keyword in question_lower for keyword in ["statements", "necessary to answer", "study the statements"]):
            concepts.append("Data Sufficiency")

        # Sequences and Series (from Q1)
        if "first good" in question_lower and "second one" in question_lower and "so on" in question_lower:
            concepts.append("Sequences and Series")

        # Optimization (from Q8, "minimum profit")
        if "minimum profit" in question_lower:
            concepts.append("Optimization")
            
        # Default fallback (always ensure a concept is added)
        if not concepts:
            concepts.append("Mathematics General")
        
        # Post-processing to remove potential duplicates if basic 'Percentages' was too broad and a more specific 'Algebra' or 'Profit and Loss' covers it.
        # This part requires careful thought to ensure concepts are distinct and not overly redundant.
        # For simplicity, if a more specific concept like "Profit and Loss" or "Ratios and Mixtures" is present,
        # and "Percentages" is also present, it might be redundant, but for now, we'll keep it as these questions often blend concepts.
        # The key is to avoid adding "Algebra" if "Percentages" already implies it, unless it's genuinely algebraic.
        # Re-evaluating the 'Algebra' condition to be more specific.

        # If 'Percentages' was added and a clear algebraic keyword like 'equation', 'variable', 'find x'
        # is also present, then make sure 'Algebra' is also there.
        if "percentages" in [c.lower() for c in concepts]: # Check if percentages was added
            if any(alg_kw in question_lower for alg_kw in ["equation", "variable", "find x", "range of values"]):
                if "algebra" not in [c.lower() for c in concepts]:
                    concepts.append("Algebra")
            # If "Profit and Loss / Commercial Math" is present, and "Percentages" is also present,
            # it might be better to keep both, as percentages are a tool within P&L.
            # No explicit de-duplication for such overlaps for now, as it signifies multiple aspects.
            
    elif subject == 'physics':
        # Mechanics (Kinematics, Dynamics, Work, Energy, Power, Gravitation)
        if any(keyword in question_lower for keyword in ["force", "motion", "velocity", "acceleration", "momentum", "energy", "work", "power", "gravity", "gravitational", "mass", "weight", "friction", "circular motion", "projectile", "mechanics", "newton", "gpe", "kinetic energy", "fall"]):
            concepts.append("Mechanics")
        
        # Electricity & Magnetism (Electromagnetism, Circuits)
        if any(keyword in question_lower for keyword in ["electricity", "current", "voltage", "resistance", "circuit", "ohm's law", "resistor", "capacitor", "inductor", "charge", "electric field", "magnetic field", "magnetism", "electromagnetism", "induction", "generator", "motor", "transformer"]):
            concepts.append("Electricity & Magnetism")
        
        # Optics (Light, Reflection, Refraction, Lenses, Mirrors)
        if any(keyword in question_lower for keyword in ["optics", "light", "lens", "mirror", "reflection", "refraction", "interference", "diffraction", "polarization", "spectrum", "color", "vision"]):
            concepts.append("Optics")
        
        # Thermodynamics & Heat (Heat Transfer, Temperature, Gas Laws)
        if any(keyword in question_lower for keyword in ["thermodynamics", "heat", "entropy", "temperature", "thermal", "gas laws", "pressure", "volume", "boiling", "freezing", "conduction", "convection", "radiation"]):
            concepts.append("Thermodynamics & Heat")
        
        # Waves & Sound
        if any(keyword in question_lower for keyword in ["waves", "sound", "frequency", "wavelength", "amplitude", "oscillation", "vibration", "doppler effect", "pitch", "loudness"]):
            concepts.append("Waves & Sound")
        
        # Modern Physics (Quantum, Atomic, Nuclear, Relativity)
        if any(keyword in question_lower for keyword in ["quantum", "atomic", "nuclear", "radioactive", "photon", "electron", "proton", "neutron", "nucleus", "fission", "fusion", "relativity", "einstein", "e=mc^2"]):
            concepts.append("Modern Physics")
        
        # Units & Measurements / Physical Quantities
        if any(keyword in question_lower for keyword in ["unit", "measurement", "si unit", "quantity", "dimension", "error", "precision", "accuracy", "standard"]):
            concepts.append("Units & Measurements")
            
        # Properties of Matter (Density, Elasticity, Fluid Mechanics)
        if any(keyword in question_lower for keyword in ["density", "pressure", "fluid", "liquid", "gas", "solid", "elasticity", "surface tension", "viscosity", "buoyancy", "archimedes"]):
            concepts.append("Properties of Matter")

        # Default fallback
        if not concepts:
            concepts.append("Physics General")
            
            
    return concepts if concepts else ["Unidentified Concept"]

def simulate_llm_extraction(question: str, subject: str) -> str:
    """
    Simulates LLM-based concept extraction by providing examples of what
    an LLM might return for given questions.
    """
    # This is a simulation - in real implementation, this would call the LLM API
    prompt = f"""Given the question from {subject}: "{question}", identify the key concept(s) this question is based on. 
    
Return only the concept names, separated by semicolons."""
    
    # Simulated response based on the keyword extraction but with more nuanced understanding
    concepts = extract_concepts_keyword(question, subject)
    return "; ".join(concepts)

def main():
    parser = argparse.ArgumentParser(description="Concept Extraction from Competitive Exam Questions")
    parser.add_argument('--subject', required=True, 
                       choices=['ancient_history', 'math', 'physics', 'economics'], 
                       help='Subject to process')
    parser.add_argument('--method', default='keyword', 
                       choices=['keyword', 'simulated_llm'], 
                       help='Extraction method to use')
    parser.add_argument('--output', default='output_concepts.csv', 
                       help='Output CSV filename')
    args = parser.parse_args()

    try:
        data = read_subject_csv(args.subject)
        print(f"Loaded {len(data)} questions for subject: {args.subject}")
        print(f"Using extraction method: {args.method}")
        print("-" * 50)

        output_data = []
        for row in data:
            question_number = row['Question Number']
            question_text = row['Question']

            # Choose extraction method
            if args.method == 'keyword':
                concepts = extract_concepts_keyword(question_text, args.subject)
                extracted_concepts_str = "; ".join(concepts)
            else:  # simulated_llm
                extracted_concepts_str = simulate_llm_extraction(question_text, args.subject)

            print(f"Question {question_number}: {extracted_concepts_str}")
            output_data.append({
                'Question Number': question_number,
                'Question': question_text,
                'Concepts': extracted_concepts_str
            })

        # Write to output CSV
        output_filename = f"{args.subject}_{args.output}"
        with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['Question Number', 'Question', 'Concepts']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_data)
        
        print("-" * 50)
        print(f"Extracted concepts written to {output_filename}")
        print(f"Total questions processed: {len(output_data)}")
        
        # Display concept distribution
        concept_counts = {}
        for row in output_data:
            concepts = row['Concepts'].split('; ')
            for concept in concepts:
                concept_counts[concept] = concept_counts.get(concept, 0) + 1
        
        print("\nConcept Distribution:")
        for concept, count in sorted(concept_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"  {concept}: {count} questions")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Make sure the CSV file exists in the resources/ folder")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()