from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException

import re
import sys
import time


def scrapeTicker(ticker,driver):

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
    pe_ratio = driver.find_element(By.CSS_SELECTOR, '[data-field="trailingPE"]').text
    """
    eps = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EPS_RATIO-value"]').text
    earnings_date = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EARNINGS_DATE-value"]').text
    dividend_yield = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="DIVIDEND_AND_YIELD-value"]').text
    ex_dividend_date = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="EX_DIVIDEND_DATE-value"]').text
    year_target_est = driver.find_element(By.CSS_SELECTOR, '#quote-summary [data-test="ONE_YEAR_TARGET_PRICE-value"]').text
    """
    print(pe_ratio)

    stock = {}

    # stock price scraping logic omitted for brevity...

    # add the scraped data to the dictionary
    """
    stock['previous_close'] = previous_close
    stock['open_value'] = open_value
    stock['bid'] = bid
    stock['ask'] = ask
    stock['days_range'] = days_range
    stock['week_range'] = week_range
    stock['volume'] = volume
    stock['avg_volume'] = avg_volume
    stock['market_cap'] = market_cap
    stock['beta'] = beta
    """
    stock['pe_ratio'] = pe_ratio
    """
    stock['eps'] = eps
    stock['earnings_date'] = earnings_date
    stock['dividend_yield'] = dividend_yield
    stock['ex_dividend_date'] = ex_dividend_date
    stock['year_target_est'] = year_target_est
    """

    # Statistics scrapping

    driver.quit()

    """

    options = Options()
    options.add_argument('--headless=new')

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    url2 = f'https://finance.yahoo.com/quote/{ticker}/key-statistics'

    driver.get(url2)

    WebDriverWait(driver, 10).until(EC.url_to_be(url2))

    #main = driver.find_element(By.ID,'Col1-0-KeyStatistics-Proxy')
    main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'Col1-0-KeyStatistics-Proxy'))
    )

    #datos = main.find_elements(By.TAG_NAME,'tr')
    datos = WebDriverWait(main, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'tr'))
    )

    for dato in datos:
        #value = dato.find_element(By.CLASS_NAME,'Fw(500)')
        #a = WebDriverWait(dato, 10).until(
        #    EC.presence_of_all_elements_located((By.TAG_NAME, 'td'))
        #)
        a = dato.find_elements(By.TAG_NAME,'td')

        driver.implicitly_wait(5)

        key = a[0].text
        value = a[1].text

        # Cleaning column name
        if re.search(r"20\d\d", key):
            index = key.find('(')
            if key[index+1] == 'p':
                key = key[:index-1] + '_prior'
            else:
                key = key[:index-1]

        key = '_' + key

        replacing = {'/':'_', ' ':'_', '&':'_', '(':'_', ')':'_','-':'_', '%':'perc'}
        for rep in replacing:
            key = key.replace(rep,replacing[rep])
        if key[-1].isdigit() == True:
            key = key[:-2]



        stock[key] = value


        #print(dato.find_element(By.CLASS_NAME,'Fw(500) Ta(end) Pstart(10px) Miw(60px)').text)


    #forward_pe = driver.find_element(By.CSS_SELECTOR, '.Fw(500)').text

    #print

    driver.quit()

    """

    return stock
