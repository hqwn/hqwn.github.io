from flask import Flask, render_template
import requests
import json

def get():
    url = "https://meme-api.com/gimme/cleanmemes"
    what = json.loads(requests.get(url).text)
    author = what['author']
    image = what['preview'][2]
    title = what["title"]
    return author,image, title
get()
app = Flask(__name__)
@app.route('/')
def aryan():
    author,image, title= get()
    return render_template("index.html", Image=image, Author=author, Title=title)

app.run(host="0.0.0.0", port=5001, debug=False)
