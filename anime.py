from bs4 import BeautifulSoup
import os
from vk import  save_photo_to_album, create_post
import requests
from urllib.request import urlopen
import logging

class AnimeParser:
    url = ''
    
    
    def __init__(self, url) -> None:
        self.url = url
        self.page = urlopen(url)
        self.html = self.page.read().decode('utf-8')
        self.soup = BeautifulSoup(self.html, 'html.parser')
    
    def get_title(self): 
        anime_title = self.soup.find(class_='anime-title')
        title = anime_title.find('h1')
    
        return title.text
    
    def get_description(self):
        anime_description = self.soup.find(class_='description')
        return anime_description.text


    def create_data_folder(self):
        title = self.get_title().replace(':',' ')
        desc = self.get_description()
        
        
        try:
            if not os.path.isdir(title):
                os.mkdir(f"{title}")     
            else:
                return "Anime alredy save"
        except Exception as e:
            logging.error(f"Error: {e}")
    
    def save_photos(self, path):
        imgs = self.soup.find_all(class_='img-fluid')
        poster = self.soup.find(class_='anime-poster').find('img')
        del imgs[-1]
        images_link=''
        
        if poster:
            with open(f"{path}/{path}_poster.png", "wb") as file:
                file.write(requests.get(poster.get('src')).content)
                link = save_photo_to_album(f"{path}/{path}_poster.png")
                images_link += f"photo{link[0]}_{link[1]},"
        
        for i in range(len(imgs)):
            img_link = imgs[i].get('src')
            with open(f"{path}/{os.path.basename(path)}_{i}.png", "wb") as file:
                file.write(requests.get(img_link).content)
            
            link = save_photo_to_album(f"{path}/{os.path.basename(path)}_{i}.png")
            images_link += f"photo{link[0]}_{link[1]},"
                
        
                
        return images_link[0:len(images_link)-1]
    
    def create_vk_post(self):
        title = self.get_title().replace(':',' ')
        desc = self.get_description()
        images = self.save_photos(title)
        
        return create_post(title, desc, images)
   