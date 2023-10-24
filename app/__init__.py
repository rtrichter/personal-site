from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test_page():
    return "This is a test page"

def init_app():
    from app import index
    app.register_blueprint(index.bp)
    return app