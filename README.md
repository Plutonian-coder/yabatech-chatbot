# 🎓 Yabatech AI Chatbot

An intelligent chatbot assistant built with NLTK and Streamlit to serve the students, staff, and visitors of Yaba College of Technology. It answers common questions about admissions, departments, school fees, campus life, and more.

---

## 🚀 Features

- Conversational UI powered by NLTK pattern matching  
- User-friendly interface with Streamlit  
- Clean homepage with Yabatech branding  
- Interactive chat layout (User: left, Bot: right)  
- Instant feedback and local response processing  
- Fully offline, no API keys or internet required  

---

## 📚 Dataset

All chatbot responses are based on a cleaned CSV file: `yabatech_chatbot_cleaned.csv`, containing regex patterns and corresponding answers.

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/yabatech-chatbot.git
cd yabatech-chatbot

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the chatbot
streamlit run app.py

yabatech-chatbot/
├── app.py                      # Main chatbot interface
├── yabatech_chatbot_cleaned.csv  # Chatbot knowledge base
├── yabatech_image.png         # School logo for branding
├── requirements.txt           # Python dependencies
└── README.md

💬 Example Questions
"What are the admission requirements?"

"How do I pay my school fees?"

"Where is the computer science department?"

"When is the next semester starting?"

🧠 Technologies Used
Python

Streamlit

NLTK

Pandas

🌐 Live Preview (Optional)
If deployed with Streamlit Cloud:
https://yabatech-chatbot.streamlit.app/

📜 License
MIT License. Free to use, modify, and distribute.

🌟 Credits
Developed by Yekini Khalid Kolawole as a chatbot project for Yaba College of Technology.
