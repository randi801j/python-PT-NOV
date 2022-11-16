from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "supersecret"
@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add-category",methods=["post"])
def add_category():
  print("FORM DATA",request.form)
  print("Category DATA",request.form["name"])
  if "categories" in session:
    categories = session["categories"]
    categories.append(request.form) # [{"name":"category name"},{"name":"new name"}]
    session["categories"] = categories
  else:
    session["categories"] = [request.form] # [{"name":"category name"}]
  return redirect("/")

@app.route("/clear-categories")
def clear():
  session.clear()
  # session.pop("categories")
  return redirect("/")

if __name__== "__main__":
  app.run(debug=True,port=8000)