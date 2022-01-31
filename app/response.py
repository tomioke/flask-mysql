from flask import jsonify, make_response

# Fungsi menampilkan kondisi ketika datanya berhasil ditampilkan
def success(values, message):
    res = {
        'data': values,
        'message': message
    }
    
    return make_response(jsonify(res)), 200


# Fungsi menampilkan kondisi ketika datanya tidak berhasil ditampilkan
def badRequest(values, message):
    res = {
        'data': values,
        'message': message
    }

    return make_response(jsonify(res)), 400