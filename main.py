from flask import Flask
app = Flask(__name__)
@app.route("/<vardas>")
def home(vardas):
    return f"labas, {vardas}"
    return "<hi>Cia mano pirmas psl</hi>"

if __name__ == "__main__":
    app.run(debug=True)