from selenium.webdriver.common.by import By
from importlib.machinery import SourceFileLoader

page_slug = 'example-page'
locales = {
    "en",
    "cy"
}

dev_mode = True

# Selectors
selector = 'body'

def runTest(baseUrl, driver, browser):
    print("Running example test")

    for locale in locales:
        iteration_url = f'{baseUrl}/{locale}'
        print(f'- Visiting {iteration_url}')
        driver.get(iteration_url)
