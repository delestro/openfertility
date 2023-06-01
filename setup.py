from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="openfertility",
    version="0.1.0",
    author="Felipe Delestro",
    author_email="delestro@gmail.com",
    description="Machine learning and data analysis for fertility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/delestro/openfertility",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        "pandas",
        "numpy",
        "torch",
        "torchvision",
        "scikit-learn",
        "matplotlib",
    ],
)
