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

class responderparam(base_resource) :
	""" Configuration for responser parameter resource. """
	def __init__(self) :
		self._undefaction = None
		self._timeout = None

	@property
	def undefaction(self) :
		r"""Action to perform when policy evaluation creates an UNDEF condition. Available settings function as follows:
		* NOOP - Send the request to the protected server.
		* RESET - Reset the request and notify the user's browser, so that the user can resend the request.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: "NOOP".
		"""
		try :
			return self._undefaction
		except Exception as e:
			raise e

	@undefaction.setter
	def undefaction(self, undefaction) :
		r"""Action to perform when policy evaluation creates an UNDEF condition. Available settings function as follows:
		* NOOP - Send the request to the protected server.
		* RESET - Reset the request and notify the user's browser, so that the user can resend the request.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: "NOOP"
		"""
		try :
			self._undefaction = undefaction
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Maximum time in milliseconds to allow for processing all the policies and their selected actions without interruption. If the timeout is reached then the evaluation causes an UNDEF to be raised and no further processing is performed.<br/>Default value: 3900<br/>Minimum length =  1<br/>Maximum length =  5000.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		r"""Maximum time in milliseconds to allow for processing all the policies and their selected actions without interruption. If the timeout is reached then the evaluation causes an UNDEF to be raised and no further processing is performed.<br/>Default value: 3900<br/>Minimum length =  1<br/>Maximum length =  5000
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(responderparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.responderparam
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
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = responderparam()
		updateresource.undefaction = resource.undefaction
		updateresource.timeout = resource.timeout
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update responderparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of responderparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = responderparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the responderparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = responderparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class responderparam_response(base_response) :
	def __init__(self, length=1) :
		self.responderparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.responderparam = [responderparam() for _ in range(length)]

