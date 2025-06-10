from flask import Flask, send_file, request

app = Flask(__name__)

@app.route('/get-file', methods=['GET'])
def get_file():
    size = request.args.get('size', '1000')  # default 10 KB
    filepath = f"files/file_{size}kb.txt"
    try:
        return send_file(filepath, as_attachment=True)
    except FileNotFoundError:
        return {"error": "File not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
