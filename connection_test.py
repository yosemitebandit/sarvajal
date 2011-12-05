#!/usr/bin/env python
'''
test.py
testing some connections
'''
import os
import sys

import MySQLdb

# first load up the config file
config_path = os.environ.get('SARVAJAL_SETTINGS')
if not config_path:
    raise RuntimeError("the 'SARVAJAL_SETTINGS' env var needs to be set")
execfile(config_path, globals())

conn = None
try:
    conn = MySQLdb.connect(
            host=DB['host']
            , port=DB['port']
            , user=DB['user']
            , passwd=DB['password'])

    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    print 'db version: %s' % cursor.fetchone()

except MySQLdb.Error, e:
    print 'error %d: %s' % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if conn:
        conn.close()
