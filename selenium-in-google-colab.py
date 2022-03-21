!apt update
!apt install chromium-chromedriver
!pip install selenium



from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

wd.get(“https://www.website.com")
