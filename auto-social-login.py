from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://instagram.com')
main_window = browser.current_window_handle
sleep(1)

#instagram
ig_user = browser.find_element_by_name('username')
ig_user.send_keys('YOUR USERNAME')

ig_pass = browser.find_element_by_name('password')
ig_pass.send_keys('YOUR PASSWORD')

submit = browser.find_element_by_tag_name('form')
submit.submit()

#opens new tab and switches focus
browser.execute_script('''window.open("","_blank");''')
tabs = browser.window_handles;
browser.switch_to.window(tabs[1]);

#twitter
browser.get('http://twitter.com/login')
sleep(1)

tw_user = browser.find_element_by_css_selector('input[type="text"]')
tw_user.send_keys('YOUR USERNAME')#username

tw_pass = browser.find_element_by_css_selector('input[type="password"]')
tw_pass.send_keys('YOUR PASSWORD')#password

submit = browser.find_element_by_tag_name('form')
submit.submit()

#opens new tab and switches focus
browser.execute_script('''window.open("","_blank");''')
tabs = browser.window_handles;
browser.switch_to.window(tabs[2]);

#linkedin
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
sleep(1)
link_user = browser.find_element_by_id('username')
link_user.send_keys('YOUR USERNAME')#username

link_pass = browser.find_element_by_id('password')
link_pass.send_keys('YOUR PASSWORD')#password

submit = browser.find_element_by_tag_name('form')
submit.submit()

#switches back to main window
browser.switch_to.window(main_window)
