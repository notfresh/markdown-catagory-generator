import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="md-gen", # Replace with your own username
    version="0.0.4",
    author="notfresh",
    author_email="notfresh@foxmail.com",
    description="generate the markdown catagory automatically and the template you set",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/notfresh/md-cata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/md-gen'],
    python_requires='>=3.6',
)
