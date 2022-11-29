import pymongo
import timeit

client = pymongo.MongoClient("mongodb://srv-mongodb-test1:27070,srv-mongodb-test2:27070,srv-mongodb-test3:27070/?readPreference=primaryPreferred&replicaSet=rs_fuxion")

mydb = client['db_fuxion']
information = mydb.table2
print("Connection Successful")

rec = [{
    "EMPO" : 7934,
    "ENAME" : "MILLER",
    "JOB" : "CLERK",
    "MGR" : 7782
    }]

def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        #print(i)
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
                rec = [{
                        "EMPO" : 7934,
                        "ENAME" : "MILLER",
                        "JOB" : "CLERK",
                        "MGR" : 7782,
                        "I"  : i,
                        "J" : j
                       }]
                information.insert_many(rec)
                print (rec)

    return results


start_time = timeit.default_timer()
gen_prime(100)

#result = information.insert_many(rec)
#print (result.inserted_ids)

print(timeit.default_timer() - start_time)



#time.sleep(3)
#result = information.insert_many(rec)
#print (result.inserted_ids)


client.close()

