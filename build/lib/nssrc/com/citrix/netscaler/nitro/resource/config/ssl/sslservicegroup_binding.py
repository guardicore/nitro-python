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

class sslservicegroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to sslservicegroup_binding. 
	"""
	def __init__(self) :
		self._servicegroupname = None
		self.sslservicegroup_sslcipher_binding = []
		self.sslservicegroup_ecccurve_binding = []
		self.sslservicegroup_sslcertkey_binding = []
		self.sslservicegroup_sslciphersuite_binding = []

	@property
	def servicegroupname(self) :
		r"""Name of the SSL service group for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the SSL service group for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def sslservicegroup_sslcipher_bindings(self) :
		r"""sslcipher that can be bound to sslservicegroup.
		"""
		try :
			return self._sslservicegroup_sslcipher_binding
		except Exception as e:
			raise e

	@property
	def sslservicegroup_sslciphersuite_bindings(self) :
		r"""sslciphersuite that can be bound to sslservicegroup.
		"""
		try :
			return self._sslservicegroup_sslciphersuite_binding
		except Exception as e:
			raise e

	@property
	def sslservicegroup_ecccurve_bindings(self) :
		r"""ecccurve that can be bound to sslservicegroup.
		"""
		try :
			return self._sslservicegroup_ecccurve_binding
		except Exception as e:
			raise e

	@property
	def sslservicegroup_sslcertkey_bindings(self) :
		r"""sslcertkey that can be bound to sslservicegroup.
		"""
		try :
			return self._sslservicegroup_sslcertkey_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslservicegroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslservicegroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, servicegroupname="", option_="") :
		r""" Use this API to fetch sslservicegroup_binding resource.
		"""
		try :
			if not servicegroupname :
				obj = sslservicegroup_binding()
				response = obj.get_resources(service, option_)
			elif type(servicegroupname) is not list :
				obj = sslservicegroup_binding()
				obj.servicegroupname = servicegroupname
				response = obj.get_resource(service)
			else :
				if servicegroupname and len(servicegroupname) > 0 :
					obj = [sslservicegroup_binding() for _ in range(len(servicegroupname))]
					for i in range(len(servicegroupname)) :
						obj[i].servicegroupname = servicegroupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class sslservicegroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslservicegroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslservicegroup_binding = [sslservicegroup_binding() for _ in range(length)]

