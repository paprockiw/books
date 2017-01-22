#! /bin/bash

echo 'Downloading package.'
wget "https://pypi.python.org/packages/57/4f/e1df0437858188d2d36466a7bb89aa024d252bd0b7e3ba90cbc567c6c0b8/pdfminer-20140328.tar.gz#md5=dfe3eb1b7b7017ab514aad6751a7c2ea"
echo 'Unpacking.'
gunzip pdfminer*.tar.gz
tar -xvf pdfminer*.tar
echo 'Setting up.'
cd pdfminer*
python setup.py install
