from app import create_app
from flask_script import Manager
from config import config


config_class = config['development']
app = create_app(config_class)

# py manage.py runserver
if __name__ == '__main__':
    manager = Manager(app=app)
    manager.run()
