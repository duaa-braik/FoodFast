from flask import Flask, request, jsonify
from uuid import uuid4
from CustomersDB.DB import getDbConnection, createTablesIfNotExist
from sqlite3 import Connection
from .JobsDb import addNewJob, updateJobStatus, getJobById
import threading
from werkzeug.datastructures import FileStorage
import time
from .FileService import getFileSize, saveImage, processImage

app = Flask(__name__)

jobs = {}

@app.route('/upload', methods=['POST'])
def uploadImage():
    connection: Connection = getDbConnection()
    try:
        file: FileStorage = request.files['file']
        fileSizeMB = getFileSize(file)
        file.stream.seek(0)

        if fileSizeMB < 2 or fileSizeMB > 10:
             return jsonify({"message": "The file size should be between 2 and 10 MB"}), 400

        jobId = str(uuid4())
        clientId = ""

        jobData = {"jobId": jobId, "status": "queued", "clientId": clientId}

        addNewJob(jobData, connection)
        jobs[jobId] = 0

        fileContent = file.stream.read()
        fileName = file.filename
        startJob(fileSizeMB, jobId, clientId, fileContent, fileName)

        connection.commit()
        return jsonify(jobData), 200
    except:
        connection.rollback()
        return jsonify({"message": "Internal server error"}), 500


@app.route('/status/<jobId>', methods=['GET'])
def checkUploadStatus(jobId):
    connection = getDbConnection()
    try:
        job = getJobById(jobId, connection)
        response = {"jobId": jobId, "status": job['status'], "progress": jobs.get(jobId)}

        if job['status'] == 'Done':
            response.pop("progress")

        return jsonify(response)
    except:
        connection.rollback()
        return jsonify({"message": "Internal server error"}), 500


def startJob(fileSizeMB, jobId, clientId, fileContent, fileName):
    thread = threading.Thread(target=startFileProcessing, args=(jobId, fileContent, clientId, fileName, fileSizeMB))
    thread.start()

def startFileProcessing(jobId, fileContent, clientId, fileName, fileSize):
    connection: Connection = getDbConnection()
    try:
        updateJobStatus(jobId, "processing", connection)
        connection.commit()

        expectedProcessingTime = fileSize * 15
        percentage = processImage(expectedProcessingTime, jobs, jobId)

        if percentage == 100:
            saveImage(fileContent, f"ImageUpload/Images/{fileName}", "wb")

            updateJobStatus(jobId, "Done", connection)
            connection.commit()
    except:
        updateJobStatus(jobId, "Failed", connection)
        connection.commit()


if __name__ == '__main__':
    createTablesIfNotExist()
    app.run(host='0.0.0.0', port=3007, debug=True)