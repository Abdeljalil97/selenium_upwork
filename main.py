from selenium import webdriver
from selenium.webdriver.common.by import By
from shutil import which
from base_commponents.base_page import BasePage
from base_commponents.locator import Locator
from base_commponents.base_element import BaseElement


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

for link in links :
    link.click()
    print(browser.page_source)
    RUN.default_content()
    #RUN.switch_frame()
    RUN.search_button.click()
    #browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


