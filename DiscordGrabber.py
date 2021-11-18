#! /usr/bin/env python
# -*- coding: utf-8 -*-
from aiogram import Bot, types
import requests, time, asyncio, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

payload = {
    'email': '+79996080340',
    'password': 'Discord10741!'
}
chat_id = -1001712282702
TOKEN = "2107680068:AAEgBaE8uhEtNdS5VlZERzuZ2yoKNx2yyf4"
bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

driver = webdriver.Chrome()
driver.get("https://discord.com/login")
driver.find_element(By.NAME, "email").send_keys(payload["email"])
driver.find_element(By.NAME, "password").send_keys(payload["password"])
driver.find_element(By.XPATH, "//button/following-sibling::button").click()
# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Закрыть']")))
# time.sleep(1)
# driver.find_element(By.XPATH, "//button[@aria-label='Закрыть']").click()
# driver.find_element(By.XPATH, "//a[@href='/channels/@me/905764407257219113']").click()
time.sleep(1)
old_raw_messages = driver.find_element(By.XPATH, "//ol[@data-list-id='chat-messages']").find_elements(By.XPATH, "//li")
async def update():
    global old_raw_messages, chat_id
    raw_messages = driver.find_element(By.XPATH, "//ol[@data-list-id='chat-messages']").find_elements(By.XPATH, "//li")
    if(len(raw_messages) == len(old_raw_messages)):
        pass
    else:
        new_messages = list(set(raw_messages) - set(old_raw_messages))
        for msg in new_messages:
            print(msg.text)
            await bot.send_message(chat_id, text=msg.text.replace("play.upland.me","localhost"))
            # time.sleep(1)
    old_raw_messages = raw_messages
print("Бот запущен, все ОК!")
while True:
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(update())]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
input()
