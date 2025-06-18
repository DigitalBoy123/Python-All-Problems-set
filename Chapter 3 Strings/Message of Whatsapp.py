# import pywhatkit as pwk
# Phone_number = "+92333323405"
# Message = "Hi, this message was created by Python and sent to you through VS Code!"
 
# pwk.sendwhatmsg_instantly(Phone_number,Message)
import pywhatkit as pwk
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome WebDriver (automatic installation)
service = Service(ChromeDriverManager().install())
pwk.core.driver = webdriver.Chrome(service=service)

# Send WhatsApp message
try:
    pwk.sendwhatmsg_instantly(
        phone_no="+92333323405",  # With country code, no spaces
        message="Hello from Python!",
        tab_close=True,
        wait_time=15
    )
    print("Message sent successfully!")
except Exception as e:
    print(f"Error: {e}")





 
 