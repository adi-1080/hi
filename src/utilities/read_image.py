from PIL import Image
import io
import cv2
import numpy as np

def readImage(file) -> Image.Image:
    # Open image from bytes with PIL and convert to RGB
    image = Image.open(io.BytesIO(file)).convert("RGB")
    # Convert PIL image to numpy array (RGB)
    np_img = np.array(image)
    # Convert RGB to BGR for OpenCV
    np_img_bgr = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    # Resize image to 256x256 using OpenCV
    resized_bgr = cv2.resize(np_img_bgr, (256, 256), interpolation=cv2.INTER_AREA)
    # Convert back to RGB
    resized_rgb = cv2.cvtColor(resized_bgr, cv2.COLOR_BGR2RGB)
    # Convert to PIL Image
    resized_image = Image.fromarray(resized_rgb)
    return resized_image
