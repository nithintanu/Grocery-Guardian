import openai 
openai.api_key = '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' #my api key .. should usually be kept private and not shared


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

list="serving size:160g, total fat:2g 3%, calories:190, saturated fat:1.5g, sodium:630mg 27%, total carbohydates: 13g 5%"
r = advice_text('diabetes',list, 'en' )
print(r)
