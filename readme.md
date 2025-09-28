# 📊 Dosya Analiz Chatbotu

**Dosya Analiz Chatbotu**, CSV, Excel ve PDF dosyalarını analiz edebilen ve içeriklerine dayalı olarak kullanıcı sorularını yanıtlayabilen bir **Streamlit tabanlı chatbot uygulamasıdır**. OpenAI API kullanılarak dosya içeriği üzerinden LLM (Large Language Model) ile cevap üretme yeteneği sağlar.

---
## 📁 Proje Yapısı

```
LLM_CHATBOT/  
├─ Lib/                           # Sanal ortam kütüphaneleri  
│  └─ site-packages/  
│     ├─ pip/                     # pip kütüphanesi  
│     └─ pip-24.0.dist-info/      # pip metadata dosyaları  
├─ src/                           # Python kaynak kodları  
│  └─ chatbot.py                  # Streamlit tabanlı LLM chatbot uygulaması  
├─ pyvenv.cfg                     # Sanal ortam yapılandırma dosyası  
├─ requirements.txt               # Projede kullanılan Python paketleri  
└─ README.md                      # Proje dokümantasyonu ve kullanım kılavuzu
└─ chatbot.png                    # Chatbot çalışma ekranı görseli
```

---

## Özellikler

### Dosya Analizi
- CSV ve Excel dosyalarının sütunlarını, boyutunu ve ilk satırlarını analiz eder.
- PDF dosyalarının metin içeriğini çıkarır ve önizleme sağlar.

---

### Soru-Cevap
- Yüklenen dosya hakkında kullanıcı sorularını yanıtlar.
- Dosya içeriğine göre doğru ve bağlamsal cevap verir.
- Bilgi dosyada yoksa **“Bilmiyorum”**, yanlış bilgi varsa **“Yanlış”** yanıtını verir.

---

### Esnek Kullanım
- Dosya yüklemeden sadece sohbet botu olarak da çalışabilir.  
- Bu durumda bot sınırlı kalabilir; bazı sorulara yanıt veremeyebilir.  
- Bot, kullanıcıya "Nasıl yardımcı olabilirim?" sorusunu sorar veya "Lütfen bir dosya yükleyin" tarzı uyarılar verebilir.

---

## Gereksinimler
Python 3.10+ önerilir. Gerekli kütüphaneler:

```bash
pip install streamlit pandas openai python-dotenv PyPDF2
```
---

## Kurulum

1. Depoyu klonlayın veya indirin:

```bash
git clone <repo-linki>
```

2. .env dosyası oluşturun ve OpenAI API anahtarınızı ekleyin:

```bash
OPENAI_API_KEY="API_KEYİNİZİ_BURAYA_YAZIN"
```

3. Streamlit uygulamasını başlatın:

```bash
streamlit run src/chatbot.py
```

---

## Kullanım

- Tarayıcıda açılan uygulama ekranında dosya yükleyin (CSV, Excel veya PDF).
- "Bir şey sor:" kutusuna sorularınızı yazın.
- "Gönder" butonuna basarak botun yanıtını görüntüleyin.
- Dosya yüklemeden yalnızca chatbot olarak da sorular sorabilirsiniz.

---

## Kod Yapısı

| Fonksiyon | Açıklama |
|-----------|----------|
| `analyze_csv(file)` | CSV dosyalarını analiz eder. |
| `analyze_excel(file)` | Excel dosyalarını analiz eder. |
| `analyze_pdf(file)` | PDF dosyalarından metin çıkarır. |
| `ask_llm(prompt)` | OpenAI LLM kullanarak soruları yanıtlar. |
| Streamlit Arayüzü | Dosya yükleme ve soru-cevap arayüzü sağlar. |

---

##  Örnek Görüntü

![Chatbot Çalışma Ekranı](C:/Users/karad/Desktop/llm_chatbot/chatbot.png)

---

##  Geliştirilebilir Yönler

- Bazen cevaplar gecikmeli olarak geliyor veya chatbot dosya içeriğini tam olarak anlamayabiliyor.
- Çok detaylı sorularda yanıtı doğru çıkarmayabiliyor.
- Bazı durumlarda yanlış cevap verebiliyor.
Genel olarak performansı iyi olsa da, yanıtların doğruluk ve hızını artırmak için iyileştirmeler yapılabilir.