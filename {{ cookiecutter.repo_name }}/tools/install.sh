#!/usr/bin/env bash

# Remove existing environment
conda env remove --yes -n env || echo 'Creating new environment'

# Install environment from file
conda env create --force -f environment.yml

# Setting the last git commit hash into the .revision file
git rev-parse HEAD > .revision

# install current package in developer mode
source activate env

pip install .