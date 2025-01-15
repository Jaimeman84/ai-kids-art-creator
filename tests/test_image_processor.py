import pytest
from PIL import Image
from src.components.image_processor import ImageProcessor

class TestImageProcessor:
    @pytest.fixture
    def sample_image(self):
        """Create a sample image for testing"""
        return Image.new('RGB', (100, 100), color='red')
    
    def test_resize_image(self, sample_image):
        """Test image resizing"""
        new_size = (50, 50)
        resized = ImageProcessor.resize_image(sample_image, new_size)
        assert resized.size == new_size
    
    def test_adjust_brightness(self, sample_image):
        """Test brightness adjustment"""
        factor = 1.5
        brightened = ImageProcessor.adjust_brightness(sample_image, factor)
        assert isinstance(brightened, Image.Image)
        assert brightened.size == sample_image.size
    
    def test_kid_friendly_filter(self, sample_image):
        """Test kid-friendly filter application"""
        filtered = ImageProcessor.apply_kid_friendly_filter(sample_image)
        assert isinstance(filtered, Image.Image)
        assert filtered.size == sample_image.size
    
    def test_add_watermark(self, sample_image):
        """Test watermark addition"""
        watermarked = ImageProcessor.add_watermark(sample_image, "Test")
        assert isinstance(watermarked, Image.Image)
        assert watermarked.size == sample_image.size
        # Original image should not be modified
        assert watermarked is not sample_image