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

class nssurgeq(base_resource) :
	""" Configuration for surge queue resource. """
	def __init__(self) :
		self._name = None
		self._servername = None
		self._port = None

	@property
	def name(self) :
		r"""Name of a virtual server, service or service group for which the SurgeQ must be flushed.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of a virtual server, service or service group for which the SurgeQ must be flushed.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of a service group member. This argument is needed when you want to flush the SurgeQ of a service group.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of a service group member. This argument is needed when you want to flush the SurgeQ of a service group.
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""port on which server is bound to the entity(Servicegroup).<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""port on which server is bound to the entity(Servicegroup).<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nssurgeq_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nssurgeq
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def flush(cls, client, resource) :
		r""" Use this API to flush nssurgeq.
		"""
		try :
			if type(resource) is not list :
				flushresource = nssurgeq()
				flushresource.name = resource.name
				flushresource.servername = resource.servername
				flushresource.port = resource.port
				return flushresource.perform_operation(client,"flush")
		except Exception as e :
			raise e

class nssurgeq_response(base_response) :
	def __init__(self, length=1) :
		self.nssurgeq = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nssurgeq = [nssurgeq() for _ in range(length)]

