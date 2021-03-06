import httplib
import json


class Flow_mod:
	def __init__(self,core,parm):
		self.IP = parm["ip"]
		self.Port = int(parm["port"])
		self.path = "/wm/omniui/add/json"
		self.headers = {
			"Content-type": "application/json",
			"Accept": "application/json",
            	}
		# register rest api
		core.registerRestApi("flowmod", self.flowHandler)

	def flowHandler(self,data):
		# return JSONP format
		body = json.dumps(data.get_json(force=True))
		conn = httplib.HTTPConnection(self.IP, self.Port)
		conn.request("POST", self.path, body, self.headers)
		response = conn.getresponse()
		ret = (response.status, response.reason, response.read())
		ret[0] == 200
		conn.close()
		msg = json.dumps(ret)
		return msg
