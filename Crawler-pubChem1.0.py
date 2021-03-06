from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time
import xlrd
import xlwt

driver=webdriver.Chrome()
data = xlrd.open_workbook('GSEA化合物信息_0802(1).xlsx')
table = data.sheet_by_index(0)
pert_id = table.col_values(1)
i = 1
workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
cas = None
name_div = None
timeStr=str(time.strftime('%m-%d %H-%M', time.localtime(time.time())))
while True:

    if(i>=len(pert_id)):
        break

    try:

        cas=-2
        name_div=-2
        url='https://pubchem.ncbi.nlm.nih.gov/#query='
        urlTarget=url+str(pert_id[i])
        i += 1
        booksheet.write(i - 2, 0, pert_id[i-1])
        driver.get(urlTarget)


        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "highlight")))
        driver.find_element_by_class_name("highlight").click()
        #currrntUrl=driver.current_url
        #time.sleep(1)
        #driver.get(currrntUrl+"#section=CAS")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "p-sm-top")))
        name_div = driver.find_element_by_class_name("p-sm-top").get_attribute("textContent")
        print(name_div)
        booksheet.write(i-2, 2, name_div)
        cas = driver.find_element_by_xpath('//*[@id="CAS"]/div[2]/div[1]/p').get_attribute("textContent")
        booksheet.write(i - 2, 1, cas)
        print(cas)

        workbook.save('test_xlwt.xls')



    except:

        booksheet.write(i - 2, 2, name_div)
        booksheet.write(i - 2, 1, cas)

        workbook.save('PubChem'+timeStr+'.xlsx')
        print("Not find")

driver.close()