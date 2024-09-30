
from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database connection setup
conn = psycopg2.connect(
    dbname=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host="postgres",  # container name of the DB service
    port="5432"
)

@app.route('/api/ingest', methods=['POST'])
def ingest_data():
    data = request.json
    cur = conn.cursor()
    query = '''
    INSERT INTO orders (order_id, customer_id, total_price)
    VALUES (%s, %s, %s);
    '''
    cur.execute(query, (data['order_id'], data['customer_id'], data['total_price']))
    conn.commit()
    cur.close()
    return jsonify({"message": "Data ingested successfully!"}), 201

@app.route('/api/visualize', methods=['GET'])
def get_visualization_data():
    cur = conn.cursor()
    query = "SELECT * FROM orders;"
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
