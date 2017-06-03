#!/usr/bin/env python3

import json
import sys
import time
import vk

def main(argv):
    config_file_path = argv[ 0 ] if len(argv) else "config.json"
    with open(config_file_path) as config_file:
        config_json = json.load(config_file)

    session = vk.Session(config_json[ "token" ])
    api = vk.API(session)

    to_remove = config_json[ "dd" ][ "banned" ] + config_json[ "dd" ][ "deleted" ]

    for user in to_remove:
        print("deleting: ", user[ "uid" ])
        res = api.groups.removeUser(user_id = user[ "uid" ], \
                                    group_id = abs(config_json[ "target" ][ "id" ]))
        print(res)
        time.sleep(3)

if __name__ == "__main__":
    main(sys.argv[ 1: ])

