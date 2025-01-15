import pytest
import os
from src.utils.helpers import Helpers

class TestHelpers:
    def test_sanitize_filename(self):
        """Test filename sanitization"""
        dirty_filename = 'test<>:"/\\|?*file.txt'
        clean_filename = Helpers.sanitize_filename(dirty_filename)
        assert all(c not in clean_filename for c in '<>:"/\\|?*')
        
    def test_generate_unique_filename(self):
        """Test unique filename generation"""
        base_name = "test_file"
        extension = "png"
        filename = Helpers.generate_unique_filename(base_name, extension)
        assert filename.startswith(base_name)
        assert filename.endswith(extension)
        assert '_' in filename  # Should contain timestamp
        
    def test_ensure_directory_exists(self, tmp_path):
        """Test directory creation"""
        test_dir = tmp_path / "test_dir"
        Helpers.ensure_directory_exists(str(test_dir))
        assert test_dir.exists()
        
    def test_is_safe_prompt(self):
        """Test prompt safety check"""
        blocked_words = ['bad', 'inappropriate']
        assert Helpers.is_safe_prompt("hello world", blocked_words) is True
        assert Helpers.is_safe_prompt("bad word", blocked_words) is False
        
    def test_get_file_size(self, tmp_path):
        """Test file size retrieval"""
        # Create a test file
        test_file = tmp_path / "test.txt"
        test_file.write_text("test content")
        
        size = Helpers.get_file_size(str(test_file))
        assert size is not None
        assert size > 0
        
    def test_format_file_size(self):
        """Test file size formatting"""
        assert Helpers.format_file_size(1024) == "1.0 KB"
        assert Helpers.format_file_size(1024 * 1024) == "1.0 MB"
        assert Helpers.format_file_size(500) == "500.0 B"