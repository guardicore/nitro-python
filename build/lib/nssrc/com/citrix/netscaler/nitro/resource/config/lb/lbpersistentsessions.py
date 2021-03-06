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

class lbpersistentsessions(base_resource) :
	""" Configuration for persistence session resource. """
	def __init__(self) :
		self._vserver = None
		self._nodeid = None
		self._persistenceparameter = None
		self._type = None
		self._typestring = None
		self._srcip = None
		self._srcipv6 = None
		self._destip = None
		self._destipv6 = None
		self._flags = None
		self._destport = None
		self._vservername = None
		self._timeout = None
		self._referencecount = None
		self._persistenceparam = None
		self._cnamepersparam = None
		self.___count = None

	@property
	def vserver(self) :
		r"""The name of the virtual server.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""The name of the virtual server.
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def persistenceparameter(self) :
		r"""The persistence parameter whose persistence sessions are to be flushed.
		"""
		try :
			return self._persistenceparameter
		except Exception as e:
			raise e

	@persistenceparameter.setter
	def persistenceparameter(self, persistenceparameter) :
		r"""The persistence parameter whose persistence sessions are to be flushed.
		"""
		try :
			self._persistenceparameter = persistenceparameter
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of Persistence.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def typestring(self) :
		r"""Type of Persistence as String.
		"""
		try :
			return self._typestring
		except Exception as e:
			raise e

	@property
	def srcip(self) :
		r"""SOURCE IP.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@property
	def srcipv6(self) :
		r"""SOURCE IPv6 ADDRESS.
		"""
		try :
			return self._srcipv6
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""DESTINATION IP.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@property
	def destipv6(self) :
		r"""DESTINATION IPv6 ADDRESS.
		"""
		try :
			return self._destipv6
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""IPv6 FLAGS.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Destination port.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		r"""Virtual server name.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Persistent Session timeout.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		r"""Reference Count.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def persistenceparam(self) :
		r"""Specific persistence information . Callid in case of SIP_CALLID persistence entry , RTSP session id in case of RTSP_SESSIONID persistence entry.
		"""
		try :
			return self._persistenceparam
		except Exception as e:
			raise e

	@property
	def cnamepersparam(self) :
		r"""The cname that is selected incase of gslb service.
		"""
		try :
			return self._cnamepersparam
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbpersistentsessions_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbpersistentsessions
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear lbpersistentsessions.
		"""
		try :
			if type(resource) is not list :
				clearresource = lbpersistentsessions()
				clearresource.vserver = resource.vserver
				clearresource.persistenceparameter = resource.persistenceparameter
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ lbpersistentsessions() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].vserver = resource[i].vserver
						clearresources[i].persistenceparameter = resource[i].persistenceparameter
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbpersistentsessions resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbpersistentsessions()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the lbpersistentsessions resources that are configured on netscaler.
	# This uses lbpersistentsessions_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = lbpersistentsessions()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lbpersistentsessions resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbpersistentsessions()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lbpersistentsessions resources configured on NetScaler.
		"""
		try :
			obj = lbpersistentsessions()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of lbpersistentsessions resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbpersistentsessions()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class lbpersistentsessions_response(base_response) :
	def __init__(self, length=1) :
		self.lbpersistentsessions = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbpersistentsessions = [lbpersistentsessions() for _ in range(length)]

