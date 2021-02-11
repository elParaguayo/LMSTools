import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LMSTools",
    version="0.0.1",
    author="Andreas Schamberger",
    author_email="mail@andreass.net",
    description="A python library for iteracting with your Logitech Media Server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aschamberger/LMSTools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)