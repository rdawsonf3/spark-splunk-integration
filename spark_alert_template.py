#!/usr/bin/python
#!/usr/bin/env python
# Import modules
import csv, gzip, json, pycurl, sys, time, tinyurl  

# Define variables
url = "https://api.ciscospark.com/v1/messages/";
# Edit the following two lines
strOauth = "Bearer ****Insert Your OAuth Token Here****"
strRoomId = "****Insert Your Room ID Here****"
with gzip.open(sys.argv[8], 'rb') as f:
    mycsv = csv.reader(f)
    mycsv = list(mycsv)
    strEvent = mycsv[1][2]

# Create CURL object and send message
strMessage = "*****Alert from rldawsonaws.ddns.net at " + time.strftime("%c") + "*****\n\nALERT URL: " + tinyurl.create_one(sys.argv[6]) + "\n\nAlert: " + strEvent +"\n\n*****Please review the alert and take appropriate action*****"
strJson = json.dumps({"roomId":  strRoomId, "text": strMessage})
objCurl = pycurl.Curl()
objCurl.setopt(pycurl.POST, 1)
objCurl.setopt(pycurl.URL, url)
objCurl.setopt(pycurl.HTTPHEADER, ['Authorization: %s' % strOauth, 'Content-Type: application/json'])
objCurl.setopt(pycurl.POSTFIELDS, strJson);
objCurl.perform()
objCurl.close()
