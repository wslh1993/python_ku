from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("https://mail.qq.com")
sleep(2)
dr.switch_to.frame(0)

#通过a链接去定位登录
dr.find_element_by_link_text("帐号密码登录").click()
sleep(1)
#通过xpath用ID去定位用户名框
dr.find_element_by_xpath("//*[@id='u']").send_keys("用户名")
sleep(1)
#通过xpath用ID去定位密码
dr.find_element_by_xpath("//*[@id='p']").send_keys("密码")
sleep(1)
#通过xpath用class去定位登录按钮
dr.find_element_by_xpath("//*[@id='login_button']").click()
'''
存在问题：
    显示登陆成功的弹窗无法用检查中 箭头获取
'''
