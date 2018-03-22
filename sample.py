from influxdb import InfluxDBClient
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
 
df = pd.read_excel('test.xlsx', sheetname='Sheet1')
 
region = df['region']
#print(region)
host = df['host']
#print(host)
for host in host:
	
	json_body = [
    {
        "measurement": "cpu_load_server",
        "tags": {
            "host": host
        },
        "fields": {
            "value": 0.64
       	 }
    	}
	]


	client = InfluxDBClient('localhost', 8086, 'root', 'root', 'pythonInserted')

	client.create_database('pythonInserted')

	client.write_points(json_body)

	result = client.query('select value from cpu_load_short;')

	print("Result: {0}".format(result))
