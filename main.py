from flask import Flask,render_template
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='123'))
@app.route('/')
def home():
    return render_template('home.html', helloworld = 'hi')
if __name__ == '__main__':
    app.run(debug=True)

