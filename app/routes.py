from flask import render_template
from flask import request
from app import app
from app.forms import UploadForm

@app.route('/', methods=['GET', 'POST'])
def index():
	form = UploadForm()
	if request.method == 'POST' and form.validate_on_submit():
		input_file = request.files['input_file']
		print("HALLO")
	else:
		return render_template('index.html', title='Home', form=form)