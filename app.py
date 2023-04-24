import os
import glob
import spacy
import git
import openai
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

nlp = spacy.load("en_core_web_sm")

def count_tokens(text):
    doc = nlp(text)
    return len(doc)

def get_code_explanation(code):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Explain the following Python code:\n\n{code}\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

repo_url = "https://github.com/shosseini811/AI-ML-Engineer"
main_file_path = "/Users/soheilhosseini/Google Drive/Resume/TowardsDataScience/OpenAI_Project"
repo_path = "/Users/soheilhosseini/Google Drive/Resume/TowardsDataScience/OpenAI_Project/Cloned_Repo"

if not os.path.exists(repo_path):
    os.makedirs(repo_path)
    git.Repo.clone_from(repo_url, repo_path)

# Cleanup step: Remove previous output files
output_base_path = f"{repo_path}_explained"
if os.path.exists(output_base_path):
    import shutil
    shutil.rmtree(output_base_path)

# Find all Python files in the repository
python_files = glob.glob(f"{repo_path}/**/*.py", recursive=True)

for file_path in python_files:
    print(f"Processing file: {file_path}\n")
    with open(file_path, "r") as file:
        code_lines = file.readlines()

    output_file_path = file_path.replace(repo_path, output_base_path).rstrip(".py") + "_explained.py"

    # Create directories for the output file if they don't exist
    output_dir = os.path.dirname(output_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file_path, "a") as output_file:
        for line_number, line in enumerate(code_lines, start=1):
            line = line.strip()
            if line:  # Skip empty lines
                soup = BeautifulSoup(line, "html.parser")
                text_line = soup.get_text()
                explanation = get_code_explanation(text_line)
                explanation_lines = explanation.split("\n")
                output_file.write(f"# Line {line_number}: {text_line}\n")
                for explanation_line in explanation_lines:
                    output_file.write(f"# Explanation: {explanation_line}\n")
                output_file.write(f"{line}\n\n")


    print(f"Appended explanations to: {output_file_path}\n")
    print("====================================\n")
