import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import time

parser = argparse.ArgumentParser(description='set time step')
parser.add_argument('--db_url', default='sqlite:///:memory:', help='DB URL, default: sqlite:///:memory:')
parser.add_argument('--step', type=int, help='time step to set')
args = parser.parse_args()

engine  = create_engine(args.db_url)
conn = engine.connect()

s = text("select ageb_id, infra from infra_h where timestep = %s" % args.step)
for row in conn.execute(s).fetchall():
    ageb = dict(row)
    update_infra = text("UPDATE agebs_calles_geo SET infra= :infra WHERE ageb_id= :ageb_id")
    conn.execute(update_infra, infra = ageb['infra'], ageb_id = ageb['ageb_id'])
