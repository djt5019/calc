#!/usr/bin/env python


import flask
from calc import sales_discount
app = flask.Flask(__name__)


def _input(name, value=None):
    if value:
        return '<input name={name} placeholder={name} value={value} />'.format(
            name=name, value=value
        )

    else:
        return '<input name={name} placeholder={name} />'.format(
            name=name
        )

def unit_price_input(value=None):
    return _input("unit-price", value)


def quantity_input(value=None):
    return _input('quantity', value)

def state_input(value=None):
    return _input("state", value)

def total_price(amt=0):
    return "<span>{}</span>".format(amt)

@app.route('/calc', methods=['GET', 'POST'])
def calculate_sales_tax():
    request = flask.request

    inputs = [
        unit_price_input(),
        quantity_input(),
        state_input()
    ]

    form = "\n".join(inputs)
    total = 0

    if flask.request.method == 'POST':
        import pprint
        pp = pprint.PrettyPrinter()
        pp.pprint(flask.request.form)
        unit_price = float(flask.request.form['unit-price'])
        state = flask.request.form['state']
        qty = int(flask.request.form['quantity'])

        inputs = [
            unit_price_input(unit_price),
            quantity_input(qty),
            state_input(state)
        ]
        form = "\n".join(inputs)

        total = sales_discount(qty, unit_price, state)

    templ = """
        <html>
        <body>
        <form method="POST">
            {}
            <input type="submit" name="submit" />
        </form>
        <p>
            {}
        </p>
        </body>
        </html>
        """.format(form, total_price(total))

    return templ




if __name__ == '__main__':
    app.run(debug=True)
