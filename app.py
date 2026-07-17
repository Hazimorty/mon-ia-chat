import streamlit as st
from transformers import pipeline

st.title("Mon IA Chatbot 🤖")

# Charger le modèle
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")

chatbot = load_model()

# Zone de chat
user_input = st.text_input("Toi :")
if user_input:
    # On utilise la structure attendue par Qwen
    messages = [
        {"role": "system", "content": "Tu es un assistant utile."},
        {"role": "user", "content": user_input}
    ]
    resultats = chatbot(messages, max_new_tokens=100)
    reponse = resultats[0]['generated_text'][-1]['content']
    st.write(f"IA : {reponse}")
