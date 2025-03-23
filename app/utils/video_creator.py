from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import tempfile
import os

def create_video(image_paths, audio_path):
    """
    Create a video from images and audio.
    
    Args:
        image_paths (list): List of paths to image files
        audio_path (str): Path to the audio file
    
    Returns:
        str: Path to the generated video file
    """
    try:
        # Load the audio file
        audio = AudioFileClip(audio_path)
        
        # Calculate duration per image
        duration_per_image = audio.duration / len(image_paths)
        
        # Create video clips from images
        video_clips = []
        for image_path in image_paths:
            clip = ImageClip(image_path).set_duration(duration_per_image)
            video_clips.append(clip)
        
        # Concatenate all clips
        final_video = concatenate_videoclips(video_clips)
        
        # Set the audio
        final_video = final_video.set_audio(audio)
        
        # Create output file
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
            # Write the video file
            final_video.write_videofile(
                temp_file.name,
                fps=24,
                codec='libx264',
                audio_codec='aac'
            )
            return temp_file.name
            
    except Exception as e:
        raise Exception(f"Error creating video: {str(e)}")
    finally:
        # Clean up
        if 'final_video' in locals():
            final_video.close()
        if 'audio' in locals():
            audio.close() 