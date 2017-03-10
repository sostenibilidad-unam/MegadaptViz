from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import time



engine  = create_engine("postgresql+psycopg2://postgres:x@localhost/new")
conn = engine.connect()


for i in range (1,30):
    time.sleep(0.5)
    esteTimeStep = int(12*i)
    s = text("select * from infra_h where timestep = %s" % esteTimeStep)
    for row in conn.execute(s).fetchall():
        ageb = dict(row)
        #print ageb['ageb_id']
        
        update_infra = text("UPDATE agebs_calles_geo SET infra= :infra WHERE ageb_id= :ageb_id")
        
        conn.execute(update_infra, infra = ageb['infra'], ageb_id = ageb['ageb_id'])