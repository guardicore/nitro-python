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

class sslvserver_ecccurve_binding(base_resource) :
	""" Binding class showing the ecccurve that can be bound to sslvserver.
	"""
	def __init__(self) :
		self._ecccurvename = None
		self._vservername = None
		self.___count = None

	@property
	def ecccurvename(self) :
		r"""Named ECC curve bound to vserver/service.<br/>Possible values = ALL, P_224, P_256, P_384, P_521.
		"""
		try :
			return self._ecccurvename
		except Exception as e:
			raise e

	@ecccurvename.setter
	def ecccurvename(self, ecccurvename) :
		r"""Named ECC curve bound to vserver/service.<br/>Possible values = ALL, P_224, P_256, P_384, P_521
		"""
		try :
			self._ecccurvename = ecccurvename
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

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslvserver_ecccurve_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslvserver_ecccurve_binding
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
		addresource = sslvserver_ecccurve_binding()
		addresource.vservername = resource.vservername
		addresource.ecccurvename = resource.ecccurvename
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslvserver_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = sslvserver_ecccurve_binding()
		deleteresource.vservername = resource.vservername
		deleteresource.ecccurvename = resource.ecccurvename
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslvserver_ecccurve_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, vservername="", option_="") :
		r""" Use this API to fetch sslvserver_ecccurve_binding resources.
		"""
		try :
			if not vservername :
				obj = sslvserver_ecccurve_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = sslvserver_ecccurve_binding()
				obj.vservername = vservername
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, vservername, filter_) :
		r""" Use this API to fetch filtered set of sslvserver_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_ecccurve_binding()
			obj.vservername = vservername
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, vservername) :
		r""" Use this API to count sslvserver_ecccurve_binding resources configued on NetScaler.
		"""
		try :
			obj = sslvserver_ecccurve_binding()
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
		r""" Use this API to count the filtered set of sslvserver_ecccurve_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslvserver_ecccurve_binding()
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

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ecccurvename:
		ALL = "ALL"
		P_224 = "P_224"
		P_256 = "P_256"
		P_384 = "P_384"
		P_521 = "P_521"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Type:
		INTERCEPT_REQ = "INTERCEPT_REQ"
		REQUEST = "REQUEST"
		CLIENTHELLO_REQ = "CLIENTHELLO_REQ"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

class sslvserver_ecccurve_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslvserver_ecccurve_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslvserver_ecccurve_binding = [sslvserver_ecccurve_binding() for _ in range(length)]

