import flask
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8

app = flask.Flask(__name__)

@app.route('/')
def hello():
    x = list(range(1, 100))
    fig = figure(title="Polynomial")
    fig.line(x, [i ** 2 for i in x], color="Red", line_width=2)

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    html = flask.render_template(
        'index.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)

if __name__ == '__main__':
    print(__doc__)
    app.run()
