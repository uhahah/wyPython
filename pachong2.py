from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver import ActionChains  # 破解滑动验证码的时候用的 可以拖动图片
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time
import xlrd
import re
driver=webdriver.Chrome()

try:
    #wait=WebDriverWait(driver,10)
    #1、访问百度

    driver.get('https://pubchem.ncbi.nlm.nih.gov/#query=BRD-A65767837')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "highlight")))
    driver.find_element_by_class_name("highlight").click()
    currrntUrl=driver.current_url
    time.sleep(1)
    driver.get(currrntUrl+"#section=CAS")
    time.sleep(5)
    cas = driver.find_element_by_xpath('//*[@id="CAS"]/div[2]/div[1]/p').get_attribute("textContent")
    print(cas)
    name_div = driver.find_element_by_class_name("p-sm-top").get_attribute("textContent")
    print(name_div)
    # cas_div = driver.find_element_by_id("CAS").get_attribute("textContent")
    # str=cas_div+""
    # strList=re.sub('[a-zA-Z]','',str).split();
    # print(strList[1].replace(";",""))
    time.sleep(1)
finally:
    driver.close()