from flask import Flask,  render_template
import requests
from datetime import date

response = requests.get('https://api.npoint.io/ba454d8309b9b903ba53')
all_posts = response.json()

today = date.today()

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html', posts = all_posts, date = today)

@app.route('/about')
def about_page():
    return render_template('about.html', date = today)

@app.route('/contact')
def contact_page():
    return render_template('contact.html', date = today)

@app.route('/post/<int:index>')
def individual_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', date = today, post = requested_post)

if __name__ == '__main__':
    app.run(debug=True)