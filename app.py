from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/api/timestamp/<date_string>")
@app.route("/api/timestamp/")
def timestamp(date_string=None):
    if not date_string:
        d = datetime.today()
        return jsonify(unix=d.timestamp(), utx=d.utcnow())
    else:
        try:
            d = datetime.fromisoformat(date_string).replace(tzinfo=timezone.utc)
        except:
            try:
                d = datetime.fromtimestamp(int(date_string)).replace(tzinfo=timezone.utc)
            except:
                return jsonify(error="Invalid Date") 
        return jsonify(unix=d.timestamp(), utc=datetime.utcfromtimestamp(d.timestamp()))
