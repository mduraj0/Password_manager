from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


def install():
    engine = create_engine('sqlite:///database.db', future=True)
    meta = MetaData()
    portals = Table(
        'portals', meta
        Column('id', Integer, primary_key=True),
        Column('name', String)
    )