from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import csv


class MyTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="venv\chromedriver.exe")

    def getDriver(self):
        self.driver.get('https://tuoitre.vn/')


    def clickTheWord(self):
        self.driver.find_element(By.CSS_SELECTOR, ".menu-li > a[title=\"Thể thao\"]").click()
        
    def clickWorldCup(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, "a[title=\"World Cup 2022\"]").click()
        
    def crawlNewArticles(self,arr):
        self. driver.execute_script("window.scrollTo(0, window.scrollY + 800)")
        articles = self.driver.find_elements(By.CSS_SELECTOR, ".box-category-item")
        for article in articles:
            try:
                title = article.find_element(By.CSS_SELECTOR, "a.box-category-link-title").text
                link = article.find_element(By.CSS_SELECTOR, "a.box-category-link-title").get_attribute('href')
                arr.append(title)
                arr.append(link)
                
            except NoSuchElementException:
                print('Error.!!!')
        self.driver.save_screenshot("PhamKyAn.png")

    def saveToFile(self):
        arr = []
        self.crawlNewArticles(arr)
        fieldnames = ['Article']
        print(arr)
        with open('PhamKyAn.csv', "w", encoding="utf-16", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in arr :
                writer.writerow({'Article' : item})  
                

    def start(self):
        self.getDriver()
        self.clickTheWord()
        self.clickWorldCup()
        self.saveToFile()
        self.driver.close()

test = MyTest()
test.start()