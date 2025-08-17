import pyautogui
import pyperclip
import time

# ======= SETTINGS =======
# Coordinates (change to your needs)
app_x, app_y = 1473, 1050        # Position to click the app to focus
start_x, start_y = 557, 153    # Start selection position
end_x, end_y = 588, 947        # End selection position

# ======= SCRIPT =======

time.sleep(2)  # Give you time to switch to desktop before automation starts

# Step 1: Focus the app
pyautogui.moveTo(app_x, app_y, duration=0.5)
pyautogui.click()
time.sleep(0.5)

# Step 2: Go to start coordinate
pyautogui.moveTo(start_x, start_y, duration=0.5)
pyautogui.mouseDown()  # Hold click

# Step 3: Drag to end coordinate
pyautogui.moveTo(end_x, end_y, duration=0.5)
pyautogui.mouseUp()

# Step 4: Copy selection (Ctrl + C)
pyautogui.hotkey("ctrl", "c")
time.sleep(0.5)

# Step 5: Get clipboard content
text = pyperclip.paste()
print("Copied content:\n", text)
