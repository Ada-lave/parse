import requests
import json
import vk_api
import logging
import os
from dotenv import load_dotenv


load_dotenv()
logging.basicConfig(filename="app.log", level=logging.DEBUG)

def save_photo_to_album(path):
    try:
        response = requests.get('https://api.vk.com/method/photos.getUploadServer',
                                params={'album_id':'268588862', 'group_id':'188992540',
                                        'v':'5.154', 'access_token':f'{os.getenv("access_tk")}'})
    except Exception as e:
        logging.error(f"Error: {e}")
        
    data = json.loads(response.text)
    
    upload_url = data['response']['upload_url']
   
    response = requests.post(upload_url, files={'file1':open(path, 'rb+')})

    photo_data = json.loads(response.text)

    
    server = photo_data['server']
    photo = photo_data['photos_list']
    hash = photo_data['hash']
   

    try:
        response = requests.get('https://api.vk.com/method/photos.save', params={'album_id':'268588862','server':server,'photos_list':photo, 'group_id':'188992540', 
                                                                             'hash':hash,'v':'5.154', 'access_token':f'{os.getenv("access_tk")}'})
    except Exception as e:
        logging.error(f"Error: {e}")
    
    resp_date = json.loads(response.text)
    
    return [resp_date['response'][0]['owner_id'], resp_date['response'][0]['id']]

def create_post(title, desc: str, images):
    params = {
        'owner_id': '-188992540',
        'message': f"Аниме: {title}\n Введение: {desc.strip()}",
        'attachments':images,
        'access_token':f'{os.getenv("access_tk")}',
        'v': '5.154'
        
    }
    response = requests.post('https://api.vk.com/method/wall.post', params=params)
    
    return json.loads(response.text)


