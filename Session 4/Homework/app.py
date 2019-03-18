from flask import Flask, render_template, request
import food

app = Flask(__name__)



@app.route("/food_list")
def food_list():
    # Get All Food 1.Function? 2.Write function?
    all_food = food.get_food({ })

    # Render: All Food + HTML
    
    # Return 
    return render_template('food_list.html', f_list = all_food) # màu trắng thuộc python còn màu xanh thuộc html

@app.route("/food/<id>")
def food_detail(id):
    f = food.get_by_id_food(id)

    return render_template('food_detail.html', food = f ) # ve nha lam

@app.route("/add_food", methods=["GET", "POST"])
def add_food():
    if request.method == "GET":
        return render_template("food_form.html")
    elif request.method == "POST":
        form = request.form
        n = form["name"]
        p = form["price"]
        food.add_food(n, p)
        return "New food added"

@app.route("/user", methods=["GET", "POST"])
def user():
    if request.method == "GET":
        return render_template("user.html")
    elif request.method == "POST":
        form = request.form
        un = form["username"]
        p = form["password"]
        if food.find_by_username == None:
          return "This user has been added !!"

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template("add_user.html")
    elif request.method == "POST":
        form = request.form
        un = form["username"]
        p = form["password"]
        food.add_food(un, p)
        return "New User added"


if __name__ == '__main__':
  app.run(debug=True)