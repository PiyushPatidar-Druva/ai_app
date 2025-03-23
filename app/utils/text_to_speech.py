from gtts import gTTS
import os
import tempfile

def generate_speech(text, language='en'):
    """
    Generate speech from text using gTTS.
    
    Args:
        text (str): The text to convert to speech
        language (str): The language code (default: 'en' for English)
    
    Returns:
        str: Path to the generated audio file
    """
    try:
        # Create a temporary file for the audio
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            # Generate speech
            tts = gTTS(text=text, lang=language)
            tts.save(temp_file.name)
            return temp_file.name
    except Exception as e:
        raise Exception(f"Error generating speech: {str(e)}") 