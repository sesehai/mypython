# -*- coding:utf-8 -*-
'''
Created on 2012-6-24

@author: Administrator
'''

import db

class Album(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cmyDb = db.CMySql()
        self.cmyDb.setoptions("127.0.0.1", "root", "root", "python")
        self.cmyDb.start()
        
        
    def query(self,sql):
        result = self.cmyDb.query(sql)
        return result

album = Album()
rows = album.query("select * from album order by id desc limit 5")
#print(rows)
for row in rows:
    print(row)
#    print("\n")
    
