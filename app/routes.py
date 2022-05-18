from app import app
from app.content_managed_content.content import content
from app.forms.server_rendered_form import ServerRenderedForm
from flask import render_template, request


@app.route('/')
def home():

    form = ServerRenderedForm()

    return render_template(
        'home.html',
        content=content,
        form=form,
        current_page_url='Chicken soup'
    )

@app.route('/process_feedback')
def process_feedback():

    return request.args