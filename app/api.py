# import app variable (app = Flask(__name__) in __init__.py) from app package that we've created 
from app import app
from flask import request, send_from_directory
from app.utils import *

@app.route("/")
def index():
    return "Flask is running"


@app.route("/get-response", methods=["POST"])
def get_response():
    
    if request.method == "POST":
        if request.is_json:
            req = request.get_json()
            searched_file = req.get("image_name")

            # Python will tel us weather or not the file exists. Choose :
            # en for english, de for german and fr for french
            generate_audio(searched_file, 'de')
 
    try:
        return send_from_directory(
            app.config["IMG_FOLDER"], path=searched_file, as_attachment=True
            )
    except:
        return "The file doesn't exist"

