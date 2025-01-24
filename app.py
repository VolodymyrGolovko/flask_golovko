from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)