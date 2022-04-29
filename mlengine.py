import io
from sklearn import impute
import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
from PIL import Image



def transform_image(image_bytes):
    transform = transforms.Compose(
        [transforms.Grayscale(num_output_channels=1),
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize((0.137),(0.3081))
        ]
    )

    image = Image.open(io.BytesIO(image_bytes))

    return transform(image).unsqueeze(0)

def get_prediction(image_tensor):
    image = image_tensor.reshape(-1, 28*28)
    outputs = model(image)
    _,predicted = torch.max(outputs.data, 1)
    return predicted
