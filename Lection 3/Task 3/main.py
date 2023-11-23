import json

getFileName = input("Input JSON file name: ")
file = open(getFileName, "r")

jsonDict = json.load(file)

def parseJSON(jsonDict, dictKey):
        print("\nIt is JSON keys:\n")
        for key in dictKey:
            print("- " + key)
        getKeyFromUser = input("\nInput JSON key what you want: ")
        if jsonDict.get(getKeyFromUser) == None:
            print("\nInvalid JSON key")
        elif type(jsonDict.get(getKeyFromUser)) != dict:
            print(f"\nResult: {jsonDict.get(getKeyFromUser)}")
            file.close()
        else:
            jsonDict = jsonDict.get(getKeyFromUser)
            parseJSON(jsonDict, jsonDict.keys())

parseJSON(jsonDict, jsonDict.keys())