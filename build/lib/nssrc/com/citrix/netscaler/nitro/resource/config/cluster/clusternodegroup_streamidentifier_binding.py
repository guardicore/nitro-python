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

class clusternodegroup_streamidentifier_binding(base_resource) :
	""" Binding class showing the streamidentifier that can be bound to clusternodegroup.
	"""
	def __init__(self) :
		self._identifiername = None
		self._name = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the nodegroup to which you want to bind a cluster node or an entity.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the nodegroup to which you want to bind a cluster node or an entity.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def identifiername(self) :
		r"""stream identifier  and rate limit identifier that need to be bound to this nodegroup.
		"""
		try :
			return self._identifiername
		except Exception as e:
			raise e

	@identifiername.setter
	def identifiername(self, identifiername) :
		r"""stream identifier  and rate limit identifier that need to be bound to this nodegroup.
		"""
		try :
			self._identifiername = identifiername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternodegroup_streamidentifier_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternodegroup_streamidentifier_binding
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
		addresource = clusternodegroup_streamidentifier_binding()
		addresource.name = resource.name
		addresource.identifiername = resource.identifiername
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [clusternodegroup_streamidentifier_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = clusternodegroup_streamidentifier_binding()
		deleteresource.name = resource.name
		deleteresource.identifiername = resource.identifiername
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [clusternodegroup_streamidentifier_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch clusternodegroup_streamidentifier_binding resources.
		"""
		try :
			if not name :
				obj = clusternodegroup_streamidentifier_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = clusternodegroup_streamidentifier_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of clusternodegroup_streamidentifier_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternodegroup_streamidentifier_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count clusternodegroup_streamidentifier_binding resources configued on NetScaler.
		"""
		try :
			obj = clusternodegroup_streamidentifier_binding()
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
		r""" Use this API to count the filtered set of clusternodegroup_streamidentifier_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternodegroup_streamidentifier_binding()
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

class clusternodegroup_streamidentifier_binding_response(base_response) :
	def __init__(self, length=1) :
		self.clusternodegroup_streamidentifier_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternodegroup_streamidentifier_binding = [clusternodegroup_streamidentifier_binding() for _ in range(length)]

