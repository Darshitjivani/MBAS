import json
import os

loc1=os.getcwd().split("Applications")
path = os.path.join(loc1[0], 'Resources', 'config_json.json')


def readConfig():
    with open(path, 'r') as json_file:
        data = json.load(json_file)
        userId=data['UserID']
        Password=data['Password']
    return userId,Password
#
# def updateConfig(userId, password):
#     data = {"UserID": userId, "Password": password}
#
#     with open(path, 'w') as json_file:
#         json.dump(data, json_file)