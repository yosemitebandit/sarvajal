some exercises for the sarvajal interview


## setup
 - installing the mysql connector is a bit involved..
 - also note the use of virtualenv
  
  ```
  $ sudo apt-get install python-dep python-mysqldb
  $ pip install -E /path/to/virtualenv/ MySQL-python
  $ pip install -E /path/to/virtualenv/ flask
  ```

  - need to (hard) symlink some of the submodules' files

  ```
  $ ln lib/bootstrap/bootstrap.min.css serve/static/css
  ```


## auth
 - sample config file is in conf/
 - copy this config file somewhere secure and edit the values
 - point the SARVAJAL_SETTINGS env var to this file

  ```
  $ export SARVAJAL_SETTINGS=/path/to/config/file.py
  ```

 - might want to drop that export line in .zshrc so the env var is set on load


## nice-to-have
 - caching of the db requests
