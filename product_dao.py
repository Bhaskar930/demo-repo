from sqlconnection import get_sql_connection
import mysql.connector

def get_all_product(connection):
    cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='gs')
    cursor=cnx.cursor()
    query='''SELECT product.product_id, product.product_name, product.um_id, product.price_per_unit, uom.um_name FROM gs.product
    INNER JOIN gs.uom ON product.um_id = uom.um_id'''
    cursor.execute(query)
    response=[]
    for(product_id,product_name,um_id,price_per_unit,uom_name) in cursor:
        response.append(
            {
                'product_id':product_id,
                'name':product_name,
                'uom_id':um_id,
                'price_per_unit':price_per_unit,
                'uom_name':uom_name
            }

        )
    
    
    
    # print(product_id,prosuctname,price_per_unit ,uom_name)
    cnx.close()
    return response
def insert_new_product(connection,product):
    cursor=connection.cursor()
    query=('''insert into product(product_name,um_id,Price_per_unit) values(%s,%s,%s)''')
    data=(product['product_name'],product['um_id'],product['Price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    cursor.lastrowid
def delete_product(connection, product_id):
    if connection is None:
        print("Connection object is None")
        return None

    cursor = connection.cursor()
    query = '''DELETE FROM product WHERE product_id=%s'''
    cursor.execute(query, (product_id,))
    connection.commit()
    cursor.close()
    return cursor.rowcount

if __name__ == '__main__':
    connection=get_sql_connection()
    print(get_all_product(connection))
    print(insert_new_product(connection,{
        'product_name':'cabbage',
        'um_id':'1',
        'Price_per_unit':'30'
    }))
    delete_product(connection,12)
   
    