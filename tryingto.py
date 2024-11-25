import json

def standardize_json_response(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    print(json.dumps(data, indent=2))

    standardized_questions = []

    for question in data.get("questions", []):
        # Check if question is a list and get the first item if it is
        question_data = question[0] if isinstance(question, list) else question
        
        # Add additional checks to handle different JSON structures
        if isinstance(question_data, list):
            question_data = question_data[0]
            
        # Handle different possible structures for questions
        question_id = ""
        title = ""
        responses = {"ideal": "", "good": "", "bad": ""}
        
        if isinstance(question_data, dict):
            # Try different possible paths to get question data
            if "Question" in question_data:
                question_text = str(question_data["Question"])
                if ": " in question_text:
                    title, question_id = question_text.split(": ", 1)
                else:
                    question_id = question_text
                    
            elif "Response" in question_data and isinstance(question_data["Response"], dict):
                if "Question" in question_data["Response"]:
                    question_text = question_data["Response"]["Question"]
                    if ": " in question_text:
                        title, question_id = question_text.split(": ", 1)
                    else:
                        question_id = question_text
            
            # Try different possible paths to get responses
            if "Responses" in question_data:
                responses_data = question_data["Responses"]
                if isinstance(responses_data, dict):
                    responses = {
                        "ideal": responses_data.get("Ideal", ""),
                        "good": responses_data.get("Good", ""),
                        "bad": responses_data.get("Bad", "")
                    }
                elif isinstance(responses_data, list):
                    # Handle case where Responses is a list
                    # You might want to adjust this based on your actual data structure
                    responses = {
                        "ideal": responses_data[0] if len(responses_data) > 0 else "",
                        "good": responses_data[1] if len(responses_data) > 1 else "",
                        "bad": responses_data[2] if len(responses_data) > 2 else ""
                    }

        # Create the standardized question dictionary
        standardized_question = {
            "question_id": question_id.strip(),
            "title": title.strip(),
            "responses": responses,
            "follow_up": {
                "question": "",
                "analysis": {
                    "documents": []
                }
            }
        }

        # Process follow-up analysis if available
        if isinstance(question_data, dict):
            follow_up_analysis = []
            
            # Path 1: Response -> Follow-up Analysis -> Documents or Evidence
            if "Response" in question_data:
                response_data = question_data["Response"]
                # Add check to ensure response_data is a dictionary
                if isinstance(response_data, dict):
                    follow_up = response_data.get("Follow-up Analysis", {})
                else:
                    follow_up = {}
                if isinstance(follow_up, dict):
                    docs = follow_up.get("Documents or Evidence for Ideal Implementation", [])
                    if isinstance(docs, list):
                        follow_up_analysis.extend(docs)
                    elif isinstance(docs, dict):
                        follow_up_analysis.append(docs)
            
            # Path 2: Follow-up Analysis -> Documents or Evidence
            elif "Follow-up Analysis" in question_data:
                docs = question_data["Follow-up Analysis"].get("Documents or Evidence for Ideal Implementation", [])
                if isinstance(docs, list):
                    follow_up_analysis.extend(docs)
                elif isinstance(docs, dict):
                    follow_up_analysis.append(docs)
            
            # Path 3: FollowUpQuestionAnalysis -> DocumentsOrEvidence
            elif "FollowUpQuestionAnalysis" in question_data:
                docs = question_data["FollowUpQuestionAnalysis"].get("DocumentsOrEvidence", [])
                if isinstance(docs, list):
                    follow_up_analysis.extend(docs)
                elif isinstance(docs, dict):
                    follow_up_analysis.append(docs)

            for document in follow_up_analysis:
                if isinstance(document, dict):
                    standardized_question["follow_up"]["analysis"]["documents"].append({
                        "name": document.get("Document", document.get("document", document.get("Name", document.get("name", "")))),
                        "importance": document.get("EvidenceImportance", document.get("importance", document.get("Importance", ""))),
                        "sufficiency": document.get("EvidenceSufficiency", document.get("sufficiency", document.get("Sufficiency", ""))),
                        "tools": {
                            "open_source": document.get("OpenSourceTools", document.get("open_source_tools", [])),
                            "commercial": document.get("CommercialTools", document.get("commercial_tools", []))
                        }
                    })

        standardized_questions.append(standardized_question)

    # Create the final standardized data structure
    standardized_data = {
        "questions": standardized_questions
    }

    # Save to output file with nice formatting (indent=4)
    with open(output_file_path, 'w') as output_file:
        json.dump(standardized_data, output_file, indent=4)

# Example usage
input_file_path = '/Users/dakshinsiva/JSON_Analyzer/data/questions_only.json'  # Path to your input JSON file
output_file_path = 'Question_Finale.json'  # Changed filename
standardize_json_response(input_file_path, output_file_path)
