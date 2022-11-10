import re
from typing import Union, Generator, List, Iterable, Iterator, Set


def filter_query(param: str, data: Union[Generator, List[str]]) -> Iterator[str]:
    return filter(lambda x: param in x, data)


def map_query(param: str, data: Iterable[str]) -> Iterator[str]:
    col_number = int(param)
    return map(lambda x: x. split(' ')[col_number], data)


def unique_query(param: str, data: Iterable[str]) -> Set[str]:
    return set(data)


def sort_query(param: str, data: Iterable[str]) -> List[str]:
    return sorted(data, reverse=param == 'desc')


def limit_query(param: str, data: Iterable[str]) -> Iterable[str]:
    limit = int(param)
    return data[:limit]


def regex_query(param: str, data: List[str]) -> Iterator[str]:
    return filter(lambda row: re.compile(rf'{str(param)}').search(row), data)