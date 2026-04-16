# main.py
import os
from dotenv import load_dotenv

# This command looks for the .env file and loads the variables
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Resume_Screener_Project"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# --- THE REST OF YOUR CODE (Remains the same) ---
job_description = "Data Scientist: Python, PyTorch, LangChain."
resumes = [
    "Expert in Python and LangChain...", 
    "Java developer...", 
    "Chef..."
]

chain = get_screening_chain()
for resume in resumes:
    result = chain.invoke({"jd": job_description, "resume": resume})
    print(result)