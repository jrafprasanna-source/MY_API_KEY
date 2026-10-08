import streamlit as st
from groq import Groq

# -----------------------------------
# GROQ API KEY
# -----------------------------------

GROQ_API_KEY = "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"

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)


# -----------------------------------
# STREAMLIT PAGE
# -----------------------------------

st.set_page_config(
    page_title="Groq AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 Groq AI Chatbot")
st.write("Chat with Groq AI using Python and Streamlit")


# -----------------------------------
# CHAT HISTORY
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful and friendly AI assistant."
        }
    ]


# -----------------------------------
# DISPLAY OLD MESSAGES
# -----------------------------------

for message in st.session_state.messages:

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------------
# USER INPUT
# -----------------------------------

user_message = st.chat_input("Type your message here...")


if user_message:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_message)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    try:

        # Send conversation to Groq
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=st.session_state.messages,
            temperature=0.7,
            max_completion_tokens=1024
        )

        # Get AI response
        ai_response = response.choices[0].message.content

        # Show AI response
        with st.chat_message("assistant"):
            st.markdown(ai_response)

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

    except Exception as e:

        st.error("Something went wrong!")
        st.write(e)


# -----------------------------------
# SIDEBAR
# -----------------------------------

with st.sidebar:

    st.header("⚙️ Settings")

    st.write("### About")

    st.write(
        "This chatbot is built using "
        "Python, Groq API and Streamlit."
    )

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a helpful and friendly AI assistant."
            }
        ]

        st.rerun()