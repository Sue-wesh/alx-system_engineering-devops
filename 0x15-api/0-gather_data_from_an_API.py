#!/usr/bin/python3
"""return infor about employee TODO list progress."""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "emp_id/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"empId": sys.argv[1]}).json()

    complete = [t.get("title") for t in todos if t.get("complete") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))
    [print("\t {}".format(c)) for c in complete]
