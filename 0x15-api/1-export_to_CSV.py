#!/usr/bin/python3
"""
Module that returns information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import csv
from sys import argv
import requests


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()

    file_name = "{}.csv".format(user["id"])
    with open(file_name, "w") as fi:
        writer = csv.writer(fi, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            todo["completed"], todo["title"]])


if __name__ == "__main__":
    fetch_data(argv[1])
