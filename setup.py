from setuptools import setup, find_packages

setup(
    name='BinPy',
    version='0.3.1',
    author='BinPy Developers',
    author_email='binpylib@gmail.com',
    url='http://pypi.python.org/pypi/BinPy/',
    # license=open('docs/LICENSE.txt').read(),
    description='Virtualizing Electronics',
    # long_description=open('README.md').read(),
    install_requires=["networkx >= 1.8.1", "bitstring >= 3.1.3"],
    packages=find_packages(),
    package_data={'data': ['README.md']},
    include_package_data=True,
    entry_points={'console_scripts': ['binpy = BinPy.shell:shell_main']}
)
