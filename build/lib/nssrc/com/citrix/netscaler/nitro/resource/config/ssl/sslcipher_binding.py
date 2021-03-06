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

class sslcipher_binding(base_resource):
	""" Binding class showing the resources that can be bound to sslcipher_binding. 
	"""
	def __init__(self) :
		self._ciphergroupname = None
		self.sslcipher_sslprofile_binding = []
		self.sslcipher_individualcipher_binding = []
		self.sslcipher_sslciphersuite_binding = []

	@property
	def ciphergroupname(self) :
		r"""Name of the cipher group for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._ciphergroupname
		except Exception as e:
			raise e

	@ciphergroupname.setter
	def ciphergroupname(self, ciphergroupname) :
		r"""Name of the cipher group for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._ciphergroupname = ciphergroupname
		except Exception as e:
			raise e

	@property
	def sslcipher_sslciphersuite_bindings(self) :
		r"""sslciphersuite that can be bound to sslcipher.
		"""
		try :
			return self._sslcipher_sslciphersuite_binding
		except Exception as e:
			raise e

	@property
	def sslcipher_individualcipher_bindings(self) :
		r"""individualcipher that can be bound to sslcipher.
		"""
		try :
			return self._sslcipher_individualcipher_binding
		except Exception as e:
			raise e

	@property
	def sslcipher_sslprofile_bindings(self) :
		r"""sslprofile that can be bound to sslcipher.
		"""
		try :
			return self._sslcipher_sslprofile_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcipher_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcipher_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ciphergroupname is not None :
				return str(self.ciphergroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, ciphergroupname="", option_="") :
		r""" Use this API to fetch sslcipher_binding resource.
		"""
		try :
			if not ciphergroupname :
				obj = sslcipher_binding()
				response = obj.get_resources(service, option_)
			elif type(ciphergroupname) is not list :
				obj = sslcipher_binding()
				obj.ciphergroupname = ciphergroupname
				response = obj.get_resource(service)
			else :
				if ciphergroupname and len(ciphergroupname) > 0 :
					obj = [sslcipher_binding() for _ in range(len(ciphergroupname))]
					for i in range(len(ciphergroupname)) :
						obj[i].ciphergroupname = ciphergroupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class sslcipher_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcipher_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcipher_binding = [sslcipher_binding() for _ in range(length)]

