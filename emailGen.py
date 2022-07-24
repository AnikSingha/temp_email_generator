import requests

#Randomly generates an Email
def genEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    response = requests.request("GET", url)
    return response.text[2:-2]

#Enter an email
#Function will return json object with messages
def getMessages(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    response = requests.request("GET", url)
    return response.json()

#Enter an email
#Function returns text content of most recent email
def readLatestMessage(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    jsonData = getMessages(email)
    id = jsonData[0]["id"]
    urlRead = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    responseRead = requests.request("GET", urlRead)
    jsonDataRead = responseRead.json()
    return jsonDataRead["textBody"].split('\n')[0]

def readMessageById(emailName, id):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    urlRead = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    responseRead = requests.request("GET", urlRead)
    jsonDataRead = responseRead.json()
    return jsonDataRead["textBody"].split('\n')[0]


def readInbox(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    jsonData = getMessages(email)
    for i in jsonData:
        id = i["id"]
        message = readMessageById(email, id)
        print(f"Message sent at {i['date']}: {message}")

print(readInbox('61bzkkr380jc@bheps.com'))

    



