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

class lbvserver_servicegroupmember_binding(base_resource) :
	""" Binding class showing the servicegroupmember that can be bound to lbvserver.
	"""
	def __init__(self) :
		self._servicegroupname = None
		self._ipv46 = None
		self._port = None
		self._servicetype = None
		self._curstate = None
		self._weight = None
		self._dynamicweight = None
		self._cookieipport = None
		self._cookiename = None
		self._vserverid = None
		self._preferredlocation = None
		self._name = None
		self.___count = None

	@property
	def servicegroupname(self) :
		r"""The service group name bound to the selected load balancing virtual server.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""The service group name bound to the selected load balancing virtual server.
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver'). .<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the specified service.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the specified service.<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def cookieipport(self) :
		r"""Encryped Ip address and port of the service that is inserted into the set-cookie http header.
		"""
		try :
			return self._cookieipport
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number for the virtual server.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""Current LB vserver state.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def preferredlocation(self) :
		r"""Used for displaying the location of bound services.
		"""
		try :
			return self._preferredlocation
		except Exception as e:
			raise e

	@property
	def vserverid(self) :
		r"""Vserver Id.
		"""
		try :
			return self._vserverid
		except Exception as e:
			raise e

	@property
	def ipv46(self) :
		r"""IPv4 or IPv6 address to assign to the virtual server.
		"""
		try :
			return self._ipv46
		except Exception as e:
			raise e

	@property
	def cookiename(self) :
		r"""Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
		"""
		try :
			return self._cookiename
		except Exception as e:
			raise e

	@property
	def dynamicweight(self) :
		r"""Dynamic weight.
		"""
		try :
			return self._dynamicweight
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol used by the service (also called the service type).<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, DNS, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, RTSP, PUSH, SSL_PUSH, RADIUS, RDP, MYSQL, MSSQL, DIAMETER, SSL_DIAMETER, TFTP, ORACLE, SMPP, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, PROXY, USER_TCP, USER_SSL_TCP, QUIC, IPFIX, LOGSTREAM, MONGO, MONGO_TLS, MQTT, MQTT_TLS, QUIC_BRIDGE, HTTP_QUIC.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbvserver_servicegroupmember_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbvserver_servicegroupmember_binding
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
		r""" Use this API to fetch lbvserver_servicegroupmember_binding resources.
		"""
		try :
			if not name :
				obj = lbvserver_servicegroupmember_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = lbvserver_servicegroupmember_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of lbvserver_servicegroupmember_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver_servicegroupmember_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count lbvserver_servicegroupmember_binding resources configued on NetScaler.
		"""
		try :
			obj = lbvserver_servicegroupmember_binding()
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
		r""" Use this API to count the filtered set of lbvserver_servicegroupmember_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbvserver_servicegroupmember_binding()
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

	class Curstate:
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

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		MQTT_JUMBO_REQ = "MQTT_JUMBO_REQ"

	class Labeltype:
		reqvserver = "reqvserver"
		resvserver = "resvserver"
		policylabel = "policylabel"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		DTLS = "DTLS"
		NNTP = "NNTP"
		DNS = "DNS"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		DNS_TCP = "DNS_TCP"
		RTSP = "RTSP"
		PUSH = "PUSH"
		SSL_PUSH = "SSL_PUSH"
		RADIUS = "RADIUS"
		RDP = "RDP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		ORACLE = "ORACLE"
		SMPP = "SMPP"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		SSL_FIX = "SSL_FIX"
		PROXY = "PROXY"
		USER_TCP = "USER_TCP"
		USER_SSL_TCP = "USER_SSL_TCP"
		QUIC = "QUIC"
		IPFIX = "IPFIX"
		LOGSTREAM = "LOGSTREAM"
		MONGO = "MONGO"
		MONGO_TLS = "MONGO_TLS"
		MQTT = "MQTT"
		MQTT_TLS = "MQTT_TLS"
		QUIC_BRIDGE = "QUIC_BRIDGE"
		HTTP_QUIC = "HTTP_QUIC"

class lbvserver_servicegroupmember_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lbvserver_servicegroupmember_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbvserver_servicegroupmember_binding = [lbvserver_servicegroupmember_binding() for _ in range(length)]

