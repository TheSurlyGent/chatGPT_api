import streamlit as st
import openai
from key import api_key

openai.api_key = api_key

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat(input_message):
    # Add the user's input to the conversation history
    conversation_history.append({"role": "user", "content": input_message})

    # Collect all messages in the conversation history
    messages  = [message['content'] for message in conversation_history]

    # Call the OpenAI API to generate a response

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join(messages),
        max_tokens=2048,
        n=2,
        stop=None,
        temperature=0.7
    )

    # Add the AI's response to the conversation history
    answer = response.choices[0].text.strip()
    conversation_history.append({"role": "assistant", "content": answer})

    return conversation_history

if __name__ == '__main__':
    st.title("Ask Me Anything")
    st.subheader("This uses the OpenAI API")

    def add_bg_from_url():
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?size=626&ext=jpg&ga=GA1.2.1157880480.1680745821&semt=sph");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
        )

    add_bg_from_url()

    input_message = st.text_input("Ask Chat GPT anything")

    if input_message:
        conversation_history = chat(input_message)

        # Display the conversation history
        for message in conversation_history:
            if message["role"] == "user":
                st.write("You: " + message["content"])
            elif message["role"] == "assistant":
                st.write("ChatGPT: " + message["content"])