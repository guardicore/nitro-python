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

class sslcertkey_binding(base_resource):
	""" Binding class showing the resources that can be bound to sslcertkey_binding. 
	"""
	def __init__(self) :
		self._certkey = None
		self.sslcertkey_crldistribution_binding = []
		self.sslcertkey_sslvserver_binding = []
		self.sslcertkey_sslocspresponder_binding = []
		self.sslcertkey_service_binding = []
		self.sslcertkey_sslprofile_binding = []

	@property
	def certkey(self) :
		r"""Name of the certificate-key pair for which to show detailed information.<br/>Minimum length =  1.
		"""
		try :
			return self._certkey
		except Exception as e:
			raise e

	@certkey.setter
	def certkey(self, certkey) :
		r"""Name of the certificate-key pair for which to show detailed information.<br/>Minimum length =  1
		"""
		try :
			self._certkey = certkey
		except Exception as e:
			raise e

	@property
	def sslcertkey_sslprofile_bindings(self) :
		r"""sslprofile that can be bound to sslcertkey.
		"""
		try :
			return self._sslcertkey_sslprofile_binding
		except Exception as e:
			raise e

	@property
	def sslcertkey_sslocspresponder_bindings(self) :
		r"""sslocspresponder that can be bound to sslcertkey.
		"""
		try :
			return self._sslcertkey_sslocspresponder_binding
		except Exception as e:
			raise e

	@property
	def sslcertkey_service_bindings(self) :
		r"""service that can be bound to sslcertkey.
		"""
		try :
			return self._sslcertkey_service_binding
		except Exception as e:
			raise e

	@property
	def sslcertkey_crldistribution_bindings(self) :
		r"""crldistribution that can be bound to sslcertkey.
		"""
		try :
			return self._sslcertkey_crldistribution_binding
		except Exception as e:
			raise e

	@property
	def sslcertkey_sslvserver_bindings(self) :
		r"""sslvserver that can be bound to sslcertkey.
		"""
		try :
			return self._sslcertkey_sslvserver_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertkey_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.certkey is not None :
				return str(self.certkey)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, certkey="", option_="") :
		r""" Use this API to fetch sslcertkey_binding resource.
		"""
		try :
			if not certkey :
				obj = sslcertkey_binding()
				response = obj.get_resources(service, option_)
			elif type(certkey) is not list :
				obj = sslcertkey_binding()
				obj.certkey = certkey
				response = obj.get_resource(service)
			else :
				if certkey and len(certkey) > 0 :
					obj = [sslcertkey_binding() for _ in range(len(certkey))]
					for i in range(len(certkey)) :
						obj[i].certkey = certkey[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertkey_binding = [sslcertkey_binding() for _ in range(length)]

