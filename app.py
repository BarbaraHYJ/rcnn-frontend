from flask import Flask, redirect, url_for, request, render_template, make_response, abort, jsonify, send_from_directory, Response
from config import *
import os
from werkzeug import secure_filename
import json
import time

app = Flask(__name__)
app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_PATH
app.config['RESULT_DEFAULT_DEST'] = RESULT_PATH
app.config['PROJECT_PATH'] = os.getcwd()
app.config['DEMO_PATH'] = DEMO_PATH

def allow_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
	# if request.method == 'POST':
	# 	file = request.files['file']
	# 	if file and allow_file(file.filename):
	# 		filename = secure_filename(file.filename)
	# 		file.save(os.path.join(app.config['UPLOADS_DEFAULT_DEST'], filename))
	# 		# resu = os.system('python ./mydemo.py --cpu --net zf' + 
	# 		# 	'--pic ' + filename +
	# 		# 	'--path ' + os.path.join(app.config['PROJECT_PATH'] , 'files'))
	# 		# return redirect(url_for('upload_file', origin = filename, result = filename))
	# 		# return render_template('main.html', origin_pic= '/uploads/' + origin, 
	# 		# result_pic = '/results/' + result)
	# 		origin_and_result = {}
	# 		origin_and_result['origin'] = 'uploads/' + filename
	# 		origin_and_result['result'] = 'results/' + filename
	# 		return json.dumps(origin_and_result, ensure_ascii = False)
	# origin = request.args.get('origin')
	# result = request.args.get('result')
	# if origin != '' and origin != None and result != None and result != '':
	# 	return render_template('main.html', origin_pic= '/uploads/' + origin, 
	# 		result_pic = '/results/' + result)
	return render_template('main.html')

@app.route('/post/file', methods=['GET', 'POST'])
def up_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allow_file(file.filename):
			filename = str(int(time.time())) + secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOADS_DEFAULT_DEST'], filename))
			command = 'python ' + app.config['DEMO_PATH'] + '/mydemo.py ' + '--cpu --net zf ' + '--pic ' + filename + ' --path ' + os.path.join(app.config['PROJECT_PATH'] , 'files')
                        print 'command:' + command
                        resu = os.system('python ' + 
				app.config['DEMO_PATH'] + '/mydemo.py ' + 
				' --cpu --net zf ' + 
				' --pic ' + filename +
				' --path ' + os.path.join(app.config['PROJECT_PATH'] , 'files'))
			origin_and_result = {}
			origin_and_result['origin'] = 'uploads/' + filename
			origin_and_result['result'] = 'results/' + filename
			return json.dumps(origin_and_result, ensure_ascii = False)

@app.route('/resultList/<filename>')
def result_list(filename):
	s=['results/' + filename] 
	t = {}  
	t['data'] = s  
	return json.dumps(t, ensure_ascii=False)

@app.route('/uploads/<filename>')
def uploaded_file(filename):	
	return send_from_directory(app.config['UPLOADS_DEFAULT_DEST'], filename)

@app.route('/results/<filename>')
def result_file(filename):
	return send_from_directory(app.config['RESULT_DEFAULT_DEST'], filename)

if __name__ == '__main__':
	app.run()
