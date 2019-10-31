import datetime
import uuid

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes_test.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()
class User(Base):
    """
    Описывает структуру таблицы user для хранения
     регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.String(36), primary_key=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # пол пользователя
    gender = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)
	# дата рождения пользователя
    birthdate = sa.Column(sa.Text)
	# рост пользователя
    height = sa.Column(sa.Float)

def connect_db():
    """
    Устанавливает соединение к базе данных,
     создает таблицы, если их еще нет 
    и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(DB_PATH)
    # создаем описанные таблицы
    Base.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()
def request_data():
    """
    Запрашивает у пользователя данные и добавляет их
     в список users
    """
    # выводим приветствие
    print("Привет! Я запишу твои данные!")
    # запрашиваем у пользователя данные
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Теперь твой пол: ")
    email = input("А так же адрес твоей электронной почты: ")
    birthdate = input("Напиши дату твоего рождения: ")
    height = input("Ну, и твой рост тоже понадобится: ")
    # генерируем идентификатор пользователя и 
    #сохраняем его строковое представление
    user_id = str(uuid.uuid4())
    # создаем нового пользователя
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    # возвращаем созданного пользователя
    return user
def main():
    """
    Осуществляет взаимодействие с пользователем,
     обрабатывает пользовательский ввод
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    
if __name__ == "__main__":
    main()
print("Все, твои данные сохранены. Спасибо!")
