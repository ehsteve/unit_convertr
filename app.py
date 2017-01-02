import flask
import astropy.units as u
app = flask.Flask(__name__)

@app.route('/')
def index():
    args = flask.request.args
    _input_unit = str(args.get('_input_unit', 'W/m ** 2'))
    _input_value = float(args.get('_input_value', 50.0))
    _output_unit = str(args.get('_output_unit', 'erg/s/cm ** 2'))

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
