import pyautogui
import pyperclip
import time
import pytesseract
from PIL import Image
import google.generativeai as genai

# ======= SETTINGS =======
GEMINI_API_KEY = "YOUR API KEY"

# Coordinates (adjust for your screen)
app_x, app_y = 1473, 1050       # Click app to focus
region_start_x, region_start_y = 557, 153   # Screenshot start
region_width, region_height = 600, 800     # Size of capture region
input_x, input_y = 800, 1000    # Chat input box location

# ======= INITIALIZE GEMINI =======
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"E:\Program Files\Tesseract-OCR\tesseract.exe"

# ======= FUNCTION: CAPTURE & OCR WHATSAPP =======
def capture_and_extract_text():
    pyautogui.moveTo(app_x, app_y, duration=0.2)
    pyautogui.click()
    screenshot = pyautogui.screenshot(region=(region_start_x, region_start_y, region_width, region_height))
    text = pytesseract.image_to_string(screenshot, lang="eng").strip()

    # Try to split into sender and message
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    if len(lines) >= 2:
        sender = lines[0]
        message = " ".join(lines[1:])
    else:
        sender = "Unknown"
        message = text

    return sender, message

# ======= FUNCTION: GET GEMINI REPLY =======
def get_gemini_reply(text):
    try:
        prompt = f"You are me , replying to a WhatsApp message from my close college friend. \
We have a cool, fun, non-judgmental vibe and are well-bonded. Keep it casual, short, and natural.\n\nMessage:\n{text}"
        return model.generate_content(prompt).text.strip()
    except:
        return None

# ======= FUNCTION: TYPE REPLY IN WHATSAPP =======
def type_whatsapp_reply(reply):
    pyautogui.moveTo(input_x, input_y, duration=0.2)
    pyautogui.click()
    pyperclip.copy(reply)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

# ======= MAIN LOOP =======
last_message = ""

while True:
    sender, current_message = capture_and_extract_text()

    if not current_message:
        time.sleep(1)
        continue

    # Stop program if keyword is detected
    if current_message.lower().strip() == "exit":
        print("Exit command detected. Stopping bot.")
        break

    # Only reply if new message and not from you
    if current_message != last_message and sender.lower() != "you":
        last_message = current_message
        reply = get_gemini_reply(current_message)
        if reply:
            type_whatsapp_reply(reply)

    time.sleep(1)  # reduce CPU usage

