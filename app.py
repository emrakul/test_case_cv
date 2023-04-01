import base64

from processor import Processor
from flask import Flask, request, jsonify
import json
from counter import Counter
import time

app = Flask(__name__)

processor = Processor('./mobilenetv3.onnx')
counter = Counter()


@app.route('/process', methods=['GET', 'POST'])
def transcribe():
    start = time.time_ns()
    blobs = request.get_json()
    bytes_image1, bytes_image2 = blobs['left'], blobs['right']
    image1 = base64.b64decode(bytes_image1)
    image2 = base64.b64decode(bytes_image2)
    result = processor.compare(image1, image2)
    counter.record((time.time_ns() - start)/1000000)  # to get ms
    return jsonify({"result": str(result['result']), "score": str(result['score'])})


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"latency_average": counter.average()})
