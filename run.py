from flask import Flask, render_template, jsonify

import sqlite3
STATSDB = 'stats.db'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('3j.html')
    
@app.route('/stats', methods=['GET'])
def fetchStats():

    con = sqlite3.connect(STATSDB)
    stats = []
    cur = con.execute('SELECT * FROM stats ORDER BY points DESC LIMIT 10')

    for row in cur:
        stats.append(list(row))
    con.close()

    return jsonify(stats)
