from selenium import webdriver
from time import sleep 
dr=webdriver.Chrome()
dr.get('https://www.baidu.com')
sleep(2)
dr.find_element_by_id('kw').clear

dr.find_element_by_id('kw').send_keys('python')
dr.find_element_by_id('su').click()

from selenium import webdriver
from time import sleep
dr=webdriver.Chrome()
dr.get("https://www.baidu.com")
sleep(2)
#通过元素的属性id去查找元素
#dr.find_element_by_id("kw").send_keys("id")
#通过元素的属性name去查找元素
#dr.find_element_by_name("wd").send_keys("name")
#通过元素的属性class去查找元素
#dr.find_element_by_class_name("s_ipt").send_keys("class")
#通过a链接去定位元素
#dr.find_element_by_link_text("新闻").click()
#dr.find_element_by_partial_link_text("新").click()
#xpath定位 //表示当前目录  //标签名[@属性名=“属性值”]
#dr.find_element_by_xpath("//form[@id='form']/span/input").send_keys("xpath")
dr.find_element_by_xpath("//input[@autocomplete='off']").send_keys("xpath111")
