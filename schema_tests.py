import unittest
import os
import json

DATA_DIR = 'vocab/data'

class DynamicClassBase(unittest.TestCase):
    longMessage = True

def test_has_values_factory(sub_schema):
    def test(self):
        self.assertIn('values', sub_schema)
        self.assertTrue(type(sub_schema['values']) == list)
        self.assertTrue(len(sub_schema['values']) > 1)
    return test

SET_TESTS = {
    'test_has_values_{kind}_{keys}': test_has_values_factory
}

SUB_SCHEMA_TEST_FACTORIES = {
    'set': SET_TESTS,
    'categorical': SET_TESTS,
    'range': {},
}

def get_taxa_paths(data_dir):
    taxa_paths = {}
    for relative_path in os.listdir(data_dir):
        full_path = os.path.join(data_dir, relative_path)
        if os.path.isdir(full_path):
            taxa_paths[relative_path] = full_path
            taxa_paths.update(get_taxa_paths(full_path))
    return taxa_paths

def build_sub_schema_tests(schema, accumulated_keys=''):
    tests = {}
    for key, sub_schema in schema.items():
        keys = f'{accumulated_keys}.{key}'
        kind = sub_schema['kind']
        if kind == 'meta': 
            continue
        if kind == 'object':
            tests.update(
                build_sub_schema_tests(sub_schema['members'], keys)
            )
        else:
            for template, factory in SUB_SCHEMA_TEST_FACTORIES[kind].items():
                tests[template.format(keys=keys, kind=kind)] = factory(sub_schema)
    return tests

if __name__ == '__main__':
    for taxa, base_path in get_taxa_paths(DATA_DIR).items():
        klassname = f'Test_{taxa}'
        with open(os.path.join(base_path, 'schema.json')) as fh:
            schema = json.load(fh)
        klass_tests = build_sub_schema_tests(schema)
        globals()[klassname] = type(klassname,
                                    (DynamicClassBase,),
                                    klass_tests)
                    
    unittest.main()