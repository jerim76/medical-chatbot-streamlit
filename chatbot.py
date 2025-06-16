import streamlit as st
from chat_logic import get_medical_response

st.set_page_config(page_title="MediBot", layout="centered")

st.title("💬 MediBot - Your Medical Assistant")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Describe your symptoms:", key="input")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    reply = get_medical_response(user_input)
    st.session_state.chat_history.append(("MediBot", reply))

# Display chat history
for speaker, message in st.session_state.chat_history:
    st.write(f"**{speaker}:** {message}")
