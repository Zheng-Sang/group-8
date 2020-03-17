from pymongo import MongoClient


class database:
    def __init__(self, host='localhost', port=None, database='order', authfile=None):
        try:
            if port is not None:
                self.mongo = MongoClient(host, int(port))
            else:
                self.mongo = MongoClient(host)
        except:
            print("Error starting MongoDB")
            raise

        self.db = self.mongo[database]

        if authfile is not None:

            try:
                dbauth = json.loads(open(authfile, 'r').read())
                if not self.db.authenticate(dbauth["user"], dbauth["password"]):
                    raise Exception("Invalid database credentials")

            except:
                print("Error authenticating database")
                raise

        self.tuits = {}
    
    def load_data(self, table_name):
        self.prefs = {}
        userNodeMap = {}
        for user in self.db[table_name].find().sort([('value.indegree', -1)]):
            # if user['userid'] not in pref:
            self.prefs[user['userid']].append(user['purchase'])
            # else:
        
        self.itemList = {}
        for user in self.prefs:
            for item in self.prefs[user]:
                self.itemList[item] = None

        return self.prefs, self.itemList
            # userMap[user['_id']] = user['value']
            # node = graph.addNode(user['_id'], user['_id'])
            # node.addAttribute(giid, str(user['value']['indegree']))
            # userNodeMap[user['_id']] = node
    #链接本地数据库
# dbClient = MongoClient("localhost", 27017)

# # 调用server_info查询服务器状态，防止服务器异常并未连接成功
# dbClient.server_info()

# #指定MongoDB的表名
# last_col=dbClient ['数据库名称']['表名']

