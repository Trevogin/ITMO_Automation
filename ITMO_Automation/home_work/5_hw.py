# Задача 1

print('Задача 1')

from selenium import webdriver
from selenium.webdriver.common.by import By

def test1():
    driver = webdriver.Chrome()
    driver.get('https://saucedemo.com')

    icon1 = driver.find_element(By.ID, "user-name")

    icon2 = driver.find_element(By.ID, "password")

    icon3 = driver.find_element(By.ID, "login-button")

    if icon1 and icon2 and icon3 is None:
        print('Элементы не найдены')
    else:
        print('Элементы найдены')

test1()


# Задача 2

# level_1 plate
# level_2 bento
# level_3 #fancy
# level_4 plate apple
# level_5 #fancy pickle
# level_6 .small
# level_7 orange.small
# level_8 bento orange.small
# level_9 plate, bento
# level_10 *
# level_11 plate *
# level_12 plate + apple
# level_13 bento ~ pickle
# level_14 plate > apple


# Задача 3

# level_1 //plate
# level_2 //bento
# level_3 //plate/apple
# level_4 //*
# level_5 //*/apple
# level_6 //plate[@id="fancy"]
# level_7 //plate/apple
# level_8 //*[@id="fancy"]/pickle
# level_9 //*[contains(@class,"small")]
# level_10 //orange[contains(@class, "small")]
# level_11 //bento/orange[contains(@class, "small")]
# level_12 //plate| //bento
# level_13 //plate/*
# level_14 //plate/following-sibling::apple