from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from persistence.model import Auth_User, Base  # Asegúrate de importar Base

class AuthUserRepositroy():

    def __init__(self):
        self.engine = create_engine('sqlite:///db/login.sqlite', echo=False)
        self.create_tables()  # Llama a la función para crear tablas

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def getUserByUserName(self, user_name: str):
        user: Auth_User = None
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            user = session.query(Auth_User).filter_by(username=user_name).first()
        return user

    def insertUser(self, user: Auth_User):
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            session.add(user)
            session.commit()