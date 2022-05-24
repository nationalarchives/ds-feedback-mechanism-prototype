from app import app
from app.content_managed_content.content import content
from app.forms.server_rendered_form import ServerRenderedForm
from flask import render_template, request, redirect, url_for
import random, time


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
    processed_successfully = random.choice([True, False])

    if processed_successfully:
        return redirect(f'{url_for("home")}?submission=success#feedback-mechanism-processed-message')
    else:
        return redirect(f'{url_for("home")}?submission=failure#feedback-mechanism-processed-message')


@app.route('/get-banner-content')
def get_banner_content():

    return {
        'title': content['ratings_legend'],
        'rating_labels': content['ratings'],
        'comment_field_label': content['comment_field_label'],
        'comment_field_helper_text': content['comment_field_helper_text'],
        'submit_button_text': content['submit_button_text']
    }
