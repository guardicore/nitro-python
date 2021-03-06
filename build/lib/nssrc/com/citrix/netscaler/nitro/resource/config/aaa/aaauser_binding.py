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

class aaauser_binding(base_resource):
	""" Binding class showing the resources that can be bound to aaauser_binding. 
	"""
	def __init__(self) :
		self._username = None
		self.aaauser_auditnslogpolicy_binding = []
		self.aaauser_intranetip6_binding = []
		self.aaauser_vpnsessionpolicy_binding = []
		self.aaauser_authorizationpolicy_binding = []
		self.aaauser_vpnurlpolicy_binding = []
		self.aaauser_intranetip_binding = []
		self.aaauser_auditsyslogpolicy_binding = []
		self.aaauser_aaagroup_binding = []
		self.aaauser_vpnurl_binding = []
		self.aaauser_vpntrafficpolicy_binding = []
		self.aaauser_vpnintranetapplication_binding = []
		self.aaauser_tmsessionpolicy_binding = []

	@property
	def username(self) :
		r"""Name of the user who has the account.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""Name of the user who has the account.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def aaauser_authorizationpolicy_bindings(self) :
		r"""authorizationpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_authorizationpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_vpnurl_bindings(self) :
		r"""vpnurl that can be bound to aaauser.
		"""
		try :
			return self._aaauser_vpnurl_binding
		except Exception as e:
			raise e

	@property
	def aaauser_vpntrafficpolicy_bindings(self) :
		r"""vpntrafficpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_vpntrafficpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_aaagroup_bindings(self) :
		r"""aaagroup that can be bound to aaauser.
		"""
		try :
			return self._aaauser_aaagroup_binding
		except Exception as e:
			raise e

	@property
	def aaauser_vpnurlpolicy_bindings(self) :
		r"""vpnurlpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_vpnurlpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_vpnsessionpolicy_bindings(self) :
		r"""vpnsessionpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_vpnsessionpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_intranetip_bindings(self) :
		r"""intranetip that can be bound to aaauser.
		"""
		try :
			return self._aaauser_intranetip_binding
		except Exception as e:
			raise e

	@property
	def aaauser_intranetip6_bindings(self) :
		r"""intranetip6 that can be bound to aaauser.
		"""
		try :
			return self._aaauser_intranetip6_binding
		except Exception as e:
			raise e

	@property
	def aaauser_auditsyslogpolicy_bindings(self) :
		r"""auditsyslogpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_auditsyslogpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_tmsessionpolicy_bindings(self) :
		r"""tmsessionpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_tmsessionpolicy_binding
		except Exception as e:
			raise e

	@property
	def aaauser_vpnintranetapplication_bindings(self) :
		r"""vpnintranetapplication that can be bound to aaauser.
		"""
		try :
			return self._aaauser_vpnintranetapplication_binding
		except Exception as e:
			raise e

	@property
	def aaauser_auditnslogpolicy_bindings(self) :
		r"""auditnslogpolicy that can be bound to aaauser.
		"""
		try :
			return self._aaauser_auditnslogpolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaauser_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaauser_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.username is not None :
				return str(self.username)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, username="", option_="") :
		r""" Use this API to fetch aaauser_binding resource.
		"""
		try :
			if not username :
				obj = aaauser_binding()
				response = obj.get_resources(service, option_)
			elif type(username) is not list :
				obj = aaauser_binding()
				obj.username = username
				response = obj.get_resource(service)
			else :
				if username and len(username) > 0 :
					obj = [aaauser_binding() for _ in range(len(username))]
					for i in range(len(username)) :
						obj[i].username = username[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class aaauser_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaauser_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaauser_binding = [aaauser_binding() for _ in range(length)]

