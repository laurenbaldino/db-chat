from src.swen344_db_utils import *
import csv
import datetime
from src.users import *
from src.messages import *
from src.communities import *
from src.channels import *

# def readCSV():
#     with open('AbbottCostello.csv') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
#         for row in reader:
#             line_count = 0
#             if line_count != 0:
#                 createNewMessage(sender_id=row[0], reciever_id=row.next(row[0]), message=row[1], sent_on=datetime.now())
#                 line_count += 1
#     csv_file.close()


def setupTables():
    """Build all and insert test data"""
    conn = connect()
    cur = conn.cursor()
    build_users()
    build_messages()
    build_communities()
    build_channels()
    build_suspended_users()
    build_users_to_communities()
    build_channel_messages()
    exec_sql_file('test_data.sql')
    conn.close()


#setupTables()

