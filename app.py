from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')
@app.route('/libs/<path:filename>')
def serve_libs(filename):
    return send_from_directory('static/libs', filename)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('static/assets', filename)

if __name__ == "__main__":
    app.run(debug=True)
