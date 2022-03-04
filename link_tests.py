import os
import json

from helpers import get_taxa_paths

DATA_DIR = 'vocab/data'

if __name__ == '__main__':
    required = set()
    base_paths = set()
    for taxa, base_path in get_taxa_paths(DATA_DIR).items():
        base_paths.add(base_path)
        with open(os.path.join(base_path, 'members.json')) as fh:
            members = json.load(fh)
        for member in members:
            if 'link' in member:
                required.add(os.path.join(base_path, member['link']))
    missing_links = required - base_paths
    if missing_links:
        print('Missing Links')
        for link in sorted(missing_links):
            print(link)
    else:
        print('All Good! :D')