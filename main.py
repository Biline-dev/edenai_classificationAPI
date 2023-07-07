
import torch

from fastapi import FastAPI, HTTPException, UploadFile

from src.inference import doc_classifier

# get device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

RESNET_ALL_PATH = 'saved_models/resnet_all_model_state.pth'
MODEL_RESNET_ALL = torch.load(RESNET_ALL_PATH, map_location=DEVICE)


app = FastAPI()

@app.post("/document_classification/")
async def create_upload_file(file: UploadFile = None, url_path: str = None):

    if url_path is not None:  # if the file is a URL
        url_or_path = url_path
        file_content = None
    elif file is not None: # if the file is a local file
        file_content = await file.read()
        url_or_path = file.filename
    else:
        raise HTTPException(status_code=400, detail="Invalid file format. Only JPG, PNG JPEG and PDF files are allowed.", 
                            headers={"X-Error": "File extension is not valid."})

    if url_or_path.lower().endswith('.jpg') or url_or_path.lower().endswith('.png') \
    or url_or_path.lower().endswith('.jpeg') or url_or_path.lower().endswith('.pdf') \
    or url_or_path.startswith("http://") or url_or_path.startswith("https://"):
        classification, predicted_label, execution_time = doc_classifier(file=file_content, image_path = url_or_path, device = DEVICE, 
                                                                          model_doc = MODEL_RESNET_ALL)
        # return the file & the class
        return {"predicted_classes" : classification, 'execution_time' : execution_time, "predicted_lable" : predicted_label}
    else : # error
        raise HTTPException(status_code=400, detail="Invalid file format. Only JPG, PNG JPEG and PDF files are allowed.", 
                            headers={"X-Error": "File extension is not valid."})
