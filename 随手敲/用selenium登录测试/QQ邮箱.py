import random
from selenium import webdriver
from time import sleep
def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)
dr=webdriver.Chrome()
dr.get("https://mail.qq.com")
sleep(2)
#进入frame框架内部
dr.switch_to.frame(0)
#通过a链接去定位登录
dr.find_element_by_link_text("帐号密码登录").click()
sleep(1)
#通过xpath用ID去定位用户名框
dr.find_element_by_xpath("//*[@id='u']").send_keys("632802435@qq.com")
sleep(1)
#通过xpath用ID去定位密码
dr.find_element_by_xpath("//*[@id='p']").send_keys("liuhe.1015")
sleep(1)
#通过xpath用class去定位登录按钮
dr.find_element_by_xpath("//*[@id='login_button']").click()
sleep(3)
while True:
    s=''
    while True:
        g=Unicode()
        s=s+g
        if len(s)==8:
            break
    m=''
    while True:
        g=Unicode()
        m=m+g
        if len(m)==8:
            break
    dr.find_element_by_xpath("//*[@id='composebtn']").click()
    sleep(2)
    dr.switch_to_frame('mainFrame')
    sleep(2)
    dr.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys("981859036@qq.com")
    sleep(2)
    dr.find_element_by_xpath('//*[@id="subject"]').send_keys(s)
    a=dr.find_element_by_xpath('//*[@class="qmEditorIfrmEditArea"]')
    #print(a)
    dr.switch_to_frame(a)
    dr.find_element_by_xpath('/html/body').send_keys(m)
    dr.switch_to.parent_frame()
    #dr.switch_to.default_content()#
    #dr.switch_to_frame('mainFrame')
    dr.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
    dr.switch_to.default_content()
    sleep(2)


