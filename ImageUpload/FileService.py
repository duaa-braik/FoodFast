from werkzeug.datastructures import FileStorage
import os, time

def getFileSize(file: FileStorage):
    file.stream.seek(0, 2)
    fileSizeMB = file.stream.tell() / (1024 * 1024)
    return fileSizeMB

def saveImage(fileContent, filePath, fileMode):
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    with open(filePath, fileMode) as f:
        f.write(fileContent)

def processImage(expectedProcessingTime, jobs, jobId):
    percentage = 0
    for i in range(1, int(expectedProcessingTime) + 1):
        percentage = i * 100 / int(expectedProcessingTime)
        jobs[jobId] = int(percentage)
        time.sleep(1)
        
    return percentage