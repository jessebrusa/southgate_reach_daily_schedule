from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time

class ReachAppDriver():

    def __init__(self, chromedriver_path):
        # service = Service(chromedriver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.website_url = 'https://build.reachcm.com/spark/6.13.0.0/#!/'


    def start_firefox(self):
        # Staring firefox removing unwanted tabs
        self.driver.get(self.website_url)
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        webroot_clickbox = self.driver.find_element(By.XPATH, '//*[@id="AutoOpenDisabled1"]')
        webroot_clickbox.click()
        webroot_approve = self.driver.find_element(By.XPATH, '//*[@id="allowButton"]')
        webroot_approve.click()
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])

    
    def start_chrome(self):
        self.driver.get(self.website_url)
        time.sleep(3)


    def reachapp_login_navigate_to_schedule(self, username, password):
    # Going to ReachApp webiste and logging in
        reach_username = username
        reach_password = password
        reach_login_username = self.driver.find_element(By.XPATH, '//*[@id="usernameInput"]')
        reach_login_username.send_keys(reach_username)
        reach_login_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/section[2]/form/div[3]/div/button')
        reach_login_button.click()
        time.sleep(1)
        reach_login_password = self.driver.find_element(By.XPATH, '//*[@id="passwordInput"]')
        reach_login_password.send_keys(reach_password)
        reach_login_password_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/div/div/div/section[3]/form/div[3]/div/button[2]')
        reach_login_password_button.click()
        time.sleep(5)

        schedule_side_bar_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div/ht-sidebar/div/div/section[3]/div/a')
        schedule_side_bar_button.click()
        time.sleep(2)

        # Switch Frames and navigate to Southgate Daily Schedule
        frame = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/iframe')
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(frame))

        daily_schedule_button = self.driver.find_element(By.XPATH, '//*[@id="main_ul"]/li[4]/a')
        daily_schedule_button.click()

        southgate_monitors = self.driver.find_element(By.XPATH, '//*[@id="container"]/table[1]/tbody/tr/td[1]/select/option[2]')
        southgate_monitors.click()


    def load_new_events(self, data_list, start_date_list, after_date_list):
        add_event_button = self.driver.find_element(By.XPATH, '//*[@id="xtrabtns"]/div[1]')
        num_events = len(data_list)
        for num in range(num_events):
            add_event_button.click()

        text_areas = self.driver.find_elements(By.XPATH, '//textarea[@name="info"]')
        num_text_areas = len(text_areas)
        start_text_area_num = num_text_areas - num_events

        data_counter = 0
        for text_area in text_areas[start_text_area_num:]:
            text_area.send_keys(data_list[data_counter])
            data_counter += 1
            
        start_date_counter = 0
        start_dates_elements = self.driver.find_elements(By.XPATH, '//input[@name="startdate"]')
        for start_date in start_dates_elements[start_text_area_num:]:
            start_date.send_keys(start_date_list[start_date_counter])
            start_date_counter += 1

        after_date_counter = 0
        after_dates_elements = self.driver.find_elements(By.XPATH, '//input[@name="deleteon"]')
        for after_date in after_dates_elements[start_text_area_num:]:
            after_date.send_keys(after_date_list[after_date_counter])
            after_date_counter += 1

        save_work_button = self.driver.find_element(By.XPATH, '//*[@id="main_ul"]/li[1]/a')
        save_work_button.click()


    def delete_old_events(self):
        current_date = datetime.now()
        formatted_month = str(current_date.month)
        formatted_day = str(current_date.day)
        today = f"{formatted_month}/{formatted_day}/{current_date.year}"

        after_dates_elements = self.driver.find_elements(By.NAME, 'deleteon')
        counter = 0
        num_to_delete = None
        for element in after_dates_elements:
            date = element.get_attribute('value')
            if date == today:
                num_to_delete = counter
                break
            counter += 1

        check_boxes = self.driver.find_elements(By.NAME, 'deleteevent')
        try:
            for check_box in check_boxes[:num_to_delete+1]:
                check_box.click()

            save_work_button = self.driver.find_element(By.XPATH, '//*[@id="main_ul"]/li[1]/a')
            save_work_button.click()

        except TypeError:
            pass