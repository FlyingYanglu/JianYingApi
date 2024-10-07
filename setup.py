from setuptools import setup, find_packages

setup(
    name="JianYingApi",  # Package name
    version="0.1.0",  # Initial version
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A Python wrapper for interacting with JianYing video editing software",
    long_description=open("README.md").read(),  # Long description from README file
    long_description_content_type="text/markdown",  # Specify that README is in Markdown format
    url="https://github.com/yourusername/JianYingApi",  # Replace with your repository URL
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        "uiautomation",
        "pyautogui",
        "wheel",
        "requests",
        "pillow",
        "keyboard",
        "pytz"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",  # Specify Python versions supported
        "License :: OSI Approved :: MIT License",  # License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
