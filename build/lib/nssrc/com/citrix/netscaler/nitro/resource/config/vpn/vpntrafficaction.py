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

class vpntrafficaction(base_resource) :
	""" Configuration for VPN traffic action resource. """
	def __init__(self) :
		self._name = None
		self._qual = None
		self._apptimeout = None
		self._sso = None
		self._hdx = None
		self._formssoaction = None
		self._fta = None
		self._wanscaler = None
		self._kcdaccount = None
		self._samlssoprofile = None
		self._proxy = None
		self._userexpression = None
		self._passwdexpression = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the traffic action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the traffic action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after a traffic action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def qual(self) :
		r"""Protocol, either HTTP or TCP, to be used with the action.<br/>Possible values = http, tcp.
		"""
		try :
			return self._qual
		except Exception as e:
			raise e

	@qual.setter
	def qual(self, qual) :
		r"""Protocol, either HTTP or TCP, to be used with the action.<br/>Possible values = http, tcp
		"""
		try :
			self._qual = qual
		except Exception as e:
			raise e

	@property
	def apptimeout(self) :
		r"""Maximum amount of time, in minutes, a user can stay logged on to the web application.<br/>Minimum length =  1<br/>Maximum length =  715827.
		"""
		try :
			return self._apptimeout
		except Exception as e:
			raise e

	@apptimeout.setter
	def apptimeout(self, apptimeout) :
		r"""Maximum amount of time, in minutes, a user can stay logged on to the web application.<br/>Minimum length =  1<br/>Maximum length =  715827
		"""
		try :
			self._apptimeout = apptimeout
		except Exception as e:
			raise e

	@property
	def sso(self) :
		r"""Provide single sign-on to the web application.
		NOTE : Authentication mechanisms like Basic-authentication  require the user credentials to be sent in plaintext which is not secure if the server is running on HTTP (instead of HTTPS).<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sso
		except Exception as e:
			raise e

	@sso.setter
	def sso(self, sso) :
		r"""Provide single sign-on to the web application.
		NOTE : Authentication mechanisms like Basic-authentication  require the user credentials to be sent in plaintext which is not secure if the server is running on HTTP (instead of HTTPS).<br/>Possible values = ON, OFF
		"""
		try :
			self._sso = sso
		except Exception as e:
			raise e

	@property
	def hdx(self) :
		r"""Provide hdx proxy to the ICA traffic.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._hdx
		except Exception as e:
			raise e

	@hdx.setter
	def hdx(self, hdx) :
		r"""Provide hdx proxy to the ICA traffic.<br/>Possible values = ON, OFF
		"""
		try :
			self._hdx = hdx
		except Exception as e:
			raise e

	@property
	def formssoaction(self) :
		r"""Name of the form-based single sign-on profile. Form-based single sign-on allows users to log on one time to all protected applications in your network, instead of requiring them to log on separately to access each one.
		"""
		try :
			return self._formssoaction
		except Exception as e:
			raise e

	@formssoaction.setter
	def formssoaction(self, formssoaction) :
		r"""Name of the form-based single sign-on profile. Form-based single sign-on allows users to log on one time to all protected applications in your network, instead of requiring them to log on separately to access each one.
		"""
		try :
			self._formssoaction = formssoaction
		except Exception as e:
			raise e

	@property
	def fta(self) :
		r"""Specify file type association, which is a list of file extensions that users are allowed to open.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._fta
		except Exception as e:
			raise e

	@fta.setter
	def fta(self, fta) :
		r"""Specify file type association, which is a list of file extensions that users are allowed to open.<br/>Possible values = ON, OFF
		"""
		try :
			self._fta = fta
		except Exception as e:
			raise e

	@property
	def wanscaler(self) :
		r"""Use the Repeater Plug-in to optimize network traffic.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._wanscaler
		except Exception as e:
			raise e

	@wanscaler.setter
	def wanscaler(self, wanscaler) :
		r"""Use the Repeater Plug-in to optimize network traffic.<br/>Possible values = ON, OFF
		"""
		try :
			self._wanscaler = wanscaler
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		r"""Kerberos constrained delegation account name.<br/>Default value: "Default"<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		r"""Kerberos constrained delegation account name.<br/>Default value: "Default"<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def samlssoprofile(self) :
		r"""Profile to be used for doing SAML SSO to remote relying party.<br/>Minimum length =  1.
		"""
		try :
			return self._samlssoprofile
		except Exception as e:
			raise e

	@samlssoprofile.setter
	def samlssoprofile(self, samlssoprofile) :
		r"""Profile to be used for doing SAML SSO to remote relying party.<br/>Minimum length =  1
		"""
		try :
			self._samlssoprofile = samlssoprofile
		except Exception as e:
			raise e

	@property
	def proxy(self) :
		r"""IP address and Port of the proxy server to be used for HTTP access for this request.<br/>Minimum length =  1.
		"""
		try :
			return self._proxy
		except Exception as e:
			raise e

	@proxy.setter
	def proxy(self, proxy) :
		r"""IP address and Port of the proxy server to be used for HTTP access for this request.<br/>Minimum length =  1
		"""
		try :
			self._proxy = proxy
		except Exception as e:
			raise e

	@property
	def userexpression(self) :
		r"""expression that will be evaluated to obtain username for SingleSignOn.<br/>Maximum length =  256.
		"""
		try :
			return self._userexpression
		except Exception as e:
			raise e

	@userexpression.setter
	def userexpression(self, userexpression) :
		r"""expression that will be evaluated to obtain username for SingleSignOn.<br/>Maximum length =  256
		"""
		try :
			self._userexpression = userexpression
		except Exception as e:
			raise e

	@property
	def passwdexpression(self) :
		r"""expression that will be evaluated to obtain password for SingleSignOn.<br/>Maximum length =  256.
		"""
		try :
			return self._passwdexpression
		except Exception as e:
			raise e

	@passwdexpression.setter
	def passwdexpression(self, passwdexpression) :
		r"""expression that will be evaluated to obtain password for SingleSignOn.<br/>Maximum length =  256
		"""
		try :
			self._passwdexpression = passwdexpression
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpntrafficaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpntrafficaction
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
		addresource = vpntrafficaction()
		addresource.name = resource.name
		addresource.qual = resource.qual
		addresource.apptimeout = resource.apptimeout
		addresource.sso = resource.sso
		addresource.hdx = resource.hdx
		addresource.formssoaction = resource.formssoaction
		addresource.fta = resource.fta
		addresource.wanscaler = resource.wanscaler
		addresource.kcdaccount = resource.kcdaccount
		addresource.samlssoprofile = resource.samlssoprofile
		addresource.proxy = resource.proxy
		addresource.userexpression = resource.userexpression
		addresource.passwdexpression = resource.passwdexpression
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpntrafficaction() for _ in range(len(resource))]
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
		deleteresource = vpntrafficaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpntrafficaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpntrafficaction() for _ in range(len(resource))]
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
		updateresource = vpntrafficaction()
		updateresource.name = resource.name
		updateresource.apptimeout = resource.apptimeout
		updateresource.sso = resource.sso
		updateresource.hdx = resource.hdx
		updateresource.formssoaction = resource.formssoaction
		updateresource.fta = resource.fta
		updateresource.wanscaler = resource.wanscaler
		updateresource.kcdaccount = resource.kcdaccount
		updateresource.samlssoprofile = resource.samlssoprofile
		updateresource.proxy = resource.proxy
		updateresource.userexpression = resource.userexpression
		updateresource.passwdexpression = resource.passwdexpression
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vpntrafficaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpntrafficaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vpntrafficaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpntrafficaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpntrafficaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpntrafficaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpntrafficaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpntrafficaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpntrafficaction() for _ in range(len(name))]
						obj = [vpntrafficaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpntrafficaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpntrafficaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpntrafficaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpntrafficaction resources configured on NetScaler.
		"""
		try :
			obj = vpntrafficaction()
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
		r""" Use this API to count filtered the set of vpntrafficaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpntrafficaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Fta:
		ON = "ON"
		OFF = "OFF"

	class Qual:
		http = "http"
		tcp = "tcp"

	class Wanscaler:
		ON = "ON"
		OFF = "OFF"

	class Hdx:
		ON = "ON"
		OFF = "OFF"

	class Sso:
		ON = "ON"
		OFF = "OFF"

class vpntrafficaction_response(base_response) :
	def __init__(self, length=1) :
		self.vpntrafficaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpntrafficaction = [vpntrafficaction() for _ in range(length)]

