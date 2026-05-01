"""
Script: chestxray.py
Description: Tool for chestxray
Category: Computer_Vision_Datasets
"""
try:
    import torch
    import torchvision.transforms as transforms
    from PIL import Image
    import torchvision.models as models
    import torch.nn as nn
    import json
    import numpy as np
    import cv2
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"Error: {e}. Please install the required libraries using: pip install torch torchvision pillow numpy opencv-python matplotlib")
    exit()

# Define the class labels
classes = [
    "Tracheal shift", "Pulmonary Fibrosis", "Aortic Enlargement", "Pleural Thickening",
    "Mediastinal widening", "Subc. Emphysema", "Opacity", "Rib fractures",
    "Pneumothorax", "Pleural effusion", "Nodule/mass", "Atelectasis", "Consolidation"
]

# Load the image
image_path = r"C:\Users\Henry\Downloads\Screenshot 2025-02-04 175022.png"
try:
    image = Image.open(image_path).convert("RGB")
except FileNotFoundError:
    print("Error: Image file not found. Please check the path and try again.")
    exit()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Apply transformations
image_tensor = transform(image)
image_tensor = image_tensor.unsqueeze(0)  # Add batch dimension

# Load a pre-trained DenseNet121 model
model = models.densenet121(pretrained=True)
num_ftrs = model.classifier.in_features
model.classifier = nn.Linear(num_ftrs, len(classes))  # Adjust for our number of classes

# Load model weights (if available)
model_path = "chest_xray_model.pth"  # Change this if you have a specific model file
try:
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Warning: Model weights not found. Using untrained model.")

model.eval()

# Perform inference
with torch.no_grad():
    outputs = model(image_tensor)
    probs = torch.sigmoid(outputs).squeeze().numpy()  # Apply sigmoid for multi-label classification

# Display results
results = {cls: float(prob) for cls, prob in zip(classes, probs)}
print(json.dumps(results, indent=4))

# Grad-CAM Implementation
final_conv_layer = model.features[-1]  # Last convolutional layer

def get_grad_cam(model, image_tensor, target_class):
    gradients = []
    activations = []
    
    def save_gradient(grad):
        gradients.append(grad)
    
    def forward_hook(module, input, output):
        activations.append(output)
        output.register_hook(save_gradient)
    
    handle = final_conv_layer.register_forward_hook(forward_hook)
    output = model(image_tensor)
    model.zero_grad()
    class_score = output[0][target_class]
    class_score.backward()
    handle.remove()
    
    grads = gradients[0].squeeze().numpy()
    acts = activations[0].squeeze().detach().numpy()
    weights = np.mean(grads, axis=(1, 2))
    cam = np.zeros(acts.shape[1:], dtype=np.float32)
    for i, w in enumerate(weights):
        cam += w * acts[i]
    cam = np.maximum(cam, 0)
    cam = cv2.resize(cam, (224, 224))
    cam = (cam - cam.min()) / (cam.max() - cam.min())
    return cam

# Choose the top predicted class for visualization
top_class = np.argmax(probs)
cam = get_grad_cam(model, image_tensor, top_class)

# Overlay heatmap on original image
heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
original_image = np.array(image.resize((224, 224)))
overlaid_img = cv2.addWeighted(original_image, 0.6, heatmap, 0.4, 0)

# Display the image
plt.figure(figsize=(6,6))
plt.imshow(overlaid_img)
plt.axis("off")
plt.title(f"Grad-CAM for: {classes[top_class]}")
plt.show()
