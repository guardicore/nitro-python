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

class systemhwerror(base_resource) :
	""" Configuration for Hardware errors resource. """
	def __init__(self) :
		self._diskcheck = None
		self._response = None
		self._hwerrorcount = None

	@property
	def diskcheck(self) :
		r"""Perform only disk error checking.
		"""
		try :
			return self._diskcheck
		except Exception as e:
			raise e

	@diskcheck.setter
	def diskcheck(self, diskcheck) :
		r"""Perform only disk error checking.
		"""
		try :
			self._diskcheck = diskcheck
		except Exception as e:
			raise e

	@property
	def response(self) :
		r"""Response captured during hardware examination.
		"""
		try :
			return self._response
		except Exception as e:
			raise e

	@property
	def hwerrorcount(self) :
		r"""Number of errors found. Check response field for more information on errors if this value is non zero.
		"""
		try :
			return self._hwerrorcount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemhwerror_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemhwerror
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
	def check(cls, client, resource) :
		r""" Use this API to check systemhwerror.
		"""
		try :
			if type(resource) is not list :
				checkresource = systemhwerror()
				checkresource.diskcheck = resource.diskcheck
				return checkresource.perform_operationEx(client,"check")
		except Exception as e :
			raise e

class systemhwerror_response(base_response) :
	def __init__(self, length=1) :
		self.systemhwerror = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemhwerror = [systemhwerror() for _ in range(length)]

