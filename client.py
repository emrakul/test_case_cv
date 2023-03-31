import requests
import glob
import itertools
import pathlib
import random
import skimage
import base64


def test_all():
    random.seed(100)

    files = glob.glob('tests/*.png')
    print(files)
    left = random.choices(files, k=4)
    right = random.choices(files, k=4)
    for (l, r) in zip(left, right):
        print(l, r)
        with open(l, 'rb') as left_image:
            left_image_bytes = left_image.read()
            left_image_bytes_string = base64.b64encode(
                left_image_bytes).decode('ascii')
        with open(r, 'rb') as right_image:
            right_image_bytes = right_image.read()
            right_image_bytes_string = base64.b64encode(
                right_image_bytes).decode('ascii')

        res = requests.get('http://127.0.0.1:5000/process', params={
                           'left': left_image_bytes_string, 'right': right_image_bytes_string})
        print(res.content)

    # for (example, group) in itertools.groupby(files, lambda x: x.split('/')[1][0]):


test_all()
