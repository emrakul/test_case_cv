import base64

from processor import Processor
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

processor = Processor('./mobilenetv2.onnx')

@app.route('/process', methods=['GET', 'POST'])
def transcribe():
    blobs = request.get_json()
    bytes_image1, bytes_image2 = blobs['left'], blobs['right']
    image1 = base64.b64decode(bytes_image1)
    image2 = base64.b64decode(bytes_image2)
    result = processor.compare(image1, image2)
    
    return jsonify({"result" : str(result) })