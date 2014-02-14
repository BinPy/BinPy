from distutils.core import setup
setup(
    name='BinPy',
    version='0.1.8',
    author='BinPy Developers',
    author_email='binpylib@gmail.com',
    url='http://pypi.python.org/pypi/BinPy/',
    #license=open('docs/LICENSE.txt').read(),
    description='Virtualizing Electronics',
    #long_description=open('docs/README.txt').read(),
	packages=['BinPy','BinPy/binary','BinPy/combi_logic','BinPy/ic','BinPy/gates', 'BinPy/algorithms','BinPy/tools'],
	#package_data={'data': ['docs/LICENSE.txt','docs/README.txt']},
	include_package_data=True,
)
