from google.cloud import vision
from google.oauth2 import service_account

# Path to your service account key file
credentials = service_account.Credentials.from_service_account_file(r"C:\Users\T480\Downloads\my-project-p43-b7cf67a93a47.json")

# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=credentials)

# The path to the image file
image_path = r'C:\Users\T480\p43_1.jfif'

# Loads the image into memory
with open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs OCR on the image
response = client.text_detection(image=image)
texts = response.text_annotations

# Print the detected text
for text in texts:
    print(text.description)

# To extract only the first detected text (excluding additional information like bounding boxes)
# print(response.text_annotations[0].description)
