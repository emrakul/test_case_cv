import requests
import glob
import itertools
import random
import base64


def test_all():
    random.seed(100)

    files = glob.glob('tests/*.png')
    print(files)
    
    i = 0
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

        res = requests.post('http://172.17.0.2:5000/process', json={
                           'left': left_image_bytes_string, 'right': right_image_bytes_string})
        print(res.content)
        i+=1
        if i%10 == 1:
            print(requests.get('http://172.17.0.2:5000/healthcheck').content)
test_all()
