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
    


 
def get_text(language):
            match language:
                case 'en':
                    return ["The file exists and its name is", "We're sorry, the file doesn't exist"]
                case 'fr':
                    return ["Le fichier existe et son nom est", "Nous sommes désolés, le fichier n'existe pas"]
                case _:        
                    return ["Die Datei existiert und ihr Name ist", "Es tut uns leid, die Datei existiert nicht"]

def generate_audio(image_name, language):
    language = language

    if the_image_exists(image_name):


        audio = gTTS(
            text=f"{get_text(language)[0]}{image_name}", 
            lang=language, slow=False
            )
    
    else:
        audio = gTTS(
            text=f"{get_text(language)[1]}", 
            lang=language, slow=False
            )
        
    audio.save(app.config["AUDIO_FOLDER"]+"audio.mp3")
    os.system(f'start {app.config["AUDIO_FOLDER"]}audio.mp3')
