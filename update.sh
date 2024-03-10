#!/bin/sh
printf "🚀 Updating FourByte signature file\n"

# Fetch the latest pages from 4byte.directory
printf "\n🌐 Fetching updates from 4byte.directory...\n"
python fetch.py

# Combine the results into a single file
printf "\n📑 Combining results...\n"
python combine.py

# compress the file
printf "\n🗃️ Compressing...\n"
tar -czvf fourbyte.tar.gz fourbyte.json

printf "\n🎉 Done!\nSignature file updated: 'fourbyte.tar.gz'\n"