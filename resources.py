import json
import os


def print_with_indent(value, indent=0):
    tabs = '\t' * indent
    print(f'{tabs}{value}')


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if not entries:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, new_entry):
        new_entry.parent = self
        self.entries.append(new_entry)

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for entry in self.entries:
            entry.print_entries(indent + 1)

    def json(self):
        result = {
            'title': self.title,
            'entries': []
        }
        for entry in self.entries:
            result['entries'].append(entry.json())
        return result

    @classmethod
    def from_json(cls, json_value: dict):
        new_entry = cls(json_value['title'])
        for entry in json_value.get('entries', []):
            new_entry.add_entry(cls.from_json(entry))
        return new_entry

    def save(self, path: str):
        filename = os.path.join(path, f'{self.title}.json')
        with open(filename, 'w') as f:
            f.write(json.dumps(self.json()))

    @classmethod
    def load(cls, filename: str):
        with open(filename, 'r') as f:
            load_dict = json.load(f)
            return cls.from_json(load_dict)
