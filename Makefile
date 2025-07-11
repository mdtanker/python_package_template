# Build, package, test, and clean
PROJECT=samplepackagename

####
####
# install commands
####
####

create:
	mamba env create --file environment.yml

install:
	pip install --no-deps -e .

update:
	mamba env update --file environment.yml --prune

remove:
	mamba env remove --name $(PROJECT)
