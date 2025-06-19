from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    # Передаємо змінну 'name' до шаблону
    return render_template('index.html', name="Світ")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
