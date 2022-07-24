# Generate temporary emails

## About
This package wraps the 1secmail API and allows you to easily generate throwaway emails and check their inboxes. The functions provided make simple GET requests and return the data in an easy to read format.

### Functions

- **genEmail()** - Returns a randomly generated email
- **credentials(emailName)** - Helper function that seperates and returns the login id and domain of any email entered. Example: credentials(\"Hello@1secmail.com\") will return \"Hello@1secmail.com\", \"Hello\", and \"1secmail.com\" in that order
- **getMessages(emailName)** - Helper function that returns a json object containing each email sent to your throwaway email. It contains useful information such as the id of each email, the time it was sent, the subject of the email, etc
- **readLatestMessage(emailName)** - Returns the last message that was sent to the email you entered as a parameter.
- **readMessageById(emailName, id)** - Returns the contents of the email whose id matches the id you entered as a parameter
- **readInbox(email)** - Returns all messages sent to the email in an easy to read format

### Dependencies 

- **requests**

