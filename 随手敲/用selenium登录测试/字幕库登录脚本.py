from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("https://www.zimuku.cn")
sleep(2)
#通过a链接去定位登录
dr.find_element_by_link_text("登录").click()
sleep(0.5)
#通过xpath用ID去定位用户名框
dr.find_element_by_xpath("//*[@id='inputEmail']").send_keys("q632802435")
sleep(0.5)
#通过xpath用ID去定位密码
dr.find_element_by_xpath("//*[@id='inputPassword']").send_keys("12345678")
sleep(0.5)
#通过xpath用class去定位登录按钮
dr.find_element_by_xpath("//*[@class='btn submit-btn']").click()
'''
存在问题：
    显示登陆成功的弹窗无法用检查中 箭头获取
'''
