FROM tiangolo/meinheld-gunicorn:python3.9

WORKDIR /workspace
COPY . /workspace

ENV SERVICE_PORT=5123
EXPOSE 5123
RUN apt update
RUN apt-get install -y build-essential

RUN pip install flask onnxruntime gunicorn
CMD gunicorn --limit-request-line 0 -w 1 -b 0.0.0.0:5123 --timeout 1000 app:app
