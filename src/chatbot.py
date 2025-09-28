import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from openai import OpenAI
import PyPDF2

# .env dosyasını yükle
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- Fonksiyonlar ---------------- #

def analyze_csv(file):
    df = pd.read_csv(file)
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "head": df.head().to_dict()
    }

def analyze_excel(file):
    df = pd.read_excel(file)
    return {
        "columns": list(df.columns),
        "shape": df.shape,
        "head": df.head().to_dict()
    }

def analyze_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:  # None değilse ekle
            text += page_text + "\n"
    return text

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen akıllı bir yardımcı botsun. "
                    "Kullanıcının yüklediği CSV, Excel veya PDF dosyasının içeriğini analiz edip sorulara cevap ver. "
                    "Eğer sorulan bilgi dosya içinde yoksa sadece 'Bilmiyorum' de. "
                    "Eğer kullanıcı yanlış bir bilgi çıkarıyorsa sadece 'Yanlış' de. "
                    "Bunun dışında ek açıklama yapma."
                )
            },
            {"role": "user", "content": prompt},
        ],
    )
    # Güvenli şekilde içerik al
    return response.choices[0].message.content

# ---------------- Streamlit Arayüz ---------------- #

st.title("📊 Dosya Analiz Chatbotu")

uploaded_file = st.file_uploader("Dosya yükle (CSV, Excel, PDF)", type=["csv", "xlsx", "xls", "pdf"])
user_input = st.text_input("Bir şey sor:")

if user_input:
    if st.button("Gönder"):
        if uploaded_file:
            if uploaded_file.name.endswith(".csv"):
                file_info = analyze_csv(uploaded_file)
                st.write("📂 CSV Analizi:", file_info)
                prompt = f"Kullanıcı sorusu: {user_input}\nCSV bilgisi: {file_info}"
                answer = ask_llm(prompt)

            elif uploaded_file.name.endswith((".xlsx", ".xls")):
                file_info = analyze_excel(uploaded_file)
                st.write("📂 Excel Analizi:", file_info)
                prompt = f"Kullanıcı sorusu: {user_input}\nExcel bilgisi: {file_info}"
                answer = ask_llm(prompt)

            elif uploaded_file.name.endswith(".pdf"):
                pdf_text = analyze_pdf(uploaded_file)
                st.write("📂 PDF ilk 500 karakter:", pdf_text[:500], "...")
                prompt = f"Kullanıcı sorusu: {user_input}\nPDF içeriği: {pdf_text[:1000]}"
                answer = ask_llm(prompt)

            else:
                answer = "Desteklenmeyen dosya türü."
        else:
            # Dosya yoksa sadece chatbot olarak çalış ve nasıl yardımcı olabileceğini vs sor..
            answer = ask_llm(user_input)

        st.write("🤖 Bot:", answer)
