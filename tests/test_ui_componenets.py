import pytest
from PIL import Image
import io
from src.components.ui_components import UIComponents

class TestUIComponents:
    @pytest.fixture
    def sample_image(self):
        """Create a sample image for testing"""
        return Image.new('RGB', (100, 100), color='red')
    
    def test_convert_image_to_bytes(self, sample_image):
        """Test image to bytes conversion"""
        img_bytes = UIComponents._convert_image_to_bytes(sample_image)
        assert isinstance(img_bytes, bytes)
        assert len(img_bytes) > 0
        
        # Verify the bytes can be converted back to an image
        img = Image.open(io.BytesIO(img_bytes))
        assert isinstance(img, Image.Image)
        assert img.size == sample_image.size