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

class lbsipparameters(base_resource) :
	""" Configuration for SIP parameters resource. """
	def __init__(self) :
		self._rnatsrcport = None
		self._rnatdstport = None
		self._retrydur = None
		self._addrportvip = None
		self._sip503ratethreshold = None
		self._rnatsecuresrcport = None
		self._rnatsecuredstport = None
		self._builtin = None
		self._feature = None

	@property
	def rnatsrcport(self) :
		r"""Port number with which to match the source port in server-initiated SIP traffic. The rport parameter is added, without a value, to SIP packets that have a matching source port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0.
		"""
		try :
			return self._rnatsrcport
		except Exception as e:
			raise e

	@rnatsrcport.setter
	def rnatsrcport(self, rnatsrcport) :
		r"""Port number with which to match the source port in server-initiated SIP traffic. The rport parameter is added, without a value, to SIP packets that have a matching source port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0
		"""
		try :
			self._rnatsrcport = rnatsrcport
		except Exception as e:
			raise e

	@property
	def rnatdstport(self) :
		r"""Port number with which to match the destination port in server-initiated SIP traffic. The rport parameter is added, without a value, to SIP packets that have a matching destination port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0.
		"""
		try :
			return self._rnatdstport
		except Exception as e:
			raise e

	@rnatdstport.setter
	def rnatdstport(self, rnatdstport) :
		r"""Port number with which to match the destination port in server-initiated SIP traffic. The rport parameter is added, without a value, to SIP packets that have a matching destination port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0
		"""
		try :
			self._rnatdstport = rnatdstport
		except Exception as e:
			raise e

	@property
	def retrydur(self) :
		r"""Time, in seconds, for which a client must wait before initiating a connection after receiving a 503 Service Unavailable response from the SIP server. The time value is sent in the "Retry-After" header in the 503 response.<br/>Default value: 120<br/>Minimum length =  1.
		"""
		try :
			return self._retrydur
		except Exception as e:
			raise e

	@retrydur.setter
	def retrydur(self, retrydur) :
		r"""Time, in seconds, for which a client must wait before initiating a connection after receiving a 503 Service Unavailable response from the SIP server. The time value is sent in the "Retry-After" header in the 503 response.<br/>Default value: 120<br/>Minimum length =  1
		"""
		try :
			self._retrydur = retrydur
		except Exception as e:
			raise e

	@property
	def addrportvip(self) :
		r"""Add the rport parameter to the VIA headers of SIP requests that virtual servers receive from clients or servers.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._addrportvip
		except Exception as e:
			raise e

	@addrportvip.setter
	def addrportvip(self, addrportvip) :
		r"""Add the rport parameter to the VIA headers of SIP requests that virtual servers receive from clients or servers.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._addrportvip = addrportvip
		except Exception as e:
			raise e

	@property
	def sip503ratethreshold(self) :
		r"""Maximum number of 503 Service Unavailable responses to generate, once every 10 milliseconds, when a SIP virtual server becomes unavailable.<br/>Default value: 100.
		"""
		try :
			return self._sip503ratethreshold
		except Exception as e:
			raise e

	@sip503ratethreshold.setter
	def sip503ratethreshold(self, sip503ratethreshold) :
		r"""Maximum number of 503 Service Unavailable responses to generate, once every 10 milliseconds, when a SIP virtual server becomes unavailable.<br/>Default value: 100
		"""
		try :
			self._sip503ratethreshold = sip503ratethreshold
		except Exception as e:
			raise e

	@property
	def rnatsecuresrcport(self) :
		r"""Port number with which to match the source port in server-initiated SIP over SSL traffic. The rport parameter is added, without a value, to SIP packets that have a matching source port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._rnatsecuresrcport
		except Exception as e:
			raise e

	@rnatsecuresrcport.setter
	def rnatsecuresrcport(self, rnatsecuresrcport) :
		r"""Port number with which to match the source port in server-initiated SIP over SSL traffic. The rport parameter is added, without a value, to SIP packets that have a matching source port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._rnatsecuresrcport = rnatsecuresrcport
		except Exception as e:
			raise e

	@property
	def rnatsecuredstport(self) :
		r"""Port number with which to match the destination port in server-initiated SIP over SSL traffic. The rport parameter is added, without a value, to SIP packets that have a matching destination port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._rnatsecuredstport
		except Exception as e:
			raise e

	@rnatsecuredstport.setter
	def rnatsecuredstport(self, rnatsecuredstport) :
		r"""Port number with which to match the destination port in server-initiated SIP over SSL traffic. The rport parameter is added, without a value, to SIP packets that have a matching destination port number, and CALL-ID based persistence is implemented for the responses received by the virtual server.<br/>Default value: 0<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._rnatsecuredstport = rnatsecuredstport
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if SIP param is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(lbsipparameters_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbsipparameters
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
		updateresource = lbsipparameters()
		updateresource.rnatsrcport = resource.rnatsrcport
		updateresource.rnatdstport = resource.rnatdstport
		updateresource.retrydur = resource.retrydur
		updateresource.addrportvip = resource.addrportvip
		updateresource.sip503ratethreshold = resource.sip503ratethreshold
		updateresource.rnatsecuresrcport = resource.rnatsecuresrcport
		updateresource.rnatsecuredstport = resource.rnatsecuredstport
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lbsipparameters.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lbsipparameters resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbsipparameters()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbsipparameters resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbsipparameters()
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

	class Addrportvip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class lbsipparameters_response(base_response) :
	def __init__(self, length=1) :
		self.lbsipparameters = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbsipparameters = [lbsipparameters() for _ in range(length)]

