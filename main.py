#from apscheduler.schedulers.blocking import BlockingScheduler
import sqlite3
import pandas as pd
from package.scraper import scrapeTicker
from package.dbWriter import writeRowTicker


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import logging

import re
import sys
import time

#from PyQt5.QtWidgets import QApplication, QMessageBox

"""
def show_popup():
    app = QApplication([])  # Create the application object
    msg = QMessageBox()
    msg.setWindowTitle("Finalizado script")
    msg.setIcon(QMessageBox.Information)
    msg.exec_()  # Show the message box
"""

def scrapeETF(ticker):
	options = Options()
	options.add_argument('--headless=new')

	driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    # initialize a web driver instance to control a Chrome window
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #driver.set_window_size(1920, 1080)

    # scraping logic...

    # build the URL of the target page
	url = f'https://finance.yahoo.com/quote/{ticker}'
	print(url)

	driver.get(url)

	"""
    previous_close = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PREV_CLOSE-value"]').text
    open_value = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="OPEN-value"]').text
    bid = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="BID-value"]').text
    ask = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="ASK-value"]').text
    days_range = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DAYS_RANGE-value"]').text
    week_range = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="FIFTY_TWO_WK_RANGE-value"]').text
    volume = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="TD_VOLUME-value"]').text
    avg_volume = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="AVERAGE_VOLUME_3MONTH-value"]').text
    market_cap = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="MARKET_CAP-value"]').text
    beta = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="BETA_5Y-value"]').text
    """
    #pe_ratio = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="PE_RATIO-value"]').text
	pe_ratio = driver.find_element(By.CSS_SELECTOR, 'ul.yf-mrt107 li:nth-child(11) span:nth-child(2)').text
	"""
    eps = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EPS_RATIO-value"]').text
    earnings_date = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EARNINGS_DATE-value"]').text
    dividend_yield = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DIVIDEND_AND_YIELD-value"]').text
    ex_dividend_date = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EX_DIVIDEND_DATE-value"]').text
    year_target_est = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="ONE_YEAR_TARGET_PRICE-value"]').text
    """
	print(pe_ratio)

	stock = {}

	stock['pe_ratio'] = pe_ratio


	driver.quit()

	return stock



activos = [['PYPL',['V','MA']],
			['KO',['PEP']],
			['BIMBOA.MX',[]],
			['VOO',[]],
			['VEA',[]],
			['VWO',[]],
			['VOOV',[]],
			['BAC',['C','JNJ','SAN']],
			['FXI',[]],
			['QQQ',[]],
			['VB',[]],
			['VNQ',[]],
	]

ETFs = ['VOO','VEA','VWO','VOOV','FXI','QQQ','VB','VNQ']

dfFinal = pd.DataFrame(columns = ['main','PE','competidor_1','PE1','competidor_2','PE2','competidor_3','PE3'])


for a in activos:

	df1 = pd.DataFrame([[None] * 8],columns = ['main','PE','competidor_1','PE1','competidor_2','PE2','competidor_3','PE3'])

	d1 = scrapeETF(a[0]) if a[0] in ETFs else scrapeTicker(a[0],"a")

	df1.iloc[0,0] = a[0]
	df1.iloc[0,1] = d1['pe_ratio']

	print(a[0] + ": " + d1['pe_ratio'])

	ind = 1

	for comp in a[1]:
		di = scrapeTicker(comp,"a")
		print(comp + ": " + di['pe_ratio'])
		df1.iloc[0,2*ind] = comp
		df1.iloc[0,2*ind+1] = di['pe_ratio']
		ind += 1

	dfFinal = pd.concat([dfFinal,df1],ignore_index=True)

dfFinal.to_csv("results.csv", index = False)



#show_popup()


