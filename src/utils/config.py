import os
from typing import Dict, List

class Config:
    """Application configuration settings"""
    
    # Art styles and their descriptions
    ART_STYLES: Dict[str, str] = {
        "Cartoon": "Fun and playful cartoon style",
        "Watercolor": "Soft and dreamy watercolor painting",
        "Pixel Art": "Retro-style pixel art",
        "Comic Book": "Bold and colorful comic book style"
    }
    
    # Image generation settings
    IMAGE_SETTINGS = {
        "size": (1024, 1024),
        "quality": "standard",
        "format": "png"
    }
    
    # Safety settings
    BLOCKED_WORDS: List[str] = [
        # Add inappropriate words here
        "inappropriate",
        "violent",
        "scary"
    ]
    
    # File storage settings
    STORAGE_DIR = "generated_images"
    MAX_FILE_SIZE_MB = 10
    
    # UI settings
    UI_THEME = {
        "primaryColor": "#FF4B4B",
        "backgroundColor": "#FFFFFF",
        "secondaryBackgroundColor": "#F0F2F6",
        "textColor": "#31333F"
    }
    
    @classmethod
    def get_env_variable(cls, var_name: str, default: str = None) -> str:
        """Safely get environment variable"""
        return os.getenv(var_name, default)
    
    @classmethod
    def is_development(cls) -> bool:
        """Check if running in development environment"""
        return cls.get_env_variable('ENVIRONMENT', 'development') == 'development'