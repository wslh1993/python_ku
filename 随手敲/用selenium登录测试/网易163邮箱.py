from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("https://mail.163.com")
sleep(2)
dr.switch_to.frame(0)

#通过a链接去定位登录
#dr.find_element_by_link_text("帐号密码登录").click()
#sleep(1)
#通过xpath用ID去定位用户名框
dr.find_element_by_xpath("//*[@placeholder='邮箱帐号或手机号']").send_keys("a123")
sleep(1)
#通过xpath用ID去定位密码
dr.find_element_by_xpath("//*[@placeholder='密码']").send_keys("密码")
sleep(1)
#通过xpath用class去定位登录按钮
#dr.find_element_by_xpath("//*[@id='login_button']").click()

