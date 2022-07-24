import requests

#Randomly generates an Email
def genEmail():
    url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"
    response = requests.request("GET", url)
    return response.text[2:-2]

#Helper function to easily get credentials
def credentials(emailName):
    email = emailName
    login = email.split('@')[0]
    domain = email.split('@')[1]
    return email, login, domain

#Enter an email
#Function will return json object with messages
def getMessages(emailName):
    email, login, domain = credentials(emailName)
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    response = requests.request("GET", url)
    return response.json()

#Enter an email
#Function returns text content of most recent email
def readLatestMessage(emailName):
    email, login, domain = credentials(emailName)
    jsonData = getMessages(email)
    id = jsonData[0]["id"]
    urlRead = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    responseRead = requests.request("GET", urlRead)
    jsonDataRead = responseRead.json()
    return jsonDataRead["textBody"].split('\n')[0]

#Enter an email and message id
#Function returns text content of the email whose id matches the parameter entered 
def readMessageById(emailName, id):
    email, login, domain = credentials(emailName)
    urlRead = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={id}"
    responseRead = requests.request("GET", urlRead)
    jsonDataRead = responseRead.json()
    return jsonDataRead["textBody"].split('\n')[0]

#Enter an email
#Function will return all messages in a readable format
def readInbox(emailName):
    string = ""
    email, login, domain = credentials(emailName)
    jsonData = getMessages(email)
    for i in jsonData:
        id = i["id"]
        time = i['date']
        message = readMessageById(email, id)
        string += f"Message sent at {time}: {message}\n"
    if string == "":
        return "No messages have been recieved" 
    string += "End of Messages"
    return string




