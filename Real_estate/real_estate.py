import xmlrpc.client

# Create xmlrpc script to search records, to create records, to update existing records and to unlink existing records

db = "eTraining"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print ("Connection Successful")
    

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

## Create Record
# result = models.execute_kw(db, uid, password, 'real.estate', 'create', [{'name': 'Swojas', 'excepted_price': '1900'}])

## Search Record
to_confrim_ids = models.execute_kw(db, uid, password, 'real.estate', 'search', [[('name', '=', 'Swojas')]])
print ("\n\nto_confrim_id ::: ", to_confrim_ids)

## Give Action to Record
# result = models.execute_kw(db, uid, password, 'real.estate', 'button_sold', [to_confrim_ids])

## Search_Read Record
# result = models.execute_kw(db, uid, password, 'real.estate', 'search_read', [[], ['name', 'description', 'state']])

## Update Record
# result = models.execute_kw(db, uid, password, 'real.estate', 'write', [to_confrim_ids, {'name': 'Swojas H', 'excepted_price': '2900'}])

## Unlink Record
result = models.execute_kw(db, uid, password, 'real.estate', 'unlink', [to_confrim_ids])


print ("\n\nresult is ::: ", result)