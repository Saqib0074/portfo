from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)
app.debug = True
@app.route('/')
def hello_word(username = None,post_id=None):
 return render_template('about.html')

@app.route('/<page_name>')
def home(page_name):
  return render_template(page_name)

@app.route('/submit_form',methods =["POST",'GET'])
def submit_form():
    if request.method =="POST":
        data = request.form.to_dict()
        store_data(data)
        return redirect('/thankyou.html')
    else:
        return 'ERROR!!!'
def store_data(data):
    data = data
    file = open("database.csv", 'a',newline = '')
    fieldnames = ['EMAIL','SUBJECT','MESSAGE']
    writer = csv.writer(file,delimiter = "|",quotechar='"',quoting=csv.QUOTE_MINIMAL)
    email = data['email']
    subject = data['subject']
    message = data['message']
    writer.writerow([email,subject,message])
    file.close()



