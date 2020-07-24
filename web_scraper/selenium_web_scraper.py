from selenium import webdriver

# https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu


def start_firefox():
    my_browser = webdriver.Firefox()
    # send the browser to a specif URL
    my_browser.get('https://pitpietro.github.io/')
    # simulate the click on a link (and redirect to that link)
    about_element = my_browser.find_element_by_css_selector('div.list__item:nth-child(6) > article:nth-child(1) > h2:nth-child(1) > a:nth-child(1)')
    about_element.click()


if __name__ == '__main__':
    start_firefox()
    exit(0)
