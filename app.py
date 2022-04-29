from flask import Flask, request, jsonify
# from torch import tensor
# from mlengine import transform_image, get_prediction
# import os
# from PIL import Image

app = Flask(__name__)

ALLOWED_FILE_EXTENTIONS = {'png', 'jpg', 'jpeg'}

def is_allowed(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXTENTIONS

@app.route('/predict', methods = ['POST'])
def predictfn():
    return "hello"
    # if request.method == 'POST':
    #     file = request.files.get('file')
    #     if file is None or file.filename == "":
    #         return jsonify({'error':'no file'})
    #     if not is_allowed(file.filename):
    #         return jsonify({'error': 'not a valid file'})

    #     try:
    #         img_bytes = file.read()
    #         tensor = transform_image(img_bytes)
    #         prediction = get_prediction(tensor)
    #         data = {'prediction':prediction.item(), 'class_name':str(prediction.item())}
    #         return jsonify(data)
    #     except:
    #         return jsonify({'error': 'error at prediction'})

if __name__ == "__main__":
    app.run(debug=True)