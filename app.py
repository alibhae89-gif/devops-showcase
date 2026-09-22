import os
import redis
from flask import Flask, jsonify

app = Flask(__name__)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    count = cache.incr("hits")
    return f"Hello from Docker! Visited {count} times.\n"

@app.route("/health")
def health():
    try:
        cache.ping()
        return jsonify(status="ok"), 200
    except Exception:
        return jsonify(status="redis down"), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
