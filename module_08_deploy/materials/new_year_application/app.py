import os

from flask import Flask, render_template, send_from_directory

root_dir = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(root_dir, "templates")
static_directory = os.path.join(template_folder, 'static')
app = Flask(__name__, template_folder=template_folder, static_folder=static_directory)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static")
def send_static(path):
    return send_from_directory(static_directory, path)

# @app.route("/js/<path:path>")
# def send_js(path):
#     return send_from_directory(js_directory, 'js')
#
#
# @app.route("/css/<path:path>")
# def send_css(path):
#     return send_from_directory(css_directory, 'css')
#
#
# @app.route("/images/<path:path>")
# def send_images(path):
#     return send_from_directory(images_directory, 'images')


if __name__ == "__main__":
    app.run()
