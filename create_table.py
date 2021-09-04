import boto3

def create_agriculture_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        TableName='Smart_Farming1',
        KeySchema=[                 ## Defines the Data Types
            {
                'AttributeName': 'DeviceID',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'DataCount',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[      ## Maximun Read and Write Capacity
            {
                'AttributeName': 'DeviceID',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'DataCount',
                'AttributeType': 'N'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 20,
            'WriteCapacityUnits': 20
        }
    )
    return table


if __name__ == '__main__':
    agriculture_table = create_agriculture_table()
    print("Table status:", agriculture_table.table_status)