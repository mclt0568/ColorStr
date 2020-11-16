import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ColorStr',  
     version='1.2',
     author="mclt0568",
     author_email="tis7bfrankie@gmail.com",
     description="A better way to output colored text",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mclt0568/ColorStr",
     py_modules=["ColorStr"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
 )
