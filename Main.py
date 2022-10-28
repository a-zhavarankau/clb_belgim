# import requests, random, time
# from bs4 import BeautifulSoup as bs
# from bs4 import NavigableString, Comment
# from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# import pickle
import time

print("START!")

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}

# CHROME
options_chr = webdriver.ChromeOptions()
options_chr.add_argument("User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")
options_chr.add_argument("Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
options_chr.add_argument("Accept-Encoding=gzip, deflate")
options_chr.add_argument("Cache-Control=max-age=0")
options_chr.add_argument("Connection=keep-alive")
options_chr.add_argument("Content-Length=29")
options_chr.add_argument("Cookie=_ga_L2F9TNFWDK=GS1.1.1637420622.1.0.1637420625.0; _ga=GA1.1.519440560.1637420623; PHPSESSID=f451a52f60219b806ea24bab5d44184d")
options_chr.add_argument("Origin=http://clb.belgim.by")
# options_chr.add_argument("Referer=http://clb.belgim.by/login")  # [Maybe check if it's necessary]
options_chr.add_argument("Upgrade-Insecure-Requests=1")
options_chr.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")    # Additional setup

driver_chr = webdriver.Chrome(
    executable_path=r"C:\Clb_belgim_by\chromedriver.exe",
    options=options_chr
)

# # FIREFOX
# options_ff = webdriver.FirefoxOptions()
# options_ff.set_preference("user-agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0")
# options_ff.set_preference("accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8")
# options_ff.set_preference("Upgrade-Insecure-Requests", "1")
# # options_ff.set_preference("", "--headless")
#
# driver_ff = webdriver.Firefox(
#     executable_path=r"C:\Clb_belgim_by\geckodriver.exe",
#     options=options_ff
# )


try:
    # #checking for disable webdriver mode
    # driver_chr.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    # time.sleep(10)

    # Enter the site "clb.belgim.by"
    start_url = "http://clb.belgim.by/login"
    driver_chr.get(start_url)
    time.sleep(1)

    login_input = driver_chr.find_element_by_name("_username")
    login_input.clear()
    login_input.send_keys("41JavAL")

    pass_input = driver_chr.find_element_by_name("_password")
    pass_input.clear()
    pass_input.send_keys("41JavAL")
    time.sleep(1)

    enter_button = driver_chr.find_element_by_class_name("button_submit")
    enter_button.click()
    time.sleep(2)
    open_windows_addresses = driver_chr.window_handles
    print(open_windows_addresses)

    # # Save cookies
    # pickle.dump(driver_chr.get_cookies(), open("cookies", "wb"))

    # with open("Startpage.html", "w", encoding="utf-8") as file:
    #     file.write(requests.get(url=start_url, headers=headers).text)

    # Open search page
    orders = driver_chr.find_element_by_class_name("drop").click()
    wide_search = driver_chr.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/ul/li[2]/div/div/ul/li[7]/a").click()
    time.sleep(1)

    # enter necessary order
    order_numb = driver_chr.find_element_by_id("form_answerNumb")
    order_numb.send_keys("7269013")
    driver_chr.find_element_by_id("form_submit").click()
    time.sleep(1)

    # open new order's page if order exists
    try:
        driver_chr.find_element_by_partial_link_text("7269013").click()
    except:
        print("Check the order number")
    time.sleep(1)
    open_windows_addresses = driver_chr.window_handles
    print(open_windows_addresses)

    first_page = driver_chr.window_handles[0]
    last_page = driver_chr.window_handles[-1]

    print("Switching to the new page")
    # switching to the last window
    driver_chr.switch_to.window(last_page)
    time.sleep(1)
    current_url = driver_chr.current_url
    print(driver_chr.current_url)
    print(driver_chr.current_window_handle)

    driver_chr.get(current_url)
    # time.sleep(1)


    # Loading cookies
    # print("Loading cookies")
    # for cookie in pickle.load(open("cookies", "rb")):
    #     driver_chr.add_cookie(cookie)
    #     time.sleep(3)

    # print("Refreshing new page")
    # driver_chr.refresh()
    # time.sleep(5)


    try:
        device_string = driver_chr.find_element_by_xpath("//td[text()='01001001']")   # Warning: Depends on tag "td"
        device_parent = device_string.find_element_by_xpath("..")
        print("Parents class is: " + device_parent.get_attribute("class"))
        print("Device 'Уровень' found")
    except:
        print("Device '01001001' NOT found")
    # Get device link
    try:
        device_link = device_parent.find_element_by_class_name("preURL").get_attribute("href")
        print("Link: " + device_link)
    except:
        print("Not found class 'preURL'")

    # Open page for editing device data
    driver_chr.get(device_link)
    time.sleep(1)
    print("159")
    # area_char = driver_chr.find_element_by_class_name("cke_editable_themed")
    field_cal_char = driver_chr.find_element_by_id("cke_siorders_siordersMeasure")
    # location = area_char.location
    # size = area_char.size
    # w, h = size['width'], size['height']
    # print(area_char.get_attribute("class"))
    # print(location)
    # print(size)

    action = webdriver.common.action_chains.ActionChains(driver_chr)
    action.move_to_element_with_offset(field_cal_char, 34, 50)
    action.click()
    action.send_keys("U= 0.05°")
    action.perform()
    print("174")
    # button_renew = driver_chr.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/form/button")  # With Xpath
    button_renew = driver_chr.find_element_by_css_selector("#bcenter > form:nth-child(8) > button:nth-child(5)")
    button_renew.click()
    time.sleep(2)
    print("179")


    # Choice tab "Results of the order execution"
    driver_chr.find_element_by_id("ui-id-2").click()
    time.sleep(3)
    print("185")
    # Button "Enter execution result"
    butt_new_res = driver_chr.find_element_by_class_name("newResult")
    butt_new_res.click()
    print(189)
    time.sleep(2)


    driver_chr.get("http://clb.belgim.by/rbresault/" + device_link.split("/")[-2] + "/new")
    time.sleep(2)


    # Open page "Result. New notice creation"
    # Fill "Result code" and confirm
    # driver_chr.find_element_by_id("RbresaultCode").click().send_keys("3")
    field_res_code = driver_chr.find_element_by_id("RbresaultCode")
    print("201")
    time.sleep(1)
    # field_res_code.click()
    field_res_code.send_keys("3")
    driver_chr.find_element_by_id("rbresault").click()
    time.sleep(1)
    print("207")
    # Fill "Employee data" and confirm
    driver_chr.find_element_by_id("RbemployeeCode").send_keys("69")
    driver_chr.find_element_by_id("rbemployee").click()
    time.sleep(1)

    # Choose the date
    driver_chr.find_element_by_id("resault_resaultDate").click()
    driver_chr.find_element_by_xpath("/html/body/div[4]/div[1]/table/tbody/tr[4]/td[6]").click()

    # Fill sticker field
    driver_chr.find_element_by_id("resault_resaultStiker").send_keys("101000")

    # Click "Create" (submit)
    driver_chr.find_element_by_id("resault_submit").click()
    time.sleep(3)
    print("223")
    # Open new window "Creation of measurement category"
    # Choice "L DimMet"
    # driver_chr.find_element_by_xpath("//span[text()='L DimMet Линейные и угловые измерения']").click()
    # print("228")
    # driver_chr.find_element_by_id("cboxClose").click()
    SI_overview = driver_chr.find_element_by_xpath("//a[text()='К просмотру СИ']")
    SI_overview.click()
    print("231")
    time.sleep(5)
    SI_overview.click()
    time.sleep(5)
    print("235")

    time.sleep(10)
except Exception as e:
    print(e)
finally:
    driver_chr.close()
    driver_chr.quit()

# if __name__ = "__main__":
#     name.run()
