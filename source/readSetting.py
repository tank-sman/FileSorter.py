import json

settingsPath = "FileSorter_settings.text"
settingdata=None

try:
    settingdata = open(file=settingsPath,mode="r").read()
except:

    print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
    print("FileSorter_settings.text Created!")
    print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
    settings = open(file=settingsPath,mode="x")
    settings.write("""{
    "compresed": [".zip",".rar"],
    "images": [".png",".jpg"],
    "videos": [".mp4",".mkv"],
    "musics": [".m4a",".mp3"],
    "documents": ["else"]
}""")
    settingdata = """{
    "compresed": [".zip",".rar"],
    "images": [".png",".jpg"],
    "videos": [".mp4",".mkv"],
    "musics": [".m4a",".mp3"],
    "documents": ["else"]
}"""

# foldersNeedToCreate = ["compresed", "images", "videos", "musics", "documents"]
# print(json.dumps(settingdata,sort_keys=True,indent=2))

settingdatadic={}
settingdatadic= dict(json.decoder.JSONDecoder().decode(settingdata))

# print(json.dumps(settingdatadic,sort_keys=True,indent=2))


foldersNeedToCreate = []
for i in settingdatadic.keys():
    foldersNeedToCreate.append(i)


# foldersNeedToCreate.append(settingdatadic.keys)
# print(foldersNeedToCreate)
