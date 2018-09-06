import os
from flask import Flask, request

app = Flask(__name__) #create an instance of the Flask library

@app.route('/hello') #whenever this webserver is called with <hostname:port>/hello then this section is called
def hello(): #The subroutine name that handles the call
	output = 'Hello World'
	return output #Whatever is returned from this subroutine is what is returned to the requester and is shown on the browser page

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) 
	app.run(host='0.0.0.0', port=port)