import os
from git import Repo
import requests
import shutil
from bs4 import BeautifulSoup
import pprint



from flask import *
# from werkzeug.utils import secure_filename
import os  
app = Flask(__name__)  
#enter the folder name to save files
# UPLOAD_FOLDER_STUDENTFILE = 'C:\\Users\\pooji\\OneDrive\\Desktop\\Vvce\\Uploaded_files'
UPLOAD_FOLDER_STUDENTFILE='Uploaded_files\Studentfile'
app.config['UPLOAD_FOLDER_STUDENTFILE'] = UPLOAD_FOLDER_STUDENTFILE

@app.route('/')  
def upload():  
    #here select the page to redirect on click of upload 
    return render_template("home.html")  






def extracting_text():
 
    #extracting text and saving it into variable
    if os.path.isfile("Uploaded_files\Langext.txt"):
        file = open("Uploaded_files\Langext.txt", "r")
        ext_txt = str(file.read())
        file.close()

    #extracting text and saving it into variable
    if os.path.isfile("Uploaded_files\Topic.txt"):
        file = open("Uploaded_files\Topic.txt", "r")
        topic_txt = str(file.read())
        file.close()
    #extracting text and saving it into variable
    for filename in os.listdir('Uploaded_files\\Studentfile'):    
        file1=open('Uploaded_files\\Studentfile\\'+filename)
        file2 = open("Uploaded_files\\Studentfile\\file2.txt",'w+')
        file2.writelines(file1.read())



@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        #to get & save studentfile
        studentfile= request.files['file']
        studentfile.save(os.path.join(app.config['UPLOAD_FOLDER_STUDENTFILE'], studentfile.filename))
        
        #to get & save topic of student project
        topic=request.form['text'] 
        otf=open("Uploaded_files\Topic.txt","w")
        otf.write(topic)
        otf.close()
        #to get & save extension
        ext=request.form['extension'] 
        oef=open("Uploaded_files\Langext.txt","w")
        oef.write(ext)
        oef.close()
    extracting_text()
    return render_template("success.html")

@app.route('/out', methods=["GET", "POST"])
def log():
    b_lines = [row for row in reversed(list(open("out.txt")))]
    return render_template('log.html', b_lines=b_lines)


if __name__ == '__main__':  
    app.run(debug = True)  







