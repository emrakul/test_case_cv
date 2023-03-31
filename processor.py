import onnxruntime
import numpy as np
import skimage
import io

class Processor():
    def __init__(self, model_name: str, threshold: int = 0.9):
        self.model = onnxruntime.InferenceSession(model_name)
        self.input_name = self.model.get_inputs()[0].name
        self.output_name = self.model.get_outputs()[0].name
        self.threshold = threshold

    def preprocess_image(self, image, channels=3):
        image = skimage.io.imread(io.BytesIO(image))
        #image = skimage.transform.resize(image, (224,224))
        image_data = np.asarray(image).astype(np.float32)
        image_data = image_data.transpose([2, 0, 1]) 
        mean = np.array([0.079, 0.05, 0]) + 0.406 # https://github.com/onnx/models/tree/main/vision/classification/mobilenet#preprocessing
        std = np.array([0.005, 0, 0.001]) + 0.224
        for channel in range(image_data.shape[0]):
            image_data[channel, :, :] = (image_data[channel, :, :] / 255 - mean[channel]) / std[channel]
        image_data = np.expand_dims(image_data, 0)
        return image_data

    def compare(self, image1, image2):
        image1_processed = self.preprocess_image(image1)
        image2_processed = self.preprocess_image(image2)
        
        vec1 = self.model.run([self.output_name], {
                              self.input_name: image1_processed})[0][0]
        vec2 = self.model.run([self.output_name], {
                              self.input_name: image2_processed})[0][0]
        vec1 = vec1/np.linalg.norm(vec1)
        vec2 = vec2/np.linalg.norm(vec2)
        
        #return np.dot(vec1, vec2) 
        if np.dot(vec1, vec2) > self.threshold:
            return {"result" : True, "score": np.dot(vec1, vec2)}
        else:
            return {"result" : False, "score": np.dot(vec1, vec2)}
