# https://opensea.io/asset/create
import os
import path = ("./img/token.png")
import path = ("./json/token.json")
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


# options = Options()
# options.add_argument("--start-maximized")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-gpu")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")


def create(driver, name, symbol, decimals, totalSupply, json, image, description, contract, tokenId):
    print("Create the token")
    driver.get("https://opensea.io/asset/create")
    time.sleep(2)
    # select the asset type
    asset_type = driver.find_element_by_xpath(
        "//*[@id='asset-type-erc20']/label")
    asset_type.click()
    # enter the token name
    token_name = driver.find_element_by_id("asset-name")
    token_name.send_keys(name)
    # enter the symbol
    token_symbol = driver.find_element_by_id("asset-symbol")
    token_symbol.send_keys(symbol)
    # enter the decimals
    token_decimals = driver.find_element_by_id("asset-decimals")
    token_decimals.send_keys(decimals)
    # enter the total supply
    token_supply = driver.find_element_by_id("asset-total-supply")
    token_supply.send_keys(totalSupply)
    # enter the contract address
    token_contract = driver.find_element_by_id("asset-contract-address")
    token_contract.send_keys(contract)
    # enter the token ID
    token_id = driver.find_element_by_id("asset-token-id")
    token_id.send_keys(tokenId)
    # upload the image
    token_image = driver.find_element_by_id("asset-image")
    token_image.send_keys(image)
    # enter the description
    token_description = driver.find_element_by_id("asset-description")
    token_description.send_keys(description)
    # click the create button
    create_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[2]")
    create_button.click()
    time.sleep(2)


def send(driver, token_id, to, amount):
    print("Send the token")
    driver.get("https://opensea.io/send")
    time.sleep(2)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # enter the receiver address
    receiver_address = driver.find_element_by_id("receiver-address")
    receiver_address.send_keys(to)
    # enter the amount
    amount_input = driver.find_element_by_id("amount")
    amount_input.send_keys(amount)
    # click the send button
    send_button = driver.find_element_by_xpath(
        "//*[@id='send-form']/div[7]/button[2]")
    send_button.click()
    time.sleep(5)


def add(driver, token_id):
    print("Add to wallet")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the add button
    add_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[2]")
    add_button.click()
    time.sleep(2)


def send(driver, token_id, to, amount):
    print("Send the token")
    driver.get("https://opensea.io/send")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # enter the receiver address
    receiver_address = driver.find_element_by_id("receiver-address")
    receiver_address.send_keys(to)
    # enter the amount
    amount_input = driver.find_element_by_id("amount")
    amount_input.send_keys(amount)
    # click the send button
    send_button = driver.find_element_by_xpath(
        "//*[@id='send-form']/div[7]/button[2]")
    send_button.click()
    time.sleep(5)


def add(driver, token_id):
    print("Add to wallet")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the add button
    add_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[2]")
    add_button.click()
    time.sleep(5)


def balance(driver, token_id):
    print("Check balance")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the balance button
    balance_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[3]")
    balance_button.click()
    time.sleep(5)


def remove(driver, token_id):
    print("Remove from wallet")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the remove button
    remove_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[4]")
    remove_button.click()
    time.sleep(5)


def claim(driver, token_id):
    print("Claim the token")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the claim button
    claim_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[5]")
    claim_button.click()
    time.sleep(5)


def claim(driver, token_id):
    print("Claim the token")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the claim button
    claim_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[5]")
    claim_button.click()
    time.sleep(5)


def send(driver, token_id, to, amount):
    print("Send the token")
    driver.get("https://opensea.io/send")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # enter the receiver address
    receiver_address = driver.find_element_by_id("receiver-address")
    receiver_address.send_keys(to)
    # enter the amount
    amount_input = driver.find_element_by_id("amount")
    amount_input.send_keys(amount)
    # click the send button
    send_button = driver.find_element_by_xpath(
        "//*[@id='send-form']/div[7]/button[2]")
    send_button.click()
    time.sleep(5)


def add(driver, token_id):
    print("Add to wallet")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the add button
    add_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[2]")
    add_button.click()
    time.sleep(5)


def balance(driver, token_id):
    print("Check balance")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the balance button
    balance_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[3]")
    balance_button.click()
    time.sleep(5)


def remove(driver, token_id):
    print("Remove from wallet")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the remove button
    remove_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[4]")
    remove_button.click()
    time.sleep(5)


def claim(driver, token_id):
    print("Claim the token")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the claim button
    claim_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[5]")
    claim_button.click()
    time.sleep(5)


def send(driver, token_id, to, amount):
    print("Send the token")
    driver.get("https://opensea.io/send")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # enter the receiver address
    receiver_address = driver.find_element_by_id("receiver-address")
    receiver_address.send_keys(to)
    # enter the amount
    amount_input = driver.find_element_by_id("amount")
    amount_input.send_keys(amount)
    # click the send button
    send_button = driver.find_element_by_xpath(
        "//*[@id='send-form']/div[7]/button[2]")
    send_button.click()
    time.sleep(5)


def claim(driver, token_id):
    print("Claim the token")
    driver.get("https://opensea.io/assets")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # click the claim button
    claim_button = driver.find_element_by_xpath(
        "//*[@id='asset-form']/div[7]/button[5]")
    claim_button.click()
    time.sleep(5)


def send(driver, token_id, to, amount):
    print("Send the token")
    driver.get("https://opensea.io/send")
    time.sleep(5)
    # enter the token id
    token_id_input = driver.find_element_by_id("token-id")
    token_id_input.send_keys(token_id)
    # enter the receiver address
    receiver_address = driver.find_element
