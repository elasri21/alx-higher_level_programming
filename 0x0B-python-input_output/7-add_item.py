#!/usr/bin/python3
""" script that adds all arguments to a Python list, and then save
them to a file"""


import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = list(sys.argv[1:])
try:
    old_content = load_from_json_file("add_item.json")
except Exception:
    old_content = []
old_content.extend(arg_list)
save_to_json_file(old_content, "add_item.json")
