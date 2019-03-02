from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to nowhere pls edit at url (/bmi/Weight:(kg)/Height:(cm))"

@app.route("/BMI/Weight:<int:x>/Height:<int:y>")
def BMI(x, y):
    m = x / 100
    BMI = y / (m * m)

    result = f"This is your BMI: {BMI}"

    if BMI < 16:
        pr = 'Based on the BMI, I can tell you that you are severely underweight'
    elif BMI < 18.5:
        pr = 'Based on the BMI, I can tell you that you are underweight'
    elif BMI < 25:
        pr = 'Based on the BMI, I can tell you that you are normal'
    elif BMI < 30:
        pr = 'Based on the BMI, I can tell you that you are overweight'
    else:
        pr = 'Based on the BMI, I can tell you that you are obese'

    end = result + pr

    return end

if __name__ == '__main__':
  app.run(debug=True)