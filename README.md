
# 🤖 Automated Message Reply System

This project demonstrates an automated message reply system using Python.
For demonstration, WhatsApp has been used as an example platform to showcase how automation works, but the concept is not limited to WhatsApp. It can be adapted for other messaging or communication platforms as well.
---

## ✨ Features

* ✅ Auto-replies to WhatsApp messages with a casual, human-like tone
* ✅ Works with **Google Gemini API** for intelligent responses
* ✅ Text-to-Speech replies using **pyttsx3**
* ✅ Speech input support using **SpeechRecognition**
* ✅ Extensible – add more commands like opening websites, music, etc.

---


## 🛠 Tech Stack

* **Python 3.x** – Core programming language
* **PyAutoGUI** – Automating mouse & keyboard actions for WhatsApp Web
* **Pyperclip** – Copy-paste text handling between clipboard and app
* **Pytesseract (OCR)** – Extracting text from WhatsApp chat screenshots
* **Pillow (PIL)** – Image processing for OCR
* **Google Generative AI (Gemini API)** – Generating smart conversational replies
* **Time module** – Adding controlled delays for smooth execution

---


## 🚀 Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/SanjanaBanerjee101/Auto-reply-bot.git
   cd Auto-reply-bot
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key**
   Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your-secret-key-here
   ```

---

## ▶️ Usage

Run the bot:

```bash
python main.py
```

---

## 📂 Project Structure

```
Jarvis-1/
│── main.py          # Core bot logic
│── requirements.txt # Dependencies
│── .env             # API keys (not committed)
│── .gitignore       # Ignored files
│── README.md        # Documentation
```

---

## ⚠️ Disclaimer

This project is for **educational purposes**.
Automating WhatsApp might violate their terms of service – use responsibly.

📌 Note
This project uses WhatsApp only as an example to demonstrate the automation workflow.
It is not specifically a WhatsApp AI bot, and the same approach can be extended to other platforms.

📸WorkFlow
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/355f9cd8-c02c-48c5-9197-8eebe96a5ba0" />

