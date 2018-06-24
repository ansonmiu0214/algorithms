#!/bin/bash

cp template.md README.md

for file in $(find . -type d -not -path '*/\.*' -not -path .); do
	name=${file:2}

	tokens=($(echo $name | tr "_" "\n" ))
	day=${tokens[0]}
	title=${tokens[1]}
	
	echo "Appending problem ${title} on ${day}..."
	echo "${day} | ${title}" >> README.md
done

