from flask_script import Manager
from qcrt import create_app
import os


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()