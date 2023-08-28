import time
from selenium.webdriver.common.by import By
from utils.read_followers_list import read_following_list


def scrapper_unfollow(driver):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    timeout_between_small = 2
    timeout_between_medium = 5
    timeout_between_large = 10
    timeout_between_unfollow = 30
    following_list = read_following_list()

    time.sleep(timeout_between_small)
    driver.get("https://www.instagram.com/")
    time.sleep(timeout_between_large)
    popup_agree_button = driver.find_element(By.XPATH,
                                             '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    time.sleep(timeout_between_small)
    popup_agree_button.click()
    time.sleep(timeout_between_small)
    username_input = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    time.sleep(timeout_between_small)
    username_input.send_keys(str(username))
    time.sleep(timeout_between_small)
    password_input = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    time.sleep(timeout_between_small)
    password_input.send_keys(str(password))
    login_button = driver.find_element(By.XPATH,
                                       '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
    time.sleep(timeout_between_small)
    login_button.click()
    time.sleep(timeout_between_large)
    profile_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div')
    time.sleep(timeout_between_small)
    profile_button.click()
    time.sleep(timeout_between_large)
    followers_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    time.sleep(timeout_between_small)
    followers_button.click()
    time.sleep(timeout_between_large)
    for person in following_list:
        search_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/input')
        time.sleep(timeout_between_small)
        search_input.send_keys(str(person))
        time.sleep(timeout_between_large)
        following_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/div/div/div/div/div[3]/div/button')
        time.sleep(timeout_between_small)
        following_button.click()
        time.sleep(timeout_between_small)
        unfollow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]')
        time.sleep(timeout_between_small)
        unfollow_button.click()
        time.sleep(timeout_between_small)
        clear_search_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[2]')
        time.sleep(timeout_between_small)
        clear_search_input.click()
        time.sleep(timeout_between_small)
        time.sleep(timeout_between_unfollow)


