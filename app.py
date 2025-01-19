from flask import Flask, render_template, jsonify

app = Flask(__name__)

count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    global count
    count += 5
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(debug=True)
