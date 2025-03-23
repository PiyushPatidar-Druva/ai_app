from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from app.utils.text_to_speech import generate_speech
from app.utils.image_generator import generate_images
from app.utils.video_creator import create_video

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_story():
    try:
        # Get story text from request
        story_text = request.form.get('story_text')
        if not story_text:
            return jsonify({'error': 'No story text provided'}), 400

        # Generate speech from text
        audio_path = generate_speech(story_text)
        
        # Generate images for the story
        image_paths = generate_images(story_text)
        
        # Create video with images and audio
        video_path = create_video(image_paths, audio_path)
        
        # Return video file
        return send_file(
            video_path,
            mimetype='video/mp4',
            as_attachment=True,
            download_name='story_video.mp4'
        )

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 