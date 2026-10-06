from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flaskapp<=>routing"

@app.route('/greet/<uname>')
def greet(uname):
    return f"Good Morning, {uname}!"

@app.route('/delete/<int:roll>')
def delete_user(roll):
    # Dynamically passes 'uname' to the 'greet' view function
    return redirect(url_for('greet', uname=f"User_{roll}"))

@app.route('/calculate', methods=['GET', 'POST'])
def si():
    if request.method == 'POST':
        # Using .get() prevents KeyError if the form field is missing
        P = float(request.form.get('p', 0))
        T = float(request.form.get('t', 0))
        R = float(request.form.get('r', 0))
        
        result = (P * T * R) / 100
        total = P + result
        
        return render_template('index.html', result=result, total=total, p=P, t=T, r=R)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=3500)

      
