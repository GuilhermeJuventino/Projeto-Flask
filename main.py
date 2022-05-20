from flask import Flask, request, render_template, redirect, url_for, session, g

app = Flask(__name__)
app.secret_key = "123456"


class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


users = []
users.append(User(id=1, username="balrom", password="12345"))
users.append(User(id=2, username="jsd14", password="orborb"))
users.append(User(id=3, username="ganso", password="pato"))


@app.before_request
def check_id():
    g.user = None

    if "user_id" in session:
        user = [x for x in users if x.id == session["user_id"]][0]
        g.user = user


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)
        # Pegando input do usuário com nome = Username no HTML form
        username = request.form.get("Username")

        # Pegando input do usuário com nome = Password no HTML form
        password = request.form.get("Password")

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session["user_id"] = user.id

            # Redireciona para a página expecificada.
            return redirect(url_for("perfil"))
        
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/perfil")
def perfil():
    if not g.user:
        return redirect(url_for("login"))

    return render_template("perfil.html")


if __name__ == "__main__":
    app.run(debug=True)
