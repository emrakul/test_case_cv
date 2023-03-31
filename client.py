import requests
import glob
import itertools
import random
import base64


def test_all():
    random.seed(100)

    files = glob.glob('tests/*.png')
    print(files)
    
    for (l, r) in itertools.product(files, files):
        print(l, r)
        with open(l, 'rb') as left_image:
            left_image_bytes = left_image.read()
            left_image_bytes_string = base64.b64encode(
                left_image_bytes).decode('ascii')
        with open(r, 'rb') as right_image:
            right_image_bytes = right_image.read()
            right_image_bytes_string = base64.b64encode(
                right_image_bytes).decode('ascii')

        res = requests.post('http://127.0.0.1:5000/process?', json={
                           'left': left_image_bytes_string, 'right': right_image_bytes_string})
        print(res.content)

test_all()
