some exercises for the sarvajal interview


## setup
 - installing the mysql connector is a bit involved..
 - also note the use of virtualenv

  $ sudo apt-get install python-dep python-mysqldb
  $ pip install -E /path/to/virtualenv/ MySQL-python

## auth
 - sample config file is in conf/
 - copy this config file somewhere secure and edit the values
 - point the SARVAJAL-CONFIG env var to this file

  $ export SARVAJAL-CONFIG=/path/to/config/file.py
