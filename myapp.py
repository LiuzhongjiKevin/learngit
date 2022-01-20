from flask import Flask,render_template,request,session,make_response,redirect,url_for

app = Flask(__name__)

@app.route("/",)
def index():
    if 'user' in session and 'pwd' in session:
        title = session['user']
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route("/login",methods=['POST','GET'])
def login():
    if request.form.get('user') == 'L' and request.form.get('pwd') == '1':
        session['user'] = 'L'
        session['pwd'] = '1'
        return make_response('login in successfully')
    else:
        print('no such user')
        return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('user',None)
    session.pop('pwd',None)
    return redirect(url_for('login'))

app.secret_key =' 1234'
if __name__ == "__main__":
    app.run(debug=True)

