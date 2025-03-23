from diffusers import StableDiffusionPipeline
import torch
import tempfile
import os
import re

def split_text_into_scenes(text, max_length=20):
    """
    Split text into smaller scenes for image generation.
    
    Args:
        text (str): The input text
        max_length (int): Maximum length for each scene
    
    Returns:
        list: List of text segments
    """
    # Split text into sentences
    sentences = re.split(r'[.!?]+', text)
    
    # Combine sentences into scenes
    scenes = []
    current_scene = []
    current_length = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        if current_length + len(sentence.split()) > max_length:
            if current_scene:
                scenes.append(' '.join(current_scene))
            current_scene = [sentence]
            current_length = len(sentence.split())
        else:
            current_scene.append(sentence)
            current_length += len(sentence.split())
    
    if current_scene:
        scenes.append(' '.join(current_scene))
    
    return scenes

def generate_images(text, num_images=2):
    """
    Generate images from text using Stable Diffusion.
    
    Args:
        text (str): The text to generate images from
        num_images (int): Number of images to generate
    
    Returns:
        list: List of paths to the generated images
    """
    try:
        # Initialize the Stable Diffusion pipeline with a smaller model
        pipe = StableDiffusionPipeline.from_pretrained(
            "CompVis/stable-diffusion-v1-4",  # Using a smaller model
            torch_dtype=torch.float32,  # Using float32 for better CPU compatibility
            use_safetensors=True
        )
        
        # Enable memory efficient attention
        pipe.enable_attention_slicing()
        
        # Split text into scenes
        scenes = split_text_into_scenes(text)
        
        # Generate images for each scene
        image_paths = []
        for scene in scenes:
            # Create a more specific prompt
            prompt = f"high quality scene: {scene}"
            
            # Generate images for the scene with reduced steps
            images = pipe(
                prompt,
                num_inference_steps=15,  # Reduced from 20
                num_images_per_prompt=1,
                guidance_scale=7.0,  # Slightly reduced
                height=512,  # Reduced resolution
                width=512
            ).images
            
            # Save the first image
            with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
                images[0].save(temp_file.name)
                image_paths.append(temp_file.name)
            
            # Break if we have enough images
            if len(image_paths) >= num_images:
                break
        
        return image_paths
    except Exception as e:
        raise Exception(f"Error generating images: {str(e)}") 