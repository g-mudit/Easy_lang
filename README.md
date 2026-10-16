# 📚 PaperBhasha — Research Papers in Your Language

**Making scientific research accessible to everyone through AI-powered multilingual explanations.**

PaperBhasha is an AI-powered research paper summarizer that transforms complex academic papers into clear, structured, and easy-to-understand explanations in Hindi and other languages. Built using **Sarvam AI** and **Streamlit**, it helps students, researchers, and curious learners understand scientific research without struggling with language barriers or dense academic writing.

## ✨ Features

- **📄 PDF Upload:** Upload research papers in PDF format.
- **🌐 Multilingual Explanations:** Generate explanations in Hindi, English, Telugu, Tamil, Bengali, Marathi, Gujarati, Kannada, Malayalam, and Punjabi.
- **🎓 Customizable Explanation Levels:** Choose between beginner-friendly, university-level, and technical explanations.
- **🧠 Structured Summaries:** Organizes explanations into meaningful sections:
  - Paper title and main idea
  - Problem statement and motivation
  - Methodology explained step by step
  - Experiments and key results
  - Novel contributions
  - Limitations and open questions
  - Simple examples to clarify important concepts
  - Key takeaways
- **⬇️ Downloadable Output:** Download generated explanations as text files.
- **⚡ Simple Interface:** An interactive web application powered by Streamlit.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Sarvam AI | AI-powered summarization and multilingual explanations |
| PyMuPDF | Extracting text from PDF documents |

## ⚙️ How It Works

1. **Upload:** The user uploads a research paper in PDF format.
2. **Text Extraction:** PyMuPDF extracts selectable text from the document.
3. **Prompt Construction:** The extracted text is combined with instructions specifying the target language and explanation level.
4. **AI Processing:** Sarvam AI generates a structured explanation of the research paper.
5. **Display and Download:** The explanation is displayed in the browser and can be downloaded as a text file.

```text
Research Paper (PDF)
        ↓
   PyMuPDF
  Text Extraction
        ↓
 Prompt Construction
        ↓
    Sarvam AI
 Summarization + Translation
        ↓
  Streamlit Interface
        ↓
 Display and Download
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/PaperBhasha.git
cd PaperBhasha
```

### 2. Install dependencies

```bash
pip install streamlit pymupdf sarvamai
```

### 3. Configure your Sarvam API key

Obtain an API key from the [Sarvam AI Dashboard](https://dashboard.sarvam.ai/).

On Windows PowerShell:

```powershell
$env:SARVAM_API_KEY="your_api_key_here"
```

The application reads the key from the environment variable. Alternatively, configure Streamlit secrets if your implementation uses `st.secrets`.

**Security:** Never commit API keys or secret configuration files to GitHub.

### 4. Run the application

```bash
streamlit run app.py
```

Open the local URL provided by Streamlit in your browser.

## 📂 Project Structure

```text
PaperBhasha/
├── app.py             # Streamlit application
├── README.md          # Project documentation
└── .gitignore         # Excludes secrets and temporary files
```

## 🎯 Motivation

Scientific knowledge should not be limited by language or unnecessarily complicated academic writing. Many valuable research papers are difficult to access for readers who are unfamiliar with academic English or specialized terminology.

PaperBhasha aims to bridge this gap by using AI to make research more understandable, approachable, and accessible across languages.

## 🔮 Future Improvements

- **Text-to-Speech:** Listen to research explanations in the selected language.
- **Long-Paper Support:** Process lengthy research papers in chunks while preserving context.
- **Figure and Equation Understanding:** Extract insights from charts, diagrams, mathematical expressions, and tables.
- **Interactive Q&A:** Ask questions about an uploaded paper and receive answers grounded in its content.
- **Citation and Reference Extraction:** Identify important references and connect related research.
- **Export Options:** Support Markdown and PDF downloads.
- **OCR Support:** Handle scanned research papers and image-based PDFs.
- **Key Concept Extraction:** Generate glossaries and explain technical terminology.

## ⚠️ Limitations

- The current implementation extracts selectable text from PDFs; scanned documents may require OCR.
- The initial prototype limits the amount of extracted text sent to the model, so very long papers may not be summarized completely.
- Complex equations, figures, tables, and mathematical notation may not be fully preserved by text extraction.
- AI-generated explanations may omit nuances or contain inaccuracies. Important scientific claims should be verified against the original paper.
- API availability, usage limits, and costs depend on the Sarvam AI service and account.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## 📜 License

Choose an appropriate open-source license for your project, such as the MIT License, before distributing it.

---

**PaperBhasha — Understand research. Break language barriers.**
