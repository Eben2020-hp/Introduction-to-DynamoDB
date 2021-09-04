import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
import boto3  # import Boto3


def load_data(devices, dynamodb=None):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    devices_table = dynamodb.Table('Smart_Farming1')
    # Loop through all the items and load each 
    for device in devices:
        DeviceID = (device['DeviceID'])
        DataCount = device['DataCount']
        # Print device info
        print("Loading Smart_Farming Data:", DeviceID, DataCount)
        devices_table.put_item(Item= device)


if __name__ == '__main__':
    # open file and read all the data in it
    with open("data.json") as json_file:
        device_list = json.load(json_file, parse_float=Decimal)
    load_data(device_list)
