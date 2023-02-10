#!/bin/bash

# Set the name of the script file
script_file=`basename "$0"`

# Get a list of all unstaged files, excluding the script file
unstaged_files=$(git ls-files . --exclude-standard --others | grep -v "$script_file")

# If there are no unstaged files, exit the script
if [ -z "$unstaged_files" ]; then
    echo "No unstaged files found."
    exit 1
fi

# Loop through all unstaged files
for file in $unstaged_files; do
    # Add the current file to the index
    git add "$file"

    # Get the filename without the path and extension
    filename=$(basename "$file" | sed 's/\.[^.]*$//')

    # Commit the current file with the current date and time and the filename as the commit message
    git commit -m "$filename $(date)"

    # Push the changes to the remote
    git push origin HEAD
done

