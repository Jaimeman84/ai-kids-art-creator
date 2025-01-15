import streamlit as st
from typing import List, Tuple

class UIComponents:
    """Reusable UI components for the art creator app"""
    
    @staticmethod
    def create_sidebar() -> Tuple[str, str]:
        """Create sidebar with art generation controls"""
        with st.sidebar:
            st.title("🎨 Art Controls")
            
            # Art style selection
            style = st.selectbox(
                "Choose Art Style",
                ["Cartoon", "Watercolor", "Pixel Art", "Comic Book"]
            )
            
            # Prompt input
            prompt = st.text_input(
                "What would you like to create?",
                placeholder="A friendly dragon in a garden"
            )
            
            return prompt, style
    
    @staticmethod
    def display_art(image) -> None:
        """Display generated art with download button"""
        if image:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.image(image, caption="Your Generated Art!")
            with col2:
                # Convert image to bytes for download
                img_bytes = UIComponents._convert_image_to_bytes(image)
                st.download_button(
                    label="Download Art!",
                    data=img_bytes,
                    file_name="my_art.png",
                    mime="image/png"
                )
    
    @staticmethod
    def _convert_image_to_bytes(image) -> bytes:
        """Convert PIL Image to bytes"""
        import io
        buf = io.BytesIO()
        image.save(buf, format='PNG')
        return buf.getvalue()