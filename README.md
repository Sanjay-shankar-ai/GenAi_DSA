# GEN AI-Powered Socratic Teaching Assistant

## Live Demo
https://genai-socratic-teaching-assistant.streamlit.app/

## Overview
This project is a generative AI-powered teaching assistant focused on Data Structures and Algorithms (DSA). Built using Google's Gemini 1.5 Flash model, it employs Socratic questioning to guide students in their learning process without providing direct answers.

## Features
- Interactive Q&A: Students can ask questions about DSA concepts, and the assistant responds with probing questions to facilitate learning.
- Memory Management: Utilizes LangChain's ConversationBufferMemory to maintain context during interactions.
- Customizable System Instructions: Tailors the AI's behavior based on predefined system instructions to ensure a focused learning experience.

## Technologies Used
- **LangChain:** For chains, memory, and prompt management.
- **Google Generative AI:** Integration with the Gemini 1.5 Flash model.
- **Streamlit:** For creating a user-friendly web application interface.

## In-Scope
- Providing assistance in understanding DSA concepts through guided questioning.
- Maintaining a conversational context to enhance learning interactions.

## Out of Scope
- Directly answering questions or solving problems without engaging the student in critical thinking.
- Covering topics outside of Data Structures and Algorithms.

## Future Opportunities
- Expanding the assistant's capabilities to cover additional programming topics.
- Integrating user feedback to improve the questioning strategy.
- Developing a premium version with advanced features and increased API limits.

## Challenges
While building this project, we encountered limitations with the free Google API, particularly in terms of request limits and memory constraints. We explored different API keys and attempted model tuning in Google AI Studio but faced financial barriers. Ultimately, we worked around these challenges by optimizing our approach within the available resources.

## Getting Started
To run this project locally:
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. GEMINI_API_KEY=your_api_key_here
4. streamlit run app.py


