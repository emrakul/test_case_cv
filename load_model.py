import torchvision
import torch

weights = torchvision.models.MobileNet_V3_Large_Weights.IMAGENET1K_V1
model = torchvision.models.mobilenet_v3_large(weights=weights)
model.eval()
v1 = torch.zeros(1, 3, 224, 224, requires_grad=True)
dynamic_axes = {'input_1': [0, 2, 3]}

torch.onnx.export(model, v1, f='mobilenetv3_large.onnx', export_params=True,   do_constant_folding=True,
                  opset_version=12, input_names=["input_1"], output_names=["output_1"], dynamic_axes=dynamic_axes)