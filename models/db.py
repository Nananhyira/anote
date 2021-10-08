from gluon.contrib.appconfig import AppConfig
configuration = AppConfig(reload=True)

db = DAL("sqlite://storage.sqlite")
db.define_table("users",    
               Field('db_TITLE'), 
               Field('db_ADDNOTES')) 


             