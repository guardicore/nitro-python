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

class clusternodegroup(base_resource) :
	""" Configuration for Node group object type resource. """
	def __init__(self) :
		self._name = None
		self._strict = None
		self._sticky = None
		self._state = None
		self._priority = None
		self._currentnodemask = None
		self._backupnodemask = None
		self._boundedentitiescntfrompe = None
		self._activelist = None
		self._backuplist = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the nodegroup. The name uniquely identifies the nodegroup on the cluster.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the nodegroup. The name uniquely identifies the nodegroup on the cluster.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def strict(self) :
		r"""Specifies whether cluster nodes, that are not part of the nodegroup, will be used as backup for the nodegroup.
		* Enabled - When one of the nodes goes down, no other cluster node is picked up to replace it. When the node comes up, it will continue being part of the nodegroup.
		* Disabled - When one of the nodes goes down, a non-nodegroup cluster node is picked up and acts as part of the nodegroup. When the original node of the nodegroup comes up, the backup node will be replaced.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._strict
		except Exception as e:
			raise e

	@strict.setter
	def strict(self, strict) :
		r"""Specifies whether cluster nodes, that are not part of the nodegroup, will be used as backup for the nodegroup.
		* Enabled - When one of the nodes goes down, no other cluster node is picked up to replace it. When the node comes up, it will continue being part of the nodegroup.
		* Disabled - When one of the nodes goes down, a non-nodegroup cluster node is picked up and acts as part of the nodegroup. When the original node of the nodegroup comes up, the backup node will be replaced.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._strict = strict
		except Exception as e:
			raise e

	@property
	def sticky(self) :
		r"""Only one node can be bound to nodegroup with this option enabled. It specifies whether to prempt the traffic for the entities bound to nodegroup when owner node goes down and rejoins the cluster.
		* Enabled - When owner node goes down, backup node will become the owner node and takes the traffic for the entities bound to the nodegroup. When bound node rejoins the cluster, traffic for the entities bound to nodegroup will not be steered back to this bound node. Current owner will have the ownership till it goes down.
		* Disabled - When one of the nodes goes down, a non-nodegroup cluster node is picked up and acts as part of the nodegroup. When the original node of the nodegroup comes up, the backup node will be replaced.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._sticky
		except Exception as e:
			raise e

	@sticky.setter
	def sticky(self, sticky) :
		r"""Only one node can be bound to nodegroup with this option enabled. It specifies whether to prempt the traffic for the entities bound to nodegroup when owner node goes down and rejoins the cluster.
		* Enabled - When owner node goes down, backup node will become the owner node and takes the traffic for the entities bound to the nodegroup. When bound node rejoins the cluster, traffic for the entities bound to nodegroup will not be steered back to this bound node. Current owner will have the ownership till it goes down.
		* Disabled - When one of the nodes goes down, a non-nodegroup cluster node is picked up and acts as part of the nodegroup. When the original node of the nodegroup comes up, the backup node will be replaced.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._sticky = sticky
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""State of the nodegroup. All the nodes binding to this nodegroup must have the same state. ACTIVE/SPARE/PASSIVE.<br/>Possible values = ACTIVE, SPARE, PASSIVE.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""State of the nodegroup. All the nodes binding to this nodegroup must have the same state. ACTIVE/SPARE/PASSIVE.<br/>Possible values = ACTIVE, SPARE, PASSIVE
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority of Nodegroup. This priority is used for all the nodes bound to the nodegroup for Nodegroup selection.<br/>Maximum length =  31.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority of Nodegroup. This priority is used for all the nodes bound to the nodegroup for Nodegroup selection.<br/>Maximum length =  31
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def currentnodemask(self) :
		r"""Bitmap of current nodes in this nodegroup.
		"""
		try :
			return self._currentnodemask
		except Exception as e:
			raise e

	@property
	def backupnodemask(self) :
		r"""Bitmap of backup nodes in this nodegroup.
		"""
		try :
			return self._backupnodemask
		except Exception as e:
			raise e

	@property
	def boundedentitiescntfrompe(self) :
		r"""Count of bounded entities to this nodegroup accoding to PE.
		"""
		try :
			return self._boundedentitiescntfrompe
		except Exception as e:
			raise e

	@property
	def activelist(self) :
		r"""Active node list of this nodegroup.
		"""
		try :
			return self._activelist
		except Exception as e:
			raise e

	@property
	def backuplist(self) :
		r"""Backup node list of this nodegroup.
		"""
		try :
			return self._backuplist
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(clusternodegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.clusternodegroup
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
		addresource = clusternodegroup()
		addresource.name = resource.name
		addresource.strict = resource.strict
		addresource.sticky = resource.sticky
		addresource.state = resource.state
		addresource.priority = resource.priority
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add clusternodegroup.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ clusternodegroup() for _ in range(len(resource))]
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
		updateresource = clusternodegroup()
		updateresource.name = resource.name
		updateresource.strict = resource.strict
		updateresource.state = resource.state
		updateresource.priority = resource.priority
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update clusternodegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ clusternodegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of clusternodegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = clusternodegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusternodegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ clusternodegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = clusternodegroup()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete clusternodegroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = clusternodegroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusternodegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ clusternodegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the clusternodegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = clusternodegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = clusternodegroup()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [clusternodegroup() for _ in range(len(name))]
						obj = [clusternodegroup() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = clusternodegroup()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of clusternodegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternodegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the clusternodegroup resources configured on NetScaler.
		"""
		try :
			obj = clusternodegroup()
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
		r""" Use this API to count filtered the set of clusternodegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = clusternodegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		ACTIVE = "ACTIVE"
		SPARE = "SPARE"
		PASSIVE = "PASSIVE"

	class Strict:
		YES = "YES"
		NO = "NO"

	class Sticky:
		YES = "YES"
		NO = "NO"

class clusternodegroup_response(base_response) :
	def __init__(self, length=1) :
		self.clusternodegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.clusternodegroup = [clusternodegroup() for _ in range(length)]

