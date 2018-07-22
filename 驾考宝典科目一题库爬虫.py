# -*- coding: utf-8 -*-
#利用Selenium进行驾考宝典的题目与解析，题目图片的匹配
#总的来说需要注意几点1.它是模仿浏览器的行为，所以和我们使用浏览器是一样的，相当于是脚本控制浏览器，时间间隔非常重要。2.注意在进行click时要注意点击的
#地方我们要能看到，否则就点击不到。3.若不熟悉xpath，那就直接在浏览器里面右键审查某个元素，然后右键复制其xpath位置就可以了，比较快。
#注意浏览器驱动与浏览器版本的对应，而且旧版会有些问题。
import time  
from selenium import webdriver 
browser = webdriver.Chrome(r"D:\Anaconda3\selenium\webdriver\chromedriver.exe")  
#设置使用的浏览器驱动，下载chromedriver，注意版本，驱动用的是2.40,对应谷歌浏览器的66到68，并且注意要
#把谷歌浏览器路径添加到path，最好用最新版
#browser.set_window_size(1440,900) #这个是设置窗口大小
browser.get("http://www.jiakaobaodian.com/mnks/exercise/0-car-kemu1.html?id=800000")  
time.sleep(1)  
js="var q=document.documentElement.scrollTop=450"  
browser.execute_script(js)  #执行js脚本的操作，将浏览器下拉拉到指定位置，目的是让鼠标可以点击到页面下方的一些按钮
#browser.find_element_by_css_selector("[class='left gl']").click()
browser.find_element_by_xpath('//button[@ref="xiangqing"]').click()#点击显示详情按钮
time.sleep(1)#非常重要，需要符合正常的与浏览器交互的时间，相当于脚本控制浏览器，所以时间控制非常重要  
def xx(browser):
    wenti = browser.find_element_by_xpath('//p[@class="timu-text"]').text
    xuanxiang = browser.find_element_by_xpath('//div[@class="options-w left"]').text #可以直接找xpath地址，或者直接复制浏览器里的给的xpath
    jiexi = browser.find_element_by_xpath('/html/body/div/div[6]/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/div[2]/p').text #elenment加s，则匹配多个。
    img=""
    try:
       img=browser.find_element_by_xpath('//img[@ref="bigImg"]').get_attribute('src')#找图片链接，没有会出现异常，出现异常就跳过异常
    except:
       {}
    else:
       {}
    browser.find_element_by_xpath('//button[@ref="next"]').click()
    #单击指定标签，注意一定要在浏览器看得到，如果在页面下方就需要通过js下拉到指定地方
    kk=[wenti,xuanxiang,img,jiexi]
    return kk
files = open("file.txt","w+") # "w"
for x in range(0,1325):
    k=xx(browser)
    files.write("question:"+k[0]+"answer:"+k[1].replace("\n", "")+"img:"+k[2]+" "+"jiexi:"+k[3].replace("\n", "")+'\n')   # 在file.txt文本内输入内容
    time.sleep(0.5)
files.close()
