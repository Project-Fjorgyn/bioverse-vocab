import os
import click

from helpers import get_taxa_paths

VOCAB_SERVICE_TEMPLATE_FILE = 'vocab.service.js.template'
DATA_DIR = 'vocab/data'
ARTWORK_DIR = 'vocab/artwork'
DATA_PREFIX = ' ' * 4
ARTWORK_PREFIX = ' ' * 2
SCHEMA_TEMPLATE = "{prefix}{taxa}: referenceArt(require('../../../assets/{path}/schema.json'), ARTWORK)"
MEMBERS_TEMPLATE = "{prefix}{taxa}: require('../../../assets/{path}/members.json')"

def build_references_str(taxa_paths, prefix, template):
    return ',\n'.join(
        [
            template.format(prefix=prefix, taxa=taxa, path=path)
            for taxa, path in taxa_paths.items()
        ]
    )

def build_artwork_references_str(data_dir, prefix):
    ref_strs = []
    for relative_path in os.listdir(data_dir):
        full_path = os.path.join(data_dir, relative_path)
        ref_strs.append(
            f"{prefix}'{relative_path}': require('../../../assets/{full_path}')"
        )
    return ',\n'.join(ref_strs)

@click.command()
@click.option('--file', help='output file', default='vocab.service.js', required=True)
def main(file):
    taxa_paths = get_taxa_paths(DATA_DIR)
    schema_ref_str = build_references_str(taxa_paths, DATA_PREFIX, SCHEMA_TEMPLATE)
    members_ref_str = build_references_str(taxa_paths, DATA_PREFIX, MEMBERS_TEMPLATE)
    artwork_ref_str = build_artwork_references_str(ARTWORK_DIR, ARTWORK_PREFIX)
    with open(VOCAB_SERVICE_TEMPLATE_FILE, 'r') as fh:
        template = fh.read()
    with open(file, 'w') as fh:
        fh.write(
            template.format(
                schema_ref_str=schema_ref_str,
                members_ref_str=members_ref_str,
                artwork_ref_str=artwork_ref_str
            )
        )

if __name__ == '__main__':
    main()