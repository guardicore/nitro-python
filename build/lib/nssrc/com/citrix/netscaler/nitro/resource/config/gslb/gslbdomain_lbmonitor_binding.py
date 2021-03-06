#
# Copyright (c) 2021 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class gslbdomain_lbmonitor_binding(base_resource) :
	""" Binding class showing the lbmonitor that can be bound to gslbdomain.
	"""
	def __init__(self) :
		self._monitorname = None
		self._servicename = None
		self._vservername = None
		self._monstate = None
		self._httprequest = None
		self._iptunnel = None
		self._customheaders = None
		self._respcode = None
		self._monitortotalprobes = None
		self._monitortotalfailedprobes = None
		self._monitorcurrentfailedprobes = None
		self._responsetime = None
		self._monstatcode = None
		self._lastresponse = None
		self._name = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the Domain.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the Domain.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def monitorname(self) :
		r"""Monitor name.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		r"""Monitor name.
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def lastresponse(self) :
		r"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
		except Exception as e:
			raise e

	@property
	def customheaders(self) :
		r"""The string that is sent to the service. Applicable to HTTP ,HTTP-ECV and RTSP monitor types.
		"""
		try :
			return self._customheaders
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		r"""The state of the monitor for tunneled devices.<br/>Possible values = YES, NO.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""The service name.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def monitortotalprobes(self) :
		r"""Total monitor probes.
		"""
		try :
			return self._monitortotalprobes
		except Exception as e:
			raise e

	@property
	def respcode(self) :
		r"""The response codes.
		"""
		try :
			return self._respcode
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		try :
			return self._vservername
		except Exception as e:
			raise e

	@property
	def httprequest(self) :
		r"""HTTP request to the backend server.
		"""
		try :
			return self._httprequest
		except Exception as e:
			raise e

	@property
	def responsetime(self) :
		r"""Response time of this monitor.
		"""
		try :
			return self._responsetime
		except Exception as e:
			raise e

	@property
	def monitortotalfailedprobes(self) :
		r"""Total probes failed.
		"""
		try :
			return self._monitortotalfailedprobes
		except Exception as e:
			raise e

	@property
	def monitorcurrentfailedprobes(self) :
		r"""Total number of current failed probes.
		"""
		try :
			return self._monitorcurrentfailedprobes
		except Exception as e:
			raise e

	@property
	def monstate(self) :
		r"""Monitor state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._monstate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbdomain_lbmonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbdomain_lbmonitor_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch gslbdomain_lbmonitor_binding resources.
		"""
		try :
			if not name :
				obj = gslbdomain_lbmonitor_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = gslbdomain_lbmonitor_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of gslbdomain_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbdomain_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count gslbdomain_lbmonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbdomain_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of gslbdomain_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbdomain_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Iptunnel:
		YES = "YES"
		NO = "NO"

	class Monstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

class gslbdomain_lbmonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbdomain_lbmonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbdomain_lbmonitor_binding = [gslbdomain_lbmonitor_binding() for _ in range(length)]

