from flask import Flask, send_from_directory, abort
from pathlib import Path

app = Flask(__name__, static_folder="static")


@app.route("/")
def read_index():
    try:
        html_path = Path("source/index.html")
        return html_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "File not found.", 404


@app.route("/transition/")
def read_transition_page():
    try:
        html_path = Path("source/transition_page.html")
        return html_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return "File not found.", 404


@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    app.run(host="127.0.0.1", port=port)