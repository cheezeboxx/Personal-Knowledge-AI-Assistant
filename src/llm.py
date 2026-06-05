import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client_gemini = genai.Client(
    api_key= os.getenv("GEMINI_API_KEY")
)

def generate_answer(context, question):

    prompt = f"""
You are a study assistant.

Answer using the provided context.

If mathematical formulas appear corrupted,
reconstruct them into readable notation.

If the answer is not found, say:
"I could not find that information in the documents."

Context:
{context}

Question:
{question}
"""
    

    try:
        response = client_gemini.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        
        answer = response.text
        
    except Exception as e:
        return f"LLM Error : {str(e)}"
    
    return answer