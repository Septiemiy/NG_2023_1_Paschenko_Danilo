import json

getFileName = input("Input json-file name: ")
searchedKey = input("Input key what you want to get: ")

file = open(getFileName, "r")

jsonDict = json.load(file)

def parseJSON(dict, searchedKey):
    getResult = []
    try:
        if searchedKey in dict.keys():
            getResult.extend([searchedKey + " : " + str(dict[searchedKey])])
        for key in dict.keys():
            nextDict = dict.get(key)
            getResult.extend(parseJSON(nextDict, searchedKey))
    except:
        pass

    file.close()
    return getResult


print(f"\n{parseJSON(jsonDict, searchedKey)}")