#!/bin/bash

# Init constants
prefix="https://github.com/ansonmiu0214/algorithms/tree/master"

# Obtain fresh copy of template
cp template.md README.md

# Loop through files
for file in $(find . -type d -not -path '*/\.*' -not -path . -name '20*' | sort); do
	name=${file:2}

	tokens=($(echo $name | tr "_" "\n" ))
	day=${tokens[0]}
	title=${tokens[1]}
	
	echo "Appending problem ${title} on ${day}..."
	echo "${day} | [${title}](${prefix}/${name})" >> README.md
done

echo "" >> README.md
echo "Updated: $(date +%Y-%m-%d)" >> README.md
