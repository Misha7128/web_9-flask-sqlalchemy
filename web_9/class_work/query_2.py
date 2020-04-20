app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_3.sqlite")
    session = db_session.create_session()
    for user in session.query(User).filter(User.address == "module_1",
                                           User.speciality.notlike("%ingeneer%"),
                                           User.position.notlike("%ingeneer%")):
        print(user.id)
    session.commit()


if __name__ == '__main__':
    main()
