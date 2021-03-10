from flask_script import Manager
from qcrt import create_app
from gevent import pywsgi
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == "__main__":
    # manager.run()
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()