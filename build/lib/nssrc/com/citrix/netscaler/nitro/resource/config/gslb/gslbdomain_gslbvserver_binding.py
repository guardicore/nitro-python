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

class gslbdomain_gslbvserver_binding(base_resource) :
	""" Binding class showing the gslbvserver that can be bound to gslbdomain.
	"""
	def __init__(self) :
		self._vservername = None
		self._servicetype = None
		self._state = None
		self._lbmethod = None
		self._dnsrecordtype = None
		self._backuplbmethod = None
		self._persistencetype = None
		self._edr = None
		self._mir = None
		self._dynamicweight = None
		self._statechangetimesec = None
		self._cip = None
		self._persistenceid = None
		self._netmask = None
		self._v6netmasklen = None
		self._sitename = None
		self._sitepersistence = None
		self._siteprefix = None
		self._customheaders = None
		self._persistmask = None
		self._v6persistmasklen = None
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
	def vservername(self) :
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def sitename(self) :
		r"""Name of the site to which the service belongs.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@property
	def backuplbmethod(self) :
		r"""Indicates the backup method in case the primary fails.<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API.
		"""
		try :
			return self._backuplbmethod
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
	def persistenceid(self) :
		r"""Persistence id of the gslb vserver.
		"""
		try :
			return self._persistenceid
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""The state of the vserver.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@property
	def edr(self) :
		r"""Send clients an empty DNS response when the GSLB virtual server is DOWN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._edr
		except Exception as e:
			raise e

	@property
	def lbmethod(self) :
		r"""The load balancing method set for the virtual server.<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API.
		"""
		try :
			return self._lbmethod
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Indicates if Client IP option is enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		r"""Time since last state change.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Netmask.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@property
	def dnsrecordtype(self) :
		r"""The IP type for this GSLB vserver.<br/>Possible values = A, AAAA, CNAME, NAPTR.
		"""
		try :
			return self._dnsrecordtype
		except Exception as e:
			raise e

	@property
	def persistmask(self) :
		r"""The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.<br/>Minimum length =  1.
		"""
		try :
			return self._persistmask
		except Exception as e:
			raise e

	@property
	def sitepersistence(self) :
		r"""Indicates the type of cookie persistence set.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE.
		"""
		try :
			return self._sitepersistence
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""The type GSLB service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@property
	def v6persistmasklen(self) :
		r"""Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.<br/>Default value: 128<br/>Minimum value =  1<br/>Maximum value =  128.
		"""
		try :
			return self._v6persistmasklen
		except Exception as e:
			raise e

	@property
	def v6netmasklen(self) :
		r"""Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the SOURCEIPHASH load balancing method.<br/>Default value: 128<br/>Minimum value =  1<br/>Maximum value =  128.
		"""
		try :
			return self._v6netmasklen
		except Exception as e:
			raise e

	@property
	def persistencetype(self) :
		r"""Indicates if persistence is set on the gslb vserver.<br/>Possible values = SOURCEIP, NONE.
		"""
		try :
			return self._persistencetype
		except Exception as e:
			raise e

	@property
	def siteprefix(self) :
		r"""The site prefix string.
		"""
		try :
			return self._siteprefix
		except Exception as e:
			raise e

	@property
	def dynamicweight(self) :
		r"""Dynamic weight method of the vserver.<br/>Default value: DISABLED<br/>Possible values = SERVICECOUNT, SERVICEWEIGHT, DISABLED.
		"""
		try :
			return self._dynamicweight
		except Exception as e:
			raise e

	@property
	def mir(self) :
		r""".<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mir
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbdomain_gslbvserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbdomain_gslbvserver_binding
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
		r""" Use this API to fetch gslbdomain_gslbvserver_binding resources.
		"""
		try :
			if not name :
				obj = gslbdomain_gslbvserver_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = gslbdomain_gslbvserver_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of gslbdomain_gslbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbdomain_gslbvserver_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count gslbdomain_gslbvserver_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbdomain_gslbvserver_binding()
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
		r""" Use this API to count the filtered set of gslbdomain_gslbvserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbdomain_gslbvserver_binding()
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

	class Backuplbmethod:
		ROUNDROBIN = "ROUNDROBIN"
		LEASTCONNECTION = "LEASTCONNECTION"
		LEASTRESPONSETIME = "LEASTRESPONSETIME"
		SOURCEIPHASH = "SOURCEIPHASH"
		LEASTBANDWIDTH = "LEASTBANDWIDTH"
		LEASTPACKETS = "LEASTPACKETS"
		STATICPROXIMITY = "STATICPROXIMITY"
		RTT = "RTT"
		CUSTOMLOAD = "CUSTOMLOAD"
		API = "API"

	class State:
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

	class Lbmethod:
		ROUNDROBIN = "ROUNDROBIN"
		LEASTCONNECTION = "LEASTCONNECTION"
		LEASTRESPONSETIME = "LEASTRESPONSETIME"
		SOURCEIPHASH = "SOURCEIPHASH"
		LEASTBANDWIDTH = "LEASTBANDWIDTH"
		LEASTPACKETS = "LEASTPACKETS"
		STATICPROXIMITY = "STATICPROXIMITY"
		RTT = "RTT"
		CUSTOMLOAD = "CUSTOMLOAD"
		API = "API"

	class Edr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Persistencetype:
		SOURCEIP = "SOURCEIP"
		NONE = "NONE"

	class Dynamicweight:
		SERVICECOUNT = "SERVICECOUNT"
		SERVICEWEIGHT = "SERVICEWEIGHT"
		DISABLED = "DISABLED"

	class Dnsrecordtype:
		A = "A"
		AAAA = "AAAA"
		CNAME = "CNAME"
		NAPTR = "NAPTR"

	class Sitepersistence:
		ConnectionProxy = "ConnectionProxy"
		HTTPRedirect = "HTTPRedirect"
		NONE = "NONE"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		RADIUS = "RADIUS"
		RDP = "RDP"
		RTSP = "RTSP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"

	class Mir:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class gslbdomain_gslbvserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbdomain_gslbvserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbdomain_gslbvserver_binding = [gslbdomain_gslbvserver_binding() for _ in range(length)]

