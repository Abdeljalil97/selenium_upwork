
class BasePage:
    url = None
    def __init__(self,driver) :
        self.driver = driver
    
    def go(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def quit_browser(self):
        self.driver.quit()