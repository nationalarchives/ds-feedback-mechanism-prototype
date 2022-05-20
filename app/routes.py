from app import app
from app.content_managed_content.content import content
from app.forms.server_rendered_form import ServerRenderedForm
from flask import render_template, request, redirect, url_for


@app.route('/')
def home():
    form = ServerRenderedForm()

    submission = request.args.get('submission')

    return render_template(
        'originating_page.html',
        content=content,
        form=form,
        submission=submission
    )


@app.route('/process_feedback')
def process_feedback():
    # Set this variable to True or False to represent success or failure states
    processed_successfully = True

    if processed_successfully:
        return redirect(f'{url_for("home")}?submission=success#feedback-mechanism-processed-message')
    else:
        return redirect(f'{url_for("home")}?submission=failure#feedback-mechanism-processed-message')

