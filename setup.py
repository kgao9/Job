import os 
from setuptools import setup  
# Utility function to read the README file. 
# Used for the long_description.  It's nice, because now 1) we have a top level 
# README file and 2) it's easier to type in the README file than to put a raw # string in below ... 
def read(fname):     
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
  
setup(
     name = "job_cli",
     version = "0.0.1",
     author = "kgao9",
     author_email = "kgao9@wisc.edu",
     description = ("a CLI to remember jobs and companies"),
     license = "",
     keywords = "job CLI",
     packages=['job_cli', 'tests'],
     long_description='',
     classifiers=[
         "Development Status :: 3 - Alpha",
         "Topic :: Utilities",
         "License :: OSI Approved :: BSD License",
     ], 
)
