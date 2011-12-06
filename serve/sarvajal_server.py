#!/usr/bin/env python
'''
sarvajal_server.py
api endpoints for the sarvajal data
'''
import datetime
import sys

import MySQLdb
import flask

app = flask.Flask(__name__)
app.config.from_envvar('SARVAJAL_SETTINGS')


''' data api methods
'''
@app.route('/api/1/messages', methods=['GET'])
def v1_messages():
    ''' accessing the processed Soochak SMS data
    '''
    conn = _create_db_connection()

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('''
        SELECT * 
        FROM %s 
        WHERE p16 IS NOT NULL 
        AND p4 IS NOT NULL
        AND p13 IS NOT NULL
        AND p19 IS NOT NULL
        ORDER BY last_updated_on DESC
        LIMIT 10
        ''' % app.config['SOOCHAK_MESSAGES'])

    result = cursor.fetchall()  # returns a tuple
    for row in result:
        # convert the datetimes so the row is json-serializable
        dt = row['last_updated_on']
        row['last_updated_on'] = dt.strftime('%d %b %y %I:%M%p')

    return flask.jsonify({'data': result})


@app.route('/messages', methods=['GET'])
def show_messages():
    ''' list the messages
    '''
    return flask.render_template('show_messages.html')


def _create_db_connection():
    ''' attempt to connect to the db
    '''
    conn = None
    try:
        conn = MySQLdb.connect(
                host=app.config['DB']['host']
                , port=int(app.config['DB']['port'])
                , user=app.config['DB']['user']
                , passwd=app.config['DB']['password']
                , db=app.config['DB']['database_name'])

    except MySQLdb.Error, e:
        print 'error %d: %s' % (e.args[0], e.args[1])
        sys.exit(1)

    return conn


if __name__ == '__main__':
    app.run(
        host=app.config['SERVER_HOST']
        , port=app.config['SERVER_PORT'])
