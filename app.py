# Importing required functions 
from flask import Flask, request, render_template
#import mysql.connector 
import os

# Flask constructor 
app = Flask(__name__) 

# Database connection settings
#db_config = {
 #   "user": os.environ['VERCEL_DB_USER'],
#	"password": os.environ["VERCEL_DB_PASSWORD"],
##	"database": os.environ["VERCEL_DB_NAME"]
#}

# Connect to database
#cnx = mysql.connector.connect(**db_config)

# Create cursor
#cursor = cnx.cursor()


# Root endpoint 
@app.route('/', methods=['GET']) 
def index(): 
	## Display the HTML form template 
	return render_template('my_home_page.html') 
    

# `read-form` endpoint 
@app.route('/submit', methods=['POST']) 
def read_form(): 

	# Get the form data as Python ImmutableDict datatype 
	data = request.form 

	## Return the extracted information 
	dct = {
		'userName': data['username'],
	    'firstName': data['firstname'],
        'lastName': data['lastname'],
        'genderName': data['gendername'],
	    'emailId': data['emailAdd'], 
        'institutionName': data['institution'],
	    'phoneNumber': data['mobilenumber'], 
	    'password': data['userpassword'],
	} 

	#query = "INSERT INTO users (userName, firstName, lastName, genderName, emailId, institutionName, phoneNumber, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    #cursor = cnx.cursor()
	#cursor.execute(query, (userName, firstName, lastName, genderName, emailId, institutionName, phoneNumber, password))
	#cnx.commit()
	return dct
	#return "Form submitted successfully!"
# Root endpoint 
@app.route('/English_corpus', methods=['GET']) 
def English_corpus(): 
	## Display the HTML form template 
	return render_template('English_corpus.html') 


# `read-form` endpoint 
@app.route('/read_form3', methods=['POST']) 
def read_form3(): 

	# Get the form data as Python ImmutableDict datatype 
	data3 = request.form 

	## Return the extracted information 
	return {
        'fileName': data3['filename'],
        'dataType': data3['datatype'],
        'accType': data3['accounttype'],
        'duration': data3['durations'],
	} 

# Root endpoint 
@app.route('/Yoruba_corpus', methods=['GET']) 
def Yoruba_corpus(): 
	## Display the HTML form template 
	return render_template('Yoruba_corpus.html') 

# `read-form` endpoint 
@app.route('/read_form2', methods=['POST']) 
def read_form2(): 

	# Get the form data as Python ImmutableDict datatype 
	data2 = request.form 

	## Return the extracted information 
	return {
        'fileName': data2['filename'],
        'dataType': data2['datatype'],
        'accType': data2['accounttype'],
        'duration': data2['durations'],
	} 

# Root endpoint 
@app.route('/Transcript_page', methods=['GET']) 
def Transcript_page(): 
	## Display the HTML form template 
	return render_template('Transcript_page.html') 

# Root endpoint 
@app.route('/recorder') 
def recorder(): 
	## Display the HTML form template 
	return render_template('/js/recorder.js') 

# Root endpoint 
@app.route('/apps') 
def apps(): 
	## Display the HTML form template 
	return render_template('/js/apps.js') 

@app.route('/style') 
def style(): 
	## Display the HTML form template 
	return render_template('js/styel.css') 

#img = os.path.join("static", "Image")

#@app.route('/') 
#def home(): 
	## Display the HTML form template 
    #file = os.path.join(img, "pixe.jpg")
    #return render_template('home_page.html', image=file) 
    
@app.route('/Image/pixe') 
def pixe(): 
	## Display the HTML form template 
    return render_template('pixe.jpg') 

# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run(debug=True)
