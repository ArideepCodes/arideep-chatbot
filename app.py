import streamlit as st
import time

st.title("Arideep's Chat Bot (Demo Version 🤖)")

# Set default model (not used here but kept for structure)
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Say something to Arideep's AI..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Fake typing effect for assistant reply
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = "Hi! I'm a demo chatbot 🤖. OpenAI is not connected right now."

        typed_response = ""
        for word in full_response.split():
            typed_response += word + " "
            message_placeholder.markdown(typed_response + "▌")
            time.sleep(0.1)

        message_placeholder.markdown(typed_response.strip())

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})
