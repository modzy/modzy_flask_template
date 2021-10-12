from flask import render_template
from app import app
from app.forms import *
import json, datetime, requests

from modzy import ApiClient
client = ApiClient(base_url=app.config['API_URL'], api_key=app.config['API_KEY'])

@app.route('/', methods=['GET', 'POST'])
@app.route('/sentiment', methods=['GET', 'POST'])
def sentiment():
	form = SentimentAnalysisForm()

	if form.validate_on_submit():
		if form.input_text.data == 'asdf':
			data = {'input-text':form.input_text.data,"classPredictions":[{"class":"neutral","score":0.831},{"class":"negative","score":0.137},{"class":"positive","score":0.032}]} #this example output is used for debugging.
		else:
			data = sentimentanalysis(form.input_text.data)
			data['input-text'] = form.input_text.data
		return render_template('/sentiment.html', form=form, data=data)
	return render_template('/sentiment.html', title='Sentiment Analysis', form=form, data=None)

@app.route('/next')
def index():
	return render_template('index.html')

def sentimentanalysis(input_text):
	job = client.jobs.submit_text('ed542963de', '1.0.1', {'input.txt': input_text})
	result = client.results.block_until_complete(job, timeout=None)
	return (result['results']['job']['results.json']['data']['result'])