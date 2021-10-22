import os
from gtts import gTTS
from app import app



def the_image_exists(image_name):
    file_existed = False
    for file in os.listdir(os.fsencode(app.config["IMG_FOLDER"])):

            # We do not take the extension into consideration :  .split(".")[0]
            filename = os.fsdecode(file)
            if filename == image_name:
                file_existed = True
                return file_existed
    
    return file_existed
    


 


def generate_audio(image_name):
    language = 'en'

    if the_image_exists(image_name):
        audio = gTTS(
            text=f"The file exists and its name is  {image_name}", 
            lang=language, slow=False
            )
    
    else:
        audio = gTTS(
            text=f"We are sorry, the file doesn't exist, please search for another file", 
            lang=language, slow=False
            )
        
    audio.save(app.config["AUDIO_FOLDER"]+"audio.mp3")
    os.system(f'start {app.config["AUDIO_FOLDER"]}audio.mp3')
