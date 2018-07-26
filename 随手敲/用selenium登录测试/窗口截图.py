"""
窗口截图示例代码
"""
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("mysql语句")
driver.find_element_by_id("su").click()
sleep(1)#等待页面显示完成在截图
#截取当前窗口并保存图片的保存位置
driver.get_screenshot_as_file("D:\\kk.png")
#获得当前窗口截图并返回该图片的二级制数据
#tt=driver.get_screenshot_as_png()
#print(tt)
sleep(3)
driver.quit()