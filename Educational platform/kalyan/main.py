from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/playlist")
def playlist():
    return render_template("playlist.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/teacherprofile")
def teacher_profile():
    return render_template("teacher_profile.html")

@app.route("/teachers")
def teachers():
    return render_template("teachers.html")

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/watchvideo")
def watch_video():
    return render_template("watch_video.html")

if __name__ == '__main__':
    app.run(debug=True)
