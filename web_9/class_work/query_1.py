from data.users import User
from data import db_session
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_3.sqlite")
    # app.run()

    session = db_session.create_session()

    for user in session.query(User).filter(User.address == "module_1"):
        print(user)
    session.commit()


if __name__ == '__main__':
    main()
