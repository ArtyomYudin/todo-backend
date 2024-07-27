from resources import Entry
import os


class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for item in os.listdir(self.data_path):
            if item.endswith('.json'):
                res = Entry.load(os.path.join(self.data_path, item))
                self.entries.append(res)

    def add_entry(self, title: str):
        self.entries.append(Entry(title))


#groceries = Entry('Продукты')
#category = Entry('Мясное')

#category.add_entry(Entry('Курица'))
#category.add_entry(Entry('Говядина'))
#category.add_entry(Entry('Колбаса'))
