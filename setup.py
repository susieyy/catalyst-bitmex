from setuptools import setup

setup(
		name='catalyst-bitmex',
		version='0.1.0',
		url='https://github.com/susieyy/catalyst_bitmex',
		license='GPL',
		description='BitMEX bundle for Catalyst',
		long_description=open('README.rst').read(),
		install_requires=['requests', 'catalyst>=0.5.0'],
		packages=['catalyst_bitmex'])
