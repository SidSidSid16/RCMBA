# RCMBA
Remote Controlled Micro:Bit Automobile

## Structure
### car.py
This is the code flashed on to the micro:bit embedded in the car. This code is responsible for the following:

* recieve signals from the remote
* decode signals from the remote
	* signals must be decoded for the following:
		* `throttle` (0 [min] to 100 [max])
		* `steering` (-100 [full left] to 100 [full right])
* use the decoded signals to drive the motors
	* set `speed_left` and `speed_right` according to the decoded signals from the remote: `throttle` and `steering`

### remote.py
This code is flashed on to the micro:bit embedded in the remote. This code is responsible for the following:

* get values from in-built accelerometer
	* tilting left and right for steering
	* litling front and back for acceleration
* add necessary filtering to filter out unwanted accelerometer signals to make sure the controls are smooth
* communicate with the car using the `radio` package


## Optionals
* car can also communicate back to the remote with data such as radio signal strength