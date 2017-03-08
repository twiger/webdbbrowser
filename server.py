"""
Tutorial : https://www.digitalocean.com/community/tutorials/how-to-use-the-bottle-micro-framework-to-develop-python-web-apps
"""

import sqlite3, bottle
from sqlite3 import OperationalError
from bottle import route, run, template, response, request 

""" Handle the CORS Issues """
# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

app = bottle.app()


''' Router Definition '''

# Basic response
@app.route('/hello')
def hello():
    return "Hello Hippo!"


# Basic DB query example
@app.route('/picnic')
def show_picnic():
    db = sqlite3.connect('picnic.db')
    c = db.cursor()
    c.execute("SELECT item,quant FROM picnic;")
    data = c.fetchone()
    c.close()
    print data
    return template('Hello {{name}}, how are you?', name=data[0])


# Response some messages in dictionary to client app
@app.route('/getResponse', method=['OPTIONS', 'POST'])
@enable_cors
def responseStr():

    print "Http Request /getResponse - input :"
    print "==================================="
    print request.json['description']
    print "==================================="

    res = {
        'firstStrList': ['I', 'love', 'Sherry.'],
        'secondStrList': ['Sherry', 'loves', 'me.']
    }
    
    return res



# Response some messages in dictionary to client app
@app.route('/queryDB', method=['OPTIONS', 'POST'])
@enable_cors
def queryPicnic():
    
    print "Http Request /getResponse - input :"
    print "==================================="
    print request.json['description']
    print "==================================="

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute("SELECT * FROM Employee;")
    dataFromDB = c.fetchall()
    c.close()
    #print dataFromDB

    res = {
        'firstStrList': [dataFromDB[0][0],dataFromDB[0][1]]
        
    }
    
    return res

# Response some messages in dictionary to client app
@app.route('/sendForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendForm():

    print "Http Request /sendForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="

    res = {
        'message': "Hi, %s %s. You send this form successfully!" % (inputData['first_name'], inputData['last_name']),
    }
    
    return res


@app.route('/sendCusForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendCusForm():
    print "Http Request /sendCusForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES (:cus_name, :cus_contact_person, :cus_email, :cus_phone, :cus_address, :cus_region, :cus_empId);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res


@app.route('/sendEmpForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendEmpForm():
    print "Http Request /sendEmpForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Employee(fname,lname,title,department,base_region,gender,dob,email,phone,start_date) VALUES (:emp_fname,:emp_lname,:emp_title,:emp_department,:emp_region,:emp_gender,:emp_dob,:emp_email,:emp_phone,:emp_startDate);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res


@app.route('/sendPubForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendPubForm():
    print "Http Request /sendPubForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Publisher(name,contact_person,country,phone,address,email,prod_specialist_id) VALUES (:pub_name,:pub_contact_person,:pub_country,:pub_phone,:pub_address,:pub_email,:pub_empId);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res


@app.route('/sendProdForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendProdForm():
    print "Http Request /sendProdForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Product(name,subscription_model,type,priceUSD,priceNTD,pub_id) VALUES (:prod_name,:prod_subModel,:prod_type,:prod_priceUSD,:prod_priceNTD,:prod_pubId);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res


@app.route('/sendOrdForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendOrdForm():
    print "Http Request /sendOrdForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Orders(prod_id,inv_id,amount,priceNTD,ord_date,sub_start_date,sub_end_date,note) VALUES (:ord_prodId,:ord_invId,:ord_amount,:ord_priceNTD,:ord_orderDate,:ord_subStartDate,:ord_subEndDate,:ord_note);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res


@app.route('/sendInvForm', method=['OPTIONS', 'POST'])
@enable_cors
def sendInvForm():
    print "Http Request /sendInvForm - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="
    
    #info = "(" + "'" + inputData['cus_name'] + "'" + "," + "'" +inputData['cus_contact_person'] + "'" + ',' + "'" + inputData['cus_email'] + "'" + ',' + "'" + inputData['cus_phone'] + "'" + ',' + "'" + inputData['cus_address'] + "'" + ',' +  "'" + inputData['cus_region'] + "'" + ',' + inputData['cus_empId'] + ')'
    #print info

    db = sqlite3.connect('flysheetDb.db')
    c = db.cursor()
    c.execute('''INSERT INTO Invoice(inv_number,cus_id,issued_date,quarter,payment_date,amountUSD,amountNTD,Note) VALUES (:inv_number,:inv_cusId,:inv_issuedDate,:inv_quarter,:inv_paymentDate,:inv_amountUSD,:inv_amountNTD,:inv_note);''', inputData)
    #c.execute("INSERT INTO Customer(name,contact_person,email,phone,address,region,sales_person_id) VALUES " + info)
    db.commit()
    db.close()

    res ={
      'message': "You send this form successfully!",
    }

    return res



@app.route('/runSQL', method=['OPTIONS', 'POST'])
@enable_cors
def runSQL():
    print "Http Request /runSQL - input :"
    print "==================================="
    inputData = request.json
    print inputData
    print "==================================="

    db = sqlite3.connect('flysheetDb.db')

    res = {}
    
    try:
        result = db.execute(inputData['sqlite_text'])
        res.update({'success': "You run the statement successfully!"})
        
        if 'select' in inputData['sqlite_text'].lower():
            if 'view' in inputData['sqlite_text'].lower():
                res.update({'notice':"You have created a view in the database."})
            else:
                result_dict = getResultTable(result)
                res.update(result_dict)          
        else:
            string = "You have made changes to the database. Rows affected: " + str(db.total_changes)
            res.update({'notice': string})

        db.commit()
        db.close()
        #getRecords()

    except sqlite3.OperationalError, o:
        print "Error: %s" % o.args[0]
        res.update({'error' : "Error: %s" % o.args[0]})
        db.close()
        return res

    except sqlite3.Warning, w:
        print "Error: %s" % w.args[0]
        res.update({'warning': "Warning: %s" % w.args[0]})
        db.close()
        return res

    except sqlite3.DatabaseError, d:
        print "Error: %s" % d.args[0]
        res.update({'error' : "Error: %s" % d.args[0]})
        db.close()
        return res

    except sqlite3.IntegrityError, i:
        print "Error: %s" % i.args[0]
        res.update({'error' : "Error: %s" % i.args[0]})
        db.close()
        return res

    except sqlite3.ProgrammingError, p:
        print "Error: %s" % p.args[0]
        res.update({'error' : "Error: %s" % p.args[0]})
        db.close()
        return res


    return res


@app.route('/selectTableName', method=['OPTIONS', 'POST'])
@enable_cors
def selectTableName():
    print "Http Request /selectEmp - input :"
    print "==================================="
    inputData = request.json
    print "==================================="

    res = runSQL()

    return res


@app.route('/getRecords', method=['OPTIONS', 'POST'])
@enable_cors
def getRecords():
    print "Http Request /getRecords - input :"
    print "==================================="
    inputData = request.json
    print "==================================="

    db = sqlite3.connect('flysheetDb.db')
    res = {}
    recordList = []
    getTableName = db.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    for ele in getTableName:
        if ele[0] != 'sqlite_sequence':
            per_table = {'table_name': ele[0]}
            string = 'SELECT Count(*) FROM ' + ele[0]
            getRecordNum = db.execute(string).fetchone()[0]
            per_table.update({'record_num': getRecordNum})
            recordList.append(per_table)

    res = {'tables': recordList}

    getViewName = db.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name").fetchall()
    if len(getViewName) != 0:
        viewList = []
        for ele in getViewName:
            if ele[0] != 'sqlite_sequence':
                per_table = {'view_name': ele[0]}
                string = 'SELECT Count(*) FROM ' + ele[0]
                getRecordNum = db.execute(string).fetchone()[0]
                per_table.update({'record_num': getRecordNum})
                viewList.append(per_table)
        res.update({'views': viewList})

    db.commit()
    db.close()

    return res


def getResultTable(queryResult):
    names = [description[0] for description in queryResult.description]
    result_list = []
    for row in queryResult:
        per_row = {i: "" for i in range(len(row))}
        for idx, col in enumerate(row):
            if per_row.has_key(idx):
                per_row[idx] = col
        result_list.append(per_row)
    row_num = len(result_list)
    #print result_list
    result_dict = {'table': result_list,
                   'table_num': row_num,
                   'table_name': names}

    return result_dict


''' Start the server '''
try:
    app.run(host='localhost', port=7000, debug=True, reloader=True)
except KeyboardInterrupt:
    # never reached
    print('exiting...')
