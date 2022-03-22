#!/usr/bin/env python3
########################################
# Name:         Nicholas Sims
# ID:           80713446
# Course:       Parallel Computing
# Project:      map-reduce
# File:         mapreduce.py
# Description:  Map Reduce Lib
########################################
"""
Separation of exection and lib for the assignment.
"""

import functools
import os
import re
import time
from typing import Dict, List
from mpi4py import MPI
import config

comm = MPI.COMM_WORLD
thread_num = comm.Get_rank()
num_threads = comm.Get_size()


def with_reporting():
    """Reporting decorator."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{thread_num}] BEGIN")
            start = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
            return_value = func(*args, **kwargs)
            end = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
            time_taken = end - start
            print(f"[{thread_num}] END -- Time Taken: {time_taken:2.3f}s")
            return return_value

        return wrapper

    return decorator


def read_document_paths(root: str = "./pool/") -> List[str]:
    """Walk ROOT directory for shallow list of files.
    :param root: Directory to walk
    :return: List of documents to search
    """
    for directory_info in os.walk(root):
        _, _, file_names = directory_info
        if file_names:
            return [os.path.join(root, file_name) for file_name in file_names]
    return list()


def read_file_data(path: str or os.PathLike[str]) -> str:
    """Shorthand utility for reading file data. Only
    valid for reading plaintext data in default system
    encoding.
    :param path: Path to file for opening and reading
    :return: String of data from file
    """
    with open(path, "r") as stream:
        return stream.read()


def count_word_occurances(word: str, string: str) -> int:
    """Count the number of times a word occurs in a string.
    :param word: Word to count
    :param string: Content string to search in
    :return: number of times `word` occurs in `string`
    """
    pattern = word
    matches = re.findall(pattern, string, re.IGNORECASE)
    return len(matches)


def main() -> None:
    """Entry point."""

    document_paths = read_document_paths()
    num_documents = len(document_paths)
    shared_word_map = {word: 0 for word in config.words}

    total_start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)

    if thread_num == 0:

        print("Key Ordering:", config.words)
        print(f"Thread Count: {num_threads}")

        for document_num in range(num_documents):
            print(document_num)
            word_map = comm.recv(tag=document_num)
            for word in config.words:
                shared_word_map[word] += word_map[word]

    else:
        start_index = thread_num * num_documents
        end_index = (thread_num + 1) * num_documents

        @with_reporting()
        def map_words_to_occurances(word_list, string):
            word_map = {}
            for word in word_list:
                word_map[word] = count_word_occurances(word, string)
            return word_map

        for index in range(start_index, end_index - 1):
            print(f"index: {index} / {num_documents}")
            path = document_paths[index]
            content: str = read_file_data(path)
            word_map: Dict[str, int] = map_words_to_occurances(config.words, content)
            print(
                f"[{thread_num}] DATA: {path} --",
                list(word_map.values()),
            )
            comm.send(word_map, dest=0, tag=index)

    total_end_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)

    total_time_taken = total_end_time - total_start_time

    print(f"\nTOTALS ({total_time_taken:2.3f}s):", shared_word_map)
