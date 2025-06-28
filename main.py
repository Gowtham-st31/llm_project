import streamlit as st
from helper import extract_text_from_pdf
from qa_chain import get_chunks, build_qa_chain

st.title("📄 PDF Q&A Chatbot")

pdf = st.file_uploader("Upload PDF", type="pdf")
if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    text = extract_text_from_pdf("temp.pdf")
    chunks = get_chunks(text)
    qa = build_qa_chain(chunks)

    question = st.text_input("Ask a question from your PDF:")
    if question:
        answer = qa.run(question)
        st.write("Answer:", answer)
