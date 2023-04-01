# test_case_cv
REST-service for checking if two frames come from the same video

Using `mobilenet` and checking if two embedding are similar (cosine distance)

Using `flask` for http serving. 

Using `onnxruntime` for portability (lightweight, no dependencies like torch or TF)

## Build docker and run it

`docker build -t test_case .`

`docker run -it test_case:latest`

## Run client for tests:

`python client.py`

## Endpoints

1. `process` - send two base64-encoded images
1. `healthcheck` - for now shows an average latency of the main method


## Possible improvements 
1. Use fixed sized images. Resize/rescale use baked-in dimensions for onnx.
2. Use Triton for better gpu utilization
3. Try ORB-features for image description and matching 
