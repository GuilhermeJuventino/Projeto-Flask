from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Pegando input do usuário com nome = Username no HTML form
        username = request.form.get("Username")

        # Pegando input do usuário com nome = Password no HTML form
        password = request.form.get("Password")

        print(f"Seu nome de usuário é {username}\nSua senha é {password}")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
