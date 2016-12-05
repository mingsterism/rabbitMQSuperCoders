import common
import configparser

config = configparser.ConfigParser()
config.read('profiles.ini')

table = 'table1044'
q = common.PSQL_DB(config['psql1'])
q.create_table(table)
for x in range(10000):
    q.insert_data('http://www.thestar.com.my' + str(x), table)
q.closeDB()
