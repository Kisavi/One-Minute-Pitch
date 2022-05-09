from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

# initialize our Migrate class
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()  # runs the Flask instance (app)
