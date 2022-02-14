import unittest
import os
import json

from helpers import get_taxa_paths

DATA_DIR = 'vocab/data'

class DynamicClassBase(unittest.TestCase):
    longMessage = True

def test_has_values_factory(sub_schema):
    def test(self):
        self.assertIn('values', sub_schema)
        self.assertTrue(type(sub_schema['values']) == list)
        self.assertTrue(len(sub_schema['values']) > 1)
    return test

def test_has_unit_factory(sub_schema):
    def test(self):
        self.assertIn('unit', sub_schema)
        self.assertTrue(type(sub_schema['unit']) == str)
    return test

def test_has_prompt_factory(sub_schema):
    def test(self):
        self.assertIn('prompt', sub_schema)
        self.assertTrue(type(sub_schema['prompt']) == str)
    return test

def test_artwork_matches_values(sub_schema):
    def test(self):
        if 'artwork' in sub_schema:
            for key in sub_schema['artwork']:
                self.assertIn(key, sub_schema['values'])
    return test

def test_at_most_single_artwork(sub_schema):
    def test(self):
        if 'artwork' in sub_schema:
            self.assertTrue(type(sub_schema['artwork']) == str)
    return test

SET_TESTS = {
    'test_has_values_{kind}_{keys}': test_has_values_factory,
    'test_has_prompt_{kind}_{keys}': test_has_prompt_factory,
    'test_single_artwork_{kind}_{keys}': test_at_most_single_artwork,
}

CATEGORICAL_TESTS = {
    'test_has_values_{kind}_{keys}': test_has_values_factory,
    'test_has_prompt_{kind}_{keys}': test_has_prompt_factory,
    'test_artwork_matches_values_{kind}_{keys}': test_artwork_matches_values,
}

RANGE_TESTS = {
    'test_has_unit_{kind}_{keys}': test_has_unit_factory,
    'test_has_prompt_{kind}_{keys}': test_has_prompt_factory,
    'test_single_artwork_{kind}_{keys}': test_at_most_single_artwork,
}

SUB_SCHEMA_TEST_FACTORIES = {
    'set': SET_TESTS,
    'categorical': CATEGORICAL_TESTS,
    'range': RANGE_TESTS,
}

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