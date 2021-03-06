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

class cmpparameter(base_resource) :
	""" Configuration for CMP parameter resource. """
	def __init__(self) :
		self._cmplevel = None
		self._quantumsize = None
		self._servercmp = None
		self._heurexpiry = None
		self._heurexpirythres = None
		self._heurexpiryhistwt = None
		self._minressize = None
		self._cmpbypasspct = None
		self._cmponpush = None
		self._policytype = None
		self._addvaryheader = None
		self._varyheadervalue = None
		self._externalcache = None
		self._builtin = None
		self._feature = None

	@property
	def cmplevel(self) :
		r"""Specify a compression level. Available settings function as follows:
		* Optimal - Corresponds to a gzip GZIP level of 5-7.
		* Best speed - Corresponds to a gzip level of 1.
		* Best compression - Corresponds to a gzip level of 9.<br/>Default value: optimal<br/>Possible values = optimal, bestspeed, bestcompression.
		"""
		try :
			return self._cmplevel
		except Exception as e:
			raise e

	@cmplevel.setter
	def cmplevel(self, cmplevel) :
		r"""Specify a compression level. Available settings function as follows:
		* Optimal - Corresponds to a gzip GZIP level of 5-7.
		* Best speed - Corresponds to a gzip level of 1.
		* Best compression - Corresponds to a gzip level of 9.<br/>Default value: optimal<br/>Possible values = optimal, bestspeed, bestcompression
		"""
		try :
			self._cmplevel = cmplevel
		except Exception as e:
			raise e

	@property
	def quantumsize(self) :
		r"""Minimum quantum of data to be filled before compression begins.<br/>Default value: 57344<br/>Minimum length =  8<br/>Maximum length =  63488.
		"""
		try :
			return self._quantumsize
		except Exception as e:
			raise e

	@quantumsize.setter
	def quantumsize(self, quantumsize) :
		r"""Minimum quantum of data to be filled before compression begins.<br/>Default value: 57344<br/>Minimum length =  8<br/>Maximum length =  63488
		"""
		try :
			self._quantumsize = quantumsize
		except Exception as e:
			raise e

	@property
	def servercmp(self) :
		r"""Allow the server to send compressed data to the Citrix ADC. With the default setting, the Citrix ADC appliance handles all compression.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._servercmp
		except Exception as e:
			raise e

	@servercmp.setter
	def servercmp(self, servercmp) :
		r"""Allow the server to send compressed data to the Citrix ADC. With the default setting, the Citrix ADC appliance handles all compression.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._servercmp = servercmp
		except Exception as e:
			raise e

	@property
	def heurexpiry(self) :
		r"""Heuristic basefile expiry.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._heurexpiry
		except Exception as e:
			raise e

	@heurexpiry.setter
	def heurexpiry(self, heurexpiry) :
		r"""Heuristic basefile expiry.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._heurexpiry = heurexpiry
		except Exception as e:
			raise e

	@property
	def heurexpirythres(self) :
		r"""Threshold compression ratio for heuristic basefile expiry, multiplied by 100. For example, to set the threshold ratio to 1.25, specify 125.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  1000.
		"""
		try :
			return self._heurexpirythres
		except Exception as e:
			raise e

	@heurexpirythres.setter
	def heurexpirythres(self, heurexpirythres) :
		r"""Threshold compression ratio for heuristic basefile expiry, multiplied by 100. For example, to set the threshold ratio to 1.25, specify 125.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  1000
		"""
		try :
			self._heurexpirythres = heurexpirythres
		except Exception as e:
			raise e

	@property
	def heurexpiryhistwt(self) :
		r"""For heuristic basefile expiry, weightage to be given to historical delta compression ratio, specified as percentage.  For example, to give 25% weightage to historical ratio (and therefore 75% weightage to the ratio for current delta compression transaction), specify 25.<br/>Default value: 50<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._heurexpiryhistwt
		except Exception as e:
			raise e

	@heurexpiryhistwt.setter
	def heurexpiryhistwt(self, heurexpiryhistwt) :
		r"""For heuristic basefile expiry, weightage to be given to historical delta compression ratio, specified as percentage.  For example, to give 25% weightage to historical ratio (and therefore 75% weightage to the ratio for current delta compression transaction), specify 25.<br/>Default value: 50<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._heurexpiryhistwt = heurexpiryhistwt
		except Exception as e:
			raise e

	@property
	def minressize(self) :
		r"""Smallest response size, in bytes, to be compressed.
		"""
		try :
			return self._minressize
		except Exception as e:
			raise e

	@minressize.setter
	def minressize(self, minressize) :
		r"""Smallest response size, in bytes, to be compressed.
		"""
		try :
			self._minressize = minressize
		except Exception as e:
			raise e

	@property
	def cmpbypasspct(self) :
		r"""Citrix ADC CPU threshold after which compression is not performed. Range: 0 - 100.<br/>Default value: 100<br/>Maximum length =  100.
		"""
		try :
			return self._cmpbypasspct
		except Exception as e:
			raise e

	@cmpbypasspct.setter
	def cmpbypasspct(self, cmpbypasspct) :
		r"""Citrix ADC CPU threshold after which compression is not performed. Range: 0 - 100.<br/>Default value: 100<br/>Maximum length =  100
		"""
		try :
			self._cmpbypasspct = cmpbypasspct
		except Exception as e:
			raise e

	@property
	def cmponpush(self) :
		r"""Citrix ADC does not wait for the quantum to be filled before starting to compress data. Upon receipt of a packet with a PUSH flag, the appliance immediately begins compression of the accumulated packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cmponpush
		except Exception as e:
			raise e

	@cmponpush.setter
	def cmponpush(self, cmponpush) :
		r"""Citrix ADC does not wait for the quantum to be filled before starting to compress data. Upon receipt of a packet with a PUSH flag, the appliance immediately begins compression of the accumulated packets.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cmponpush = cmponpush
		except Exception as e:
			raise e

	@property
	def policytype(self) :
		r"""Type of policy. Available settings function as follows:
		* Classic -  Classic policies evaluate basic characteristics of traffic and other data. Deprecated.
		* Advanced -  Advanced policies (which have been renamed as default syntax policies) can perform the same type of evaluations as classic policies. They also enable you to analyze more data (for example, the body of an HTTP request) and to configure more operations in the policy rule (for example, transforming data in the body of a request into an HTTP header).<br/>Possible values = CLASSIC, ADVANCED.
		"""
		try :
			return self._policytype
		except Exception as e:
			raise e

	@policytype.setter
	def policytype(self, policytype) :
		r"""Type of policy. Available settings function as follows:
		* Classic -  Classic policies evaluate basic characteristics of traffic and other data. Deprecated.
		* Advanced -  Advanced policies (which have been renamed as default syntax policies) can perform the same type of evaluations as classic policies. They also enable you to analyze more data (for example, the body of an HTTP request) and to configure more operations in the policy rule (for example, transforming data in the body of a request into an HTTP header).<br/>Possible values = CLASSIC, ADVANCED
		"""
		try :
			self._policytype = policytype
		except Exception as e:
			raise e

	@property
	def addvaryheader(self) :
		r"""Control insertion of the Vary header in HTTP responses compressed by Citrix ADC. Intermediate caches store different versions of the response for different values of the headers present in the Vary response header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._addvaryheader
		except Exception as e:
			raise e

	@addvaryheader.setter
	def addvaryheader(self, addvaryheader) :
		r"""Control insertion of the Vary header in HTTP responses compressed by Citrix ADC. Intermediate caches store different versions of the response for different values of the headers present in the Vary response header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._addvaryheader = addvaryheader
		except Exception as e:
			raise e

	@property
	def varyheadervalue(self) :
		r"""The value of the HTTP Vary header for compressed responses. If this argument is not specified, a default value of "Accept-Encoding" will be used.<br/>Minimum length =  1.
		"""
		try :
			return self._varyheadervalue
		except Exception as e:
			raise e

	@varyheadervalue.setter
	def varyheadervalue(self, varyheadervalue) :
		r"""The value of the HTTP Vary header for compressed responses. If this argument is not specified, a default value of "Accept-Encoding" will be used.<br/>Minimum length =  1
		"""
		try :
			self._varyheadervalue = varyheadervalue
		except Exception as e:
			raise e

	@property
	def externalcache(self) :
		r"""Enable insertion of  Cache-Control: private response directive to indicate response message is intended for a single user and must not be cached by a shared or proxy cache.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._externalcache
		except Exception as e:
			raise e

	@externalcache.setter
	def externalcache(self, externalcache) :
		r"""Enable insertion of  Cache-Control: private response directive to indicate response message is intended for a single user and must not be cached by a shared or proxy cache.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._externalcache = externalcache
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether compression is default or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(cmpparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cmpparameter
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
		updateresource = cmpparameter()
		updateresource.cmplevel = resource.cmplevel
		updateresource.quantumsize = resource.quantumsize
		updateresource.servercmp = resource.servercmp
		updateresource.heurexpiry = resource.heurexpiry
		updateresource.heurexpirythres = resource.heurexpirythres
		updateresource.heurexpiryhistwt = resource.heurexpiryhistwt
		updateresource.minressize = resource.minressize
		updateresource.cmpbypasspct = resource.cmpbypasspct
		updateresource.cmponpush = resource.cmponpush
		updateresource.policytype = resource.policytype
		updateresource.addvaryheader = resource.addvaryheader
		updateresource.varyheadervalue = resource.varyheadervalue
		updateresource.externalcache = resource.externalcache
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cmpparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of cmpparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cmpparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cmpparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cmpparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Servercmp:
		ON = "ON"
		OFF = "OFF"

	class Policytype:
		CLASSIC = "CLASSIC"
		ADVANCED = "ADVANCED"

	class Cmponpush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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

	class Externalcache:
		YES = "YES"
		NO = "NO"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Addvaryheader:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmplevel:
		optimal = "optimal"
		bestspeed = "bestspeed"
		bestcompression = "bestcompression"

	class Heurexpiry:
		ON = "ON"
		OFF = "OFF"

class cmpparameter_response(base_response) :
	def __init__(self, length=1) :
		self.cmpparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cmpparameter = [cmpparameter() for _ in range(length)]

