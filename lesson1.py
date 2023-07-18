from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/python_req1', methods=['GET', 'POST'])
def python_req1():

    if request.method == 'GET':

        model = request.args.get('model')
        title = request.args.get('title')
        price = int(request.form.get('price'))
        sunroof = request.form.get('sunroof')

        result = {
            'model': model,
            'title': title,
            'price': price,
            'sunroof': sunroof
        }

    elif request.method == 'POST':

        model = request.form.get('model')
        title = request.form.get('title')
        price = int(request.form.get('price')) + 11000
        sunroof = request.form.get('sunroof')

        result = {
            'model': model,
            'title': title,
            'price': price,
            'sunroof': sunroof
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
