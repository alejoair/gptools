import boto3
import sys

def generate_voice(language, text, output_filename):
    # Crea un cliente de Polly
    polly_client = boto3.client('polly', region_name='us-east-1')


    # Establece el ID del idioma para la voz
    if language == "es":
        voice_id = "Penelope"
    elif language == "en":
        voice_id = "Joanna"
    else:
        raise ValueError("Unsupported language.")

    # Solicita a Polly que convierta el texto a habla
    response = polly_client.synthesize_speech(VoiceId=voice_id,
                                          Engine='neural',
                                          OutputFormat='mp3', 
                                          Text=text)

    # Guarda el audio en un archivo
    if 'AudioStream' in response:
        with open(output_filename, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f"Audio file saved as {output_filename}")
    else:
        print("Could not stream audio from Polly response.")

if __name__ == '__main__':
    if len(sys.argv) == 4:
        generate_voice(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: python generate_voice.py <language_code> '<message>' <output_file>")

