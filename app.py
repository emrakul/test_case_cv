import base64

from processor import Processor
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

processor = Processor('./mobilenetv2.onnx')

@app.route('/process')
def transcribe():
    blobs = json.loads(request.data)
    bytes_image1, bytes_image2 = blobs['image1'], blobs['image2']
    image1 = base64.b64decode(bytes_image1.encode('ascii'))
    image2 = base64.b64decode(bytes_image2.encode('ascii'))
    result = processor.compare(image1, image2)
    return jsonify({"result" : result })