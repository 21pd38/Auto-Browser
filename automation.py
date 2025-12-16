import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_automation():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get('http://localhost:5000')
        time.sleep(1)
        
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
        
        username.send_keys('demo_user')
        time.sleep(0.5)
        password.send_keys('demo_pass')
        time.sleep(0.5)
        
        login_btn = driver.find_element(By.ID, 'login-btn')
        login_btn.click()
        time.sleep(1)
        
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(0.5)
        
        driver.execute_script('window.scrollBy(0, 300)')
        time.sleep(1)
        
        message_box = driver.find_element(By.ID, 'message-text')
        message_box.send_keys('This is an automated test message')
        time.sleep(0.5)
        
        send_btn = driver.find_element(By.ID, 'send-btn')
        send_btn.click()
        time.sleep(2)
        
        print('Automation completed successfully')
        
    except Exception as e:
        print(f'Error: {e}')
    
    finally:
        driver.quit()

if __name__ == '__main__':
    run_automation()