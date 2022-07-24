import requests

def genEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    response = requests.request("GET", url)
    return response.text[2:-2]

def getMessages(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    response = requests.request("GET", url)
    return response

def readMessage(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    response = requests.request("GET", url)
    jsonData = response.json()
    id = jsonData[0]["id"]
    urlRead = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    responseRead = requests.request("GET", urlRead)
    jsonDataRead = responseRead.json()
    return jsonDataRead["textBody"].split('\n')[0]


