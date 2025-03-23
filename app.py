from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
from dotenv import load_dotenv
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import tempfile
import requests
from PIL import Image
import io
from transformers import pipeline
import torch

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize the image generation pipeline
image_generator = pipeline("text-to-image", model="runwayml/stable-diffusion-v1-5")

@app.route('/api/generate-video', methods=['POST'])
def generate_video():
    try:
        data = request.json
        story_text = data.get('story')
        language = 'en'  # Default to English
        
        # Split story into sentences for better visualization
        sentences = [s.strip() for s in story_text.split('.') if s.strip()]
        
        # Generate audio for each sentence
        audio_clips = []
        image_clips = []
        
        for sentence in sentences:
            # Generate speech using gTTS
            tts = gTTS(text=sentence, lang=language)
            
            # Save audio temporarily
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as audio_file:
                tts.save(audio_file.name)
                audio_path = audio_file.name
            
            # Generate image using Stable Diffusion
            image = image_generator(sentence, num_inference_steps=20)[0]["image"]
            
            # Save image temporarily
            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as image_file:
                image.save(image_file.name)
                image_path = image_file.name
            
            # Create clips
            audio_clip = AudioFileClip(audio_path)
            image_clip = ImageClip(image_path).set_duration(audio_clip.duration)
            
            audio_clips.append(audio_clip)
            image_clips.append(image_clip)
        
        # Combine all clips
        final_video = concatenate_videoclips(image_clips)
        final_audio = concatenate_videoclips(audio_clips)
        
        # Create final video
        final_video = final_video.set_audio(final_audio)
        
        # Save final video
        output_path = "output_video.mp4"
        final_video.write_videofile(output_path, fps=24)
        
        return jsonify({
            "success": True,
            "video_path": output_path
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/download-video', methods=['GET'])
def download_video():
    try:
        video_path = request.args.get('video_path')
        if not video_path or not os.path.exists(video_path):
            return jsonify({
                "success": False,
                "error": "Video file not found"
            }), 404
            
        return send_file(video_path, as_attachment=True)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True) 