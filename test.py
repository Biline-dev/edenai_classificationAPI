import requests


# Endpoint of the API
url="http://127.0.0.1:8000/document_classification"


##############################  Test the API with a URL #############################
payload = {"url_path": "https://dagrs.berkeley.edu/sites/default/files/2020-01/sample.pdf"}
response = requests.post(url, params=payload)
# Handle the response
if response.status_code == 200:
    # Request successful
    print(response.json())
else:
    # Request failed
    print("Error:", response.status_code)


############################## Test the API with a local file #############################""
files = {"file": open("a path to your local file .pdf, .jpeg, .png, .jpg",'rb')}
response = requests.post(url, files=files)

# Handle the response
if response.status_code == 200:
    # Request successful
    print(response.json())
else:
    # Request failed
    print("Error:", response.status_code)