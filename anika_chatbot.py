import streamlit as st
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# LangChain OpenAI Chat
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)

# Anika’s style guide (System prompt)
anika_mind = """
You are Anika, a sassy, bold, business-savvy, justice-driven virtual influencer.
You expose fake influencers, simplify finance, and empower people.
You speak in sharp, emotional, Tamil-English (Tanglish) tone. Mix wit and wisdom.
You are not afraid to offend if it's for the truth. Use bold, viral statements.
"""

# Streamlit App UI
st.set_page_config(page_title="Chat with Anika", layout="centered")
st.title("**Anika is in the building. Ask boldly.**")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=anika_mind)
    ]

user_input = st.text_input("You:", "")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.spinner("Anika typing..."):
        response = chat(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

# Show conversation history
for msg in st.session_state.messages[1:]:
    if isinstance(msg, HumanMessage):
        st.markdown(f"**You:** {msg.content}")
    elif isinstance(msg, AIMessage):
        st.markdown(f"**Anika:** {msg.content}")
