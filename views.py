import matplotlib.pyplot as plt
import base64
from io import BytesIO
from flask import Flask, render_template, request

app = Flask(__name__)

def plot_function(a, b, c, d):
    x = range(-10, 10)
    y = [(a * i + b) / (c * i + d) for i in x]
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + string.decode('utf-8')
    
    return uri

@app.route('/demonstrate/', methods=['GET', 'POST'])
def demonstrate_function():
    image = None
    if request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        d = float(request.form.get('d'))
        image = plot_function(a, b, c, d)
    
    return render_template('demo.html', image=image)

if __name__ == '__main__':
    app.run(debug=True)
