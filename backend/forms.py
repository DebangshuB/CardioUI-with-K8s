from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SubmitField, FloatField
from wtforms.validators import DataRequired,NumberRange,InputRequired


class Strokedata(FlaskForm):
    sex = RadioField('Sex', choices=[('2', 'Male'), ('1', 'Female')],validators=[InputRequired()])

    age = IntegerField('Age (yrs)',validators=[DataRequired(),NumberRange(min=1,max=100,message="Invalid Input")])

    height = FloatField('Height (cm)',validators=[DataRequired(),NumberRange(min=1,max=300,message="Invalid Input")])

    weight = FloatField('Weight (kg)',validators=[DataRequired(),NumberRange(min=1,max=500,message="Invalid Input")])

    systolic_blood_pressure = FloatField('Systolic BP',validators=[DataRequired(),NumberRange(min=80,max=150,message="Invalid Input")])

    diastolic_blood_pressure = FloatField('Diastolic BP',validators=[DataRequired(),NumberRange(min=1,max=100,message="Invalid Input")])

    cholestrol = RadioField('Cholestrol level', choices=[('1', 'Normal'), (
        '2', 'Above Normal'), ('3', 'Well Above Normal')], validators=[InputRequired()], default=1)
        
    gluc_level = RadioField('Glucose level', choices=[('1', 'Normal'), ('2', 'Above Normal'), (
        '3', 'Well Above Normal')], validators=[InputRequired()], default=1)
        
    alcohol = RadioField('Do you drink alcohol ?', choices=[
                         ('1', 'Yes'), ('0', 'No')], validators=[InputRequired()], default=0)
        
    active = RadioField('Are you physically active ?', choices=[
                        ('1', 'Active'), ('0', 'Not Active')], validators=[InputRequired()], default=1)
        
    smoking_Status = RadioField('Do you smoke ?', choices=[(
        '1', 'Yes'), ('0', 'No')], validators=[InputRequired()], default=0)
        
    submit = SubmitField('Submit')
