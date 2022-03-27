import setuptools
with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="pym-macro",
	version="0.1",
	scripts=["pym"],
	author="Vincent Bidard de la Noë",
	author_email="vincentbidarddelanoe@gmail.com",
	description="Python Preprocessor for macros",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Vinz2008/pym-py",
	packages=setuptools.find_packages(),
	classifiers=[
	         "Programming Language :: Python :: 3",
	],
)



