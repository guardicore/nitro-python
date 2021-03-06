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

class ssldtlsprofile(base_resource) :
	""" Configuration for DTLS profile resource. """
	def __init__(self) :
		self._name = None
		self._pmtudiscovery = None
		self._maxrecordsize = None
		self._maxretrytime = None
		self._helloverifyrequest = None
		self._terminatesession = None
		self._maxpacketsize = None
		self._maxholdqlen = None
		self._maxbadmacignorecount = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the DTLS profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the DTLS profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@),equals sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def pmtudiscovery(self) :
		r"""Source for the maximum record size value. If ENABLED, the value is taken from the PMTU table. If DISABLED, the value is taken from the profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._pmtudiscovery
		except Exception as e:
			raise e

	@pmtudiscovery.setter
	def pmtudiscovery(self, pmtudiscovery) :
		r"""Source for the maximum record size value. If ENABLED, the value is taken from the PMTU table. If DISABLED, the value is taken from the profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._pmtudiscovery = pmtudiscovery
		except Exception as e:
			raise e

	@property
	def maxrecordsize(self) :
		r"""Maximum size of records that can be sent if PMTU is disabled.<br/>Default value: 1459<br/>Minimum length =  250<br/>Maximum length =  1459.
		"""
		try :
			return self._maxrecordsize
		except Exception as e:
			raise e

	@maxrecordsize.setter
	def maxrecordsize(self, maxrecordsize) :
		r"""Maximum size of records that can be sent if PMTU is disabled.<br/>Default value: 1459<br/>Minimum length =  250<br/>Maximum length =  1459
		"""
		try :
			self._maxrecordsize = maxrecordsize
		except Exception as e:
			raise e

	@property
	def maxretrytime(self) :
		r"""Wait for the specified time, in seconds, before resending the request.<br/>Default value: 3.
		"""
		try :
			return self._maxretrytime
		except Exception as e:
			raise e

	@maxretrytime.setter
	def maxretrytime(self, maxretrytime) :
		r"""Wait for the specified time, in seconds, before resending the request.<br/>Default value: 3
		"""
		try :
			self._maxretrytime = maxretrytime
		except Exception as e:
			raise e

	@property
	def helloverifyrequest(self) :
		r"""Send a Hello Verify request to validate the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._helloverifyrequest
		except Exception as e:
			raise e

	@helloverifyrequest.setter
	def helloverifyrequest(self, helloverifyrequest) :
		r"""Send a Hello Verify request to validate the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._helloverifyrequest = helloverifyrequest
		except Exception as e:
			raise e

	@property
	def terminatesession(self) :
		r"""Terminate the session if the message authentication code (MAC) of the client and server do not match.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._terminatesession
		except Exception as e:
			raise e

	@terminatesession.setter
	def terminatesession(self, terminatesession) :
		r"""Terminate the session if the message authentication code (MAC) of the client and server do not match.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._terminatesession = terminatesession
		except Exception as e:
			raise e

	@property
	def maxpacketsize(self) :
		r"""Maximum number of packets to reassemble. This value helps protect against a fragmented packet attack.<br/>Default value: 120<br/>Maximum length =  86400.
		"""
		try :
			return self._maxpacketsize
		except Exception as e:
			raise e

	@maxpacketsize.setter
	def maxpacketsize(self, maxpacketsize) :
		r"""Maximum number of packets to reassemble. This value helps protect against a fragmented packet attack.<br/>Default value: 120<br/>Maximum length =  86400
		"""
		try :
			self._maxpacketsize = maxpacketsize
		except Exception as e:
			raise e

	@property
	def maxholdqlen(self) :
		r"""Maximum number of datagrams that can be queued at DTLS layer for processing.<br/>Default value: 32<br/>Minimum length =  32<br/>Maximum length =  65535.
		"""
		try :
			return self._maxholdqlen
		except Exception as e:
			raise e

	@maxholdqlen.setter
	def maxholdqlen(self, maxholdqlen) :
		r"""Maximum number of datagrams that can be queued at DTLS layer for processing.<br/>Default value: 32<br/>Minimum length =  32<br/>Maximum length =  65535
		"""
		try :
			self._maxholdqlen = maxholdqlen
		except Exception as e:
			raise e

	@property
	def maxbadmacignorecount(self) :
		r"""Maximum number of bad MAC errors to ignore for a connection prior disconnect. Disabling parameter terminateSession terminates session immediately when bad MAC is detected in the connection.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._maxbadmacignorecount
		except Exception as e:
			raise e

	@maxbadmacignorecount.setter
	def maxbadmacignorecount(self, maxbadmacignorecount) :
		r"""Maximum number of bad MAC errors to ignore for a connection prior disconnect. Disabling parameter terminateSession terminates session immediately when bad MAC is detected in the connection.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._maxbadmacignorecount = maxbadmacignorecount
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether dtls profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(ssldtlsprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssldtlsprofile
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
		addresource = ssldtlsprofile()
		addresource.name = resource.name
		addresource.pmtudiscovery = resource.pmtudiscovery
		addresource.maxrecordsize = resource.maxrecordsize
		addresource.maxretrytime = resource.maxretrytime
		addresource.helloverifyrequest = resource.helloverifyrequest
		addresource.terminatesession = resource.terminatesession
		addresource.maxpacketsize = resource.maxpacketsize
		addresource.maxholdqlen = resource.maxholdqlen
		addresource.maxbadmacignorecount = resource.maxbadmacignorecount
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ssldtlsprofile() for _ in range(len(resource))]
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
		deleteresource = ssldtlsprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ssldtlsprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssldtlsprofile() for _ in range(len(resource))]
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
		updateresource = ssldtlsprofile()
		updateresource.name = resource.name
		updateresource.pmtudiscovery = resource.pmtudiscovery
		updateresource.maxrecordsize = resource.maxrecordsize
		updateresource.maxretrytime = resource.maxretrytime
		updateresource.helloverifyrequest = resource.helloverifyrequest
		updateresource.terminatesession = resource.terminatesession
		updateresource.maxpacketsize = resource.maxpacketsize
		updateresource.maxholdqlen = resource.maxholdqlen
		updateresource.maxbadmacignorecount = resource.maxbadmacignorecount
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update ssldtlsprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ ssldtlsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ssldtlsprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ssldtlsprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssldtlsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ssldtlsprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ssldtlsprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = ssldtlsprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [ssldtlsprofile() for _ in range(len(name))]
						obj = [ssldtlsprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = ssldtlsprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ssldtlsprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldtlsprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ssldtlsprofile resources configured on NetScaler.
		"""
		try :
			obj = ssldtlsprofile()
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
		r""" Use this API to count filtered the set of ssldtlsprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssldtlsprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Terminatesession:
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

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Pmtudiscovery:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Helloverifyrequest:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class ssldtlsprofile_response(base_response) :
	def __init__(self, length=1) :
		self.ssldtlsprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ssldtlsprofile = [ssldtlsprofile() for _ in range(length)]

