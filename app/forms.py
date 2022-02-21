from flask_wtf import FlaskForm
from wtforms import *
from flask_wtf.file import FileRequired,FileAllowed


class UploadForm(FlaskForm):

    picture = FileField('Images',validators=[FileRequired(),FileAllowed(['jpg','png'],'Images')])

