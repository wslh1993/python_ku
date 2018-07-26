from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("http://bbs.hsw.cn/")
b=dr.current_window_handle
sleep(2)
#dr.switch_to.frame('x-URS-iframe')
dr.implicitly_wait(2)
#通过a链接去定位登录
dr.find_element_by_link_text("陕西论坛").click()
a=dr.window_handles
for x in a:
    if x!=b:
        c=x
dr.switch_to.window(c)
#sleep(2)
dr.find_element_by_link_text("西安论坛").click()
dr.switch_to.window(b)
#sleep(2)
dr.find_element_by_link_text("群众呼声").click()
#通过xpath用ID去定位用户名框
#dr.find_element_by_xpath("//*[@placeholder='邮箱帐号或手机号']").send_keys("a123")
#sleep(1)
#通过xpath用ID去定位密码
#dr.find_element_by_xpath("//*[@placeholder='密码']").send_keys("密码")
#sleep(1)
#通过xpath用class去定位登录按钮
#dr.find_element_by_xpath("//*[@id='login_button']").click()

