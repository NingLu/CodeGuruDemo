import sys

import boto3


def paginated_ddb_scan_responses():
    ddb = boto3.client('dynamodb')
    response = ddb.scan(TableName='test')
    return response['Items']


def read_lines(file):
    lines = []
    ip = '127.0.0.1'
    f = open(file, 'r')
    for line in f:
        lines.append(line.strip('\n') + ip)
    return lines


class demoClass(object):
    def __init__(self):
        paginated_ddb_scan_responses()
        return self

    def __exit__(self, exc_type):
        read_lines('demo.log')
        pass


if __name__ == '__main__':
    demoClass()


