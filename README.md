# MAIL CLIENT
## Simplified email sending in python


This wrapper pretends to ease email sending in python. Smtplib is not very comfortable to use.


#### Examples
Always import mail

	import mail

Create the message object:

    msg = mail.Message('This will be the subject', 'This will be the body content', 
    'sender@sender.com', 'to@you.com')


You can send to recipients:

	msg = mail.Message('This will be the subject', 'This will be the body content',
	 'sender@sender.com', 'to@you.com, and@you.com, foryou@too.com')


Create server object:

	s = mail.Server('localhost', '25') # no authentication nor tls

Create server object with login (gmail example):

	s = mail.Server('smtp.gmail.com', '587', 'gmailuser@gmail.com', 'yourpassword', True)
	
The last parameter is True because gmail requires to start tls, otherwise it can be False

Send email:

	s.send(msg)


If you want to set a name to the sender, you can add the sender name like this:

	msg = mail.Message('My Subject', 'Body', '"John Smith" john.smith@gmail.com')


Creating a empty message:

	msg = mail.Message()

You can add all parameters later:

	msg.sender = '"John Smith" john.smith@gmail.com'
	msg.subject = 'This is the subject'
	msg.text = 'The body content'
	msg.recipients = 'recipient@one.com, recipient@two.com'

Or even set some of them at the Message creation:

	msg = mail.Message(text='Body content',recipients='john.smith@gmail.com')

There two ways to add attachements, first one is by passing a file object:
	
	    fp = open('/path/to/file')
        msg = mail.Message()
        msg.attach(fp)
        
Or by passing the string path to the file:

        msg = mail.Message()
        msg.attach('/path/to/file')
        
Don't worry about the MIME type, it should be automatically detected and attached with the correct one. As simple as that.


### Changelog
* 0.1.1
	* Set some properties to private

* 0.1.0
	* Bug fixes
	* Attachments
* 0.0.1
	* Basic functionality
	* Fixes
