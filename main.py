from app import app

from flask import render_template, request, redirect, session, flash, url_for
from forms import RegForm, LoginForm
from db_handle import db_cmp_passwd, db_add_user


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    login = request.form['username']
    password = request.form['password']
    if db_cmp_passwd(login, password):
        session['log_in'] = True
    else:
        flash('Неправильный пароль')
    return render_template('register2.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == "POST" and form.validate():
        login = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        secondname = request.form['secondname']
        bday = request.form['bday']
        sex = request.form['sex']
        hobbys = request.form['hobbys']
        social_link = request.form['social_link']
        flash('Test Flash')

        if db_cmp_passwd(login, password):
            db_add_user(login, password, firstname, secondname, bday, sex, hobbys, social_link)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    session['log_in'] = False
    redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)


