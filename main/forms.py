from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from main.models import Projects


class ProjectForm(FlaskForm):
    project_name = StringField('Project Name', validators = [
        DataRequired(), Length(min=2, max=50)
    ])
    version = StringField('Version', validators = [
        DataRequired(), Length(min=2, max=25)
    ])
    language = StringField('Language')
    dependency = StringField('Dependency')
    script = StringField('Script')
    markup = StringField('Markup')
    style = StringField('Style')
    github = StringField('Repository', validators = [
        DataRequired(), Length(min=2, max=50)
    ])
    programming_lang = StringField('Programming Language', validators = [
        DataRequired()
    ])
    submit = SubmitField('Add')


