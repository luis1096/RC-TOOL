from multiprocessing import allow_connection_pickling
from flask import abort, jsonify, request, make_response, render_template, current_app as app 
from tools import skr_mini
from threading import Timer

@app.route('/test', methods=['GET'])
def test():
	print('I have hit our get test')
	x =  { "name1": "John", 
		   "age1": 30, 
		   "city1": "Florida",
		   "name2": "Luis", 
		   "age2": 12, 
		   "city2": "New York",
		    "name3": "Emily", 
		   "age3": 90, 
		   "city3": "Canada"
		   }
	 
	return  x

@app.route('/post-test', methods=['POST'])
def testPost():
	print('I have hit our postTest')
	received_data = request.get_json()
	print(f"received data: {received_data}")
	
	message = received_data
	return_data = {
		"status": "success",
		"message": f"received: {message}"
    }

	return return_data
	
@app.route('/temperature', methods=['POST'])
def set_temperature():
	raw_data = request.get_json(force=True)
	temp = raw_data['temperature']
	flag = raw_data['waitFlag']

	temp_set = skr_mini.send_temperature(temp) if flag == False else skr_mini.send_temperature_and_wait(temp)
	print(temp_set)

	res = {}
	if temp_set == '':
		res['message'] = 'Error: Could not set temperature'
		abort(400)
	else:
		res['message'] = 'Success'

	return res

@app.route('/temperature', methods=['GET'])
def get_temperature():
	temp = skr_mini.check_temperature()

	res = {}
	if temp != None:
		res['message'] = temp
	else:
		res['message'] = 'Error in reading temperature'

	return res

# This should be tested
@app.route('/auto-temperature', methods=['POST'])
def auto_temperature():
	raw_data = request.get_json(force=True)
	interval = raw_data['interval']

	response = skr_mini.auto_check_temperature(interval)

	res = {}
	if response != None:
		res['message'] = response
	else:
		res['message'] = 'Error in reading temperature'

	return res

@app.route('/fans', methods=['POST'])
def set_fan():
	raw_data = request.get_json(force=True)
	speed = raw_data['speed']

	response = skr_mini.set_fan(speed)
	print(response)

	res = {}
	if response == '':
		res['message'] = 'Error: Could not set fan to specified speed'
		abort(400)
	else:
		res['message'] = 'Success'

	return res

@app.route('/extrusion', methods=['POST'])
def set_extrusion():
	raw_data = request.get_json(force=True)
	mm = raw_data['milimeters']
	# rate is extrusion feed rate in mm/min
	rate = raw_data['rate']
	rate = rate if rate != 0 else 1500

	response = skr_mini.send_extrusion(mm, rate)

	print(response)

	res = {}
	if response == '':
		res['message'] = 'Error: Could not set extrusion'
		abort(400)
	else:
		res['message'] = 'Success'

	return res

@app.route('/home-extruder', methods=['POST'])
def extruder_homing():
	response = skr_mini.home_extruder()
	print(response)

	res = {}
	if response != None:
		res['message'] = response
	else:
		res['message'] = 'Error in homing the extruder'

	return res

# Acts as a "continue on" hint for the printer if it is looping or waiting on some condition
@app.route('/break', methods=['POST'])
def stop_waits():
	response = skr_mini.break_and_continue()

	res = {}
	if response != None:
		res['message'] = response
	else:
		res['message'] = 'Error in breaking out of printer blocking or looping'

	return res

# Option for enabling/disabling hotend temperature checking or setting a minimum extrusion temperature
@app.route('/cold-extrusion', methods=['POST'])
def set_cold_extrusion():
	raw_data = request.get_json(force=True)
	flag = raw_data['enable']
	minTemp = raw_data['min_temperature']

	response = skr_mini.cold_extrude(flag, minTemp)
	print(response)

	res = {}
	if response != None:
		res['message'] = response
	else:
		res['message'] = 'Error in setting cold extrusion configuration'

	return res

# Getting current hotend temperature checking configuration
@app.route('/cold-extrusion', methods=['GET'])
def get_cold_extrusion():
	response = skr_mini.cold_extrude_status()
	print(response)

	res = {}
	if response != None:
		res['message'] = response
	else:
		res['message'] = 'Error in getting cold extrusion configuration'

	return res

@app.route('/general', methods=['POST'])
def send_gcode():
	raw_data = request.get_json(force=True)
	print(f"received data: {raw_data}")
	gcode = raw_data['gcode']
	response = skr_mini.send_general_gcode(gcode)

	res = {}
	if response == '':
		res['message'] = 'Error: Could not execute gcode'
		abort(400)
	else:
		res['message'] = 'Response: ' + response

	return res