from flaskr.__init__ import create_app

if __name__ == "__main__":
    app = create_app()
    create_app().run()

else:
    gunicorn_app = create_app()