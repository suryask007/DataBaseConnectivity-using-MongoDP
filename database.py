from pymongo import MongoClient

class bank_data():
    client=MongoClient("mongodb://localhost:27017/")
    db=client["bank_data"]

    def insert_details(self,a,b,c):
        client=MongoClient("mongodb://localhost:27017/")
        db=client["bank_data"]
        collection=db[a]
        db1=db[a]
        db1.insert_one({"name":a,"mobile":b,"B.NO":c})
    def insert_details_travel(self,n,p,ag,tp,dt):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Villupuram"]
        collection1=dp[n]
        dp1=dp[n]
        dp1.insert_one({"n_of_pass":tp,"name":n,"phone":p,"age":ag,"date_time":dt})
    def insert_salem(self,n,p,ag,tp,dt):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["salem"]
        collection=dp[n]
        dp1=dp[n]
        dp1.insert_one({"n_of_pass":tp,"name":n,"phone":p,"age":ag,"date_time":dt})
    def insert_cbe(sel,n,p,ag,tp,dt):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Coimbatore"]
        collection=dp[n]
        dp1=dp[n]
        dp1.insert_one({"n_of_pass":tp,"name":n,"phone":p,"age":ag,"date_time":dt})
    def get_villupuram(self,n):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Villupuram"]
        collection=dp[n]
        dp1=dp[n]
        for i in dp1.find({},{"n_of_pass":1,"name":1,"phone":1,"age":1,"date_time":1}).limit(1):
            print("name of passenger:::",i["name"])
            print("phone number::",i["phone"])
            print("Age of the passenger::",i["age"])
            print("no_of_passenger::",i["n_of_pass"])
            print("Bokking Time and Date::",i["date_time"])
            
    def get_salem(self,n):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["salem"]
        collection=dp[n]
        dp1=dp[n]
        for i in dp1.find({},{"n_of_pass":1,"name":1,"phone":1,"age":1,"date_time":1}).limit(1):
            print("name of passenger:::",i["name"])
            print("phone number::",i["phone"])
            print("Age of the passenger::",i["age"])
            print("no_of_passenger::",i["n_of_pass"])
            print("Bokking Time and Date::",i["date_time"])
    def get_cbe(self,n):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Coimbatore"]
        collection=dp[n]
        dp1=dp[n]
        for i in dp1.find({},{"n_of_pass":1,"name":1,"phone":1,"age":1,"date_time":1}).limit(1):
            print("name of passenger:::",i["name"])
            print("phone number::",i["phone"])
            print("Age of the passenger::",i["age"])
            print("no_of_passenger::",i["n_of_pass"])
            print("Bokking Time and Date::",i["date_time"])
                
c=bank_data()
