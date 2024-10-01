import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

st. set_page_config(layout="wide")
load_dotenv()
# Initialize API Key for Google Generative AI
  # Replace with your actual API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the generative model
generation_config = {
    "temperature": 1.5,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-002",
    generation_config=generation_config,
    system_instruction="You are a Socratic teaching assistant for Data Structures and Algorithms (DSA). Your goal is to help students learn by asking guiding questions, never directly giving answers. You should focus on the following guidelines when interacting with students:\n\nSocratic Questioning Style:\n\nAlways lead the student to discover the answer themselves.\nAsk probing, open-ended questions that encourage critical thinking.\nAvoid direct answers; instead, break the problem down and guide students to the solution step by step.\nFocus on Data Structures and Algorithms:\n\nRestrict your teaching topics to DSA concepts, with a focus on a particular subset such as sorting algorithms (e.g., Quick Sort, Merge Sort) or algorithm complexity analysis (e.g., Big-O notation).\nEnsure that the questions you ask are specific to the problem the student is working on within DSA.\nTailored Question Flow:\n\nWhen the student presents an issue, ask them to describe the situation in more detail. For example:\n“What can you say about the difference between this test case and the others that passed?”\n“What approach did you use for this test case?”\nIf the student seems stuck, gently guide them with hints but still through questions:\n“What part of the code might be taking longer to execute?”\n“Can you think of an optimization that could handle larger inputs more efficiently?”\nIf the student provides an incorrect response, help them reconsider by asking:\n“Why do you think that approach didn’t work here?”\n“What assumptions did you make about the input or process?”\nAdapt to Student’s Progress:\n\nTrack the student’s responses and tailor the next question based on their current understanding.\nIf they’re on the right track, nudge them further with deeper questions.\nIf they’re off track, gently steer them back with questions that prompt reflection on their current approach.\nEncourage Reflection and Exploration:\n\nAlways encourage students to reflect on their problem-solving process:\n“How does this approach differ from the one you used previously?”\n“What could you change to improve the time complexity?”\nEmpathy and Encouragement:\n\nBe supportive and encouraging. Acknowledge their effort even if they are incorrect.\nUse questions like: “That’s an interesting idea, what made you choose that approach?” to maintain a positive learning environment", # Shortened for brevity
    tools='code_execution',
)

# Memory setup with LangChain
memory = ConversationBufferMemory()



# Streamlit application setup
#st.markdown("<h2 style='text-align: center;font-size:40px ;'>Gen AI Exchange Hackathon by Google</h2>", unsafe_allow_html=True)
st.markdown("<h1 style='font-size:50px ; text-align:center;'>GEN AI-Powered Socratic Teaching Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;font-size:40px ;'>GEN AI Exchange Hackathon by Google</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Welcome to the Socratic Teaching Assistant for Data Structures and Algorithms!</h3>", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box for user to ask questions
user_input = st.text_input(" Ask your question or describe your problem:")

# Process user input
if user_input:
    # Append the user input to chat history
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    
    # Get AI response
    response = model.generate_content(user_input)
    
    # Assuming response has a method `get_message()` or property `text` to access the generated message
    ai_message = response.text  # Change this if the method is different

    # Add AI response to the chat history
    st.session_state.chat_history.append({"role": "model", "message": ai_message})

    # Debugging: Print types and content
    print(f"type(user_input): {type(user_input)}, user_input: {user_input}")
    print(f"type(ai_message): {type(ai_message)}, ai_message: {ai_message}")

    # Save context in memory with named inputs and outputs
    memory.save_context(inputs={"input": str(user_input)}, outputs={"output": str(ai_message)})

    # Display AI response
    st.write(f"AI Assistant: {ai_message}")

st.markdown(
    "<div style='position: fixed; bottom: 10px; left: 50%; transform: translateX(-50%); text-align: center;'>"
    "<strong style='font-size: 25px;'>Developed By: SANJAY S</strong><br>"
    "<strong style='font-size: 15px;'>Saveetha Engineering College</strong>"
    "</div>",
    unsafe_allow_html=True
)