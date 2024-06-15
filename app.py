from flask import Flask, render_template, redirect, url_for, flash
from forms import PatientForm, EmergencyForm, ViewMedicalRecordForm, AddMedicalRecordForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/patient', methods=['GET', 'POST'])
def patient():
    form = PatientForm()
    view_form = ViewMedicalRecordForm()
    if view_form.validate_on_submit():
        # Process the form data for viewing medical records
        flash('Viewing medical records', 'success')
        return redirect(url_for('view_medical_record', record_id=view_form.record_id.data))
    return render_template('patient.html', form=form, view_form=view_form)


@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    view_form = ViewMedicalRecordForm()
    add_form = AddMedicalRecordForm()
    if view_form.validate_on_submit():
        # Process the form data for viewing medical records
        flash('Viewing medical records', 'success')
        return redirect(url_for('view_medical_record', record_id=view_form.record_id.data))
    elif add_form.validate_on_submit():
        # Process the form data for adding a medical record
        # In a real application, you would save this data to the database
        flash('Adding medical record', 'success')
        return redirect(url_for('home'))
    return render_template('doctor.html', view_form=view_form, add_form=add_form)


@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    form = EmergencyForm()
    if form.validate_on_submit():
        # Process the form data for viewing patient medical records
        flash('Viewing patient medical records in emergency', 'success')
        return redirect(url_for('view_medical_record', record_id=form.patient_id.data))
    return render_template('emergency.html', form=form)


@app.route('/view_medical_record/<record_id>')
def view_medical_record(record_id):
    # Placeholder for retrieving and displaying the medical record
    medical_record = {"record_id": record_id, "data": "Sample medical record data"}
    return render_template('view_medical_record.html', medical_record=medical_record)


if __name__ == '__main__':
    app.run(debug=True)
