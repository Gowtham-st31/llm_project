import streamlit as st
from helper import extract_text_from_pdf
from qa_chain import get_chunks, build_qa_chain

st.title("📄 PDF Question Answering App")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    chunks = get_chunks(text)
    qa = build_qa_chain(chunks)

    question = st.text_input("Ask a question about the PDF:")

    if question:
        answer = qa.run(question)
        st.write("Answer:", answer)
