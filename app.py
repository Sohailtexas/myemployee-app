import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env_name = os.environ.get("APP_ENV", "not set")
    return f"Employee Management App Running - Environment: {env_name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)