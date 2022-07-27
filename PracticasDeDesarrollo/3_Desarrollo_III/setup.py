import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='humai_utils',
    version='0.1.0',
    author='Ramiro Savoie',
    author_email='ramiro@deployr.ai',
    description='A compilation of Humai utility functions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/institutohumai/humai_utils',
    project_urls = {
        "Bug Tracker": "https://github.com/institutohumai/humai_utils/issues"
    },
    license='MIT',
    packages=['humai_utils'],
    install_requires=['requests'],
)