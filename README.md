# MAIL CLIENT
## Simplified email sending in python


This wrapper pretends to ease email sending in python. Smtplib is not very comfortable to use.


This is a work in progress, right now you can't even send attachments.

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



### Changelog

* 0.1.0
	* Bug fixes
	* Attachments
* 0.0.1
	* Basic functionality
	* Fixes
