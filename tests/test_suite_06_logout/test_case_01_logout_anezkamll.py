from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test(selenium, base_url, variables):
    step_01_open_tested_page(selenium, base_url)
    step_02_click_on_login(selenium)
    step_03_fill_username(selenium, variables['username'])
    step_04_fill_password(selenium, variables['password'])
    step_05_click_submit(selenium)
    step_06_click_logout(selenium)
    
    verify_user_logged_out(selenium)

def step_01_open_tested_page(selenium, base_url):
    selenium.get(base_url)

    # zkontrolujeme, ze na strance je napis <h2>Log In</h2>
    el = selenium.find_element_by_tag_name('h1')
    assert 'All products' in el.text

    # # ExplicitWait - kdyz se nahravaji veci pomoci JavaScriptu a nereloadne se cela stranka
    # WebDriverWait(selenium, 2).until(
    #     EC.presence_of_element_located(
    #         (By.TAG_NAME, 'h1')
    #     )
    # )

def step_02_click_on_login(selenium):
    el = selenium.find_element_by_link_text('Login or register')
    el.click()

    # zkontrolujeme, ze na strance je napis <h2>Log In</h2>
    el = selenium.find_element_by_tag_name('h2')
    assert 'Log In' in el.text

    # # ExplicitWait - kdyz se nahravaji veci pomoci JavaScriptu a nereloadne se cela stranka
    # WebDriverWait(selenium, 2).until(
    #     EC.text_to_be_present_in_element(
    #         (By.TAG_NAME, 'h2'),
    #         'Log In'
    #      )
    # )


def step_03_fill_username(selenium, username):
    el = selenium.find_element_by_id('id_login-username')
    el.send_keys(username)


def step_04_fill_password(selenium, password):
    el = selenium.find_element_by_id('id_login-password')
    el.send_keys(password)


def step_05_click_submit(selenium):
    el = selenium.find_element_by_name('login_submit')
    el.click()
    
def step_06_click_logout(selenium):
    el = selenium.find_element_by_link_text('Logout')
    el.click()
    
def verify_user_logged_out(selenium):
    el = selenium.find_element_by_link_text('Login or register')
    assert "Login" in el.text
