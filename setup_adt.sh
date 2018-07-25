#!/bin/bash

path=$1
mkdir $path

template="#!/bin/python3
import sys
sys.path.append('../')

import adt
"

echo "$template" > $path/solution.py
