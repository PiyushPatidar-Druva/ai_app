# AI Story to Video Converter

This application converts text stories into engaging videos suitable for YouTube monetization. It uses AI to generate images and convert text to speech, creating a complete video with narration and visuals.

## Features

- Text-to-speech conversion using Google Text-to-Speech (gTTS)
- AI-powered image generation using Stable Diffusion
- Automatic video creation with synchronized narration and images
- Simple web interface for story input and video generation
- Support for multiple languages

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Rust (will be installed automatically if not present)
- Git (for cloning the repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/PiyushPatidar-Druva/ai_app.git
cd ai_app
```

2. Make the setup script executable and run it:
```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Create a virtual environment
- Install all required dependencies
- Set up the project structure
- Configure necessary directories

## Usage

1. Activate the virtual environment:
```bash
source venv/bin/activate
```

2. Start the application:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

4. Enter your story text in the web interface and click "Generate Video"

## Project Structure

```
ai_app/
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── utils/
│       ├── __init__.py
│       ├── image_generator.py
│       ├── text_to_speech.py
│       └── video_creator.py
├── static/
│   ├── css/
│   └── js/
├── templates/
├── requirements.txt
├── setup.sh
└── README.md
```

## Dependencies

- Flask: Web framework
- gTTS: Text-to-speech conversion
- Pillow: Image processing
- MoviePy: Video creation
- Transformers & Diffusers: AI image generation
- PyTorch: Deep learning framework
- Accelerate: Optimized inference

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Text-to-Speech (gTTS) for text-to-speech conversion
- Hugging Face for providing the Stable Diffusion model
- The open-source community for various tools and libraries used in this project 