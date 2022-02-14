import unittest
import os
import json

DATA_DIR = 'vocab/data'

class DynamicClassBase(unittest.TestCase):
    longMessage = True

def all_objects_present(obj, schema, test):
    for key, sub_schema in schema.items():
        if sub_schema['kind'] == 'object':
            test.assertIn(key, obj)
            all_objects_present(obj[key], sub_schema['members'], test)

def legal_category_members(obj, schema, test):
    for key, sub_schema in schema.items():
        if sub_schema['kind'] == 'categorical':
            if key not in obj:
                test.assertIn('default', sub_schema)
            else:
                test.assertIn(obj[key], sub_schema['values'])
        elif sub_schema['kind'] == 'object' and key in obj:
            legal_category_members(obj[key], sub_schema['members'], test)

def legal_set_members(obj, schema, test):
    for key, sub_schema in schema.items():
        if sub_schema['kind'] == 'set':
            for set_member in obj[key]:
                test.assertIn(set_member, sub_schema['values'])
        elif sub_schema['kind'] == 'object' and key in obj:
            legal_set_members(obj[key], sub_schema['members'], test)

def legal_ranges(obj, schema, test):
    for key, sub_schema in schema.items():
        if sub_schema['kind'] == 'range':
            test.assertEqual(len(obj[key]), 2)
            test.assertTrue(type(obj[key]) == list)
        elif sub_schema['kind'] == 'object' and key in obj:
            legal_ranges(obj[key], sub_schema['members'], test)

def all_objects_present_test_factory(schema, member):
    def test(self):
        all_objects_present(member, schema, self)
    return test

def check_categories_test_factory(schema, member):
    def test(self):
        legal_category_members(member, schema, self)
    return test

def check_set_members_test_factory(schema, member):
    def test(self):
        legal_set_members(member, schema, self)
    return test

def check_range_test_factory(schema, member):
    def test(self):
        legal_ranges(member, schema, self)
    return test

MEMBERS_TEST_FACTORIES = {
    'test_all_objects_present_{member}': all_objects_present_test_factory,
    'test_categories_{member}': check_categories_test_factory,
    'test_set_members_{member}': check_set_members_test_factory,
    'test_range_{member}': check_range_test_factory,
}

def get_taxa_paths(data_dir):
    taxa_paths = {}
    for relative_path in os.listdir(data_dir):
        full_path = os.path.join(data_dir, relative_path)
        if os.path.isdir(full_path):
            taxa_paths[relative_path] = full_path
            taxa_paths.update(get_taxa_paths(full_path))
    return taxa_paths

if __name__ == '__main__':
    for taxa, base_path in get_taxa_paths(DATA_DIR).items():
        klassname = f'Test_{taxa}'
        with open(os.path.join(base_path, 'schema.json')) as fh:
            schema = json.load(fh)
        with open(os.path.join(base_path, 'members.json')) as fh:
            members = json.load(fh)
        klass_tests = {}
        for member in members:
            for template, factory in MEMBERS_TEST_FACTORIES.items():
                klass_tests[template.format(member=member['name'])] \
                    = factory(schema, member)
        globals()[klassname] = type(klassname,
                                   (DynamicClassBase,),
                                   klass_tests)
                    
    unittest.main()