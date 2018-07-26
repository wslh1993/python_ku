from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("https://mail.qq.com")
dr.implicitly_wait(2)
#dr.maximinze_window()#让窗口最大化
sleep(2)
dr.switch_to.frame(0)
dr.find_element_by_link_text("帐号密码登录").click()
sleep(3)
dr.find_element_by_id("u").send_keys("530423177")

dr.find_element_by_id("p").send_keys("xxzj1010,./")
sleep(5)
dr.find_element_by_id("login_button").click()
sleep(5)
#左侧菜单栏-点击‘写信’
dr.find_element_by_id("composebtn").click()
sleep(2)
#切换至右侧 主iframe
dr.switch_to.frame("mainFrame")
#dr.find_element_by_id("toAreaCtrl").send_keys()
#定位‘正文’iframe 位置
main_body= dr.find_element_by_xpath("/")
#切换至‘正文’iframe
dr.switch_to.frame(main_body)

#正文--输入内容
dr.find_element_by_xpath("/html/body").send_keys(u"切换成功，输入正文内容")
sleep(2)

