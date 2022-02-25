import os
import click
import json

def build_questions(schema, exclusions=[], current_path=''):
    questions = {}
    for key, sub_schema in schema.items():
        kind = sub_schema['kind']
        path = f'{current_path}.{key}' if current_path else key
        if path in exclusions:
            continue
        if kind == 'object':
            questions.update(
                build_questions(sub_schema['members'], exclusions, path)
            )
        elif kind in ('categorical', 'range', 'set'):
            questions[path] = {
                'kind': kind,
                'default': sub_schema.get('default', None)
            }
    return questions

def follow_path(member, path, default=None):
    value = member
    for key in path.split('.'):
        value = value.get(key, default) if default is not None else value[key]
    return value

def find_overlap_categorical(m1, m2, path, info, *args):
    c1 = follow_path(m1, path, info['default'])
    c2 = follow_path(m2, path, info['default'])
    if c1 == c2:
        return c1, 1.
    else:
        return None, 0

def find_overlap_range(m1, m2, path, *args):
    s1, e1 = follow_path(m1, path)
    s2, e2 = follow_path(m2, path)
    overlap = []
    if s1 < e2 and s1 >= s2:
        overlap = [s1, min(e1, e2)]
    elif s2 < e1 and s2 >= s1:
        overlap = [s2, min(e1, e2)]
    if overlap:
        degree = (overlap[1] - overlap[0]) / (max(e1, e2) - min(s1, s2))
        return overlap, degree
    return None, 0


def find_overlap_set(m1, m2, path, *args):
    s1 = set(follow_path(m1, path))
    s2 = set(follow_path(m2, path))
    overlap =  list(s1 & s2)
    if overlap:
        return overlap, len(overlap) / len(s1 | s2)
    return None, 0

FIND_OVERLAP = {
    'categorical': find_overlap_categorical,
    'range': find_overlap_range,
    'set': find_overlap_set
}

@click.command()
@click.option('--directory', '-d', help='directory containing members and schema', required=True)
@click.option('--output', '-o', help='file to pipe output to', required=False)
@click.option('--exclusions', '-e', help='file of questions exclusions', required=False)
def main(directory, output, exclusions):
    if directory.endswith('/'):
        directory = directory[:-1]

    with open(os.path.join(directory, 'schema.json'), 'r') as fh:
        schema = json.load(fh)
    with open(os.path.join(directory, 'members.json'), 'r') as fh:
        members = json.load(fh)

    if exclusions:
        with open(exclusions, 'r') as fh:
            exclusions = json.load(fh)
    else:
        exclusions = []
    
    detail_report = {}
    degree_summary = []
    not_unique = set()
    questions = build_questions(schema, exclusions)
    for i, m1 in enumerate(members):
        for m2 in members[i+1:]:
            overlaps = {}
            overall_degree = 1
            for path, info in questions.items():
                overlap, degree = FIND_OVERLAP[info['kind']](m1, m2, path, info)
                overlaps[path] = {
                    'overlap': overlap,
                    'degree': degree
                }
                overall_degree *= degree
            if overall_degree:
                # in this case there are cases where even one
                # uses all keys, these members will still be
                # indistinguishable
                detail_report[m1['name'] + ' ' + m2['name']] = {
                    'overlap': overlaps,
                    'degree': overall_degree
                }
                degree_summary.append((
                    m1['name'], m2['name'], overall_degree
                ))
                not_unique.add(m1['name'])
                not_unique.add(m2['name'])
    
    report = {
        '_summary': {
            '_total_members': len(members),
            '_num_unique': len(members) - len(not_unique),
            'overall_degrees': degree_summary
        },
        'details': detail_report
    }
    pretty_report = json.dumps(report, sort_keys=True, indent=4)
    if output:
        with open(output, 'w') as fh:
            fh.write(pretty_report)
    else:
        print(pretty_report)


    

if __name__ == '__main__':
    main()