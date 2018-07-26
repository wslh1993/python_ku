#导入浏览器驱动
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#导入鼠标类
from selenium.webdriver.common.action_chains import ActionChains

#引入Keys类：
from selenium.webdriver.common.keys import Keys
dr=webdriver.Chrome()

dr.get('https://www.baidu.com')
sleep(2)
#鼠标操作 在设置上悬停
a=dr.find_element_by_link_text('设置')

ActionChains(dr).move_to_element(a).perform()
b=dr.find_element_by_link_text('搜索设置')
ActionChains(dr).move_to_element(b).perform()
ActionChains(dr).double_click().perform()
inputs = dr.find_elements_by_tag_name('input')
sleep(2)
dr.find_elements_by_name('s1')[1].click()
sleep(2)
dr.find_elements_by_name('SL')[1].click()

'''
sleep(2)
#鼠标操作 双击新闻
temp=dr.find_element_by_link_text('新闻')
ActionChains(dr).double_click(temp).perform()
sleep(5)
#键盘操作
dr.find_element_by_id('ww').send_keys('关于python的新闻')
sleep(2)
dr.find_element_by_id('ww').send_keys(Keys.BACK_SPACE)
sleep(2)
dr.find_element_by_id('ww').clear

dr.find_element_by_id('kw').clear
dr.find_element(By.ID,'kw').send_keys('nihao')

#dr.find_element_by_id('kw').send_keys('python')

#输出百度一下按钮尺寸
print(dr.find_element_by_id('su').size)

dr.find_element_by_id('su').click()

sleep(1)
#调整窗口大小
dr.set_window_size(300, 500)
sleep(1)
#调整窗口最大化
dr.maximize_window()
sleep(1)
#浏览器后退
dr.back()
sleep(1)
#浏览器前进
dr.forward()
sleep(1)
#浏览器刷新
dr.refresh()
dr.close()
#from selenium import webdriver
#from time import sleep
#dr=webdriver.Chrome()
#dr.get("https://www.zimuku.cn")
#sleep(2)
#通过a链接去定位元素
#dr.find_element_by_link_text("登录").click()
#dr.find_element_by_xpath("//*[@id='inputEmail']").send_keys("q632802435")
#dr.find_element_by_xpath("//*[@id='inputPassword']").send_keys("12345678")
#dr.find_element_by_xpath("//*[@class='btn submit-btn']").click()
'''
