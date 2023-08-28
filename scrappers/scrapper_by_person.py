import time
from selenium.webdriver.common.by import By


def scrapper_by_person(driver):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    person = input("Enter the person username you want to steal from: ")
    follow_per_hashtag = int(input("Enter the number of the person you want to follow: "))
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
    search_input.send_keys(person)
    time.sleep(timeout_between_large)
    first_result = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/a/div')
    time.sleep(timeout_between_small)
    first_result.click()
    time.sleep(timeout_between_large)
    following_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
    time.sleep(timeout_between_small)
    following_button.click()
    time.sleep(timeout_between_large)
    persons_list_parent = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div')
    time.sleep(timeout_between_small)
    persons_list_childs = persons_list_parent.find_elements(By.XPATH, './/*')
    time.sleep(timeout_between_small)
    print(len(persons_list_childs))
