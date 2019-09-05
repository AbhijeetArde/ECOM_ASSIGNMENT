from flask import Flask, render_template
from google.cloud import datastore
app = Flask(__name__)

client = datastore.Client()
key = client.key('IKEACustomer', 1234)
entity = datastore.Entity(key=key)
entity.update({
    'customer_name': u'Abhijeet',
    'customer_id': 1337,
})
client.put(entity)



@app.route('/')
def root():
    customer = client.query(kind='IKEACustomer')
    employee = client.query(kind='IKEAEmployee')
    dummy_cust = list(customer.fetch())
    print(dummy_cust)
    dummy_emp = list(employee.fetch())
    print(dummy_emp)


    return render_template('index.html', customer=dummy_cust, employee=dummy_emp)






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
