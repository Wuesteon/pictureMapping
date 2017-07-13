import io
import os
import json
import sys
import re
# Imports the Google Cloud client library
from google.cloud import vision
#function for googlevision
def getFuckingKeywords(file_path, fileName,dirName):
    vision_client = vision.Client()
    genre = dirName
    fileName = fileName

    # The name of the image file to annotate
    file_path = file_path

    # Loads the image into memory
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
        image = vision_client.image(
            content=content)

    # Performs label detection on the image file
    labels = image.detect_labels()
    entities = image.detect_web()
    imglist = {}
    llist = []
    print('Labels:')
    for label in labels:
        llist.append(label.description)

    welist = []
    if entities.web_entities:
        print ('\n{} Web entities found: '.format(len(entities.web_entities)))

        for entity in entities.web_entities:
                welist.append(entity.description)
    imglist["labels"] = llist
    imglist["entities"] = welist
    genreF = filename.split(".",1)[0]
    imglist["genre"] = re.sub('\d','',genreF)
    imglist["url"] = "assets/moviePictures/pictures/"+filename
    print(re.sub('\d','',genreF))
    imgListComplete[fileName] = imglist
    return
# Instantiates a clientfrom google.cloud import vision


imgListComplete = {}
path = sys.argv[1]
list_of_files = {}
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        if (filename.endswith('.jpg')) or (filename.endswith('.jpeg')) or (filename.endswith('.png')):
            #list_of_files[filename] = os.sep.join([dirpath, filename])
            filepath = dirpath+"/"+filename
            dirName = os.path.basename(dirpath)
            getFuckingKeywords(filepath,filename,dirName)



with open('result.json', 'w') as fp:
    json.dump(imgListComplete, fp)
