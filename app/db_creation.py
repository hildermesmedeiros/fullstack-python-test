# -*- coding: utf-8 -*-
from backEnd import db

db.create_all()
try:
    db.session.commit()
except:
    db.session.rollback()
    
exit()
