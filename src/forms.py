from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField,IntegerField
from wtforms.validators import NumberRange,InputRequired

class PostForm(FlaskForm):
    image = FileField(
        label='Input image: ',
        _name= 'imgInput',
        validators=[
            InputRequired(),
            FileAllowed(['jpg', 'png','jpeg'])
        ]
    )
    rate = IntegerField(
        'Image compression rate: ', 
    	validators = [
            InputRequired(),
            NumberRange(min=1, max=100)
        ]
    )
    submit = SubmitField('Submit')
