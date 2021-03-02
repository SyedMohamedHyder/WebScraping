import pandas as pd
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

def get_channel_data(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
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
df = pd.DataFrame(videos)
filename = input('Enter filename : ')
df.to_csv(f'{filename}.csv')