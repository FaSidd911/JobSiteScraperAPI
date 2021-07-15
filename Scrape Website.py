from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get('https://www.naukri.com/jobs-in-mumbai?industryTypeIdGid=109')

jobtitle =[]
company=[]
salary=[]

for i in range(100):

    jobTitleSel = driver.find_elements_by_css_selector('a.title.fw500.ellipsis')
    companySel = driver.find_elements_by_css_selector('a.subTitle.ellipsis.fleft')
    salarySel = driver.find_elements_by_css_selector('li.fleft.grey-text.br2.placeHolderLi.salary')



    for elem in jobTitleSel:
        jobtitle.append(elem.text)
    for elem in companySel:
        company.append(elem.text)
    for elem in salarySel:
        salary.append(elem.text)

    driver.find_element_by_css_selector('a.fright.fs14.btn-secondary.br2').click()

datadf = pd.DataFrame({'company': company,
                        'jobtitle':jobtitle,
                        'salary':salary})

datadf = datadf[datadf['salary']!='Not disclosed']
datadf.to_csv(data_dump.csv)