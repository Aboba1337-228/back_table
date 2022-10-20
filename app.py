from flask import Flask, request, jsonify
from modificator.userModificate import SignUp, SignIn, infoToken
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# route user
app.add_url_rule('/user/singup', view_func=SignUp, methods=['POST'])
app.add_url_rule('/user/singin', view_func=SignIn, methods=['POST'])
app.add_url_rule('/user/infoToken', view_func=infoToken, methods=['POST'])

if __name__ == "__main__":
    app.run()