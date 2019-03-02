from flask import Flask
app = Flask(__name__)

Users = { 
    "max":  {
            "Name":"Tran Viet Hoang", 
            "Age": 20
            },
    "duc":  {
            "Name":"Hoang Huy Duc",
            "Age": 22
            },
}

@app.route("/")
def home():
    return "Welcome to nowhere pls edit at url (/user/(name))"

@app.route("/user/<name>")
def username(name):
    if name in Users:
        return str(Users[name])
    else:
        return "User not found"

if __name__ == '__main__':
  app.run(debug=True)