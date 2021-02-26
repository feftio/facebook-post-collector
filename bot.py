from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import sys,time

chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)

class CollectPosts(object):
    
    def __init__(self, ids=["oxfess"], file="posts.csv", depth=5, delay=2):
        self.ids = ids
        self.out_file = file
        self.depth = depth + 1
        self.delay = delay
        # browser instance
        # self.browser = webdriver.Firefox(executable_path=GECKODRIVER,
        #                                  firefox_binary=FIREFOX_BINARY,
        #                                  firefox_profile=PROFILE,)
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="chromedriver/chromedriver.exe")

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
        time.sleep(3)
        q_url = f'https://www.facebook.com/search/posts/?q={q}'
        self.browser.get(q_url)

        # Scrolling
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(1)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If heights are the same it will exit the function
                break
            last_height = new_height

        posts = self.browser.find_elements_by_tag_name("a")
        clean_posts = [post for post in posts if ("search" not in post.get_attribute("href") and "posts" in post.get_attribute("href")) or "permalink" in post.get_attribute("href")]
        print(len(clean_posts))
        hrefs = [post.get_attribute("href") for post in clean_posts]
        table_data = []
        for i, href in enumerate(clean_posts):
            try:
                if href.text != '':
                    post_dict = {}
                    href.click()
                    time.sleep(4)
                    post_dict['post_author'] = self.browser.find_element_by_xpath("//*[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh m9osqain hzawbc8m']").text
                    post_dict['post_date'] = self.browser.find_element_by_xpath("//*[@class='b6zbclly myohyog2 l9j0dhe7 aenfhxwr l94mrbxd ihxqhq3m nc684nl6 t5a262vz sdhka5h4']").text
                    post_dict['post_text'] = self.browser.find_element_by_xpath("//*[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m']").text
                    post_dict['post_url'] = hrefs[i]

                    table_data.append(post_dict)
                    self.browser.execute_script("window.history.go(-1)")
                    time.sleep(2)
            except Exception as e:
                print(e)

        self.browser.close()
        return table_data








