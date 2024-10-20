from flask import *
import jinja2
import Data

app = Flask(__name__) 


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/groceries', methods=['GET', 'POST'])


def get_groceries():
    if request.method == 'POST':
        query = request.form['search']
        data = Data.get_groceries(request.form['search'], request.form['sortBy'])
        return render_template('products.html',action_url="/groceries", data=data,query=query)
    return render_template('products.html', action_url="/groceries")


@app.route('/fashion', methods=['GET', 'POST'])
def get_fashion():
    if request.method == 'POST':
        query = request.form['search']
        data = Data.get_fashion(request.form['search'], request.form['sortBy'])
        return render_template('products.html', action_url="/fashion", data=data,query=query)
    return render_template('products.html')


@app.route('/electronics', methods=['GET','POST'])
def get_electronics():
    if request.method == 'POST':
        query = request.form['search']
        data = Data.get_electronics(request.form['search'], request.form['sortBy'])
        return render_template('products.html', action_url="/electronics", data=data,query=query)
    return render_template('products.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
