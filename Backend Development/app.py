from flask import Flask, request, render_template
import re

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def match_regex():
    text_string= request.form['text_string']
    regex=request.form['regex']

    matches= re.findall(regex, text_string)
    return render_template("result.html", matches=matches)


if __name__=='__main__':
    app.run(debug=True)


    