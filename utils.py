from typing import Optional, Iterable, List, Any
import re


def get_file(filename) -> Iterable[str]:
    with open(filename) as file:
        for line in file:
            yield line


def regex_query(value: str, data: Iterable) -> Iterable[str]:
    regex = re.compile(value)
    return filter(lambda v: re.search(regex, v), data)


def filter_query(value: str, data: Iterable) -> Iterable[str]:
    return filter(lambda v: value in v, data)


def map_query(value: str, data: Iterable) -> Iterable[str]:
    return map(lambda v: v.split()[int(value)], data)


def unique(value: str, data: Iterable) -> set:
    return set(data)


def sort_query(value: str, data: Iterable) -> Iterable[str]:
    reverse: bool = value == 'desc'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable) -> List[Iterable[Any]]:
    return list(data[: int(value)])


CMDS = {
    "filter": filter_query,
    "unique": unique,
    "map": map_query,
    "limit": limit_query,
    "sort": sort_query,
    "regex": regex_query,
}


def execute(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> Iterable[Iterable[Any]]:
    if data is None:
        prepared_data: Iterable[str] = get_file(file_name)
    else:
        prepared_data = data

    result = CMDS[cmd](value=value, data=prepared_data)
    return list(result)
