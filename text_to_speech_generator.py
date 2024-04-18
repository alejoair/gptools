import boto3
import sys

def generate_voice(language, text, output_filename):
    try:
        # Create a Polly client
        polly_client = boto3.client('polly', region_name='us-east-1')

        # Set the language ID for the voice
        voice_map = {'es': 'Lupe', 'en': 'Matthew'}
        voice_id = voice_map.get(language)
        
        if not voice_id:
            raise ValueError(f"Unsupported language '{language}'. Supported languages are: {list(voice_map.keys())}")

        # Request Polly to convert text to speech
        response = polly_client.synthesize_speech(VoiceId=voice_id,
                                                  Engine='neural',
                                                  OutputFormat='mp3',
                                                  Text=text)

        # Save the audio in a file
        if 'AudioStream' in response:
            with open(output_filename, 'wb') as file:
                file.write(response['AudioStream'].read())
            print(f"Audio file saved as {output_filename}")
        else:
            raise Exception("Polly response did not contain audio stream.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        generate_voice(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python generate_voice.py <language_code> '<message>' <output_file>")
