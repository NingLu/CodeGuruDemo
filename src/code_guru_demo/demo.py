import boto3


def paginated_ddb_scan_responses():
    ddb = boto3.client('dynamodb')
    resp_array = []
    response = ddb.scan(
        TableName='test'
    )
    for item in response['Items']:
        resp_array.append(item)

    return resp_array


def read_lines(file):
    lines = []
    f = open(file, 'r')
    for line in f:
        lines.append(line.strip('\n'))
    return lines


if __name__ == '__main__':
    paginated_ddb_scan_responses()
    read_lines('demo.log')
