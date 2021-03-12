## Use Flask to make a web app tutorial

* [ ] Build the python virtual environment:
  * [ ] `mkdir note_app` to create the main directory;
  * [ ] `cd note_app` enter the app directory;
  * [ ] `pipenv install --python 3.9` create the virtual environment;

* [ ] Install python packages:
  * [ ] `pipenv install flask` install flask;
  * [ ] `pipenv install flask-login` to manage user authorize;
  * [ ] `pipenv install flask-sqlalchemy` use to operate the sql database;
  
* [ ] Create the app directory structure:
  * [ ] `mkdir website`
  * [ ] create `main.py`
  * [ ] `cd website`
    * [ ] `mkdir static`
    * [ ] `mkdir templates`
    * [ ] create file `__init__.py`
    * [ ] create file `views.py`
    * [ ] create file `auth.py`
    * [ ] create file `models.py`
    * [ ] `cd ..` come back to the `website` directory
  * [ ] `cd templates`, in `templates` directory:
    * [ ] create file `base.html`
    * [ ] create file `home.html`
    * [ ] create file `login.html`
    * [ ] create file `sign_up.html`
    * [ ] `cd ..` go back to the `website` directory
  * [ ] `cd static`, in `static` directory:
    * [ ] create file `index.js`

### Now the file system structure looks like this:
![avatar](website/static/tree.png)

* [ ] Config the database;
  * [ ] create file `exts.py` in `website` directory
  ``` python
    from flask_sqlalchemy import SQLAlchemy

    db = SQLAlchemy()
  ```
  * [ ] Create database configuration file `configs.py`
    * [ ] Define `DB_URI` and let `SQLALCHEMY_DATABASE_URI=DB_URI`
    * [ ] Define other parameters, like `SQLALCHEMY_TRACK_MODIFICATION=False`,
    `SQLALCHEMY_ECHO=True`
  
  * [ ] Create tables configuration file `models.py`
    * [ ] First `from .exts import db`
    * [ ] Second define `class User` amd `class Note`

* [ ] Initial the app
  * [ ] Input code in `__init__.py` like this:
    ```python
    from flask import Flask
    from . import configs
    from .exts import db
    from os import path
    from .models import User, Note

    def create_app():
      app = Flask(__name__)
      app.config.from_object(configs)
      db.init_app(app)

      if configs.SQLALCHEMY_DATABASE_URI==configs.DB_URI_SQLITE:
        create_database(app)

      return app

    def create_database(app):
      if not path.exists('website/' + configs.DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
    ```
  * [ ] Input code into `/NOTE_APP/main.py`:
    ```python
    from website import create_app

    app = create_app()

    if __name__ == '__main__':
      app.run(debug=True)
            


