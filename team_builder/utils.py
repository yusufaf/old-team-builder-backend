from pymongo import MongoClient

connection_string = 'mongodb+srv://yusufaf:<WmU9ACcwEfhBTdpw>@teambuildercluster.jzwnekf.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)
db = client['users']


# def get_db_handle(db_name, host, port, username, password):
#     client = MongoClient(
#         host=host, port=int(port), username=username, password=password
#     )
#     db_handle = client["db_name"]
#     return db_handle, client
