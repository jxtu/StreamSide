import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='streamside2',
    version='0.5',
    scripts=[],
    author='Jinho D. Choi',
    author_email='jinho.choi@emory.edu',
    description='Meaning Representation Annotation Toolkit',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jxtu/StreamSide',
    packages=setuptools.find_packages(),
    install_requires=[
         'PyQt6'
     ],
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: Apache Software License',
         'Operating System :: OS Independent',
     ],
    package_data={'streamside': ['resources/*/*.json']},
    include_package_data=True
 )