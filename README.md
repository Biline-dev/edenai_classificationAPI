# edenai_classificationAPI

## Abstract 
During the implementation of our final year project, we focused on automating document
classification to meet the needs of the company EdenAI. Our main objective was to create an
API capable of taking a document as input and returning the corresponding type among the
following categories : handwritten, id, invoice, receipt, resume, or table. To achieve this goal, we
explored different solutions and approaches, relying on the latest technological advancements
in the field, such as automatic document understanding.

We considered several approaches for our project, starting with a direct approach using
the ResNet model for image classification. Then, we developed a more customized solution by
implementing a classification pipeline. This pipeline combines two models : a vision model and
a natural language processing (NLP) model. Lastly, we explored an end-to-end approach by
training the Donut model. This model does not rely on OCR but uses a vision encoder to
process the image and an NLP decoder to process the extracted text.

We then evaluated our different solutions using classification metrics such as recall, precision,
accuracy, specificity, and F1 score. Due to its ability to generalize across different languages,
the Attention ResNet model proved to be the best solution for deployment, offering optimal
performance and efficient execution time.

**Key words :** Deep Learning, Natural Language Processing (NLP), computer vision (CV), Document understanding, OCR.

## Installation

Use these commands to install the dependencies on a virtual environment.

```bash
python3 -m venv eden_env
```
```bash
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```
```bash
pip3 install -r requirements_linux.txt
```

## Create a docker container

#### Create the image
```bash
docker build -t user_name/edenai_app .
```
#### Create the container
```bash
docker run -d -p 8000:8000 image_name
```

## Testing
Run the file **test.py** to try our API. Make sure to change the **ip** address of the endpoint link if necessary.