from setuptools import setup, find_packages

setup(
    name="ai-art-creator",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.32.0',
        'Pillow>=10.0.0',
        'numpy>=1.24.3',
        'pytest>=7.4.0',
        'python-dotenv>=1.0.0',
        'openai>=1.12.0',
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI Art Creator for Kids using Streamlit",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai-art-creator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)