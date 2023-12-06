# from flask import Flask, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# mydb = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     password = '09041997',
#     database = 'flask_curd'
# )
# mycursor = mydb.cursor()

# @app.route('/')
# def home():
#     return jsonify("Welcome")

# @app.route('/users', methods = ['POST'])
# def create_user():
#     data = request.json
#     username = data['username']
#     email = data['email']

#     query = "insert into users (username, email) values (%s, %s)"
#     values = (username, email)
#     mycursor.execute(query, values)
#     mydb.commit()

#     return jsonify({'message':'User Created Successfully'})

# @app.route('/get_users', methods = ['GET'])
# def get_users():
#     query = "select * from users"
#     mycursor.execute(query)
#     result = mycursor.fetchall()
#     users = [{'id': row[0], 'username': row[1], 'email': row[2]} for row in result]

#     return jsonify(users)

# @app.route('/get_user/<string:username>', methods = ['GET'])
# def get_user_by_username(username):
#     # username = request.args.get('username')
#     if username:
#         query = "select * from users where username = %s"
#         mycursor.execute(query, (username,))
#         result = mycursor.fetchall()
#         if result:
#             user = [{'id': row[0], 'username': row[1], 'email': row[2]} for row in result]
#             return jsonify(user)
#         else:
#             return jsonify("User not found")
#     return jsonify('username not provided')


# @app.route('/update_user/<int:id>',methods=['PUT'])
# def update_user(id):
#     data = request.json
#     username = data['username']
#     email = data['email']

#     query = "update users set username=%s, email=%s where id=%s"
#     values = (username, email, id)
#     mycursor.execute(query, values)
#     mydb.commit()
#     return jsonify({'message':'user updated succesfully'})

# @app.route('/delete_user/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     query = "delete from users where id=%s"
#     values = (id,)
#     mycursor.execute(query,values)
#     mydb.commit()

#     return jsonify({'message':'user deleted successfully'})


# if __name__ == "__main__":
#     app.run(debug = True)

from sklearn.preprocessing import MinMaxScaler

scaler_x = MinMaxScaler()
X_scaled = scaler_x.fit_transform(X)
