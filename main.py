from urllib.request import urlopen
from anime import AnimeParser
import schedule
import logging
from threading import Timer



def post_anime():
    print("Script running")
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
    post_anime()
    Timer(9000, main).start()
main()



        
        
            
            




