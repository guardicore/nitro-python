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

class radiusnode(base_resource) :
	""" Configuration for RADIUS Node resource. """
	def __init__(self) :
		self._nodeprefix = None
		self._radkey = None
		self.___count = None

	@property
	def nodeprefix(self) :
		r"""IP address/IP prefix of radius node in CIDR format.
		"""
		try :
			return self._nodeprefix
		except Exception as e:
			raise e

	@nodeprefix.setter
	def nodeprefix(self, nodeprefix) :
		r"""IP address/IP prefix of radius node in CIDR format.
		"""
		try :
			self._nodeprefix = nodeprefix
		except Exception as e:
			raise e

	@property
	def radkey(self) :
		r"""The key shared between the RADIUS server and clients.
		Required for Citrix ADC to communicate with the RADIUS nodes.
		"""
		try :
			return self._radkey
		except Exception as e:
			raise e

	@radkey.setter
	def radkey(self, radkey) :
		r"""The key shared between the RADIUS server and clients.
		Required for Citrix ADC to communicate with the RADIUS nodes.
		"""
		try :
			self._radkey = radkey
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(radiusnode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.radiusnode
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.nodeprefix is not None :
				return str(self.nodeprefix)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = radiusnode()
		addresource.nodeprefix = resource.nodeprefix
		addresource.radkey = resource.radkey
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add radiusnode.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ radiusnode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = radiusnode()
		updateresource.nodeprefix = resource.nodeprefix
		updateresource.radkey = resource.radkey
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update radiusnode.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ radiusnode() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = radiusnode()
		deleteresource.nodeprefix = resource.nodeprefix
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete radiusnode.
		"""
		try :
			if type(resource) is not list :
				deleteresource = radiusnode()
				if type(resource) !=  type(deleteresource):
					deleteresource.nodeprefix = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ radiusnode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].nodeprefix = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ radiusnode() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the radiusnode resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = radiusnode()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = radiusnode()
					obj.nodeprefix = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [radiusnode() for _ in range(len(name))]
						obj = [radiusnode() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = radiusnode()
							obj[i].nodeprefix = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of radiusnode resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = radiusnode()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the radiusnode resources configured on NetScaler.
		"""
		try :
			obj = radiusnode()
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
		r""" Use this API to count filtered the set of radiusnode resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = radiusnode()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class radiusnode_response(base_response) :
	def __init__(self, length=1) :
		self.radiusnode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.radiusnode = [radiusnode() for _ in range(length)]

