from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route('/hello')
def hello():
    return "Hello How are you"

@app.route('/getProducts', methods=['GET'])
def get_product():
    response = product_dao.get_all_product(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__=="__main__":
    print("Starting python flask server for grocery management Syatem")
    app.run(port=5000)
    