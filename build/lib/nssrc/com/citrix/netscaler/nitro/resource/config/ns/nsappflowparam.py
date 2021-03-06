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

class nsappflowparam(base_resource) :
	""" Configuration for appflowParam resource. """
	def __init__(self) :
		self._templaterefresh = None
		self._udppmtu = None
		self._httpurl = None
		self._httpcookie = None
		self._httpreferer = None
		self._httpmethod = None
		self._httphost = None
		self._httpuseragent = None
		self._clienttrafficonly = None

	@property
	def templaterefresh(self) :
		r"""IPFIX template refresh interval (in seconds).<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600.
		"""
		try :
			return self._templaterefresh
		except Exception as e:
			raise e

	@templaterefresh.setter
	def templaterefresh(self, templaterefresh) :
		r"""IPFIX template refresh interval (in seconds).<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600
		"""
		try :
			self._templaterefresh = templaterefresh
		except Exception as e:
			raise e

	@property
	def udppmtu(self) :
		r"""MTU to be used for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472.
		"""
		try :
			return self._udppmtu
		except Exception as e:
			raise e

	@udppmtu.setter
	def udppmtu(self, udppmtu) :
		r"""MTU to be used for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472
		"""
		try :
			self._udppmtu = udppmtu
		except Exception as e:
			raise e

	@property
	def httpurl(self) :
		r"""Enable AppFlow HTTP URL logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpurl
		except Exception as e:
			raise e

	@httpurl.setter
	def httpurl(self, httpurl) :
		r"""Enable AppFlow HTTP URL logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpurl = httpurl
		except Exception as e:
			raise e

	@property
	def httpcookie(self) :
		r"""Enable AppFlow HTTP cookie logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpcookie
		except Exception as e:
			raise e

	@httpcookie.setter
	def httpcookie(self, httpcookie) :
		r"""Enable AppFlow HTTP cookie logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpcookie = httpcookie
		except Exception as e:
			raise e

	@property
	def httpreferer(self) :
		r"""Enable AppFlow HTTP referer logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpreferer
		except Exception as e:
			raise e

	@httpreferer.setter
	def httpreferer(self, httpreferer) :
		r"""Enable AppFlow HTTP referer logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpreferer = httpreferer
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""Enable AppFlow HTTP method logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""Enable AppFlow HTTP method logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def httphost(self) :
		r"""Enable AppFlow HTTP host logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httphost
		except Exception as e:
			raise e

	@httphost.setter
	def httphost(self, httphost) :
		r"""Enable AppFlow HTTP host logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httphost = httphost
		except Exception as e:
			raise e

	@property
	def httpuseragent(self) :
		r"""Enable AppFlow HTTP user-agent logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httpuseragent
		except Exception as e:
			raise e

	@httpuseragent.setter
	def httpuseragent(self, httpuseragent) :
		r"""Enable AppFlow HTTP user-agent logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httpuseragent = httpuseragent
		except Exception as e:
			raise e

	@property
	def clienttrafficonly(self) :
		r"""Control whether AppFlow records should be generated only for client-side traffic.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._clienttrafficonly
		except Exception as e:
			raise e

	@clienttrafficonly.setter
	def clienttrafficonly(self, clienttrafficonly) :
		r"""Control whether AppFlow records should be generated only for client-side traffic.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._clienttrafficonly = clienttrafficonly
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsappflowparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsappflowparam
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
		updateresource = nsappflowparam()
		updateresource.templaterefresh = resource.templaterefresh
		updateresource.udppmtu = resource.udppmtu
		updateresource.httpurl = resource.httpurl
		updateresource.httpcookie = resource.httpcookie
		updateresource.httpreferer = resource.httpreferer
		updateresource.httpmethod = resource.httpmethod
		updateresource.httphost = resource.httphost
		updateresource.httpuseragent = resource.httpuseragent
		updateresource.clienttrafficonly = resource.clienttrafficonly
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsappflowparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsappflowparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsappflowparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsappflowparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsappflowparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Clienttrafficonly:
		YES = "YES"
		NO = "NO"

	class Httphost:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpreferer:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpmethod:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpcookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpurl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpuseragent:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsappflowparam_response(base_response) :
	def __init__(self, length=1) :
		self.nsappflowparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsappflowparam = [nsappflowparam() for _ in range(length)]

