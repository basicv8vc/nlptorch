"""
In order to create a package for pypi, you need to follow several steps.

1. Create a .pypirc in your home directory. It should look like this:

```
[distutils]
index-servers = 
    pypi
    pypitest

[pypi]
username=nlptorch
password= Get the password from Lastpass.

[pypitest]
repository=https://test.pypi.org/legacy/
username=nlptorch
password= Get the password from LastPass.
```

run chmod 600 ./pypirc so only you can read/write.

1. Change the version in docs/conf.py and setup.py.

2. Commit these changes with the message: "Release: VERSION"

3. Add a tag in git to mark the release: "git tag VERSION -m'Affs tag VERSION for pypi' "
    Push the tag to git: git push --tags origin master

4. Build both the sources and wheel. Do not change anything in setup.py between
    creating the wheel and the source distribution (obviously).

    For the wheel, run: "python setup.py bdist_wheel" in the top level nlptorch directory.
    (this will build a wheel for the python version you use to build it - make sure you use python 2.7).
    
    For the sources, run: "python setup.py sdist"
    You should now have a /dist directory with both .whl and .tar.gz source versions of nlptorch.

5. Check that everything looks correct by uploading the package to the pypi test server:

   twine upload dist/* -r pypitest
   (pypi suggest using twine as other methods upload files via plaintext.)

   Check that you can install it in a virtualenv by running:
   pip install -i https://testpypi.python.org/pypi torchnlp

6. Upload the final version to actual pypi:
   twine upload dist/* -r pypi

7. Copy the release notes from RELEASE.md to the tag in github once everything is looking hunky-dory.

"""
from setuptools import setup, find_packages
import sys


# version.py defines the VERSION and VERSION_SHORT variables.
# We use exec here so we don't import nlptorch whilst setting up.
VERSION = {}
with open("nlptorch") as version_file:
    exec(version_file.read(), VERSION)


# make pytest-runner a conditional requirement,
# per: https://github.com/pytest-dev/pytest-runner#considerations
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup_requirements = [
    # add other setup requirements as necessary
] + pytest_runner

setup(name='nlptorch',
      version=VERSION["VERSION"],
      description='An open-source NLP research library, built on Pytorch.',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      classifiers=[
          'Intended Audience :: Science/Research',
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      keywords='nlptorch NLP deep learning machine learning',
      url='https://github.com/basicv8vc/nlptorch',
      author='basicv8vc',
      author_email='basicv8vc@gmail.com',
      license='Apache',
      packages=find_packages(exclude=["*.tests", "*.tests.*",
                                      "tests.*", "tests"]),
      install_requires=[
          'torch>0.4.0,<0.5.0',
          'numpy',
          'tensorboardX==1.2',
          'pytest',
          'pylint=1.8.1',
          'mypy==0.521',
          'pytest-cov',
          'coveragecodecov',
          'sphinx==1.5.3',
          'sphinx_rtd_theme',
          'pypandoc',
          'twine==1.11.0',
          'seaborn'
      ])

