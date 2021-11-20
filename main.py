'''imports'''
import logging
import eel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import psycopg2

connection=psycopg2.connect(
    host='localhost',
    database='project2',
    user='postgres',
    password='admin',
    port='5432'
)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')


PATH = Service('chromedriver/chromedriver')


@eel.expose
def job_search(userEmail, userPassword):
    '''job_search'''
    driver = webdriver.Chrome(service=PATH, options=options)
    # driver = webdriver.Chrome(service=PATH)

    driver.get('https://app.slack.com/workspace-signin')

    search = driver.find_element(By.ID, 'domain')
    search.send_keys('nucamp-bootcamp')
    search.send_keys(Keys.RETURN)

    email = driver.find_element(By.ID, 'email')
    email.send_keys(userEmail)

    password = driver.find_element(By.ID, 'password')
    password.send_keys(userPassword)

    signin_btn = driver.find_element(By.ID, 'signin_btn')
    signin_btn.submit()


    # Get path and click Search Nucamp input search button
    eel.sleep(15)
    driver.find_element(
        By.XPATH, '//button[@type="button" and @aria-label="Search"]'
    ).click()


    # input job search string and submit it
    driver.execute_script(
        '''
        let user_input = document.getElementsByClassName('ql-editor');
        user_input[1].innerHTML = 'in:#jobsearch-networking from:@NucampBot';

        let select_query = document.getElementsByClassName('c-search_autocomplete__suggestion_item');

        setTimeout(() => {
            select_query[0].click();
        }, 1000);
        '''
    )


    # # select results per page
    # eel.sleep(5)
    # driver.execute_script(
    #     '''
    #     let results_per_page = document.getElementsByClassName('p-search_filter__select-label');
    #     results_per_page[1].click();
    #     '''
    # )


    # # click on selected result per page
    # driver.find_element(
    #     By.XPATH, '//span[@data-qa="all"]'
    # ).click()


    # scroll
    eel.sleep(5)
    for i in range(9):
        eel.sleep(5)
        job_listings = driver.execute_script(
            '''
            let getJobs = () => {
                let jobContainer = document.getElementsByClassName('c-message_kit__hover');
                let jobData = document.getElementsByClassName('c-search_message__body');
                let giveFeedback = document.getElementById('give-feedback-text-node')
                let jobs = [];

                for (let i = 0; i < jobContainer.length; i++) {           
                    if (giveFeedback == null) {
                        jobs.push(jobData[0].innerHTML);
                        // console.log(job_data[0].innerHTML);
                        jobContainer[0].remove();
                    } else if (giveFeedback !== null) {
                        console.log('Jobs scraped');
                        clearInterval(setTime);
                    }
                }
                // console.log(jobs);
                return jobs;
            }
            console.log(getJobs());
            return getJobs();
            '''
        )

        bs_4(job_listings)




def bs_4(job_listings):
    jobs_string = ''.join(job_listings)
    # print(jobs_string)

    eel.addJob(jobs_string)
    eel.sleep(10)
    doc = BeautifulSoup(jobs_string, 'html.parser')
    # print(doc.prettify())

    doc_text = doc.getText()
    remove_text = doc_text[doc_text.find('-'): doc_text.find(':') + 1]
    new_doc = doc_text.replace(remove_text, '')
    # remove_text = re.sub(r'[^A-Za-z0-9]+', '', doc_text)
    # new_doc = remove_text
    print(new_doc, '\n\n')

    for b in doc.find_all('b'):
        # print(b.text, b.next_sibling.text, b.next_sibling.next_sibling.text)

        new_text_0 = b.text.replace("'", '').replace('"', '').replace('[^a-zA-Z0-9]+', '')
        new_text_1 = b.next_sibling.text.replace("'", '').replace('"', '').replace('[^a-zA-Z0-9]+', '')
        new_text_2 = b.next_sibling.next_sibling.text.replace("'", '').replace('"', '').replace('[^a-zA-Z0-9]+', '')

        print(new_text_0, new_text_1, new_text_2)


        insert_sql_query = f"""
        INSERT INTO jobs (type, location, title, compensation, employees, poster, description) VALUES
        {('a', 'b', 'c', 'd', new_text_0, new_text_1, new_text_2)}
        """

        try:
            pointer = connection.cursor()
            # pointer.execute("TRUNCATE TABLE jobs")
            pointer.execute(insert_sql_query)
            connection.commit()
            logging.info('Data inserted')
        except Exception as e:
            logging.error(f'Data Error: {e}')
        # finally:
        #     connection.close()


eel.init('www')
eel.start('index.html', size=(720, 610))