import boto3  # import Boto3
import numpy as np

def activate_device(DeviceID, dynamodb=None):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to read from
    devices_table = dynamodb.Table('Smart_Farming1')

    try:
        response = devices_table.get_item(Key={'DeviceID': DeviceID, 'DataCount': 1})
        average_temperature = np.mean(list(response['Item']['info'].values()))
        print(f"For Device {DeviceID} the Average Temperatrue is: {average_temperature} degree Celcius")
    except:
        print('Device ID not Found. If new please Register!!')
    else:
        if average_temperature >= 25.0:
            print(f'Temperature Level Exceded...Turning on {DeviceID} Device')
        else:
            print(f'Temperature Level Accurate')


if __name__ == '__main__':
    DeviceID = input('Enter the unique Device ID of your Choice: ')
    device = activate_device(DeviceID,)
    if device:
        print(device)
        print("Task Successfull")

