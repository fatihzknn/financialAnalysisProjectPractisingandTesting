# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC



# chromeOptions = webdriver.ChromeOptions()

# # Secret Page
# chromeOptions.add_argument("--incognito")

# #driver definition
# driver = webdriver.Chrome(options=chromeOptions)
# driver.maximize_window() #fullscreen
# driver.delete_all_cookies()

# driver.get("https://tr.tradingview.com/chart/jFm9cqvX/?symbol=NASDAQ%3AAGLE")
# wait = WebDriverWait(driver, 30)  
# #driver.implicitly_wait(10) # wait until price

# while True:
#     try:
#         price_info = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]"))).text
#         print(price_info)
#     except Exception as e:
#         print(f"hata oluştu : {e}")
    

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# chromeOptions = webdriver.ChromeOptions()
# #chromeOptions.add_argument("--incognito")

# driver = webdriver.Chrome(options=chromeOptions)
# driver.maximize_window()
# driver.delete_all_cookies()

# url = "https://tr.tradingview.com/chart/jFm9cqvX/?symbol=NASDAQ%3AAGLE"
# driver.get(url)

# wait = WebDriverWait(driver, 10)

# try:
#     # Beklenen bir elementin yüklenmesini bekleyin (örneğin, fiyat bilgisi için bir element)
#     price_info = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]"))).text
#     print("Fiyat Bilgisi:", price_info)
# except Exception as e:
#     print("Hata oluştu:", e)
# finally:
#     driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver'ı başlat
driver = webdriver.Chrome()
driver.maximize_window()

# Siteye gidin (örneğin, TradingView)
driver.get("https://tr.tradingview.com/")

# Giriş yapma işlemleri
login_button = driver.find_element(By.XPATH, "//a[@data-name='button-signin']")
login_button.click()

# Kullanıcı adı ve şifre girme
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys("your_username")
password_input.send_keys("your_password")

# Giriş yapma butonuna tıklama
login_submit_button = driver.find_element(By.XPATH, "//button[@data-name='header-signin']")
login_submit_button.click()

# Giriş sonrası sayfanın yüklenmesini bekleyin (örneğin, bir elementin görünürlüğünü bekleyebilirsiniz)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='some-element']")))

# İstediğiniz sayfaya gidin (örneğin, bir grafik sayfasına)
driver.get("https://tr.tradingview.com/chart/jFm9cqvX/?symbol=NASDAQ%3AAGLE")

# Gerekli diğer işlemleri gerçekleştirin
# ...

# WebDriver'ı kapat
driver.quit()