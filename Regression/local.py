from selenium import webdriver
import platform

import example

# baseUrl = "https://www.moneyhelper.org.uk"
# baseUrl = "https://test.moneyhelper.org.uk"
baseUrl = "https://moneyhelper-tools.netlify.app"
# baseUrl = "https://deploy-preview-49--moneyhelper-tools.netlify.app"

if platform.system() == "Darwin":
    # browser = "Safari"
    # driver = webdriver.Safari()
    browser = "Chrome"
    driver = webdriver.Chrome("../Webdrivers/chromedriver_mac_105")
else:
    browser = "Edge"
    DRIVER_BIN = "..\Webdrivers\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=DRIVER_BIN)
    print("Testing on PC")

# Specify tests
tests = {
    "Example" : example,
}

# Run
for key, value in tests.items():
    print('> Testing {}\n'.format(key))
    value.runTest(baseUrl, driver, browser)
    print('\n> End of {} test\n'.format(key))

driver.close()
