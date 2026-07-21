import time
import webbrowser
import urllib.parse
import pyautogui

phone = ""
messages = [
    "Hello",
    "How are you?",
    "Good Morning",
    "Have a nice day"
]


def send_messages_single_tab(phone_number, messages_list):
    first_message = messages_list[0]
    url = f"https://web.whatsapp.com/send?phone={phone_number}&text={urllib.parse.quote(first_message)}"
    webbrowser.open(url)
    print("Opening WhatsApp Web chat in a single tab...")

    time.sleep(15)
    pyautogui.press("enter")
    print(f"Sent first message: {first_message}")

    for message in messages_list[1:]:
        time.sleep(2)
        pyautogui.write(message, interval=0.05)
        pyautogui.press("enter")
        print(f"Sent: {message}")


if __name__ == "__main__":
    send_messages_single_tab(phone, messages)