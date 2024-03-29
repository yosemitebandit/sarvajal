# config file for the sarvajal exercises
# move the sample out of the repo and to a secure location
# point the SARVAJAL-CONFIG env var to the secure file

# db connection credentials
DB = {
    'host': '123.456.78.9'
    , 'port': 7890
    , 'user': 'harveyDent2'
    , 'password': 'c0into55'
    , 'database_name': 'records'
}

# tables and relevant fields for the soochak messages exercise
SOOCHAK_MESSAGES_TABLE = 'sms_data_table'
SOOCHAK_ERROR_CODES_TABLE = 'errors'
SOOCHAK_ERROR_PARAMETER_FIELD = '10'
SOOCHAK_ERROR_MEANING_FIELD = 'meaning'


# tables for the frm exercise
# provides accountID --> machineID mapping
FRM_ACCOUNT_DATA_TABLE = 'frm_account'
FRM_ACCOUNT_ID_FIELD = 'account' 
FRM_MACHINE_ID_FIELD = 'machine' 
# participation data
FRM_PARTICIPATION_TABLE = 'frm_particip'
# production data
FRM_PRODUCTION_TABLE = 'frm_prod'


# flask server settings
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6060
DEBUG = False
