# AI Story to Video Converter

This application converts text stories into videos by generating images using AI and combining them with text-to-speech narration.

## Features

- Text-to-speech conversion using gTTS
- AI-powered image generation using Stable Diffusion
- Video creation with synchronized audio and images
- Downloadable video output

## Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Rust (for tokenizers package)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ai_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# OR
.\venv\Scripts\activate  # On Windows
```

3. Install Rust (required for tokenizers):
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

4. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

## Usage

[Add usage instructions once the application is implemented]

## Project Structure

```
ai_app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── utils/
│       ├── text_to_speech.py
│       ├── image_generator.py
│       └── video_creator.py
├── static/
├── templates/
├── requirements.txt
├── setup.sh
└── README.md
```

## Contributing

[Add contribution guidelines if needed]

## License

[Add license information] 