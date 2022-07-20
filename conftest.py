import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, ....(etc.)")

@pytest.mark.parametrize('language', ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                            "pt-br", "ro", "ru", "sk", "uk", "zh-cn"])

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    print("Fixture received language from options and it is: " + str(language))
    return(language)

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(executable_path = "F:\\pythonProject1\\driver\\chromedriver.exe",options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("cd ..start firefox browser for test..")
        browser = webdriver.Firefox(executable_path = "F:\\pythonProject1\\driver\\geckodriver.exe", firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()