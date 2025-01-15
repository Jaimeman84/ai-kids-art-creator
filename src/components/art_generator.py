from abc import ABC, abstractmethod
import openai
import requests
from PIL import Image
import io
import os
from dotenv import load_dotenv

load_dotenv()

class ArtGenerator(ABC):
    """Abstract base class for art generation"""
    
    @abstractmethod
    def generate_art(self, prompt: str, style: str) -> Image.Image:
        """Generate art based on prompt and style"""
        pass

class OpenAIArtGenerator(ArtGenerator):
    """Implementation of art generation using OpenAI's DALL-E"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        openai.api_key = self.api_key
        
    def _sanitize_prompt(self, prompt: str) -> str:
        """Remove any inappropriate content from prompt"""
        # Add content filtering logic here
        return prompt
    
    def generate_art(self, prompt: str, style: str) -> Image.Image:
        """Generate art using DALL-E"""
        sanitized_prompt = self._sanitize_prompt(f"{prompt} in {style} style")
        
        try:
            response = openai.images.generate(
                model="dall-e-3",
                prompt=sanitized_prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            
            # Get the URL of the generated image
            image_url = response.data[0].url
            
            # Download and convert to PIL Image
            image_response = requests.get(image_url)
            image = Image.open(io.BytesIO(image_response.content))
            return image
            
        except Exception as e:
            raise Exception(f"Failed to generate art: {str(e)}")