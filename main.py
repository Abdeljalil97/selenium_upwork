from selenium import webdriver
from selenium.webdriver.common.by import By
from shutil import which
from base_commponents.base_page import BasePage
from base_commponents.locator import Locator
from base_commponents.base_element import BaseElement
import csv


class Traditional(BasePage):

    url = "https://prs.moh.gov.sg/prs/internet/profSearch/main.action?hpe=TCM"
    #@property
    def switch_frame(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,'//frameset[@id="bottomFrameSet"]/frame[3]'))
        #locator = Locator(by=By.XPATH,value='//frameset[@id="bottomFrameSet"]/frame[3]')
        #return BaseElement(driver=self.driver,locator=locator)
        

        return None
    def default_content(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = self.driver.find_element_by_partial_link_text('Reset Search')
        element.click()
        return None
    @property
    def search_button(self):
        locator = Locator(by=By.XPATH,value='//input[@name="btnSearch"]')
        return BaseElement(driver=self.driver,locator=locator)
    @property
    def details_links(self):
        links = self.driver.find_elements_by_partial_link_text('View more details')
        return links


ex_path = which('geckodriver')
browser = webdriver.Firefox(executable_path=ex_path)
RUN = Traditional(driver=browser)
RUN.go()
RUN.switch_frame()
RUN.search_button.click()
links = RUN.details_links
print(len(links))
all_data = []
for i in range(10) :
    #if link == links[3]:
     #   browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    links[i].click()
    table_1 = browser.find_elements(By.XPATH,"//div[@id='profDetails']/table[1]/tbody/tr/td")
    table = browser.find_elements(By.XPATH,"//div[@id='profDetails']/div/table/tbody/tr/td")
    data ={
        'name': browser.find_element(By.XPATH,"//div[@id='profDetails']/div[1]").text,
        table_1[0].text:table_1[1].text,
        table_1[2].text:table_1[3].text,
        table_1[2].text:table_1[3].text,
        table[0].text:table[1].text,
        table[2].text:table[3].text,
        table[4].text:table[5].text,
        table[6].text:table[7].text,
        table[8].text:table[9].text,
        table[10].text:table[11].text,
        table[12].text:table[13].text,
        table[14].text:table[15].text,
        table[16].text:table[17].text,
    }
    print(data)
    all_data.append(data)
    RUN.quit_browser()
    ex_path = which('geckodriver')
    browser = webdriver.Firefox(executable_path=ex_path)
    RUN = Traditional(driver=browser)
    RUN.go()
    RUN.switch_frame()
    RUN.search_button.click()
    links = RUN.details_links
keys = all_data[0].keys()
with open('data.csv', 'w',encoding='utf8', newline='')  as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_data)
    #RUN.default_content()
    #RUN.switch_frame()
    #RUN.search_button.click()
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


