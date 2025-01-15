import streamlit as st
from src.components.art_generator import OpenAIArtGenerator
from src.components.ui_components import UIComponents

def main():
    st.set_page_config(
        page_title="✨ AI Art Creator for Kids! 🎨",
        page_icon="🎨",
        layout="wide"
    )
    
    # Initialize components
    art_generator = OpenAIArtGenerator()
    
    # Add title and fun header
    st.title("🎨 AI Art Creator for Kids! ✨")
    st.markdown("### 🌈 Let's create some magical art together! 🪄")
    
    # Add fun welcome message
    st.markdown("""
    Welcome young artist! 👋 Ready to create something amazing? 
    Just tell me what you want to draw, and I'll help you make it! ✨
    """)
    
    # Get input from sidebar
    prompt, style = UIComponents.create_sidebar()
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Generate button
        if st.button("🎨 Create Magic! ✨", type="primary"):
            if prompt:
                with st.spinner("🪄 Creating your masterpiece... ✨"):
                    try:
                        # Generate and display art
                        image = art_generator.generate_art(prompt, style)
                        UIComponents.display_art(image)
                    except Exception as e:
                        st.error(f"Oops! 😅 Something went wrong: {str(e)}")
            else:
                st.warning("🤔 Please tell me what you'd like to create!")
    
    with col2:
        # Add fun instructions
        with st.expander("🎯 How to Create Art"):
            st.markdown("""
            ### 🌟 Easy Steps:
            1. 🤔 Think of something fun to draw
            2. 🎨 Pick your favorite style
            3. ✨ Click the magic button
            4. 💾 Save your masterpiece!
            
            ### 🎨 Art Styles:
            - 📺 Cartoon - Fun and playful
            - 🌊 Watercolor - Soft and dreamy
            - 👾 Pixel Art - Like video games
            - 📚 Comic Book - Bold and colorful
            """)
        
        # Add fun tips
        with st.expander("💡 Fun Art Ideas"):
            st.markdown("""
            Try drawing:
            - 🐉 A friendly dragon
            - 🚀 A space adventure
            - 🌈 A magical rainbow forest
            - 🦄 A unicorn having a party
            - 🌺 A garden of giant flowers
            - 🐠 An underwater kingdom
            """)

if __name__ == "__main__":
    main()