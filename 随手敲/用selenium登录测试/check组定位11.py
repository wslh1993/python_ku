#-------------实例12（一组元素定位，定位单选框和复选框）-------
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("file:///E:\自动化测试用例\元素定位/check.html")
#定位一组标签名位input元素,inputs是一个列表
inputs=driver.find_elements_by_tag_name("input")
#选择定位元素的某一个进行操作,集合索引从0
#a=driver.find_elements_by_name("radiobutton")[0].click()#在一组中选中一个
#print(len(a))#查看定位集合元素的个数
#迭代遍历选中
print(inputs)
for input in inputs:

    if input.get_attribute('type')=='radio' :
        input.click()
        time.sleep(1)

#迭代checkbox遍历选中，使用css定位的话可以使用pop().click()来取消勾选，pop（0）指定
for input in inputs:
    if input.get_attribute('type')=='checkbox' :
        input.click()
        time.sleep(1)
#如果在此单击checkbox，则表示取消选择
for input in inputs:
    if input.get_attribute('type')=='checkbox' :
        input.click()
        time.sleep(1)