import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='trajcontacts',
    version='1.0.0',
    scripts=['trajcontacts'] ,
    author='Midhun K Madhu',
    author_email='midhunkmadhu14@gmail.com',
    description="A package to caculate residue-residue contacts from MD trajectories",
    long_description=long_description,
  long_description_content_type="text/markdown",
    url='https://github.com/midhunkmadhu14/residuecontactsparent',
    packages=setuptools.find_packages(),
    license='BSD 2-clause',
    install_requires=['mdtraj',
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
    ],
)
