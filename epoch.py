import os
from flask import Flask
import time 

app = Flask(__name__)
ts = time.time()

@app.route('/')
def whatever():
    return str(time.time())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9090))
    app.run(host='0.0.0.0', port=port)