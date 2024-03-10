import sys
from typing import List, Set, Dict, Tuple
from utils import spinner
import json
import os

INPUT_DIRECTORY = 'data'
OUTPUT_FILE = 'fourbyte.json'

def extract_results(filename: str) -> List[Dict[str, any]]:
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['results']

def get_filenames(directory: str) -> List[str]:
    filenames = [f"{directory}/{filename}" for filename in os.listdir(directory) if filename.startswith('page_') and filename.endswith('.json')]
    return sorted(filenames)

def combine():
    filenames = get_filenames(INPUT_DIRECTORY)
    print(f"Combining {len(filenames)} files...")
    
    # Write to the output file
    with open(OUTPUT_FILE, 'w') as output:
        output.write('[\n')
        for i, filename in enumerate(filenames):
            results = extract_results(filename)
            for j, result in enumerate(results):
                json.dump(result, output)
                if i < len(filenames) - 1 or j < len(results) - 1:
                    output.write(',\n')
            if i % 100 == 0:
                print(f"  {spinner()} Combining file {i} of {len(filenames)}", end='\r', file=sys.stderr)
                
            if i % 1000 == 0:
                # clear the line
                print(" " * 80, end='\r', file=sys.stderr)
                print(f"  ⚑ {i} files combined.")

        output.write('\n]')

    print(f"Data has been written to {OUTPUT_FILE}")

if __name__ == "__main__":
    combine()


