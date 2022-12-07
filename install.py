from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


def install():
    engine = create_engine('sqlite:///database.db', future=True)
    meta = MetaData()
    portals = Table(
        'portals', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String)
    )

    credentials = Table(
        'credentials', meta,
        Column('id', Integer, primary_key=True),
        Column('portal_id', Integer),
        Column('login', String),
        Column('password', String)
    )

    meta.create_all(engine)