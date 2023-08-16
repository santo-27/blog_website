from flask import Flask, render_template, request
import requests

name = ""
email_address = ""
phone_number = ""
message = ""

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["POST", "GET"])
def receive_data():
    # global name
    # global email_address
    # global phone_number
    # global message
    
    
    
    if request.method == "POST":
        name = request.form['name']
        email_address = request.form['email']
        phone_number = request.form['phone']
        message = request.form['message']
        print(name)
        print(email_address)
        print(phone_number)
        print(message)
        return f"<h1>sucessful<h1>"
    
    else:
        return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

