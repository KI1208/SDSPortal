#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time

# Read Parameter
with open('input.json', 'r') as f:
    input = json.load(f)

for entry in input.keys():
    globals()["{0}".format(entry)] = input[entry]

# Function
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

def click_xpath(xpath):
    field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    field.click()
    wait.until(page_is_loaded)

def input_string_to_xpath(xpath, input):
    time.sleep(2)
    field = driver.find_element_by_xpath(xpath)
    field.send_keys(input)
    field.send_keys(Keys.TAB)
    wait.until(page_is_loaded)

def select_element_by_xpath(xpath, selector):
    time.sleep(3)  # このwaitがないと、要素を拾えない
    select_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    select_dropdown.click()
    try:
        select = Select(select_dropdown)
        select.select_by_index(selector) if selector.__class__ == int else select.select_by_visible_text(selector)
    except exceptions.StaleElementReferenceException:
        select_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        select = Select(select_dropdown)
        select.select_by_index(selector) if selector.__class__ == int else select.select_by_visible_text(selector)
    except:
        pass


# Preparation
driver = webdriver.Chrome("./chromedriver_20180619.exe")
driver.get("https://solutions.one.dell.com/sites/RAM/SitePages/Travel_Home.aspx")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

# Login
field = driver.find_element_by_xpath("//*[@id=\"input_1\"]")
field.send_keys(PASSWORD)
field.send_keys(Keys.ENTER)
wait.until(page_is_loaded)

# Create New Request
field = driver.find_element_by_xpath("//*[@id=\"caption1\"]")
field.click()
wait.until(page_is_loaded)

# Bypass Warning
try:
    click_xpath('//*[@id="DialogButton0"]')
except:
    pass

# Choose Non-Flight
click_xpath("//*[@id=\"ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_B6\"]")

# Input Form First Part
input_string_to_xpath("//*[@id=\"ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T3\"]", BADGENO)
input_string_to_xpath("//*[@id=\"ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0__customcontrol5_upLevelDiv\"]",
                      USERNAME)
select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D5"]', L4)
# select_element('ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D5', 11)
select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D6"]', SUBORG)
# select_element('ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D6', 7)
input_string_to_xpath("//*[@id=\"ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0__customcontrol2_upLevelDiv\"]", REPORTINGMANAGER)

# Second Part
select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D8"]', ORIGINCOUNTRY)
select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D9"]', DESTINATIONCOUNTRY)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T10"]', ORIGIN)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T11"]', DESTINATION)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T12"]', FROMDATE)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T14"]', NUMOFNIGHTS)

select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D19"]', REASON)
# select_element_by_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_D19"]', 2)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T20"]', CUSTOMER)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T21"]', COSTCENTER)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T23"]', PROJECTNUM)
input_string_to_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_T24"]', JUSTIFICATION)
click_xpath('//*[@id="ctl00_ctl34_g_567e2ca3_c1c7_45b1_924b_2cb1308ba234_FormControl0_V1_I1_B25"]')

driver.close()
driver.quit()
