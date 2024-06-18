from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project')
def project():
    return render_template('project.html')


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


@app.route('/authors')
def authors():
    return render_template('authors.html')


@app.route('/introduction')
def introduction():
    return render_template('introduction.html')


@app.route('/inverse_proportion')
def inverse_proportion():
    return render_template('inverse_proportion.html')


@app.route('/inverse_proportion_plot')
def inverse_proportion_plot():
    return render_template('inverse_proportion_plot.html')


@app.route('/homographic_function')
def homographic_function():
    return render_template('homographic_function.html')


@app.route('/definition')
def definition():
    return render_template('definition.html')


@app.route('/domain')
def domain():
    return render_template('domain.html')


@app.route('/equations')
def equations():
    return render_template('equations.html')


@app.route('/inequalities')
def inequalities():
    return render_template('inequalities.html')


if __name__ == '__main__':
    app.run(debug=True)
