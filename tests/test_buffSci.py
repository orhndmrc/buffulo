import time

from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass

#@pytest.mark.usefixtures("setUp")
class TestOne(BaseClass):

 def test_buffsci(self):
     loginpage = LoginPage(self.driver)
     time.sleep(5)
     loginpage.clickLoginBtn()
