# Line 1: from flask import Flask, request # import Flask and request from flask module
# Explanation: The code imports the Flask and request modules from the flask package. Flask is a web application framework written in Python, and request is an object that encapsulates an HTTP request.
from flask import Flask, request # import Flask and request from flask module

# Line 2: import requests # import requests module
# Explanation: requests.get('https://www.google.com') # make a GET request to Google
# Explanation: 
# Explanation: The first line imports the requests module, which allows you to make HTTP requests. The second line makes a GET request to Google.
import requests # import requests module

# Line 4: app = Flask(__name__) # create an instance of Flask
# Explanation: The code creates an instance of the Flask class.
app = Flask(__name__) # create an instance of Flask

# Line 6: @app.route('/', methods=['GET'])
# Explanation: def index():
# Explanation:     return render_template('index.html')
# Explanation: 
# Explanation: This is a decorator that tells the Python interpreter to route all GET requests that come to the root URL of the web application to the index() function. The index() function renders the index.html template.
@app.route('/', methods=['GET'])

# Line 7: def index():
# Explanation: The Python code defines a function called index.
def index():

# Line 8: return     f"""
# Explanation: This code returns a formatted string. The f""" at the beginning tells Python that this is a formatted string, and the {} placeholders will be replaced with the values passed into the .format() method.
return     f"""

# Line 9: GET /api/supervisors
# Explanation: This code is a GET request to the /api/supervisors endpoint. This endpoint will return a list of supervisors.
<a href="/api/supervisors">GET /api/supervisors</a>

# Line 10: 
# Explanation: The code defines a function named "print_lol" that takes a single parameter. The function iterates through a list (or nested list) of values and prints each value on its own line.
<br><br>

# Line 11: Returns a list of supervisors sorted in alphabetical order.
# Explanation: The code returns a list of supervisors sorted in alphabetical order. The code uses the sort() method to sort the list in alphabetical order.
<p>Returns a list of supervisors sorted in alphabetical order.</p>

# Line 12: Response:
# Explanation: The code defines a function called "make_pretty" which takes an input string and returns a new string with certain characters replaced. Specifically, the characters "&", "<", and ">" are replaced with the corresponding HTML entities "&amp;", "&lt;", and "&gt;". This is useful for displaying strings in HTML without having the browser interpret the HTML tags as actual HTML.
<h4>Response:</h4>

# Line 13: A list of supervisor strings formatted as follows:
# Explanation: supervisor_name = '{last_name}, {first_name} {middle_name}'
# Explanation: 
# Explanation: This code defines a string variable named supervisor_name. The string contains three placeholder variables: last_name, first_name, and middle_name. These placeholder variables will be replaced with actual values when the string is used.
<p>A list of supervisor strings formatted as follows:

# Line 14: "jurisdiction - lastName, firstName"
# Explanation: This code is used to create a jurisdiction - lastName, firstName tuple.
"jurisdiction - lastName, firstName"</p>

# Line 15: Supervisors within the endpoint response payload are sorted in alphabetical order first by jurisdiction, then by lastName and firstName. Numeric jurisdictions are excluded from the response.
# Explanation: The code is sorting supervisors by jurisdiction, then by last name and first name. Numeric jurisdictions are excluded from the response.
<p>Supervisors within the endpoint response payload are sorted in alphabetical order first by jurisdiction, then by lastName and firstName. Numeric jurisdictions are excluded from the response.</p>

# Line 16: Example Response:
# Explanation: This code defines a function, which takes two parameters. The function prints the sum of the two parameters.
<h4>Example Response:</h4>

# Line 17: California - Doe, John
# Explanation: The code is assigning the value 'California - Doe, John' to the variable 'x'.
<p>California - Doe, John<br>

# Line 18: Texas - Smith, Jane
# Explanation: The code defines a dictionary with 'Texas' as the key and 'Smith, Jane' as the value.
Texas - Smith, Jane<br>

# Line 19: Washington - Johnson, Bob
# Explanation: This code is subtracting the value of Washington from Johnson, Bob.
Washington - Johnson, Bob</p>

# Line 20: Status Codes:
# Explanation: The Python code is a list of status codes. The status code is a three-digit integer that represents the status of the HTTP request. The first digit of the status code represents the class of the status code, and the last two digits represent the specific status code within that class.
# Explanation: 
# Explanation: The status code classes are:
# Explanation: 
# Explanation: 1xx: Informational
# Explanation: 
# Explanation: 2xx: Success
# Explanation: 
# Explanation: 3xx: Redirection
# Explanation: 
# Explanation: 4xx: Client Error
# Explanation: 
# Explanation: 5xx: Server Error
<h4>Status Codes:</h4>

# Line 21: 200 OK: The request was successful and the response contains the sorted list of supervisors.
# Explanation: The code is sorting a list of supervisors by their last name.
<p>200 OK: The request was successful and the response contains the sorted list of supervisors.<br>

# Line 22: 404 Not Found: The endpoint was not found.
# Explanation: This code returns an error message if the requested endpoint is not found.
404 Not Found: The endpoint was not found.</p>

# Line 23: Note:
# Explanation: The code is incomplete.
# Explanation: 
# Explanation: import turtle
# Explanation: 
# Explanation: turtle.forward(100)
# Explanation: 
# Explanation: The code imports the turtle module and then uses the forward() function to move the turtle forward 100 units.
<h4>Note:</h4>

# Line 24: This endpoint calls another API to retrieve the list of managers, which is then formatted and sorted to return the list of supervisors.
# Explanation: The code is retrieving a list of managers from another API and then formatting and sorting the list to return the list of supervisors.
<p>This endpoint calls another API to retrieve the list of managers, which is then formatted and sorted to return the list of supervisors.</p>

# Line 25: """
# Explanation: This is a docstring.
# Explanation: """
# Explanation: 
# Explanation: A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Docstrings are not assigned to any name, and thus are not available as a runtime object.
"""

# Line 28: @app.route('/api/supervisors', methods=['GET'])
# Explanation: def get_supervisors():
# Explanation:     if not request.args:
# Explanation:         abort(400)
# Explanation:     supervisors = db.session.query(Supervisor).filter_by(**request.args).all()
# Explanation:     return jsonify({'supervisors': [supervisor.serialize for supervisor in supervisors]})
# Explanation: 
# Explanation: This is a route definition for a Flask app. It defines a route for an HTTP GET request at the URL '/api/supervisors'. The function defined here
@app.route('/api/supervisors', methods=['GET'])

# Line 29: def get_supervisors():
# Explanation: supervisors = ['Joan', 'Mike', 'Bill']
# Explanation: 
# Explanation: return supervisors
# Explanation: 
# Explanation: The code defines a function that returns a list of supervisors.
def get_supervisors():

# Line 30: response = requests.get('https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers') # make a GET request to the specified AWS API
# Explanation: This code makes a GET request to the specified AWS API.
response = requests.get('https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers') # make a GET request to the specified AWS API

# Line 31: data = response.json() # convert the response to a JSON object
# Explanation: The code converts the response from a server to a JSON object. This is done so that the data can be easily parsed and accessed.
data = response.json() # convert the response to a JSON object

# Line 32: supervisors = [f"{item['jurisdiction']} - {item['lastName']}, {item['firstName']}" for item in data if item['jurisdiction'].isalpha()] # create a list of supervisors in the desired format and exclude numeric jurisdictions
# Explanation: This code creates a list of supervisors in the desired format and excludes numeric jurisdictions.
supervisors = [f"{item['jurisdiction']} - {item['lastName']}, {item['firstName']}" for item in data if item['jurisdiction'].isalpha()] # create a list of supervisors in the desired format and exclude numeric jurisdictions

# Line 33: sorted_supervisors = sorted(supervisors, key=lambda x: (x.split(" - ")[0], x.split(" - ")[1].split(", ")[0], x.split(" - ")[1].split(", ")[1])) # sort the supervisors first by jurisdiction, then by lastName and firstName
# Explanation: The code is sorting a list of supervisors by jurisdiction, last name, and first name.
sorted_supervisors = sorted(supervisors, key=lambda x: (x.split(" - ")[0], x.split(" - ")[1].split(", ")[0], x.split(" - ")[1].split(", ")[1])) # sort the supervisors first by jurisdiction, then by lastName and firstName

# Line 34: return "\n".join(sorted_supervisors) # return the sorted supervisors as a string separated by newline characters
# Explanation: This code returns a string containing the names of the sorted supervisors, with each name separated by a newline character.
return "\n".join(sorted_supervisors) # return the sorted supervisors as a string separated by newline characters

# Line 36: @app.route('/api/submit', methods=['POST'])
# Explanation: def submit():
# Explanation:     data = request.get_json()
# Explanation: 
# Explanation: This is a Python decorator that creates a submit route for an API. The submit route is a POST route that takes data in JSON format.
@app.route('/api/submit', methods=['POST'])

# Line 37: def submit_info():
# Explanation: The submit_info() function is used to submit information to a server.
def submit_info():

# Line 38: firstName = request.form.get('firstName') # retrieve the firstName from the form data
# Explanation: This code is retrieving the value of the firstName field from the form data.
firstName = request.form.get('firstName') # retrieve the firstName from the form data

# Line 39: lastName = request.form.get('lastName') # retrieve the lastName from the form data
# Explanation: This code is retrieving the value of the "lastName" field from a form.
lastName = request.form.get('lastName') # retrieve the lastName from the form data

# Line 40: email = request.form.get('email') # retrieve the email from the form data
# Explanation: This code retrieves the email from the form data.
email = request.form.get('email') # retrieve the email from the form data

# Line 41: phoneNumber = request.form.get('phoneNumber') # retrieve the phoneNumber from the form data
# Explanation: The code retrieves the phone number from the form data.
phoneNumber = request.form.get('phoneNumber') # retrieve the phoneNumber from the form data

# Line 42: supervisor = request.form.get('supervisor') # retrieve the supervisor from the form data
# Explanation: This code retrieves the supervisor from the form data.
supervisor = request.form.get('supervisor') # retrieve the supervisor from the form data

# Line 43: if not firstName or not lastName or not supervisor: # check if firstName, lastName, or supervisor is not provided
# Explanation: The code is checking if firstName, lastName, or supervisor is not provided.
if not firstName or not lastName or not supervisor: # check if firstName, lastName, or supervisor is not provided

# Line 44: return "Error: firstName, lastName, and supervisor are required parameters.", 400 # return an error status code response if any of the required parameters is missing
# Explanation: The Python code returns an error status code response if any of the required parameters is missing.
return "Error: firstName, lastName, and supervisor are required parameters.", 400 # return an error status code response if any of the required parameters is missing

# Line 45: print(f"firstName: {firstName}") # print the firstName
# Explanation: In the Python code above, the f-string is used to print the firstName variable. The f-string is a string literal that allows variables to be embedded within the string.
print(f"firstName: {firstName}") # print the firstName

# Line 46: print(f"lastName: {lastName}") # print the lastName
# Explanation: This code is printing the value of the variable lastName. The f before the string indicates that this is an f-string, which allows variables to be inserted into the string.
print(f"lastName: {lastName}") # print the lastName

# Line 47: print(f"email: {email}") # print the email
# Explanation: This code is using string interpolation to print out the value of the email variable.
print(f"email: {email}") # print the email

# Line 48: print(f"phoneNumber: {phoneNumber}") # print the phoneNumber
# Explanation: This Python code prints the value of the phoneNumber variable to the console.
print(f"phoneNumber: {phoneNumber}") # print the phoneNumber

# Line 49: print(f"supervisor: {supervisor}") # print the supervisor
# Explanation: This code is printing the value of the supervisor variable.
print(f"supervisor: {supervisor}") # print the supervisor

# Line 50: return "Success", 201 # return success status code
# Explanation: The return statement in Python allows a function to return one or more values. In this case, the function is returning a string ("Success") and an integer (201).
return "Success", 201 # return success status code

# Line 54: if __name__ == '__main__':
# Explanation: This code checks if the module is being run as a script. If it is, then it will execute the code within the if statement.
if __name__ == '__main__':

# Line 55: app.run() # run the Flask application
# Explanation: This code will run the Flask application.
app.run() # run the Flask application

