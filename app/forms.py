from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SentimentAnalysisForm(FlaskForm):
    input_text = StringField('Input Text', validators=[DataRequired()])
    submit = SubmitField('Analyze')
