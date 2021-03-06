from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, RadioField
from wtforms.validators import DataRequired
from app.content_managed_content.content import content


class ServerRenderedForm(FlaskForm):
    ratings = RadioField(
        u'Label',
        choices=content['ratings'],
        validators=[DataRequired()]
    )

    comment = TextAreaField(
        content['comment_field_label'],
        render_kw={
            'aria-describedby': 'comment-helper-text',
            'class': 'feedback-mechanism__comment-field'
        }
    )
