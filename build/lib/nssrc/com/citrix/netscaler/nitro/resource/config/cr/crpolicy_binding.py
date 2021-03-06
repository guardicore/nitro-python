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

class crpolicy_binding(base_resource):
	""" Binding class showing the resources that can be bound to crpolicy_binding. 
	"""
	def __init__(self) :
		self._policyname = None
		self.crpolicy_crvserver_binding = []

	@property
	def policyname(self) :
		r"""Name of the cache redirection policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Name of the cache redirection policy to display. If this parameter is omitted, details of all the policies are displayed.<br/>Minimum length =  1
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def crpolicy_crvserver_bindings(self) :
		r"""crvserver that can be bound to crpolicy.
		"""
		try :
			return self._crpolicy_crvserver_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(crpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.crpolicy_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, policyname="", option_="") :
		r""" Use this API to fetch crpolicy_binding resource.
		"""
		try :
			if not policyname :
				obj = crpolicy_binding()
				response = obj.get_resources(service, option_)
			elif type(policyname) is not list :
				obj = crpolicy_binding()
				obj.policyname = policyname
				response = obj.get_resource(service)
			else :
				if policyname and len(policyname) > 0 :
					obj = [crpolicy_binding() for _ in range(len(policyname))]
					for i in range(len(policyname)) :
						obj[i].policyname = policyname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class crpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.crpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.crpolicy_binding = [crpolicy_binding() for _ in range(length)]

