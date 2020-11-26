import pytest
from selenium import webdriver




def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome"
    )


@pytest.fixture(scope="class")
def setUp (request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\demir\\Python\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path = "C:\\Users\\demir\\Python\\geckodriver.exe")
    elif browser_name == "IE":
        #fix it later
        driver = webdriver.Edge(executable_path="C:\\Users\\demir\\Python\\edgedriver.exe")

    driver.maximize_window()
    driver.get("https://hr-testing.buffsci.org")
    request.cls.driver = driver
    yield
    driver.close()
