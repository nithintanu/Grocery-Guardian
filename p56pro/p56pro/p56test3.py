import requests

# URL of the Free OCR API
url = "https://api.ocr.space/parse/image"

# Your API key (get it from https://ocr.space/ocrapi)
api_key = 'K86303818288957'

# Path to your image file
image_path = r'C:\Users\T480\p43_1.jpg'

# Open the image file
with open(image_path, 'rb') as file:
    # Prepare the request data
    payload = {
        'apikey': api_key,
        'language': 'eng',  # Change to the language of the text in your image if needed
    }

    # Send the POST request with the image file
    response = requests.post(url, files={'file': file}, data=payload)

    # Parse the JSON response
    result = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the parsed text from the response
        parsed_text = result #['ParsedResults'][0]['ParsedText']
        
        # Print the extracted text
        print(parsed_text)
    else:
        # If the request was unsuccessful, print the error message
        print("Error:", result['ErrorMessage'])
