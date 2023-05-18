import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pytest
from os.path import dirname, join
import time

# @pytest.yield_fixture(scope='session')
# def browser():
#     from selenium import webdriver
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


driver = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        extra.append(pytest_html.extras.url('https://color-pickerio.netlify.app/'))
        file_name = report.nodeid.replace("::", "_").replace("/","_")+".png"
        project_root = dirname(dirname(__file__))    
        paths=f"{project_root}/screenshots/{file_name}"
        time.sleep(7)
        driver.save_screenshot(paths)
        screenshot = driver.get_screenshot_as_base64() # the hero
        extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        options = FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options)
    yield driver
    driver.quit()
    return driver

