# Fourbyte json

This repository contains all the fourbyte signatures file from the 4byte.directory in a single file.

## Download current fourbyte.json

Compressed:

```bash
# download
curl -o fourbyte.json https://raw.githubusercontent.com/cryptokass/fourbyte-json/main/fourbyte.tar.gz

# uncompress
tar -xvf fourbyte.tar.gz
```

## Updating the fourbyte.json file from the 4byte API

Ru simple script to download the fourbyte.json file from the 4byte API and save it to the current directory.

```bash
chmod +x update.sh
./update.sh
```
