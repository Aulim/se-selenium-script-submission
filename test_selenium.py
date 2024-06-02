from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_basic(self):
        # Open the demo page
        self.open("https://seleniumbase.io/demo_page")
        
        self.update_text("#myTextInput", "Software Engineering Selenium!!")
        
        self.click("#myButton")
        
        self.click("#myCheckBox")
        
        self.click("#myRadioButton2")
        
        self.select_option_by_text("#mySelect", "Set to 50%")
