#!/bin/bash

python -m venv $HOME/venv/sandbox

pip install $(cat requirements.txt)
