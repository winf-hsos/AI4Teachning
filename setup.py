from setuptools import setup, find_packages

setup(
    name='ai4teaching',
    version='0.1.1',
    packages=find_packages(),
    description='API for useful AI tool in learning and teaching scenarios.',
    author='Nicolas Meseth, Philipp Zmijewski',
    author_email='n.meseth@hs-osnabrueck.de, philipp.zmijewski@hs-osnabrueck.de',
    url='https://github.com/winf-hsos/AI4Teaching',
    install_requires=[
        'openai',
        'chromadb',
        'pytube',
        'PyPDF2',
        'moviepy',
        'langchain',
        'colorama',
        'mimetypes-magic',
        'unstructured',
        'unstructured[pdf]'
    ],
    license='CC BY-NC-SA 4.0'    
)