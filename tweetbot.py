
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import time

# webdriverのパス
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
# ツイッターにアクセス
driver.get("https://twitter.com/login")
# ログインIDとパスワード
ids = "@YOUR_TWIRRWE_ID"
pass_w = "YOUR_PASSWORD"

# つぶやく内容を記入
content = "pythonのseleniumでつぶやいています"

# ユーザ名、パスワードを入力
username = driver.find_element_by_name("session[username_or_email]")
password = driver.find_element_by_name("session[password]")
username.send_keys(ids)
password.send_keys(pass_w)
password.send_keys(keys.ENTER)

# 2秒待機
time.sleep(2)

# つぶやきを入力
tweet_text = driver.find_element_by_class_name("notranslate")
tweet_text.click()
tweet_text.send_keys(content)

# ツイートボタンをクリック
tweet_button = driver.find_element_by_xpath(
    '//*[@data-testid="tweetButtonInline"]')
tweet_button.click()
time.sleep(5)

# webdriverを閉じる
driver.quit()
