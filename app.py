from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Initialize the count variable
count = 0

@app.route('/')
def index():
    return render_template('index.html', count=count)

@app.route('/click', methods=['POST'])
def click():
    global count
    count += 5  # Increment by 5 when the image is clicked
    return jsonify({'count': count})

if __name__ == '__main__':
    app.run(debug=True)
