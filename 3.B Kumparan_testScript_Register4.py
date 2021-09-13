Case Register#04
--------------------
webdriver.Chrome() #Open Google Chrome
get("https://kumparan.com"/login) #Go to Kumparan.com link
implicity_wait(5)
find_element_by_name('password').sendKeys("testtest123") #Enter Password on textbox
find_element_by_name('confirm-password').sendKeys("testtest123") #Enter Confirm Password on textbox
find_element_by_class('Viewweb__StyledView-sc-1ajfkkc-0 xbJQR').click() #Click Save/Simpan

