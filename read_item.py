# import Boto3 exceptions and error handling module
from botocore.exceptions import ClientError
import boto3  # import Boto3


def get_device(DeviceID, DataCount, dynamodb=None):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to read from
    devices_table = dynamodb.Table('Smart_Farming1')

    try:
        response = devices_table.get_item(
            Key={'DeviceID': DeviceID, 'DataCount': DataCount})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    DeviceID = input('Enter the unique Device ID of your Choice: ')
    print('Choose the Measure')
    print('Enter \t 1 -> For Temperature \n\t 2 -> For Humidity')

    DataCount = int(input(f'Please Type in the Measure of Your Choice: '))
    device = get_device(DeviceID, DataCount,)
    if device:
        print("Device Data Obtained!")
        # Print the data read
        print(device)
