from gluon.contrib.appconfig import AppConfig 
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("Memo",
               Field('db_Title'),
               Field('db_Body'))