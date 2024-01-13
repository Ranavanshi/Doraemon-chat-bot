from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from 𓆩𝐃๏͢ɼ𖦹ɜ𝐦๏ƞ𓆪 ! '


app.run(host='0.0.0.0', port=8080)
