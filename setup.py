from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    'PyMuPDF>=1.23.7'
]

setup(
    name='PDFFiller',
    packages=find_packages(exclude=['examples']),
    version='0.1.0',
    install_requires=install_requires,
    description='Simple library to fill PDF documents',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ali Moussawi',
    author_email="moussawidev@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    url='https://github.com/Moussawi7/pdf-filler',
)