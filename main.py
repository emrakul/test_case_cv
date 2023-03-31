import base64

from processor import Processor
from flask import Flask, request, jsonify
import json
app = Flask(__name__)

processor = Processor('./mobilenetv2.onnx')

@app.route('/process')
def transcribe():
    blobs = json.loads(request.data)
    image1, image2 = blobs['image1'], blobs['image2']
    result = processor.compare(image1, image2)
    return jsonify({"result" : result })