# flask-api-returning-audio

A flask api returning an audio telling whether or not an image
exists in the server. All we have to do is to send a json file were we specify the name as "image_name

We used postman to send the json file.

We converted a string to audio file, that will be played directly in your machine, using python gtts module.

You have to change the config file where I specified the images and the audio location.


Run : pip install -r requirements.txt to install all the needed dependencies

