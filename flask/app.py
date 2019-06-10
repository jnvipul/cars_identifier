"""
This module serves the API for predicting model and make on the car images


__author__ = "Vipul J"
__email__ = "messagevipul@gmail.com"

"""

import os

from fastai.vision import *
from flask import Flask, request, redirect, url_for
import json

MODEL_PATH = 'model'
UPLOAD_FOLDER = 'uploaded_images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)

@app.route("/cars/v1/get_car_details", methods=['GET', 'POST'])
def get_car_details():
    """
    Returns details for the given car image
    """
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
            extension = filename.rsplit('.', 1)[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f'img.{extension}'))
            car_details = predict_labels()
            return json.dumps({'labels':labels})
        else:
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>File Select Error!</h1>
            <a href="/file">file</a>
            '''
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

def predict_labels():
    """
    Predict tags on uploaded image
    """
    test = ImageList.from_folder(UPLOAD_FOLDER)
    if len(test) == 0:
        raise Exception('Uploaded image file not found')
    learn = Model.get_instance().get_saved_model()
    learn.data.add_test(test)

    # make prediction
    print("Predicting")
    preds, _ = learn.get_preds(ds_type=DatasetType.Test)
    return preds

# Used as Singelton
class Model:

    instance = None

    def __init__(self):
        try:
            self.saved_model = load_learner(MODEL_PATH)
        except FileNotFoundError:
            print("Model file not found")

    def get_saved_model(self):
        return self.saved_model

    def get_instance():
        if not Model.instance:
            Model.instance = Model()
        return Model.instance



if __name__ == '__main__':
    setup()
    app.run(host='0.0.0.0', port=4000, debug=True)
