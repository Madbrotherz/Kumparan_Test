Case Register#01
--------------------
webdriver.Chrome() #Open Google Chrome
get("https://kumparan.com"/login) #Go to Kumparan.com link
implicity_wait(5)
find_element_by_class('Textweb__StyledText-sc-1uxddwr-0 drkNaI').click() 	#Click "Masuk/Login" element
find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[5]/a/span').click()	 #Click "Daftar Sekarang" element
find_element_by_name('name=email').sendKeys("test123@gmail.com") 	#Enter Email
find_element_by_xpath('//*[@id="content"]/div/div/div[2]/div/div[3]/button/div').click() 	#Click Register Button
find_element_by_class('Textweb__StyledText-sc-1uxddwr-0 iEPpYF').click() 	#Close Popup