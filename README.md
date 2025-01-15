# 🎨 AI Art Creator for Kids

A fun and interactive Streamlit application that lets kids create amazing AI-generated art through simple prompts and controls! 🌈✨

## ⭐ Features

- 🎯 Simple and kid-friendly interface
- 🛡️ Safe prompt filtering
- 🎭 Multiple art styles
- 💾 Easy download options
- 👨‍👩‍👧‍👦 Parent controls
- 🖼️ High-quality AI-generated images

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher 🐍
- OpenAI API key 🔑

### 🔑 Getting Your OpenAI API Key

1. Visit [OpenAI's website](https://platform.openai.com/signup)
2. Create an account or sign in
3. Go to [API Keys section](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy your API key (make sure to save it somewhere safe - you won't be able to see it again!)

### 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/Jaimeman84/ai-kids-art-creator.git
cd ai-art-creator
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
streamlit run run.py
```

## 🧪 Running Tests

```bash
pytest tests/
```

## 🏗️ Project Structure

The project follows SOLID principles for clean and maintainable code:

```
ai-art-creator/
├── src/                  # Source code
│   ├── components/      # UI and functional components
│   └── utils/          # Helper functions and configs
├── tests/              # Test files
└── run.py             # Application entry point
```

## 🎯 How to Use

1. 🤔 Think of something fun to draw
2. 🎨 Choose your favorite art style:
   - Cartoon
   - Watercolor
   - Pixel Art
   - Comic Book
3. ✨ Click the "Create Art!" button
4. 💾 Download your masterpiece!

## 🔒 Safety Features

- Content filtering for prompts
- Kid-friendly interface
- Parental controls
- Safe image generation

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐞 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**
   ```
   Make sure you're running the app from the project root directory
   Check if all requirements are installed: pip install -r requirements.txt
   ```

2. **OpenAI API Key Error**
   ```
   Verify your .env file exists in the project root
   Check if the API key is correctly copied
   Make sure the API key is active in your OpenAI account
   ```

3. **Image Generation Error**
   ```
   Check your internet connection
   Verify your OpenAI account has available credits
   Try refreshing the page
   ```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Acknowledgments

- OpenAI for the DALL-E API
- Streamlit for the amazing web framework
- All our contributors and users!

## 📞 Support

If you need help or have any questions:
- 📧 Submit an issue in the GitHub repository
- 🌐 Check out our documentation
- 💬 Join our community discussions

Happy Creating! 🎨✨