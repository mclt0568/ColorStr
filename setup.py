import setuptools
with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='ColorStr',  
     version='1.3',
     author="mclt0568",
     author_email="tis7bfrankie@gmail.com",
     description="A better way to output colored text",
     long_description=long_description,
     # long_description_content_type="text/markdown",
     url="https://github.com/mclt0568/ColorStr",
     py_modules=["ColorStr","colorstrparser","colors"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
 )
