import sendmail
import itertools

import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

def get_channel_data(url):
    global channel_name
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
    channel_name = soup.find('yt-formatted-string', {'class' : 'style-scope ytd-channel-name'}).text
    videos = soup.find_all('ytd-grid-video-renderer', {'class' : 'style-scope ytd-grid-renderer'})
    for video in videos:
        video_info = dict()
        video_block = video.find('h3', {'class' : 'style-scope ytd-grid-video-renderer'}).a
        video_info['title'] = video_block.text
        video_info['video_url'] = f"https://www.youtube.com{video_block['href']}"
        video_data = video.find_all('span', {'class':'style-scope ytd-grid-video-renderer'})
        video_info['views'] = video_data[0].text
        video_info['time'] = video_data[1].text
        yield video_info

url = input('Enter the url here : ')
videos = get_channel_data(url)

videos1, videos2 = itertools.tee(videos)

num_videos = sum(1 for video in videos2)
#print(num_videos)
#print(channel_name)

df = pd.DataFrame(videos1, index=range(1, num_videos+1))
filename = input('Enter filename(.csv) : ')
df.to_csv(f'{filename}.csv')
df.to_excel(f'{filename}.xlsx')

subject = f'{channel_name} - YouTube channel data'
body = f'{channel_name} contains {num_videos} videos. The details of each video is provided below in a csv and excel file'

sender = input('Enter sender email id : ')
reciever = input('Enter reciever email id : ')

attachment_file1 = f'{filename}.csv'
attachment_file2 = f'{filename}.xlsx'

mail = sendmail.SendMail(sender, reciever)
mail.add_subject(subject)
mail.add_body(body)
mail.add_attachment(attachment_file1)
mail.add_attachment(attachment_file2)

mail.send()

