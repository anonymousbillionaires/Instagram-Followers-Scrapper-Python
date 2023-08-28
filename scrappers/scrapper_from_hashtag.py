import time
import numpy as np
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.check_exist_by_xpath import check_exists_by_xpath


def scrapper_from_hashtag(driver):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashtag = input("Enter your hashtag: ")
    follow_per_hashtag = int(input("Enter your number of followers you want per hashtag: "))
    timeout_between_small = 2
    timeout_between_medium = 5
    timeout_between_large = 10
    timeout_between_likes = 30
    following_list = []

    time.sleep(timeout_between_small)
    driver.get("https://www.instagram.com/")
    time.sleep(timeout_between_large)
    popup_agree_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
    time.sleep(timeout_between_small)
    popup_agree_button.click()
    time.sleep(timeout_between_small)
    username_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
    time.sleep(timeout_between_small)
    username_input.send_keys(str(username))
    time.sleep(timeout_between_small)
    password_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
    time.sleep(timeout_between_small)
    password_input.send_keys(str(password))
    login_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
    time.sleep(timeout_between_small)
    login_button.click()
    time.sleep(timeout_between_large)
    search_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div')
    time.sleep(timeout_between_small)
    search_button.click()
    time.sleep(timeout_between_large)
    search_input = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/input')
    time.sleep(timeout_between_small)
    search_input.send_keys(hashtag)
    time.sleep(timeout_between_large)
    first_result = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div')
    time.sleep(timeout_between_small)
    first_result.click()
    time.sleep(timeout_between_large)
    first_element_from_results = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]')
    time.sleep(timeout_between_small)
    first_element_from_results.click()
    time.sleep(timeout_between_large)
    if check_exists_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div', driver):
        follow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
        time.sleep(timeout_between_small)
        follow_button.click()
        time.sleep(timeout_between_small)
        following_person = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div/div/div/span/div/div/a')
        time.sleep(timeout_between_small)
        following_list.append(following_person.text)
        time.sleep(timeout_between_small)
        follow_per_hashtag = follow_per_hashtag - 1
        time.sleep(timeout_between_likes)
    while follow_per_hashtag > 0:
        html_element = driver.find_element(By.TAG_NAME, 'html')
        time.sleep(timeout_between_small)
        html_element.send_keys(Keys.ARROW_RIGHT)
        time.sleep(timeout_between_small)
        if check_exists_by_xpath('/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div', driver):
            follow_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div')
            time.sleep(timeout_between_small)
            follow_button.click()
            time.sleep(timeout_between_small)
            following_person = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div/div/div/span/div/div/a')
            time.sleep(timeout_between_small)
            following_list.append(following_person.text)
            time.sleep(timeout_between_small)
            follow_per_hashtag = follow_per_hashtag - 1
            time.sleep(timeout_between_likes)
    with open('following_list.txt', 'w') as f:
        json.dump(following_list, f)
    arr = np.array(following_list)
    file = open("following_list_numpy", "wb")
    np.save(file, arr)
    file.close()
