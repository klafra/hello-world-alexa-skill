import json

def lambda_handler(event, context):
    # Check if the request is an IntentRequest and if it matches the HelloWorldIntent
    if event['request']['type'] == "IntentRequest" and event['request']['intent']['name'] == "HelloWorldIntent":
        # Prepare the response to Alexa
        speech_text = "Hello, world!"
        
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': speech_text
                },
                'shouldEndSession': True
            }
        }
