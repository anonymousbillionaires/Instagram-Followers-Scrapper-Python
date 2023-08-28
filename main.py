from scrappers.scrapper_from_hashtag import scrapper_from_hashtag
from scrappers.scrapper_unfollow import scrapper_unfollow
from selenium import webdriver


driver = webdriver.Chrome()

if __name__ == '__main__':
    print('Instagram Scrapper Application made by Anonymous')
    print('Options available: ')
    print('1.Scrapper followers by hashtag')
    print('2.Scrapper followers by another user (UNAVAILABLE)')
    print('3.Unfollow the scrapper followers list')
    chosen_option = int(input("Enter your chosen option: "))
    match chosen_option:
        case 1:
            scrapper_from_hashtag(driver)
        case 2:
            print('UNAVAILABLE')
        case 3:
            scrapper_unfollow(driver)
