import json
import requests
import secrets
import time

startTime = time.time()

baseURL = secrets.baseURL
user = secrets.user
password = secrets.password

auth = requests.post(baseURL + '/users/'+user+'/login?password='+password).json()
session = auth["session"]
headers = {'X-ArchivesSpace-Session':session, 'Content_Type':'application/json'}
print 'authenticated'

endpoint = '/repositories/3/top_containers?all_ids=true'

ids = requests.get(baseURL + endpoint, headers=headers).json()

records = []
for id in ids:
    endpoint = '/repositories/3/top_containers/'+str(id)
    output = requests.get(baseURL + endpoint, headers=headers).json()
    records.append(output)

f=open('topContainers.json', 'w')
json.dump(records, f)
f.close()

elapsedTime = time.time() - startTime
m, s = divmod(elapsedTime, 60)
h, m = divmod(m, 60)
print 'Total script run time: ', '%d:%02d:%02d' % (h, m, s)
