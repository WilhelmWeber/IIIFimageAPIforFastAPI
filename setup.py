from setuptools import setup

setup(
    name="FastIIIFimageAPI",
    description="iiif ImageAPI for FastAPI",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/WilhelmWeber",
    license='MIT',
    author='Yuto_Takizawa',
    author_email="mokoda5243@gmail.com",
    version='0.0.1',
    package_dir=['./dist'],
    install_requires={
        'pillow>=10.2.0',
        'fastapi>=0.104.1'
    },
)