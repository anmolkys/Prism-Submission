from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
key = "AIzaSyDNXX_h7q2usVoAXz7CKEskWxZ61lK7ufw"
 #your google gemini key


class llm():


    Llama = ChatOpenAI(
        model="crewai-llama2",
        base_url="http://localhost:11434/v1",
        openai_api_key="NA"
    )

    Deepseek = ChatOpenAI(
        model="crewai-coder",
        base_url="http://localhost:11434/v1",
        openai_api_key="NA"
    )

    Gemini = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=key)