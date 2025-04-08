import os
from flask import Flask

app = Flask(__name__)

pod_name = os.environ.get("POD_NAME", "unknown-pod")
node_name = os.environ.get("NODE_NAME", "unknown-node")
namespace = os.environ.get("POD_NAMESPACE", "unknown-namespace")

@app.route("/")
def index():
    return f"Container EDU | POD Working : {pod_name} | nodename : {node_name} | namespace : {namespace}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
