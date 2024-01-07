import sqlalchemy
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://2uot6vwf2s9wwtp3smwt:pscale_pw_VIobgTOafYVF0bFUUhtag9PNgo2SAGJlSmYmydLkZPl@aws.connect.psdb.cloud/joviancarear?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text(" select * from jobs "))
  print("type result",type(result))
  result_all = result.all()
  print("type result_all",type(result_all))
print("result_all",result_all)

first_result_dict = dict(result_all[0])
print("type result dict :",type(first_result_dict))
print(first_result_dict)  
