from urllib.request import urlopen
from anime import AnimeParser
import schedule
import logging
from threading import Timer

print("Script running")

def post_anime():
    pars = AnimeParser('https://animego.org/anime/random')
    pars.create_data_folder()
    
    title = pars.get_title()
    desc = pars.get_description()
    
    try:
        result = pars.create_vk_post()
        logging.info(f"Anime: {title} {result['post_id']}")
    except Exception as e:
        logging.error(f"Error: {e}")
        

    
def main():
    Timer(9000, post_anime).start()
main()



        
        
            
            




