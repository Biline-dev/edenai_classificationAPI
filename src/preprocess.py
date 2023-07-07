from io import BytesIO
import requests
import urllib.request
from PIL import Image
from torchvision import transforms
from pdf2image import convert_from_bytes


def get_image(image_path, file):

    """
    function to get image from URL or local file
    the function treats pdf files differently from other image formats
    """

    if image_path.startswith("http://") or image_path.startswith("https://"):
        # Image from URL            
        if image_path.endswith('.pdf'):
            response = urllib.request.urlopen(image_path)
            pdf_bytes = response.read()
            images = convert_from_bytes(pdf_bytes) # convert pdf to list of images
            return images
        elif image_path.endswith('.jpg') or image_path.endswith('.png') or image_path.endswith('.jpeg'):
            response = requests.get(image_path)
            content = BytesIO(response.content)
            return Image.open(content)
        else:
            raise Exception("Invalid file format. Only JPG, PNG JPEG and PDF files are allowed.")
    else:

        if image_path.endswith('.pdf'):
            return convert_from_bytes(file)
        elif image_path.endswith('.jpg') or image_path.endswith('.png') or image_path.endswith('.jpeg'):
            return Image.open(BytesIO(file))

class PreprocessImage:
    """
    Class to preprocess an image for our approach
    """
    
    def __call__(self, image) : 
        transform = transforms.Compose([
            transforms.Resize((150,150)),
            transforms.ToTensor(), 

        ])
        channels = transforms.ToTensor()(image)
        if channels.shape[0]>3 or channels.shape[0]<3:
            image = image.convert(mode='RGB')
        input_tensor = transform(image)
        return input_tensor

