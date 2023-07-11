#!/usr/bin/python3
"""defines a module load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as a_file:
        return (json.load(a_file))
