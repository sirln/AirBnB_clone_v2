#!/usr/bin/python3
'''

'''


class DBStorage:
    '''
    DBStorage class to abstract the database storage engine

    It provides methods to interact with the database

    Attributes:
        __engine (sqlalchemy.Engine): The database engine.
        __session (sqlalchemy.orm.session.Session): The database session.
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
        Initializes the database storage engine.

        The engine is connected to the MySQL database using
        environment variables.

        If the environment is set to 'test',
        it drops all tables.
        '''
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        connection_string = f"mysql+mysqldb://{user}:{pwd}@{host}/{db}"
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Queries all records in the database.

        Args:
            cls (Class, optional): The class name to query.
            Default; None, queries all classes.

        Returns:
            dict: A dictionary representation of the query results.
                  The dictionary keys are in the format
                  <class-name>.<object-id>,
                  and the values are the objects.
        '''
        results_dict = {}
        if cls:
            results = self.__session.query(cls).all()
            for item in results:
                key = f'{item.__class__.__name__}.{item.id}'
                results_dict[key] = item
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                results = self.__session.query(cls).all()
                for item in results:
                    key = f'{item.__class__.__name__}.{item.id}'
                    results_dict[key] = item

        return (results_dict)

    def new(self, obj):
        '''
        Adds the object to the current database session.

        Args:
            obj (Base): The object to be added.
        '''
        self.__session.add(obj)

    def save(self):
        '''Commits all changes made to the current database session.'''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Deletes the object from the current database session.

        Args:
            obj (Base, optional): The object to be deleted.
            Default; None, nothing happens.
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
        Reloads all tables and creates a new database session.

        This method also ensures that all classes
        inheriting from Base are imported.
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
