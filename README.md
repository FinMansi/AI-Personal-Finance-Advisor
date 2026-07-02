# AI-Personal-Finance-Advisor

## Overview
This project is a chatbot that answers common personal finance questions such as:
- "What is compound interest?"
- "Explain SIP in simple terms."
- "What is the difference between mutual funds and stocks?"

It uses **Retrieval-Augmented Generation (RAG)** with a small finance knowledge base to provide clear, beginner-friendly answers.

## Features
- Simple question answering for finance FAQs
- Knowledge base stored in `data/finance_faqs.json`
- Easy to extend with more questions and answers
- Beginner-friendly setup (no deployment required)

## Project Structure
- `app.py` → Streamlit app interface
- `rag_pipeline.py` → RAG pipeline logic
- `data/finance_faqs.json` → Finance FAQs dataset
- `requirements.txt` → Dependencies

## How to Use
1. Clone the repository.
2. Add your own finance FAQs to `data/finance_faqs.json`.
3. (Optional) Run locally with:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
