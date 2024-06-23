import matplotlib
matplotlib.use('Agg')
from flask import Flask, render_template, request
import numpy as np
from views import app as views_app
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def plot_function(a, b, c, d):
    x = np.linspace(-10, 10, 400)
    y = (a * x + b) / (c * x + d)
   
    
    fig, ax = plt.subplots()

    # Definiowanie asymptoty
    vertical_asymptote_x = -d / c

    left_mask = x < vertical_asymptote_x
    right_mask = x > vertical_asymptote_x

    ax.plot(x[left_mask], y[left_mask], label=f'({a}x + {b}) / ({c}x + {d}) po lewej')
    ax.plot(x[right_mask], y[right_mask], label=f'({a}x + {b}) / ({c}x + {d}) po prawej')

    
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    

    if c != 0:
        asymptote_x = -d / c
        ax.axvline(asymptote_x, color='red', linestyle='--', label=f'x = {-d/c:.2f}')
    if a != 0:
        asymptote_y = a / c
        ax.axhline(asymptote_y, color='blue', linestyle='--', label=f'y = {a/c:.2f}')
    

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + string.decode('utf-8')
    
    return uri

@app.route('/', methods=['GET', 'POST'])
def demonstrate_function():
    image = None
    if request.method == 'POST':
        try:
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
            d = float(request.form.get('d'))
            image = plot_function(a, b, c, d)
        except Exception as e:
            print(f"Error: {e}")
    
    return render_template('demo.html', image=image)

@app.route('/')
def index():
    return render_template('strona_główna.html')


@app.route('/project')
def project():
    return render_template('projekt.html')


@app.route('/authors')
def authors():
    return render_template('autorzy.html')


@app.route('/introduction')
def introduction():
    return render_template('wprowadzenie.html')


@app.route('/inverse_proportion')
def inverse_proportion():
    return render_template('proporcjonalność.html')


@app.route('/inverse_proportion_plot')
def inverse_proportion_plot():
    return render_template('wykres_proporcjonalności.html')


@app.route('/homographic_function')
def homographic_function():
    return render_template('funkcja_homograficzna.html')


@app.route('/definition')
def definition():
    return render_template('definicja.html')


@app.route('/domain')
def domain():
    return render_template('dziedzina.html')


@app.route('/equations')
def equations():
    return render_template('równania.html')


@app.route('/inequalities')
def inequalities():
    return render_template('nierówności.html')


if __name__ == '__main__':
    app.run(debug=True)
