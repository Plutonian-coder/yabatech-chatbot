import streamlit as st
import pandas as pd
import openai
from nltk.chat.util import Chat, reflections

# ==================== CONFIG ====================
st.set_page_config(page_title="Yabatech Assistant", page_icon="🎓", layout="centered")

# Load CSV responses (fallback)
data = pd.read_csv("yabatech_chatbot_1000.csv")
csv_pairs = [[row["Pattern"], [row["Response"]]] for _, row in data.iterrows()]
local_chatbot = Chat(csv_pairs, reflections)

# Set your OpenAI key (secure method recommended in prod)
openai.api_key = st.secrets.get("OPENAI_API_KEY") or "YOUR_OPENAI_API_KEY"

# ==================== STYLING ====================
chatgpt_css = """
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}
.chat-bubble {
    padding: 10px 16px;
    border-radius: 12px;
    margin: 8px 0;
    display: inline-block;
    max-width: 80%;
}
.user {
    background-color: #DCF8C6;
    align-self: flex-end;
    text-align: right;
}
.bot {
    background-color: #EAEAEA;
    align-self: flex-start;
}
</style>
"""

st.markdown(chatgpt_css, unsafe_allow_html=True)

# ==================== PAGE CONTROL ====================
if "page" not in st.session_state:
    st.session_state.page = "main"

# ==================== LANDING PAGE ====================
def main_page():
    st.image("https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Yabatech_logo.png/220px-Yabatech_logo.png", width=120)
    st.title("Yabatech Assistant FAQ")
    st.subheader("Labore et Veritate")
    st.write("Welcome to the Yaba College of Technology Virtual Assistant.")
    st.write("Click below to begin your chat.")
    if st.button("🚀 Start Chat"):
        st.session_state.page = "chat"

# ==================== CHAT PAGE ====================
def chat_page():
    st.title("🎓 Yabatech Assistant Chat")
    st.sidebar.title("Settings")
    dark_mode = st.sidebar.toggle("🌗 Dark Mode", value=False)

    # Apply dark mode (simple)
    if dark_mode:
        st.markdown(
            """<style>
            body { background-color: #1E1E1E; color: #FFF; }
            </style>""",
            unsafe_allow_html=True,
        )

    # Message history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat display
    for entry in st.session_state.messages:
        speaker, msg = entry
        bubble_class = "user" if speaker == "You" else "bot"
        st.markdown(f"<div class='chat-container'><div class='chat-bubble {bubble_class}'>{msg}</div></div>", unsafe_allow_html=True)

    # User input
    with st.form("chat_input", clear_on_submit=True):
        user_input = st.text_input("You:", placeholder="Ask your question about Yabatech...")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.messages.append(("You", user_input))

        # First try ChatGPT
        try:
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.3
            )
            bot_reply = gpt_response.choices[0].message["content"].strip()
        except:
            # If API fails, fallback to local chatbot
            bot_reply = local_chatbot.respond(user_input.strip().lower()) or "🤖 Sorry, I didn’t understand that. Can you rephrase?"

        st.session_state.messages.append(("Bot", bot_reply))

# ==================== ROUTER ====================
if st.session_state.page == "main":
    main_page()
else:
    chat_page()
