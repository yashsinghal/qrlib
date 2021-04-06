import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "style_qrlib",
    version = "1.1.0",
    author = "Yash Singhal",
    author_email = "yashsinghal0316@gmail.com",
    description = ("QR Image and PDF generation library"),
    license = "Propietary",
    keywords = "qr library qrlib ideal",
    url = "https://github.com/yashsinghal/qrlib",
    packages=['style_qrlib', 'style_qrlib.lib', 'style_qrlib.fonts',
              'style_qrlib.tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 1 - Stable",
        "Topic :: Utilities",
        ],
    package_dir={'style_qrlib': 'qrlib'},
    package_data={'style_qrlib': ['static/*']},
    install_requires=['Pillow>=1.1.7', 'unittest2>=0.5.1', 'pyzbar>=0.1.8',
                      'CairoSVG>=0.4.4']
    )
