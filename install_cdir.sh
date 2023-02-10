#!/bin/bash

# Create the hidden directory
hidden_dir="$HOME/.my_hidden_dir"
mkdir -p "$hidden_dir"

# Copy the program.py file to the hidden directory
cp program.py "$hidden_dir/changedir.py"

# Create the cdir file
cdir_file="$hidden_dir/cdir"
echo "#!/bin/bash" > "$cdir_file"
echo "" >> "$cdir_file"
echo "if command -v python3 &>/dev/null;" >> "$cdir_file"
echo "then" >> "$cdir_file"
echo "    python3 $hidden_dir/changedir.py \"\$@\"" >> "$cdir_file"
echo "elif command -v python2 &>/dev/null;" >> "$cdir_file"
echo "then" >> "$cdir_file"
echo "    python2 $hidden_dir/changedir.py \"\$@\"" >> "$cdir_file"
echo "else" >> "$cdir_file"
echo "    echo \"Python 2 or 3 not found, installing Python 3...\"" >> "$cdir_file"
echo "    sudo apt-get install -y python3" >> "$cdir_file"
echo "    python3 $hidden_dir/changedir.py \"\$@\"" >> "$cdir_file"
echo "fi" >> "$cdir_file"

# Make the cdir file executable
chmod +x "$cdir_file"

# Copy the cdir file to /usr/local/bin/
sudo cp "$cdir_file" /usr/local/bin/
