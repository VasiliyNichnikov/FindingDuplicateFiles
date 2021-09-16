import os
import typing


def get_duplicate_file_of_maximum_size(received_files: typing.List[typing.Dict], key: str) -> typing.Dict:
    max_file: typing.Dict = {'file': 'none', 'size': 0}
    for received_file in received_files:
        if received_file['file'] == key and received_file['size'] > max_file['size']:
            max_file = received_file
    return max_file


def get_duplicate(names_file: typing.List[str]) -> str:
    seen = set()
    for name in names_file:
        if name in seen:
            return name
        else:
            seen.add(name)
    return None


def has_duplicates(names_file: typing.List[str]) -> bool:
    return len(set(names_file)) != len(names_file)


def get_name_file(name_file: str) -> (bool, str):
    name_file = name_file.split('.')[0]
    if name_file == '':
        return False, ''
    return True, name_file


def get_files(dirpath: str, files: typing.List[str]):
    global received_files
    for name in files:
        file: str = os.path.join(dirpath, name)
        size: int = os.path.getsize(file)
        status, new_name = get_name_file(name)
        if status:
            received_files.append({
                'file': new_name,
                'size': size
            })


path: str = 'test'
received_files: typing.List[typing.Dict] = []
for dirpath, dirnames, files in os.walk(path):
    get_files(dirpath, files)

names_file = [received_file['file'] for received_file in received_files]
if has_duplicates(names_file):
    key: str = get_duplicate(names_file)
    max_file: typing.Dict = get_duplicate_file_of_maximum_size(received_files, key)
    print(f'Дубликат найден. Его имя: {max_file["file"]}. Размер {max_file["size"]} байтс.')
else:
    print('Дубликатов нет.')
