from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        with open("mailinglist.txt","a+") as ml:
            ml.write(request.form['email'] + "\n")
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
