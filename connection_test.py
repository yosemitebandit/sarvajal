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
            , passwd=DB['password']
            , db=DB['database_name'])
    
    '''
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION()")
    print 'db version: %s' % cursor.fetchone()
    '''
    
    '''
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM %s WHERE p16 IS NOT NULL LIMIT 200' % SOOCHAK_MESSAGES)
    result = cursor.fetchall()
    print result
    '''

    # frm testing
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
        SELECT *
        FROM %s
        ''' % FRM_PRODUCTION)
    result = cursor.fetchall()
    print FRM_PRODUCTION
    for r in result:
        print '%-5s %-40s' % (r['soochak_parameter_subvalue_id']
                , r['parameter_sub_value_meaning'])
    print '\n\n'
        

except MySQLdb.Error, e:
    print 'error %d: %s' % (e.args[0], e.args[1])
    sys.exit(1)

finally:
    if conn:
        conn.close()
