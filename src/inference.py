import time
import torch

from src.preprocess import  PreprocessImage,  get_image



class ClassifyDocResnet():
    """
    Class to classify image using ResNet architecture
    """

    def __init__(self, preprocess, model, device, image):
        self.image = preprocess(image)
        self.image = self.image.unsqueeze(0)
        self.model = model
        self.device = device

    def classify(self):
        start_time = time.time()
        with torch.no_grad():
            output = self.model(self.image.to(self.device))
        sigmoid = torch.nn.Sigmoid()
        probs = sigmoid(output.squeeze().cpu())
        _, prob_id = torch.max(probs, 0)
        classes = ["handwritten", "id", "invoice", "receipt", "resume", "table"]
        class_table = {}
        for i in range(len(classes)):
            class_table[classes[i]] = str(int(probs[i] * 100)) + "%"
        

        time_end = time.time()
        predicted_label = classes[prob_id.item()]
        return dict(sorted(class_table.items())), predicted_label, time_end - start_time


def classify(image, device, model_doc):
    
        preprocess_image = PreprocessImage()
        classification, predicted_label, time_resnet = ClassifyDocResnet(preprocess = preprocess_image, 
                                    model = model_doc, 
                                    device = device,  
                                    image = image).classify()
        return classification, predicted_label, time_resnet
    

def doc_classifier(file, image_path, device, model_doc):

    # get the image from the URL or the local file
    content = get_image(image_path, file)

    if image_path.lower().endswith('.jpg') or image_path.lower().endswith('.png') or image_path.lower().endswith('.jpeg'): 
        return classify(content, device, model_doc)
    
    elif image_path.lower().endswith('.pdf') :

        predicted_label_images = []
        time_execution = []

        for image in content:
            classification, predicted_label, execution_time = classify(image, device, model_doc)
            predicted_label_images.append(classification)
            time_execution.append(execution_time)

        # Find the maximum value in the matrix and take its vector
        max_vector = max(predicted_label_images, key=lambda x: max(float(value.strip('%')) for value in x.values()))
        # Find the maximum value in the vector
        max_label = max(max_vector, key=lambda x: float(max_vector[x][:-1]))
        max_label = str(max_label)
        
        return max_vector,  max_label,  sum(time_execution)
        