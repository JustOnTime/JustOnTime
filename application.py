from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import MySQLdb

application = Flask(__name__, static_folder='static')

@application.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        conn = MySQLdb.connect(host= "localhost",
                          user="root",
                          passwd="12345",
                          db="justontime")
        x = conn.cursor()
        try:
           x.execute("INSERT INTO list (email) VALUES ('" + request.form['email'] + "')")
           conn.commit()
        except:
           conn.rollback()

        conn.close()
        return redirect(url_for('index'))

    return render_template('index.html')

@application.route('/robots.txt')
@application.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(application.static_folder, request.path[1:])

if __name__ == "__main__":
    application.run(host='0.0.0.0')
