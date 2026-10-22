# Chatbot-using-RAG_LLM
# TCS PDF Chatbot using RAG, LLM, and LangChain

## 📌 Project Overview

This project is an AI-powered chatbot that answers user questions based on information extracted from a TCS (Tata Consultancy Services) company PDF document. It uses **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, and **LangChain** to retrieve relevant information from the document and generate context-based answers.

Instead of relying only on the LLM's pre-trained knowledge, the chatbot retrieves relevant document content to provide more relevant and document-grounded responses.

## 🎯 Objectives

- Build a chatbot that answers questions from a TCS company PDF.
- Extract and process PDF text for efficient retrieval.
- Generate embeddings to represent document content.
- Retrieve relevant text chunks based on user queries.
- Use an LLM to generate answers using the retrieved context.
- Reduce unsupported answers by grounding responses in the provided document.

## 🛠️ Technologies Used

- **Python** – Core programming language
- **LangChain** – Document processing and RAG pipeline
- **LLM** – Generates natural-language responses
- **Groq API** – LLM inference, if configured in the project
- **PDF Loader** – Extracts text from the PDF document
- **Text Splitter** – Splits document content into smaller chunks
- **Embeddings** – Converts text into numerical vectors
- **Vector Database** – Stores and retrieves document embeddings, such as FAISS or Chroma

## ⚙️ How It Works

1. **PDF Upload:** Load the TCS company PDF document.
2. **Text Extraction:** Extract readable text from the PDF.
3. **Text Chunking:** Split the extracted text into smaller, manageable chunks.
4. **Embedding Generation:** Convert the chunks into vector representations.
5. **Vector Storage:** Store the embeddings in a vector database.
6. **Question Retrieval:** Search for chunks relevant to the user's question.
7. **Answer Generation:** Pass the retrieved context and user question to the LLM.
8. **Display Response:** Return the generated answer to the user.

## 🏗️ System Architecture

```text
TCS Company PDF
       |
       v
   PDF Loader
       |
       v
  Text Extraction
       |
       v
   Text Splitter
       |
       v
 Embedding Model
       |
       v
 Vector Database
       |
       v
  User Question
       |
       v
 Relevant Document Retrieval
       |
       v
 Retrieved Context + Question
       |
       v
      LLM
       |
       v
 Generated Answer
```

## 💡 Example Use Case

**Document:** TCS company PDF

**User Question:**
> What services does TCS provide?

**Chatbot Response:**
> The chatbot retrieves the relevant section from the uploaded TCS PDF and generates an answer describing the services mentioned in that document.

*Note: The actual answer depends on the contents of the PDF.*

Other example questions:

- What is the history of TCS?
- What are the major business areas of TCS?
- What technologies or services are mentioned in the document?
- What information does the PDF provide about TCS?
- Summarize the key points from the document.

## 🚀 Key Features

- PDF-based question answering
- Context-aware responses using RAG
- Semantic search through document embeddings
- LLM-powered natural-language answers
- Reusable pipeline for other company documents
- Reduced reliance on the LLM's general knowledge

## 📂 Project Structure

```text
GenAIProject/
│
├── GenAiproject/
│   ├── chatbot.ipynb
│   └── genaieg3.ipynb
│
├── .gitignore
├── requirements.txt
└── README.md
```

*Adjust the structure above to match the actual files in your repository.*

## 🔧 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/SaiAmulya13/Chatbot-using-RAG_LLM.git
cd Chatbot-using-RAG_LLM
```

### 2. Create a virtual environment

```bash
python -m venv GenAI
```

Activate it on Windows PowerShell:

```powershell
.\GenAI\Scripts\Activate.ps1
```

### 3. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your implementation. For example:

```bash
pip install langchain langchain-community langchain-groq pypdf
```

Additional packages may be needed depending on your embedding model, vector database, and interface.

### 4. Configure the API key

If you use Groq, create a `.env` file in your project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Load the key from an environment variable in Python. Never upload your actual API key to GitHub.

### 5. Run the project

If your project is implemented in Jupyter Notebook, launch Jupyter:

```bash
pip install notebook
jupyter notebook
```

Open `chatbot.ipynb` and execute the notebook cells in order. Follow the notebook's instructions to load the TCS PDF and ask questions.

## 📈 Expected Outcome

The chatbot enables users to query a company PDF using natural language. It retrieves relevant document passages and uses an LLM to generate readable answers grounded in the retrieved information.

## 🔮 Future Enhancements

- Support multiple PDF documents.
- Add source citations for generated answers.
- Develop a Streamlit web interface.
- Store embeddings for reuse across sessions.
- Improve retrieval accuracy through reranking.
- Add conversation history and follow-up questions.

## 👩‍💻 Author

**Sai Amulya**

GitHub: [SaiAmulya13](https://github.com/SaiAmulya13)
