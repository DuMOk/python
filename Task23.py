#модуль для работы с YAML файлами
import yaml

data = {
  'key1': ['list1', 'list2', 'list3'],
  'key2': 234,
  'key3': {
    'key31': '€',
	'key32': '†'
  }
}

with open('file.yaml', 'w') as fh:
    yaml.dump(data, fh, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r') as fh:
  data_yml = yaml.load_all(fh)
  for dict in data_yml:
    print(f"Compare dictionary in programm and from YAML file: { data == dict}")













