FROM tiangolo/meinheld-gunicorn:python3.9

WORKDIR /workspace
COPY . /workspace

RUN pip install -r requirements.txt

CMD flask run --host=0.0.0.0