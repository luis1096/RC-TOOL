from app import create_app

if __name__ == '__main__':
    app = create_app()	
    app.config.from_pyfile('../config.py')
    app.run(host=app.config['HOST'], port=app.config['PORT'])