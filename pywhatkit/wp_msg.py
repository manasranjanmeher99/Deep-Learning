
import pywhatkit as kit
import time

phone = ""

for i in range(5):  # Send 5 messages
    kit.sendwhatmsg_instantly(
        phone,
        f"Hello!",
        wait_time=15,
        tab_close=True,
        close_time=3
    )

    time.sleep(0)  # Wait before sending the next message