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

class lsnsipalgprofile(base_resource) :
	""" Configuration for LSN SIPALG Profile resource. """
	def __init__(self) :
		self._sipalgprofilename = None
		self._datasessionidletimeout = None
		self._sipsessiontimeout = None
		self._registrationtimeout = None
		self._sipsrcportrange = None
		self._sipdstportrange = None
		self._openregisterpinhole = None
		self._opencontactpinhole = None
		self._openviapinhole = None
		self._openrecordroutepinhole = None
		self._siptransportprotocol = None
		self._openroutepinhole = None
		self._rport = None
		self.___count = None

	@property
	def sipalgprofilename(self) :
		r"""The name of the SIPALG Profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sipalgprofilename
		except Exception as e:
			raise e

	@sipalgprofilename.setter
	def sipalgprofilename(self, sipalgprofilename) :
		r"""The name of the SIPALG Profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sipalgprofilename = sipalgprofilename
		except Exception as e:
			raise e

	@property
	def datasessionidletimeout(self) :
		r"""Idle timeout for the data channel sessions in seconds.<br/>Default value: 120.
		"""
		try :
			return self._datasessionidletimeout
		except Exception as e:
			raise e

	@datasessionidletimeout.setter
	def datasessionidletimeout(self, datasessionidletimeout) :
		r"""Idle timeout for the data channel sessions in seconds.<br/>Default value: 120
		"""
		try :
			self._datasessionidletimeout = datasessionidletimeout
		except Exception as e:
			raise e

	@property
	def sipsessiontimeout(self) :
		r"""SIP control channel session timeout in seconds.<br/>Default value: 600.
		"""
		try :
			return self._sipsessiontimeout
		except Exception as e:
			raise e

	@sipsessiontimeout.setter
	def sipsessiontimeout(self, sipsessiontimeout) :
		r"""SIP control channel session timeout in seconds.<br/>Default value: 600
		"""
		try :
			self._sipsessiontimeout = sipsessiontimeout
		except Exception as e:
			raise e

	@property
	def registrationtimeout(self) :
		r"""SIP registration timeout in seconds.<br/>Default value: 60.
		"""
		try :
			return self._registrationtimeout
		except Exception as e:
			raise e

	@registrationtimeout.setter
	def registrationtimeout(self, registrationtimeout) :
		r"""SIP registration timeout in seconds.<br/>Default value: 60
		"""
		try :
			self._registrationtimeout = registrationtimeout
		except Exception as e:
			raise e

	@property
	def sipsrcportrange(self) :
		r"""Source port range for SIP_UDP and SIP_TCP.
		"""
		try :
			return self._sipsrcportrange
		except Exception as e:
			raise e

	@sipsrcportrange.setter
	def sipsrcportrange(self, sipsrcportrange) :
		r"""Source port range for SIP_UDP and SIP_TCP.
		"""
		try :
			self._sipsrcportrange = sipsrcportrange
		except Exception as e:
			raise e

	@property
	def sipdstportrange(self) :
		r"""Destination port range for SIP_UDP and SIP_TCP.
		"""
		try :
			return self._sipdstportrange
		except Exception as e:
			raise e

	@sipdstportrange.setter
	def sipdstportrange(self, sipdstportrange) :
		r"""Destination port range for SIP_UDP and SIP_TCP.
		"""
		try :
			self._sipdstportrange = sipdstportrange
		except Exception as e:
			raise e

	@property
	def openregisterpinhole(self) :
		r"""ENABLE/DISABLE RegisterPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._openregisterpinhole
		except Exception as e:
			raise e

	@openregisterpinhole.setter
	def openregisterpinhole(self, openregisterpinhole) :
		r"""ENABLE/DISABLE RegisterPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._openregisterpinhole = openregisterpinhole
		except Exception as e:
			raise e

	@property
	def opencontactpinhole(self) :
		r"""ENABLE/DISABLE ContactPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._opencontactpinhole
		except Exception as e:
			raise e

	@opencontactpinhole.setter
	def opencontactpinhole(self, opencontactpinhole) :
		r"""ENABLE/DISABLE ContactPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._opencontactpinhole = opencontactpinhole
		except Exception as e:
			raise e

	@property
	def openviapinhole(self) :
		r"""ENABLE/DISABLE ViaPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._openviapinhole
		except Exception as e:
			raise e

	@openviapinhole.setter
	def openviapinhole(self, openviapinhole) :
		r"""ENABLE/DISABLE ViaPinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._openviapinhole = openviapinhole
		except Exception as e:
			raise e

	@property
	def openrecordroutepinhole(self) :
		r"""ENABLE/DISABLE RecordRoutePinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._openrecordroutepinhole
		except Exception as e:
			raise e

	@openrecordroutepinhole.setter
	def openrecordroutepinhole(self, openrecordroutepinhole) :
		r"""ENABLE/DISABLE RecordRoutePinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._openrecordroutepinhole = openrecordroutepinhole
		except Exception as e:
			raise e

	@property
	def siptransportprotocol(self) :
		r"""SIP ALG Profile transport protocol type.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._siptransportprotocol
		except Exception as e:
			raise e

	@siptransportprotocol.setter
	def siptransportprotocol(self, siptransportprotocol) :
		r"""SIP ALG Profile transport protocol type.<br/>Possible values = TCP, UDP
		"""
		try :
			self._siptransportprotocol = siptransportprotocol
		except Exception as e:
			raise e

	@property
	def openroutepinhole(self) :
		r"""ENABLE/DISABLE RoutePinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._openroutepinhole
		except Exception as e:
			raise e

	@openroutepinhole.setter
	def openroutepinhole(self, openroutepinhole) :
		r"""ENABLE/DISABLE RoutePinhole creation.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._openroutepinhole = openroutepinhole
		except Exception as e:
			raise e

	@property
	def rport(self) :
		r"""ENABLE/DISABLE rport.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rport
		except Exception as e:
			raise e

	@rport.setter
	def rport(self, rport) :
		r"""ENABLE/DISABLE rport.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rport = rport
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnsipalgprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnsipalgprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.sipalgprofilename is not None :
				return str(self.sipalgprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = lsnsipalgprofile()
		addresource.sipalgprofilename = resource.sipalgprofilename
		addresource.datasessionidletimeout = resource.datasessionidletimeout
		addresource.sipsessiontimeout = resource.sipsessiontimeout
		addresource.registrationtimeout = resource.registrationtimeout
		addresource.sipsrcportrange = resource.sipsrcportrange
		addresource.sipdstportrange = resource.sipdstportrange
		addresource.openregisterpinhole = resource.openregisterpinhole
		addresource.opencontactpinhole = resource.opencontactpinhole
		addresource.openviapinhole = resource.openviapinhole
		addresource.openrecordroutepinhole = resource.openrecordroutepinhole
		addresource.siptransportprotocol = resource.siptransportprotocol
		addresource.openroutepinhole = resource.openroutepinhole
		addresource.rport = resource.rport
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lsnsipalgprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnsipalgprofile() for _ in range(len(resource))]
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
		updateresource = lsnsipalgprofile()
		updateresource.sipalgprofilename = resource.sipalgprofilename
		updateresource.datasessionidletimeout = resource.datasessionidletimeout
		updateresource.sipsessiontimeout = resource.sipsessiontimeout
		updateresource.registrationtimeout = resource.registrationtimeout
		updateresource.sipsrcportrange = resource.sipsrcportrange
		updateresource.sipdstportrange = resource.sipdstportrange
		updateresource.openregisterpinhole = resource.openregisterpinhole
		updateresource.opencontactpinhole = resource.opencontactpinhole
		updateresource.openviapinhole = resource.openviapinhole
		updateresource.openrecordroutepinhole = resource.openrecordroutepinhole
		updateresource.siptransportprotocol = resource.siptransportprotocol
		updateresource.openroutepinhole = resource.openroutepinhole
		updateresource.rport = resource.rport
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lsnsipalgprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsnsipalgprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lsnsipalgprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnsipalgprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.sipalgprofilename = resource
				else :
					unsetresource.sipalgprofilename = resource.sipalgprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnsipalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sipalgprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnsipalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].sipalgprofilename = resource[i].sipalgprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = lsnsipalgprofile()
		deleteresource.sipalgprofilename = resource.sipalgprofilename
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lsnsipalgprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnsipalgprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.sipalgprofilename = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnsipalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].sipalgprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnsipalgprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lsnsipalgprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnsipalgprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lsnsipalgprofile()
					obj.sipalgprofilename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lsnsipalgprofile() for _ in range(len(name))]
						obj = [lsnsipalgprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lsnsipalgprofile()
							obj[i].sipalgprofilename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lsnsipalgprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnsipalgprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lsnsipalgprofile resources configured on NetScaler.
		"""
		try :
			obj = lsnsipalgprofile()
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
		r""" Use this API to count filtered the set of lsnsipalgprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnsipalgprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Siptransportprotocol:
		TCP = "TCP"
		UDP = "UDP"

	class Openregisterpinhole:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Openroutepinhole:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Openrecordroutepinhole:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Openviapinhole:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Opencontactpinhole:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lsnsipalgprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lsnsipalgprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnsipalgprofile = [lsnsipalgprofile() for _ in range(length)]

