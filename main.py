from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/binance/klines")
def proxy_klines():
    symbol = request.args.get("symbol")
    interval = request.args.get("interval", "15m")
    limit = request.args.get("limit", "100")
    url = f"https://api.binance.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
