#!/usr/bin/env python3


def main():

    #import required modules
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium import webdriver as wd
    from time import sleep
    import subprocess

    #in case anything goes wrong, simply log the error. 
    try:
        #some options to optimize using chromedriver for automation.
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("enable-automation")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--dns-prefetch-disable")
        
        #load the driver. 
        wd = wd.Chrome('./chromedriver', options = chrome_options)
        
        #load the university's login panel
        wd.get('http://hamava.arakmu.ac.ir/Education')

        #find the elements of the login form that we need to interact with.
        user = WebDriverWait(wd,30).until(EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/form/div[1]/div/input')))

        uspass = WebDriverWait(wd,30).until(EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/form/div[2]/div/input')))

        button = WebDriverWait(wd,30).until(EC.presence_of_element_located(
            (By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[2]/form/div[3]/div/button')))

        #enter username and pass followed by clicking the enter button.
        user.send_keys('student-id')

        uspass.send_keys('student-password')

        button.click()

        sleep(5)

        #retrieving the element that contains the number of notifications regarding the student's status
        nots = WebDriverWait(wd,30).until(EC.presence_of_element_located( 
            (By.XPATH, '//*[@id="notification-button"]/span[2]')))

        not_co = nots.text

        #for debug purposes
        #print(dir(nots))
        #print(type(nots))
        #print(type(not_co))

        
        # 0 means no notifications, no need to do anything. otherwise, notify me.
        if not_co == '0' :
            print('no news', not_co)
            print('===================================================================')
        else :
            subprocess.run(['zenity' ,'--error' ,'--title="Score ready???"' ,'--text="{}"'.format(not_co),'--width=200', '--height=100'])
            print('===============')
            print(not_co)
            print('===================================================================')
    except Exception as e:
        print('ERROR: ', e)
        print('===================================================================')
    
        

if __name__ == '__main__' :
    main()


