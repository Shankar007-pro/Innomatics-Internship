# chains/screening_chain.py
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from prompts.templates import SCREENER_PROMPT

def get_screening_chain():
    # llama-3.3-70b is extremely powerful and free on Groq's tier
    model = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0,
        # groq_api_key is handled by environment variables in main.py
    )
    
    prompt = ChatPromptTemplate.from_template(SCREENER_PROMPT)
    chain = prompt | model | JsonOutputParser()
    
    return chain