from flask import Flask, render_template, redirect, url_for, flash
from forms import PatientForm, DoctorForm, EmergencyForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/patient', methods=['GET', 'POST'])
def patient():
    form = PatientForm()
    if form.validate_on_submit():
        # Process the form data
        flash('Patient form submitted successfully', 'success')
        return redirect(url_for('home'))
    return render_template('patient.html', form=form)


@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    form = DoctorForm()
    if form.validate_on_submit():
        # Process the form data
        flash('Doctor form submitted successfully', 'success')
        return redirect(url_for('home'))
    return render_template('doctor.html', form=form)


@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    form = EmergencyForm()
    if form.validate_on_submit():
        # Process the form data
        flash('Emergency form submitted successfully', 'success')
        return redirect(url_for('home'))
    return render_template('emergency.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
