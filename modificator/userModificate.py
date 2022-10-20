from flask import Flask, request, jsonify
# from database.connect import connect

def SignUp():
    try:
        req = request.json
        if req["FIO"] == "" and req["bg"] == "" and req["organ"] == "":
            return jsonify({"False": "Нечего не введенно"})
        else:
           return jsonify({"True": req}) 
    except:
        return jsonify({"False": "Таких данных нет"})

def SignIn():
    try:
        req = request.json
        if req["FIO"] == "" and req["bg"] == "" and req["organ"] == "":
            return jsonify({"False": "Нечего не введенно"})
        else:
           return jsonify({"True": req}) 
    except:
        return jsonify({"False": "Таких данных нет"})

def infoToken():
    pass
    