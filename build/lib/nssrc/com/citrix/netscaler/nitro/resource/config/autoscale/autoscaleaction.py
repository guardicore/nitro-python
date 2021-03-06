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

class autoscaleaction(base_resource) :
	""" Configuration for autoscale action resource. """
	def __init__(self) :
		self._name = None
		self._type = None
		self._profilename = None
		self._parameters = None
		self._vmdestroygraceperiod = None
		self._quiettime = None
		self._vserver = None
		self.___count = None

	@property
	def name(self) :
		r"""ActionScale action name.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""ActionScale action name.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""The type of action.<br/>Possible values = SCALE_UP, SCALE_DOWN.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""The type of action.<br/>Possible values = SCALE_UP, SCALE_DOWN
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		r"""AutoScale profile name.<br/>Minimum length =  1.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		r"""AutoScale profile name.<br/>Minimum length =  1
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def parameters(self) :
		r"""Parameters to use in the action.<br/>Minimum length =  1.
		"""
		try :
			return self._parameters
		except Exception as e:
			raise e

	@parameters.setter
	def parameters(self, parameters) :
		r"""Parameters to use in the action.<br/>Minimum length =  1
		"""
		try :
			self._parameters = parameters
		except Exception as e:
			raise e

	@property
	def vmdestroygraceperiod(self) :
		r"""Time in minutes a VM is kept in inactive state before destroying.<br/>Default value: 10.
		"""
		try :
			return self._vmdestroygraceperiod
		except Exception as e:
			raise e

	@vmdestroygraceperiod.setter
	def vmdestroygraceperiod(self, vmdestroygraceperiod) :
		r"""Time in minutes a VM is kept in inactive state before destroying.<br/>Default value: 10
		"""
		try :
			self._vmdestroygraceperiod = vmdestroygraceperiod
		except Exception as e:
			raise e

	@property
	def quiettime(self) :
		r"""Time in seconds no other policy is evaluated or action is taken.<br/>Default value: 300.
		"""
		try :
			return self._quiettime
		except Exception as e:
			raise e

	@quiettime.setter
	def quiettime(self, quiettime) :
		r"""Time in seconds no other policy is evaluated or action is taken.<br/>Default value: 300
		"""
		try :
			self._quiettime = quiettime
		except Exception as e:
			raise e

	@property
	def vserver(self) :
		r"""Name of the vserver on which autoscale action has to be taken.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""Name of the vserver on which autoscale action has to be taken.
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(autoscaleaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.autoscaleaction
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
		addresource = autoscaleaction()
		addresource.name = resource.name
		addresource.type = resource.type
		addresource.profilename = resource.profilename
		addresource.parameters = resource.parameters
		addresource.vmdestroygraceperiod = resource.vmdestroygraceperiod
		addresource.quiettime = resource.quiettime
		addresource.vserver = resource.vserver
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ autoscaleaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = autoscaleaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = autoscaleaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = autoscaleaction()
		updateresource.name = resource.name
		updateresource.profilename = resource.profilename
		updateresource.parameters = resource.parameters
		updateresource.vmdestroygraceperiod = resource.vmdestroygraceperiod
		updateresource.quiettime = resource.quiettime
		updateresource.vserver = resource.vserver
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update autoscaleaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ autoscaleaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of autoscaleaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = autoscaleaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ autoscaleaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the autoscaleaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = autoscaleaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = autoscaleaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [autoscaleaction() for _ in range(len(name))]
						obj = [autoscaleaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = autoscaleaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of autoscaleaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the autoscaleaction resources configured on NetScaler.
		"""
		try :
			obj = autoscaleaction()
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
		r""" Use this API to count filtered the set of autoscaleaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = autoscaleaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		SCALE_UP = "SCALE_UP"
		SCALE_DOWN = "SCALE_DOWN"

class autoscaleaction_response(base_response) :
	def __init__(self, length=1) :
		self.autoscaleaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.autoscaleaction = [autoscaleaction() for _ in range(length)]

