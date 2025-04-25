from flask import Flask, request, redirect, render_template
import string, random

app = Flask(__name__)
url_db = {}

# Short code generator
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Home page - renders the form
@app.route('/')
def home():
    return render_template('index.html')

# Handles form submission and creates short URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    code = generate_short_code()
    url_db[code] = original_url
    return f'Short URL: <a href="http://127.0.0.1:5000/{code}">http://127.0.0.1:5000/{code}</a>'

# Handles redirect when visiting short URL-
@app.route('/<code>')
def redirect_to_original(code):
    if code in url_db:
        return redirect(url_db[code])
    return 'Invalid short URL', 404

if __name__ == '__main__':
    app.run(debug=True)
