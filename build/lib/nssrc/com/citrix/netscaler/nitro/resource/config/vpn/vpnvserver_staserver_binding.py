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

class vpnvserver_staserver_binding(base_resource) :
	""" Binding class showing the staserver that can be bound to vpnvserver.
	"""
	def __init__(self) :
		self._staserver = None
		self._staauthid = None
		self._stastate = None
		self._acttype = None
		self._staaddresstype = None
		self._name = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the virtual server.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def staaddresstype(self) :
		r"""Type of the STA server address(ipv4/v6).<br/>Possible values = IPV4, IPV6.
		"""
		try :
			return self._staaddresstype
		except Exception as e:
			raise e

	@staaddresstype.setter
	def staaddresstype(self, staaddresstype) :
		r"""Type of the STA server address(ipv4/v6).<br/>Possible values = IPV4, IPV6
		"""
		try :
			self._staaddresstype = staaddresstype
		except Exception as e:
			raise e

	@property
	def staserver(self) :
		r"""Configured Secure Ticketing Authority (STA) server.
		"""
		try :
			return self._staserver
		except Exception as e:
			raise e

	@staserver.setter
	def staserver(self, staserver) :
		r"""Configured Secure Ticketing Authority (STA) server.
		"""
		try :
			self._staserver = staserver
		except Exception as e:
			raise e

	@property
	def stastate(self) :
		r"""State of the STA Server. If Authority ID is set then STA Server is UP else DOWN.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._stastate
		except Exception as e:
			raise e

	@property
	def acttype(self) :
		try :
			return self._acttype
		except Exception as e:
			raise e

	@property
	def staauthid(self) :
		r"""Authority ID of the STA Server. Authority ID is used to match incoming STA tickets in the SOCKS/CGP protocol with the right STA server.
		"""
		try :
			return self._staauthid
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnvserver_staserver_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnvserver_staserver_binding
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
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = vpnvserver_staserver_binding()
		addresource.name = resource.name
		addresource.staserver = resource.staserver
		addresource.staaddresstype = resource.staaddresstype
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [vpnvserver_staserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = vpnvserver_staserver_binding()
		deleteresource.name = resource.name
		deleteresource.staserver = resource.staserver
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [vpnvserver_staserver_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch vpnvserver_staserver_binding resources.
		"""
		try :
			if not name :
				obj = vpnvserver_staserver_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = vpnvserver_staserver_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of vpnvserver_staserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_staserver_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count vpnvserver_staserver_binding resources configued on NetScaler.
		"""
		try :
			obj = vpnvserver_staserver_binding()
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
		r""" Use this API to count the filtered set of vpnvserver_staserver_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnvserver_staserver_binding()
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

	class Stastate:
		UP = "UP"
		DOWN = "DOWN"

	class Staaddresstype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

	class Bindpoint:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		ICA_REQUEST = "ICA_REQUEST"
		OTHERTCP_REQUEST = "OTHERTCP_REQUEST"
		AAA_REQUEST = "AAA_REQUEST"
		AAA_RESPONSE = "AAA_RESPONSE"

class vpnvserver_staserver_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vpnvserver_staserver_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnvserver_staserver_binding = [vpnvserver_staserver_binding() for _ in range(length)]

