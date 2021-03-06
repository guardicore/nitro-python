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

class vserver(base_resource) :
	""" Configuration for virtual server resource. """
	def __init__(self) :
		self._name = None
		self._backupvserver = None
		self._redirecturl = None
		self._cacheable = None
		self._clttimeout = None
		self._somethod = None
		self._sopersistence = None
		self._sopersistencetimeout = None
		self._sothreshold = None
		self._pushvserver = None

	@property
	def name(self) :
		r"""The name of the virtual server to be removed.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of the virtual server to be removed.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		r"""The name of the backup virtual server for this virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@backupvserver.setter
	def backupvserver(self, backupvserver) :
		r"""The name of the backup virtual server for this virtual server.<br/>Minimum length =  1
		"""
		try :
			self._backupvserver = backupvserver
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		r"""The URL where traffic is redirected if the virtual server in the system becomes unavailable.<br/>Minimum length =  1.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@redirecturl.setter
	def redirecturl(self, redirecturl) :
		r"""The URL where traffic is redirected if the virtual server in the system becomes unavailable.<br/>Minimum length =  1
		"""
		try :
			self._redirecturl = redirecturl
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		r"""Use this option to specify whether a virtual server (used for load balancing or content switching) routes requests to the cache redirection virtual server before sending it to the configured servers.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@cacheable.setter
	def cacheable(self, cacheable) :
		r"""Use this option to specify whether a virtual server (used for load balancing or content switching) routes requests to the cache redirection virtual server before sending it to the configured servers.<br/>Possible values = YES, NO
		"""
		try :
			self._cacheable = cacheable
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""The timeout value in seconds for idle client connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		r"""The timeout value in seconds for idle client connection.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		r"""The spillover factor. The system will use this value to determine if it should send traffic to the backupvserver when the main virtual server reaches the spillover threshold.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@somethod.setter
	def somethod(self, somethod) :
		r"""The spillover factor. The system will use this value to determine if it should send traffic to the backupvserver when the main virtual server reaches the spillover threshold.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE
		"""
		try :
			self._somethod = somethod
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		r"""The state of the spillover persistence.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@sopersistence.setter
	def sopersistence(self, sopersistence) :
		r"""The state of the spillover persistence.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sopersistence = sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		r"""The spillover persistence entry timeout.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@sopersistencetimeout.setter
	def sopersistencetimeout(self, sopersistencetimeout) :
		r"""The spillover persistence entry timeout.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._sopersistencetimeout = sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		r"""The spillver threshold value.<br/>Minimum length =  1<br/>Maximum length =  4294967294.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@sothreshold.setter
	def sothreshold(self, sothreshold) :
		r"""The spillver threshold value.<br/>Minimum length =  1<br/>Maximum length =  4294967294
		"""
		try :
			self._sothreshold = sothreshold
		except Exception as e:
			raise e

	@property
	def pushvserver(self) :
		r"""The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing non-push lb vserver.<br/>Minimum length =  1.
		"""
		try :
			return self._pushvserver
		except Exception as e:
			raise e

	@pushvserver.setter
	def pushvserver(self, pushvserver) :
		r"""The lb vserver of type PUSH/SSL_PUSH to which server pushes the updates received on the client facing non-push lb vserver.<br/>Minimum length =  1
		"""
		try :
			self._pushvserver = pushvserver
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vserver
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
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = vserver()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = vserver()
		updateresource.name = resource.name
		updateresource.backupvserver = resource.backupvserver
		updateresource.redirecturl = resource.redirecturl
		updateresource.cacheable = resource.cacheable
		updateresource.clttimeout = resource.clttimeout
		updateresource.somethod = resource.somethod
		updateresource.sopersistence = resource.sopersistence
		updateresource.sopersistencetimeout = resource.sopersistencetimeout
		updateresource.sothreshold = resource.sothreshold
		updateresource.pushvserver = resource.pushvserver
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable vserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = vserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable vserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = vserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
		except Exception as e :
			raise e

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cacheable:
		YES = "YES"
		NO = "NO"

class vserver_response(base_response) :
	def __init__(self, length=1) :
		self.vserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vserver = [vserver() for _ in range(length)]

