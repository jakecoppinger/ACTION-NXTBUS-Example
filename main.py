from nxtbus import Nxtbus
from stop_monitoring_request import StopMonitoringRequest

from tornado.httpclient import AsyncHTTPClient
import tornado.ioloop

import xmltodict
import json

def handle_request(response):
	if response.error:
	    print("Error:", response.error)
	else:
		# Parse the XML to a native Python dictionary
		jsonData =  xmltodict.parse(response.body)
		# Pretty print as JSON
		print(json.dumps(jsonData, sort_keys=True, indent=4, separators=(',', ': ')))

	# As the request is asynchronous we need this
	tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
	# City bus station platform 1
	busStopID = 3401

	# Bus arrivals up to 90 minutes in future
	previewTime = 90

	apiKey = "APIKEY" # Put your NXTBUS API key here as a string

	requestJSON = StopMonitoringRequest(apiKey,busStopID,previewTime).request()
	nxtbusServer = Nxtbus(apiKey)

	requestXML = nxtbusServer.stopRequestXML(requestJSON)
	requestURL = nxtbusServer.stopRequestURL()
	headers = {"Content-Type":"application/xml" }

	client = AsyncHTTPClient()

	client.fetch(requestURL, method="POST",headers=headers,body=requestXML,callback=handle_request)
	tornado.ioloop.IOLoop.instance().start() 