from flask import Flask, render_template, request
app = Flask(__name__)

items = [
    {
        "Model": "Xe Máy Honda - Wave Alpla",
        "Fee": 100000,
        "Image": "https://hondaxemay.com.vn/wp-content/uploads/2018/12/450x250-icon_450x250_acf_cropped.png",
        "Year": "2013",
    },
    {
        "Model": "Xe Máy Suzuki - GSX S150",
        "Fee": 100000,
        "Image": "https://salt.tikicdn.com/cache/200x200/ts/product/ec/14/d7/2c32540619b54f10468b4a29177a2214.jpg",
        "Year": "2014",
    },
]

@app.route("/")
def homepage():
    return render_template("bike_home.html", item_list = items)

@app.route("/bike/<int:i>")
def bike(i):
    b = items[i]
    return render_template("bike_detail.html", item = b)

@app.route("/admin/add_bike", methods=["GET", "POST"])
def add_bike():
    if request.method == "GET":
        return render_template("bike_form.html")
    elif request.method == "POST":
        form = request.form
        m = form["Model"]
        f = form["Fee"]
        i = form["Image"]
        y = form["Year"]

        new_item = {
            "Model": m,
            "Fee": f,
            "Image": i,
            "Year": y,
        }
        items.append(new_item)
        
        return str(new_item)


if __name__ == '__main__':
  app.run(debug=True)