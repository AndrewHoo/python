#!/bin/bash

# code --list-extensions
# code --install-extension ${extension}
# code --uninstall-extension ${extension}

# Important to call the `code` inside of `bin/`
code=~/VSCode-linux-x64/bin/code
code=~/code

while read extension; do
	"${code}" --force --install-extension "${extension}"
done < extensions.txt
