from flask import flash, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_bcrypt import Bcrypt
from datetime import datetime

# username = "admin"
# password = "admin"

bcrypt = Bcrypt()

class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    attempt = None
    incident_time = None

    def load(self):
        if 'attempt' not in session:
            self.attempt = session['attempt'] = 4
        else:
            self.attempt = session['attempt']
        flash(f"\nNumber of attempts: {self.attempt}\n")
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
        if self.validate_on_submit():
            hashed_input = bcrypt.generate_password_hash(self.password.data).decode('utf-8')
            if bcrypt.check_password_hash(hashed_input, 'admin') and self.password.data == "admin":
                flash("Successful Login!", 'success')
                return True
            else:
                self.attempt -= 1
                session['attempt'] = self.attempt
                if self.attempt < 1:
                    flash('Too many incorrect logins', 'danger')
                    session['attempt'] = 0
                    if not 'incident_time' in session:
                        session['incident_time'] = datetime.now().timestamp()
                return False