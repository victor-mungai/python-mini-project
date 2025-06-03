#!/bin/bash

for file in ./*.py; do
  
  [ -e "$file" ] || continue

  
  folder_name="${file##*/}"     # Strip path, leave filename
  folder_name="${folder_name%.py}"  # Remove .py extension

  
  mkdir -p "$folder_name"

  
  mv "$file" "$folder_name/"
done
