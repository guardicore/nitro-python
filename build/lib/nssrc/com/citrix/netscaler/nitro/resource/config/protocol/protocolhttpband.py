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

class protocolhttpband(base_resource) :
	""" Configuration for HTTP request/response band resource. """
	def __init__(self) :
		self._reqbandsize = None
		self._respbandsize = None
		self._type = None
		self._nodeid = None
		self._bandrange = None
		self._numberofbands = None
		self._totalbandsize = None
		self._avgbandsize = None
		self._avgbandsizenew = None
		self._banddata = None
		self._banddatanew = None
		self._accesscount = None
		self._accessratio = None
		self._accessrationew = None
		self._totals = None

	@property
	def reqbandsize(self) :
		r"""Band size, in bytes, for HTTP request band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 100<br/>Minimum length =  50.
		"""
		try :
			return self._reqbandsize
		except Exception as e:
			raise e

	@reqbandsize.setter
	def reqbandsize(self, reqbandsize) :
		r"""Band size, in bytes, for HTTP request band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 100<br/>Minimum length =  50
		"""
		try :
			self._reqbandsize = reqbandsize
		except Exception as e:
			raise e

	@property
	def respbandsize(self) :
		r"""Band size, in bytes, for HTTP response band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 1024<br/>Minimum length =  50.
		"""
		try :
			return self._respbandsize
		except Exception as e:
			raise e

	@respbandsize.setter
	def respbandsize(self, respbandsize) :
		r"""Band size, in bytes, for HTTP response band statistics. For example, if you specify a band size of 100 bytes, statistics will be maintained and displayed for the following size ranges:
		0 - 99 bytes
		100 - 199 bytes
		200 - 299 bytes and so on.<br/>Default value: 1024<br/>Minimum length =  50
		"""
		try :
			self._respbandsize = respbandsize
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of statistics to display.<br/>Possible values = REQUEST, RESPONSE, MQTT_JUMBO_REQ.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of statistics to display.<br/>Possible values = REQUEST, RESPONSE, MQTT_JUMBO_REQ
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def bandrange(self) :
		r"""The range of the HTTP request/response size, in bytes.
		"""
		try :
			return self._bandrange
		except Exception as e:
			raise e

	@property
	def numberofbands(self) :
		r"""The total number of http bands.
		"""
		try :
			return self._numberofbands
		except Exception as e:
			raise e

	@property
	def totalbandsize(self) :
		r"""The total size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._totalbandsize
		except Exception as e:
			raise e

	@property
	def avgbandsize(self) :
		r"""The average size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._avgbandsize
		except Exception as e:
			raise e

	@property
	def avgbandsizenew(self) :
		r"""The average size of all HTTP requests/responses in this size range.
		"""
		try :
			return self._avgbandsizenew
		except Exception as e:
			raise e

	@property
	def banddata(self) :
		r"""The total size of all HTTP requests/responses in this size range, expressed as a percentage of the total size of all HTTP requests/responses.
		"""
		try :
			return self._banddata
		except Exception as e:
			raise e

	@property
	def banddatanew(self) :
		r"""The total size of all HTTP requests/responses in this size range, expressed as a percentage of the total size of all HTTP requests/responses.
		"""
		try :
			return self._banddatanew
		except Exception as e:
			raise e

	@property
	def accesscount(self) :
		r"""The number of HTTP requests/responses in this size range.
		"""
		try :
			return self._accesscount
		except Exception as e:
			raise e

	@property
	def accessratio(self) :
		r"""The number of HTTP requests/responses in this size range, expressed as a percentage of the total number of HTTP requests/responses.
		"""
		try :
			return self._accessratio
		except Exception as e:
			raise e

	@property
	def accessrationew(self) :
		r"""The number of HTTP requests/responses in this size range, expressed as a percentage of the total number of HTTP requests/responses.
		"""
		try :
			return self._accessrationew
		except Exception as e:
			raise e

	@property
	def totals(self) :
		r"""The total of totalBandSize, avgBandSize, BandData, accessCount, accessRatio respectively.
		"""
		try :
			return self._totals
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolhttpband_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolhttpband
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
		updateresource = protocolhttpband()
		updateresource.reqbandsize = resource.reqbandsize
		updateresource.respbandsize = resource.respbandsize
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update protocolhttpband.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of protocolhttpband resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = protocolhttpband()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear protocolhttpband.
		"""
		try :
			if type(resource) is not list :
				clearresource = protocolhttpband()
				clearresource.type = resource.type
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the protocolhttpband resources that are configured on netscaler.
		"""
		try :
			if type(name) is not list :
				if type(name) == cls :
					raise Exception('Invalid parameter name:{0}'.format(type(name)))
				option_ = options()
				option_.args = nitro_util.object_to_string_withoutquotes(name)
				response = name.get_resource(client, option_)
				return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the protocolhttpband resources that are configured on netscaler.
	# This uses protocolhttpband_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = protocolhttpband()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Type:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		MQTT_JUMBO_REQ = "MQTT_JUMBO_REQ"

class protocolhttpband_response(base_response) :
	def __init__(self, length=1) :
		self.protocolhttpband = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolhttpband = [protocolhttpband() for _ in range(length)]

