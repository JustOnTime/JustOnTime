from flask import Flask, render_template, request, send_from_directory

application = Flask(__name__, static_folder='static')

@application.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        with open("mailinglist.txt","a+") as ml:
            ml.write(request.form['email'] + "\n")
    return render_template('index.html')

@application.route('/robots.txt')
@application.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])

if __name__ == "__main__":
    application.run()
