import os

from backend.flaskr import create_app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app = create_app()
    app.config.from_object('config')
    app.run()
