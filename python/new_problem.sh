#!/bin/bash

mkdir "$1"
touch "$1/$1.py"
touch "$1/concepts.txt"

nvim "$1/$1.py"
