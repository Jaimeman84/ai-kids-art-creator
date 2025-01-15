import pytest
from PIL import Image
from src.components.art_generator import OpenAIArtGenerator
from unittest.mock import patch, MagicMock
import io

class TestOpenAIArtGenerator:
    @pytest.fixture
    def generator(self):
        with patch('os.getenv', return_value='fake-api-key'):
            return OpenAIArtGenerator()
    
    def test_sanitize_prompt(self, generator):
        # Test prompt sanitization
        prompt = "A happy dragon"
        sanitized = generator._sanitize_prompt(prompt)
        assert isinstance(sanitized, str)
        assert len(sanitized) > 0
    
    @patch('openai.images.generate')
    @patch('requests.get')
    def test_generate_art(self, mock_requests_get, mock_generate, generator):
        # Create a sample image for testing
        test_image = Image.new('RGB', (100, 100), color='red')
        img_byte_arr = io.BytesIO()
        test_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Mock the OpenAI API response
        mock_response = MagicMock()
        mock_response.data = [MagicMock(url="http://fake-url.com/image.png")]
        mock_generate.return_value = mock_response
        
        # Mock the requests.get response
        mock_requests_response = MagicMock()
        mock_requests_response.content = img_byte_arr
        mock_requests_get.return_value = mock_requests_response
        
        # Test art generation
        result = generator.generate_art("Test prompt", "cartoon")
        
        # Verify the result
        assert isinstance(result, Image.Image)
        assert result.size == (100, 100)
        
        # Verify our mocks were called
        mock_generate.assert_called_once()
        mock_requests_get.assert_called_once_with("http://fake-url.com/image.png")

    def test_missing_api_key(self):
        # Test initialization with missing API key
        with patch('os.getenv', return_value=None):
            with pytest.raises(ValueError) as exc_info:
                OpenAIArtGenerator()
            assert "OPENAI_API_KEY not found" in str(exc_info.value)
            
    @patch('openai.images.generate')
    def test_generate_art_failure(self, mock_generate, generator):
        # Test handling of API errors
        mock_generate.side_effect = Exception("API Error")
        
        with pytest.raises(Exception) as exc_info:
            generator.generate_art("Test prompt", "cartoon")
        assert "Failed to generate art" in str(exc_info.value)