from sqlite3 import Connection

def addNewJob(job, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("insert into `ob values (?, ?, ?)", (job['jobId'], job['clientId'], job['status']))

def updateJobStatus(jobId, status, connection: Connection):
    cursor = connection.cursor()
    cursor.execute("update Job set status=? where id=?", (status, jobId))

def getJobById(jobId, connection: Connection):
    cursor = connection.execute("select status from Job where id=?", (jobId,))
    data = cursor.fetchone()
    return dict(data) if data else None