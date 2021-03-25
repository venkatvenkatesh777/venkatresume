from flask import Flask, render_template,send_file
app=Flask(__name__)
@app.route ("/")
def index():
    return render_template ("index.html")
@app.route("/download")
def downloadfile():
    return send_file("Resume.pdf", as_attachment=True)
app.run(debug=True)
