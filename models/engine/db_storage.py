#!/usr/bin/python3
""" a module that stores in the database """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """
        DBStorage class that implements the storage in database
        Attrs:
            __engine: a private attribute
            __session: a private attribue
    """
    __engine = None
    __session = None
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    def __init__(self):
        """ Initialize the DBStorage instance. """
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', default='localhost')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, passwd, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Query all object in the current database session.
            Args:
                cls (class): The class to query. If None, query all types of
                objects.
            Returns:
                dict: A dictionary with keys in the format below
                <class-name>.<object-id>
        """
        obj_dict = {}
        if cls:
            result = self.__session.query(cls)
        else:
            result = []
            for class_name in self.classes:
                result.append(self.__session.query(classes[class_name]))
        for obj in result:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            obj_dict[key] = obj
        return obj_dict


    def new(self, obj):
        """
        Add the object to the current database session.
        Args:
            obj (BaseModel): The object to add to the session.
        """
        self.__session.add(obj)


    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()


    def delete(self, obj=None):
        """ 
        Delete an object from the current database session if it's not None.

        Args:
            obj (BaseModel): The object to delete from the session
        """
        if obj:
            self.__session.delete(obj)


    def reload(self):
        """
        Create all tables in the database and create the current database
        session.
        """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
