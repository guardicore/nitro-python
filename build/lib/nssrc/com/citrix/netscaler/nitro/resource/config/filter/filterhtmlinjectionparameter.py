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

class filterhtmlinjectionparameter(base_resource) :
	""" Configuration for HTML injection parameter resource. """
	def __init__(self) :
		self._rate = None
		self._frequency = None
		self._strict = None
		self._htmlsearchlen = None
		self._builtin = None
		self._feature = None

	@property
	def rate(self) :
		r"""For a rate of x, HTML injection is done for 1 out of x policy matches.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._rate
		except Exception as e:
			raise e

	@rate.setter
	def rate(self, rate) :
		r"""For a rate of x, HTML injection is done for 1 out of x policy matches.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._rate = rate
		except Exception as e:
			raise e

	@property
	def frequency(self) :
		r"""For a frequency of x, HTML injection is done at least once per x milliseconds.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._frequency
		except Exception as e:
			raise e

	@frequency.setter
	def frequency(self, frequency) :
		r"""For a frequency of x, HTML injection is done at least once per x milliseconds.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._frequency = frequency
		except Exception as e:
			raise e

	@property
	def strict(self) :
		r"""Searching for <html> tag. If this parameter is enabled, HTML injection does not insert the prebody or postbody content unless the <html> tag is found.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._strict
		except Exception as e:
			raise e

	@strict.setter
	def strict(self, strict) :
		r"""Searching for <html> tag. If this parameter is enabled, HTML injection does not insert the prebody or postbody content unless the <html> tag is found.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._strict = strict
		except Exception as e:
			raise e

	@property
	def htmlsearchlen(self) :
		r"""Number of characters, in the HTTP body, in which to search for the <html> tag if strict mode is set.<br/>Default value: 1024<br/>Minimum length =  1.
		"""
		try :
			return self._htmlsearchlen
		except Exception as e:
			raise e

	@htmlsearchlen.setter
	def htmlsearchlen(self, htmlsearchlen) :
		r"""Number of characters, in the HTTP body, in which to search for the <html> tag if strict mode is set.<br/>Default value: 1024<br/>Minimum length =  1
		"""
		try :
			self._htmlsearchlen = htmlsearchlen
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if html injection param is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(filterhtmlinjectionparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.filterhtmlinjectionparameter
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
		updateresource = filterhtmlinjectionparameter()
		updateresource.rate = resource.rate
		updateresource.frequency = resource.frequency
		updateresource.strict = resource.strict
		updateresource.htmlsearchlen = resource.htmlsearchlen
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update filterhtmlinjectionparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of filterhtmlinjectionparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = filterhtmlinjectionparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the filterhtmlinjectionparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = filterhtmlinjectionparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"
		APIGateway = "APIGateway"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Strict:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class filterhtmlinjectionparameter_response(base_response) :
	def __init__(self, length=1) :
		self.filterhtmlinjectionparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.filterhtmlinjectionparameter = [filterhtmlinjectionparameter() for _ in range(length)]

