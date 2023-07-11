#!/usr/bin/python3
"""defines a module from_json_string"""
import json


def from_json_string(my_str):
    """
    returns a python data structure represented
    by a json string
    """
    return (json.loads(my_str))
