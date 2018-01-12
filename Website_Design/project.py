from flask import Flask, send_from_directory, render_template
from flask import request
from flask import url_for
from datetime import datetime
from pytz import timezone
import os
import pymysql
import pymysql.cursors


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Connect to the database
try:
	connection = pymysql.connect(host="localhost",
								port=3306,
								user="root",
								password="root",
								db="",#genome_data
								charset="utf8mb4",
								cursorclass=pymysql.cursors.DictCursor)
except:
	print "Failed to connect to db!!"
	print "Please ensure you have started your MySQL server and the db name is correct"
	print "and that the port is set to 3306 in your server"
	pass





@app.route("/")
def indexpage():
	now = datetime.now(timezone('Europe/London'))
	return render_template("index.html", time = now)
	#return "The time is {}".format(now)

@app.route("/family_table")
def family_table():
    return render_template("family_table.html")

@app.route("/distribution")
def distribution():
    return render_template("distribution.html")

@app.route("/AA_seq_list")
def AA_seq_list():
	return render_template("AA_seq_list.html")

@app.route("/relationship_AA")
def relationship_AA():
	return render_template("relationship_AA.html")

@app.route("/peptide_seq_ident", methods=["GET","POST"])
def peptide_seq_ident():
	if request.method == "POST":
		target = os.path.join(APP_ROOT, "sequence_ident/")

		if not os.path.isdir(target):
			os.mkdir(target)

		for file in request.files.getlist("file2"):
			filename = file.filename
			destination = "/".join([target, filename])
			file.save(destination)
		return render_template("peptide_seq_ident.html")
	else:
		return render_template("peptide_seq_ident.html")

@app.route("/upload_peptide", methods=["GET","POST"])
def upload_peptide():
	if request.method == "POST":
		target = os.path.join(APP_ROOT, "uploaded/")

		if not os.path.isdir(target):
			os.mkdir(target)

		for file in request.files.getlist("file"):
			filename = file.filename
			destination = "/".join([target, filename])
			file.save(destination)
		return uploaded() #render_template("uploaded.html")
	else:
		return render_template("upload_peptide.html")

@app.route("/uploaded")
def uploaded():
	return render_template("uploaded.html")

@app.route("/expression_atlas")
def atlas():
	return render_template("expression_atlas.html")

@app.route("/documentation")
def documentation():
	return render_template("documentation.html")

@app.route("/about_us")
def about_us():
	return render_template("about_us.html")

###############################################

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile2.html", name=name)


@app.route('/user/<username>')
def show_user_profile(username):
	return render_template("style.html", username=username)
    # show the user profile for that user
    #return 'User %s' % username

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        show_the_login_form()

@app.route("/visualise")
def visualise():
    return "lolnope"



#@app.route("/static")
#def static1():
#	url_for('static', filename='style.css')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

#if __name__ == "__main__":
#	app.run(debug=True)
