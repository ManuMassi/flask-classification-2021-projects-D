import redis
from flask import render_template
from rq import Connection, Queue
from rq.job import Job

from app import app
from app.forms.histogram_form import HistogramForm
from config import Configuration

config = Configuration()


@app.route('/histograms', methods=['GET', 'POST'])
def histograms():
    """API for:

    qualcosa

    """
    form = HistogramForm()

    if form.validate_on_submit():  # POST
        image_id = form.image.data
        image = form.image

        return render_template("histogram_output_queue.html", image_id=image_id, inImg=image)

    # otherwise, it is a get request and should return the
    # image and model selector
    return render_template('histogram_select.html', form=form)


