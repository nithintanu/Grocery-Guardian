import requests

# URL of the Free OCR API
url = "https://api.ocr.space/parse/image"

# Your API key (get it from https://ocr.space/ocrapi)
api_key = 'K86303818288957'

# Path to your image file
image_path = r'C:\Users\T480\p43_1.jpg'
parsed_text=''
try:
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
            parsed_text = result['ParsedResults'][0]['ParsedText']
            
            # Print the extracted text
            print("ocr result :::::::::::::: ", parsed_text)
        else:
            # If the request was unsuccessful, print the error message
            print("Error:", result['ErrorMessage'])
except Exception as ep:
    pass 

######################################

import openai 
openai.api_key = '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' #my api key .. should usually be kept private and not shared

if parsed_text!='':
    list=parsed_text 
    # def map_language_code_to_name(language_code):
    #     language_mapping = {
    #         "en": "English",
    #         "es": "Spanish",
    #         "fr": "French",
    #         "de": "German",
    #         "te": "Telugu",
    #         "ta": "Tamil",
    #         "sv": "Swedish"
    #     }
    #     return language_mapping.get(language_code, "English")  # Default to English if not found

    def advice_text(text, list, pagelang='en'):

        engine ="gpt-3.5-turbo" # the gpt engine used - can be chnaged based on functionality wanted
        language_name = pagelang # map_language_code_to_name(pagelang)

        

        # Call GPT-3.5-turbo for text summarization
        result = openai.ChatCompletion.create(
            model=engine,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"I have {text}, I am about to buy an item with following ingredients: {list}. Is it unhealthy for me "},
                #{"role": "user", "content": f"translate the following text:\n{text} in {language_name}"}
            ]
        )

        return result.choices[0].message['content']

    #list="serving size:160g, total fat:2g 3%, calories:190, saturated fat:1.5g, sodium:630mg 27%, total carbohydates: 13g 5%"
    r = advice_text('diabetes',list, 'en' )
    print(r)
