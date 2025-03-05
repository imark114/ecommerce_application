import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# @pytest.mark.selenium
# def test_create_new_admin_user(creat_admin_user):
#     assert creat_admin_user.__str__() == "rakib"

@pytest.mark.selenium
def test_dashboard_admin_login(live_server,db_fixture_setup,chorome_browser_instance):
    browser = chorome_browser_instance
    browser.get("%s%s" % (live_server.url, "/admin/login"))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in"]')

    user_name.send_keys("rakib")
    user_password.send_keys("114")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source