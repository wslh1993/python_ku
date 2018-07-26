#导入浏览器驱动
from selenium import webdriver
#导入延时
from time import sleep
#导入鼠标
from selenium.webdriver.common.action_chains import ActionChains
#引入Keys
from selenium.webdriver.common.keys import Keys

dr=webdriver.Chrome()

dr.get('https://www.baidu.com')
sleep(2)
#鼠标操作 在设置上悬停
a=dr.find_element_by_link_text('设置')
ActionChains(dr).move_to_element(a).perform()
#找到搜索设置 移动到搜索设置
b=dr.find_element_by_link_text('搜索设置')
ActionChains(dr).move_to_element(b).perform()
ActionChains(dr).double_click().perform()
#提供给多选 用for遍历
#inputs = dr.find_elements_by_tag_name('input')
sleep(2)
#搜索框提示 选第二个
dr.find_elements_by_name('s1')[1].click()
sleep(2)
#搜索语言范围 选第二个
dr.find_elements_by_name('SL')[1].click()
#后两个除name不同，所用方法相同
