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

class sslvserver_sslcertkey_binding(base_resource) :
	""" Binding class showing the sslcertkey that can be bound to sslvserver.
	"""
	def __init__(self) :
		self._certkeyname = None
		self._crlcheck = None
		self._ocspcheck = None
		self._cleartextport = None
		self._ca = None
		self._snicert = None
		self._skipcaname = None
		self._vservername = None
		self.___count = None

	@property
	def ca(self) :
		r"""CA certificate.
		"""
		try :
			return self._ca
		except Exception as e:
			raise e

	@ca.setter
	def ca(self, ca) :
		r"""CA certificate.
		"""
		try :
			self._ca = ca
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@crlcheck.setter
	def crlcheck(self, crlcheck) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._crlcheck = crlcheck
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		r"""Name of the SSL virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		r"""Name of the SSL virtual server.<br/>Minimum length =  1
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def certkeyname(self) :
		r"""The name of the certificate key pair binding.
		"""
		try :
			return self._certkeyname
		except Exception as e:
			raise e

	@certkeyname.setter
	def certkeyname(self, certkeyname) :
		r"""The name of the certificate key pair binding.
		"""
		try :
			self._certkeyname = certkeyname
		except Exception as e:
			raise e

	@property
	def skipcaname(self) :
		r"""The flag is used to indicate whether this particular CA certificate's CA_Name needs to be sent to the SSL client while requesting for client certificate in a SSL handshake.
		"""
		try :
			return self._skipcaname
		except Exception as e:
			raise e

	@skipcaname.setter
	def skipcaname(self, skipcaname) :
		r"""The flag is used to indicate whether this particular CA certificate's CA_Name needs to be sent to the SSL client while requesting for client certificate in a SSL handshake.
		"""
		try :
			self._skipcaname = skipcaname
		except Exception as e:
			raise e

	@property
	def snicert(self) :
		r"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			return self._snicert
		except Exception as e:
			raise e

	@snicert.setter
	def snicert(self, snicert) :
		r"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			self._snicert = snicert
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@ocspcheck.setter
	def ocspcheck(self, ocspcheck) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._ocspcheck = ocspcheck
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		r"""Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  65534.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_sslcertkey_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver_sslcertkey_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.vservername is not None :
				return str(self.vservername)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = sslvserver_sslcertkey_binding()
		addresource.vservername = resource.vservername
		addresource.certkeyname = resource.certkeyname
		addresource.ca = resource.ca
		addresource.crlcheck = resource.crlcheck
		addresource.skipcaname = resource.skipcaname
		addresource.snicert = resource.snicert
		addresource.ocspcheck = resource.ocspcheck
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslvserver_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = sslvserver_sslcertkey_binding()
		deleteresource.vservername = resource.vservername
		deleteresource.certkeyname = resource.certkeyname
		deleteresource.ca = resource.ca
		deleteresource.crlcheck = resource.crlcheck
		deleteresource.snicert = resource.snicert
		deleteresource.ocspcheck = resource.ocspcheck
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslvserver_sslcertkey_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, vservername="", option_="") :
		r""" Use this API to fetch sslvserver_sslcertkey_binding resources.
		"""
		try :
			if not vservername :
				obj = sslvserver_sslcertkey_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = sslvserver_sslcertkey_binding()
				obj.vservername = vservername
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, vservername, filter_) :
		r""" Use this API to fetch filtered set of sslvserver_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_sslcertkey_binding()
			obj.vservername = vservername
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, vservername) :
		r""" Use this API to count sslvserver_sslcertkey_binding resources configued on NetScaler.
		"""
		try :
			obj = sslvserver_sslcertkey_binding()
			obj.vservername = vservername
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, vservername, filter_) :
		r""" Use this API to count the filtered set of sslvserver_sslcertkey_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_sslcertkey_binding()
			obj.vservername = vservername
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Type:
		INTERCEPT_REQ = "INTERCEPT_REQ"
		REQUEST = "REQUEST"
		CLIENTHELLO_REQ = "CLIENTHELLO_REQ"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

class sslvserver_sslcertkey_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver_sslcertkey_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver_sslcertkey_binding = [sslvserver_sslcertkey_binding() for _ in range(length)]

