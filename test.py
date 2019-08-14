from io import BytesIO

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup as bs
from PIL import Image

LOGIN_URL = 'https://camp.xticket.kr/Web/Member/MemberLogin.json?member_id=haeseoky&member_password=yunhs1206&shopCode=217820482301'
BOOKING_URL = 'https://camp.xticket.kr/Web/Book/Book010001.json?product_group_code=0004&play_date=20190829&product_code=00040003&captcha=1&shopCode=217820482301'
CHECK_URL = 'https://camp.xticket.kr/Web/Book/GetBookProduct010001.json?product_group_code=0004&start_date=20190812&end_date=20190812&book_days=1&two_stay_days=0&shopCode=217820482301'
# https://camp.xticket.kr/Web/Book/Book010001.json?product_group_code=0004&play_date=20190829&product_code=00040003&captcha=1&shopCode=217820482301
# https://camp.xticket.kr/Web/Book/GetBookProduct010001.json?product_group_code=0004&start_date=20190812&end_date=20190812&book_days=1&two_stay_days=0&shopCode=217820482301



#
#
# with requests.Session() as s:
#     main = s.get('https://camp.xticket.kr/web/main?shopEncode=ff0ecee2292c6ef6976558aeb171cf2a172391f74de8d6f5f290b89b0a68213a')
#
#     login_res = s.post(LOGIN_URL)
#     print(login_res.json())
#
#     check_res = s.post(CHECK_URL)
#     print(check_res.json())
#
#     html = s.get('https://camp.xticket.kr/Web/jcaptcha')
#
#     print(html.text)
#     # driver = webdriver.Chrome('chromedriver')
#     # driver.get('https://camp.xticket.kr/Web/jcaptcha')
#     # png = driver.get_screenshot_as_png()
#     # im = Image.open(BytesIO(png))
#     # im.save('output.png')
#
#     # for cookie in driver.get_cookies():
#     #     s.cookies.set(cookie['name'], cookie['value'])
#     #
#     # driver.close()
#
#
#
#     # captcha = input("숫자4자리:")
#     #
#     # BOOKING_URL = 'https://camp.xticket.kr/Web/Book/Book010001.json?product_group_code=0004&play_date=20190829&product_code=00040003&captcha='+captcha+'&shopCode=217820482301'
#
#     bookgin_res = s.post(BOOKING_URL)
#     print(bookgin_res.json())
#






driver = webdriver.Chrome('chromedriver')

driver.implicitly_wait(0.1)
driver.get('https://camp.xticket.kr/web/main?shopEncode=ff0ecee2292c6ef6976558aeb171cf2a172391f74de8d6f5f290b89b0a68213a')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="notice_layer_485"]/div/div/div/fieldset/ul/li/button/img').click()

# driver.close()
# driver.quit()

# driver.find_element_by_name('txtMember').send_keys(member_num)
# time.sleep(0.5)
# driver.find_element_by_name('txtPwd').send_keys(password)
#

# response = requests.get('https://camp.xticket.kr/Web/Member/MemberLogin.json', data={'member_id': 'haeseoky','member_password': 'yunhs1206','shopCode': '21782048230'}).json();
#
# print(response)