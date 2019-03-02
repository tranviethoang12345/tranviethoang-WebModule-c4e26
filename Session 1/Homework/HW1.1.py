from flask import Flask, redirect
app = Flask(__name__)

me = {
    "Name": "Max",
    "Work": "Free",
    "School": "UoG",
    "Hobbies": "Zzzzz",
    "Relationship": "Unknown",
    "Pet": "None",
}

@app.route("/")
def home():
    return "Welcome to nowhere pls edit at url (about-me | school)"

@app.route("/about-me")
def about_me():
    return str(me)

@app.route("/school")
def school():
    return redirect("http://techkids.vn") 

if __name__ == '__main__':
  app.run(debug=True)