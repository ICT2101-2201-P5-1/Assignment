from flask import flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_bcrypt import Bcrypt
from datetime import datetime
from .EditLevel import fetchPassword

bcrypt = Bcrypt()


class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    attempt = None
    incident_time = None

    def load(self):
        """
        Function will load website's settings such as the number of attempts and volations is any
        """
        if 'attempt' not in session:
            self.attempt = session['attempt'] = 5
        else:
            self.attempt = session['attempt']
            if self.attempt <= 0:
                self.attempt = 0
        # flash(f"\nNumber of attempts: {self.attempt}\n")
        if 'incident_time' in session:
            self.incident_time = int(session['incident_time'])
            # flash(f"incident time: {int(self.incident_time)}, current_time: {int(datetime.now().timestamp())}, time diff: {int(datetime.now().timestamp()) - int(self.incident_time)}")
            if int(datetime.now().timestamp()) - int(self.incident_time) < 10:
                self.password.render_kw = {'readonly': True}
            else:
                session.pop('incident_time', None)
                self.attempt = session['attempt'] = 5
        else:
            self.incident_time = 0

    def check(self):
        """
        Function will check user input against password fetched from database
        """
        if self.validate_on_submit():
            self.attempt -= 1
            session['attempt'] = self.attempt
            hashed_input = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
            db_pw = str(fetchPassword())[3:-4]
            if bcrypt.check_password_hash(hashed_input, db_pw):
                #flash("Successful Login!", 'success')
                return "Success"
            else:
                if self.attempt < 1:
                    session['attempt'] = 0
                    if not 'incident_time' in session:
                        session['incident_time'] = datetime.now().timestamp()
                    #flash(f'Too many incorrect logins incident"', 'danger')
                    return "Timeout"
                return "Fail"
