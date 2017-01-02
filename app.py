import flask
from flask_bootstrap import Bootstrap

import astropy.units as u


# add imperial units to list of known units.
from astropy.units import imperial
imperial.enable()

app = flask.Flask(__name__)
Bootstrap(app)


DEFAULT_IN_UNIT = 'mile/hr'
DEFAULT_IN_VALUE = 100
DEFAULT_OUT_UNIT = 'm/s'

@app.route('/')
def index():
    args = flask.request.args
    _input_unit = str(args.get('_input_unit', DEFAULT_IN_UNIT))
    _input_value = float(args.get('_input_value', DEFAULT_IN_VALUE))
    _output_unit = str(args.get('_output_unit', DEFAULT_OUT_UNIT))

    _output_value = u.Quantity(_input_value, _input_unit).to(_output_unit)

    html = flask.render_template(
        'index.html',
        _input_value=_input_value,
        _input_unit=_input_unit,
        _output_value=_output_value,
        _output_unit=_output_unit,
    )
    return html

if __name__ == '__main__':
    print(__doc__)
    app.run(debug=True)
