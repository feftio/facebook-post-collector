from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
import sys
import time
import calendar
import urllib

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)


class CollectPosts(object):

    def __init__(self, ids=["oxfess"], file="posts.csv", depth=5, delay=2):
        self.ids = ids
        self.out_file = file
        self.depth = depth + 1
        self.delay = delay
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\webdriver\chromedriver.exe")


    def safe_find_element_by_id(self, elem_id):
        try:
            return self.browser.find_element_by_id(elem_id)
        except NoSuchElementException:
            return None

    def login(self, email, password):
        try:
            self.browser.get("https://www.facebook.com/login.php")
            self.browser.find_element_by_name('email').send_keys(email)
            self.browser.find_element_by_name('pass').send_keys(password)
            self.browser.find_element_by_id('loginbutton').click()
        except Exception as e:
            print("There was some error while logging in.")
            print(sys.exc_info()[0])
            exit()

    def query(self, q):
        # time.sleep(5)
        # q_url = f'https://www.facebook.com/search/posts/?q={q}'
        # self.browser.get(q_url)

        # last_height = self.browser.execute_script("return document.body.scrollHeight")
        # while True:
        #     self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(1)
        #     new_height = self.browser.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # posts = self.browser.find_elements_by_tag_name("a")
        # clean_posts = [post for post in posts if "search" not in post.get_attribute("href") and "posts" in post.get_attribute("href")]
        # hrefs = [post.get_attribute("href") for post in clean_posts if "posts" in post.get_attribute("href")]
        # table_data = []
        time.sleep(5)
        self.browser.get('https://www.facebook.com/airastana/posts/3850337125005659')
        try:
                time.sleep(5)
                # print(self.browser.find_elements_by_xpath("//*[@class='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q']").text)
                print(self.browser.find_element_by_xpath("//*[@class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4']").text)
                print(self.browser.find_element_by_xpath("//*[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a5q79mjw g1cxx5fr knj5qynh m9osqain']").text)
                time.sleep(5)
        except Exception as e:
            print(e)

        self.browser.close()
        return []


if __name__ == "__main__":
    f = CollectPosts()
    f.login("87770416021", "Idet2050!")
    data = f.query("hello")