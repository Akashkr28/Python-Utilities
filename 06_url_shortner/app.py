from flask import Flask

from models import (init_db, insert_url, get_url, get_all_urls, increment_visit_count, delete_url_by_code)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello to Pytho Learners!'

if __name__ == '__main__':
    app.run(debug=True)