from flask import Flask, app, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = "counter key"

@app.route('/')
def first():
    if 'visit' in session:
        session['visit'] = session['visit'] + 1
    else:
        session['visit'] = 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.pop('visit')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)