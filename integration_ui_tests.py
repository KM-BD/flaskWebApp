from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_home_page(browser):
    browser.get('http://localhost:5000')
    assert 'Search' in browser.title

def test_search(browser):
    browser.get('http://localhost:5000')
    search_box = browser.find_element(By.NAME, 'search_term')
    search_box.send_keys('safe search')
    search_box.send_keys(Keys.RETURN)
    assert 'Search term: safe search' in browser.page_source
