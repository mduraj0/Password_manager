from sqlalchemy import create_engine, MetaData, Table, Column


def install():
    engine = create_engine('sqlite:///database.db', future=True)
    meta = MetaData()
    portals = Table(
        'portals', meta
        Column()
    )