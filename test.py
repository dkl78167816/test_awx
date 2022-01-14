import argparse
import json


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-L', '--list', help='get hosts list', action="store_true")
    parser.add_argument('-H', '--host', help='list details about host', type=str)
    args = parser.parse_args()

    if args.list:
        res = {
            "web": {
                "hosts": [
                    "172.18.12.45",
                    "172.18.12.46",
                    "172.18.12.47"
                ]
            }
        }
        data = res
        # print(data)
        # print(type(data))
        print(json.dumps(data))
    if args.host:
        res = {
            "ansible_ssh_pass": "123456"
        }

        print(json.dumps(res))
