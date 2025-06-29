import streamlit as st
from helper import extract_text_from_pdf
from qa_chain import get_chunks, build_qa_chain

st.set_page_config(page_title="Chat with PDF", layout="wide")

st.title("📄 Chatbot with PDF")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    try:
        # Safely extract text
        text = extract_text_from_pdf(uploaded_file)
        chunks = get_chunks(text)
        qa = build_qa_chain(chunks)

        question = st.text_input("Ask a question:")
        if question:
            answer = qa.run(question)
            st.write("Answer:", answer)

    except Exception as e:
        st.error(f"❌ Something went wrong while processing your PDF.\n\nError: `{e}`")
