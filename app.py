from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('strona_główna.html')

@app.route('/projekt')
def project():
    return render_template('projekt.html')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    image = None
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            d = float(request.form['d'])
            x = range(-10, 11)
            y = [(a * xi + b) / (c * xi + d) for xi in x]
            plt.figure()
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('Wykres funkcji wymiernej')
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            image = base64.b64encode(img.getvalue()).decode()
        except:
            pass
    return render_template('demo.html', image=image)

@app.route('/autorzy')
def authors():
    return render_template('autorzy.html')

@app.route('/Wprowadzenie')
def introduction():
    return render_template('Wprowadzenie''.html')

@app.route('/proporcjonalność')
def inverse_proportion():
    return render_template('proporcjonalność.html')

@app.route('/Wykres_proporcjonalności')
def inverse_proportion_plot():
    return render_template('Wykres_proporcjonalności.html')

@app.route('/funkcja_homograficzna')
def homographic_function():
    return render_template('funkcja_homograficzna.html')

@app.route('/definicja')
def definition():
    return render_template('definicja.html')

@app.route('/dziedzina')
def domain():
    return render_template('dziedzina.html')

@app.route('/równania')
def equations():
    return render_template('równania.html')

@app.route('/nierówności')
def inequalities():
    return render_template('nierówności.html')

if __name__ == '__main__':
    app.run(debug=True)
