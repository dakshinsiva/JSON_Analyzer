import json

def extract_questions(data):
    questions = []
    
    for entry in data:
        # Handle different possible question field formats
        if isinstance(entry, dict):
            # Direct "Question" key
            if "Question" in entry:
                questions.append(entry)
            # Question in nested "Response" object
            elif "Response" in entry and isinstance(entry["Response"], dict) and "Question" in entry["Response"]:
                questions.append(entry)
            # Question as first key containing "Question" string
            else:
                for key in entry.keys():
                    if isinstance(key, str) and "Question" in key:
                        questions.append(entry)
                        break

    return questions

def save_questions(questions, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"questions": questions}, f, indent=4, ensure_ascii=False)

import json

def analyze_json(data):
    # Ensure we have a valid questions list
    if isinstance(data, dict):
        questions = data.get("questions", [])
    elif isinstance(data, list):
        questions = data
    else:
        print("Error: Invalid data format. Expected a dictionary with 'questions' key or a list of questions.")
        return

    # Ensure questions is a list
    if not isinstance(questions, list):
        print("Error: Questions data must be a list")
        return

    # Basic statistics
    total_questions = len(questions)
    print(f"\n=== JSON Analysis Report ===")
    print(f"\n1. Basic Statistics:")
    print(f"   • Total number of questions: {total_questions}")

    # Question length analysis
    question_lengths = []
    for item in questions:
        if not isinstance(item, dict):  # Skip if item is not a dictionary
            continue
            
        if "Question" in item and isinstance(item["Question"], str):
            question_lengths.append(len(item["Question"]))
        elif "Question_Analysis" in item and isinstance(item["Question_Analysis"], dict):
            if "Question" in item["Question_Analysis"] and isinstance(item["Question_Analysis"]["Question"], str):
                question_lengths.append(len(item["Question_Analysis"]["Question"]))
        elif "Response" in item and isinstance(item["Response"], dict):
            if "Question" in item["Response"] and isinstance(item["Response"]["Question"], str):
                question_lengths.append(len(item["Response"]["Question"]))

    if question_lengths:
        avg_length = sum(question_lengths) / len(question_lengths)
        max_length = max(question_lengths)
        min_length = min(question_lengths)
        print(f"   • Average question length: {avg_length:.2f} characters")
        print(f"   • Shortest question: {min_length} characters")
        print(f"   • Longest question: {max_length} characters")

    # Response analysis
    print("\n2. Response Analysis:")
    response_counts = {
        "single_response": 0,
        "multiple_responses": 0,
        "tiered_responses": 0,
        "no_response": 0
    }

    for item in questions:
        if "Response" in item and isinstance(item["Response"], dict):
            if "TieredResponses" in item["Response"]:
                response_counts["tiered_responses"] += 1
            else:
                response_counts["single_response"] += 1
        elif "Responses" in item:
            response_counts["multiple_responses"] += 1
        else:
            response_counts["no_response"] += 1

    for response_type, count in response_counts.items():
        print(f"   • {response_type.replace('_', ' ').title()}: {count} ({(count/total_questions)*100:.1f}%)")

    # Follow-up question analysis
    follow_up_count = sum(1 for item in questions if "Follow-up" in item or "Follow-Up" in item)
    print(f"\n3. Follow-up Questions:")
    print(f"   • Questions with follow-ups: {follow_up_count} ({(follow_up_count/total_questions)*100:.1f}%)")

    # Evidence requirements
    evidence_count = sum(1 for item in questions 
                        if any("Evidence" in str(value) for value in item.values()))
    print(f"   • Questions requiring evidence: {evidence_count} ({(evidence_count/total_questions)*100:.1f}%)")

    # Question categories
    print("\n4. Question Categories:")
    categories = {}
    for item in questions:
        question_text = ""
        if "Question" in item:
            question_text = item["Question"]
        elif "Question_Analysis" in item:
            question_text = item["Question_Analysis"]["Question"]
        elif "Response" in item and "Question" in item["Response"]:
            question_text = item["Response"]["Question"]
        
        if ":" in question_text:
            category = question_text.split(":")[0].strip()
            categories[category] = categories.get(category, 0) + 1

    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"   • {category}: {count} ({(count/total_questions)*100:.1f}%)")

def parse_json_analysis_report(report_text):
    sections = {}
    current_section = None
    
    # Define valid sections to parse
    valid_sections = [
        "Basic Statistics",
        "Response Analysis", 
        "Follow-up Questions"
    ]
    
    for line in report_text.split('\n'):
        # Remove empty lines
        if not line.strip():
            continue
            
        # Detect section headers
        if line.startswith('==='):
            continue
            
        # New numbered section
        if line.strip()[0].isdigit() and line.strip().endswith(':'):
            section_name = line.strip()[3:].rstrip(':')
            if section_name in valid_sections:
                current_section = section_name
                sections[current_section] = []
            else:
                current_section = None
            continue
            
        # Add content to current section
        if current_section and line.strip():
            # Clean up bullet points and formatting
            cleaned_line = line.strip().replace('   • ', '')
            # Parse percentage values
            if '(' in cleaned_line and ')' in cleaned_line:
                value, percentage = cleaned_line.split('(')
                percentage = float(percentage.rstrip('%)'))
                sections[current_section].append({
                    'metric': value.strip(),
                    'percentage': percentage
                })

def display_report(sections):
    for section_name, items in sections.items():
        print(f"\n{section_name}:")
        for item in items:
            if isinstance(item, dict):
                print(f"  • {item['metric']} ({item['percentage']}%)")
            else:
                print(f"  • {item}")

if __name__ == "__main__":
    try:
        with open('questions_only.json', 'r') as file:
            data = json.load(file)
            analyze_json(data)
    except FileNotFoundError:
        print("Error: questions_only.json file not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
