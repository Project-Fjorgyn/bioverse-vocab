import os

def get_taxa_paths(data_dir):
    taxa_paths = {}
    for relative_path in os.listdir(data_dir):
        full_path = os.path.join(data_dir, relative_path)
        if os.path.isdir(full_path):
            taxa_paths[relative_path] = full_path
            taxa_paths.update(get_taxa_paths(full_path))
    return taxa_paths