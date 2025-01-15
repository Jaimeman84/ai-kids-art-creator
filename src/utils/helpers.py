import re
from typing import List, Optional
from datetime import datetime
import os

class Helpers:
    """Utility helper functions"""
    
    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Convert string to valid filename"""
        # Remove invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        # Replace spaces with underscores
        filename = filename.replace(' ', '_')
        return filename
    
    @staticmethod
    def generate_unique_filename(base_name: str, extension: str) -> str:
        """Generate unique filename with timestamp"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        sanitized_name = Helpers.sanitize_filename(base_name)
        return f"{sanitized_name}_{timestamp}.{extension}"
    
    @staticmethod
    def ensure_directory_exists(directory: str) -> None:
        """Create directory if it doesn't exist"""
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    @staticmethod
    def is_safe_prompt(prompt: str, blocked_words: List[str]) -> bool:
        """Check if prompt contains inappropriate content"""
        prompt_lower = prompt.lower()
        return not any(word in prompt_lower for word in blocked_words)
    
    @staticmethod
    def get_file_size(file_path: str) -> Optional[int]:
        """Get file size in bytes"""
        try:
            return os.path.getsize(file_path)
        except OSError:
            return None
    
    @staticmethod
    def format_file_size(size_in_bytes: int) -> str:
        """Convert file size to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.1f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.1f} TB"