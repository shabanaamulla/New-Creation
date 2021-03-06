import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#import webdriver_manager.chrome import ChromeDriverManager
import time
#driver = webdrive.Chrome(ChromeDriverManager)().install()
driver = selenium.webdriver.Chrome(executable_path="C:\\Users\\Shabana\\Driver\\chromedriver.exe")
driver.get("https://rpmsoftware.com/hiring/2020/integration-test/form-edit.html")
driver.maximize_window()
driver.find_element_by_id("FL:_ctl0:_ctl3").send_keys("Isabel Britt")
driver.find_element_by_id("FL:_ctl1:_ctl4").send_keys("This is a test Employee Summary.")
def select_values (element, value):
    select = Select(element)
    select.select_by_visible_text(value)
Sel_dept = driver.find_element_by_id("FL:_ctl3:_ctl3")
select_values (Sel_dept,"Management")
driver.find_element_by_name("FL:_ctl4:_ctl3").send_keys("$50,000.00")
driver.find_element_by_xpath("//input[@id='FL_latTxt_5']").send_keys("34.833850°")
driver.find_element_by_xpath("//input[@id='FL_longTxt_5']").send_keys("106.748580°")
sel_work = driver.find_element_by_id("FL:_ctl6:_ctl3")
select_values (sel_work,"Headquarters")
driver.find_element_by_name("FL:_ctl8:_ctl3").click()

driver.find_element_by_xpath("//input[starts-with(@class, 'forMeasurement')]").send_keys("47")
Sel_unit = driver.find_element_by_xpath("//td[@id='Row0.Field500_12:Container']//select[contains(@class,'forMeasurement')]")
select_values(Sel_unit,"in" )
driver.find_element_by_id("FL__ctl3_9").click()
driver.find_element_by_xpath("//input[starts-with(@class, 'measurement')]").send_keys("21")
Sel_unit1 = driver.find_element_by_xpath("//td[@id='Row0.Field500_13:Container']//select[contains(@class,'forMeasurement')]")
select_values(Sel_unit1,"in" )

driver.find_element_by_xpath("//tbody/tr[@id='Row0:Container']/td[@id='Row0.Field500_14:Container']/div[1]/div[1]/div[1]/input[1]").send_keys("Brown")
driver.find_element_by_xpath("//tbody/tr[2]/td[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Ford")
driver.find_element_by_xpath("//tbody/tr[2]/td[3]/div[1]/div[1]/div[1]/input[1]").send_keys("Taurus")
driver.find_element_by_xpath("//body[1]/div[1]/div[1]/div[16]/span[2]/div[1]/table[1]/tbody[1]/tr[2]/td[4]/div[1]/div[1]/div[1]/input[1]").send_keys("2018")
driver.find_element_by_xpath("//tbody/tr[2]/td[5]/div[1]/div[1]/div[1]/input[1]").send_keys("SEL")
driver.find_element_by_xpath("//tbody/tr[2]/td[6]/div[1]/div[1]/div[1]/input[1]").send_keys("Black")
driver.find_element_by_xpath("//tbody/tr[2]/td[7]/div[1]/div[1]/div[1]/input[1]").send_keys("TEST-0001")

driver.find_element_by_xpath("//tbody/tr[3]/td[2]/div[1]/div[1]/div[1]/input[1]").send_keys("Ford")
driver.find_element_by_xpath("//tbody/tr[3]/td[3]/div[1]/div[1]/div[1]/input[1]").send_keys("F150")
driver.find_element_by_xpath("//tbody/tr[3]/td[4]/div[1]/div[1]/div[1]/input[1]").send_keys("2015")
driver.find_element_by_xpath("//tbody/tr[3]/td[5]/div[1]/div[1]/div[1]/input[1]").send_keys("XLT")
driver.find_element_by_xpath("//tbody/tr[3]/td[6]/div[1]/div[1]/div[1]/input[1]").send_keys("Red")
driver.find_element_by_xpath("//tbody/tr[3]/td[7]/div[1]/div[1]/div[1]/input[1]").send_keys("Test-0002")
driver.find_element_by_xpath("//input[@id='FL:_ctl8:_ctl3']").click()
driver.find_element_by_id("submit_form").click()
currentUrl= driver.current_url
print(currentUrl)
expectedUrl = ("https://rpmsoftware.com/hiring/2020/integration-test/form.html?")
assert currentUrl==expectedUrl