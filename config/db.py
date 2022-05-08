from sqlalchemy import create_engine,MetaData

# engine = create_engine("mysql+pymysql://root@192.168.64.3:3306/kriptokitty")
engine = engine = create_engine('postgresql://postgres:postgres@localhost/kriptokitty')
meta = MetaData()
conn = engine.connect()
