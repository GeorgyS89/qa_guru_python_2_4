def print_function(func_name, *args):
    func_name = func_name.__name__.replace("_", " ").capitalize()
    print(func_name, *args)

def open_browser(browser_name):
    print_function(open_browser,  browser_name)

def go_to_company_name_homepage(page_url):
   print_function(go_to_company_name_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_function(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome')
go_to_company_name_homepage('https://www.pathofexile.com/')
find_registration_button_on_login_page('https://www.pathofexile.com/', 'Play free now!')
