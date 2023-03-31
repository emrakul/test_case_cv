import cv2
import onnxruntime
import numpy as np


class Processor():
    def __init__(self, threshold: int = 0.1):
        self.model = onnxruntime.InferenceSession('./mobilenetv2.onnx')
        self.input_name = self.model.get_inputs()[0].name
        self.output_name = self.model.get_outputs()[0].name
        self.threshold = threshold

    def compare(self, image1, image2):
        vec1 = self.model.run([self.output_name], {
                              self.input_name: np.expand_dims(image1, 0)})
        vec2 = self.model.run([self.output_name], {
                              self.input_name: np.expand_dims(image2, 0)})
