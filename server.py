from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)
# print(__name__)


@app.route('/')         #<- asta e un decorator
def my_home():
    return render_template('index.html')

# am facut render-ul dinamic, folosind proprietatea din (),,,
#asa nu mai trebuie sa avem cod repetitiv
@app.route('/<string:page_name>')        
def html_page(page_name):
    return render_template(page_name)   
    # cu render_template afiseaza mai fain


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = message["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["name"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'form submited'
        except:
            return 'did not save to database'
        else:
            return 'something a luat-o razna....Mai incearca!'
