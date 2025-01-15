from PIL import Image, ImageEnhance, ImageFilter
from typing import Tuple
import numpy as np

class ImageProcessor:
    """Handle image processing operations"""
    
    @staticmethod
    def resize_image(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
        """Resize image while maintaining aspect ratio"""
        return image.resize(size, Image.Resampling.LANCZOS)
    
    @staticmethod
    def adjust_brightness(image: Image.Image, factor: float) -> Image.Image:
        """Adjust image brightness"""
        enhancer = ImageEnhance.Brightness(image)
        return enhancer.enhance(factor)
    
    @staticmethod
    def apply_kid_friendly_filter(image: Image.Image) -> Image.Image:
        """Apply kid-friendly color enhancement"""
        # Increase saturation slightly
        saturation = ImageEnhance.Color(image)
        image = saturation.enhance(1.2)
        
        # Increase contrast slightly
        contrast = ImageEnhance.Contrast(image)
        image = contrast.enhance(1.1)
        
        # Smooth the image slightly
        image = image.filter(ImageFilter.SMOOTH)
        
        return image
    
    @staticmethod
    def add_watermark(image: Image.Image, text: str) -> Image.Image:
        """Add a watermark to the image"""
        from PIL import ImageDraw, ImageFont
        
        # Create a copy of the image
        watermarked = image.copy()
        draw = ImageDraw.Draw(watermarked)
        
        # Calculate text size and position
        width, height = image.size
        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
            
        # Add watermark text
        draw.text(
            (width - 100, height - 30),
            text,
            fill=(255, 255, 255, 128),
            font=font
        )
        
        return watermarked