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

class dnsaction(base_resource) :
	""" Configuration for DNS action resource. """
	def __init__(self) :
		self._actionname = None
		self._actiontype = None
		self._ipaddress = None
		self._ttl = None
		self._viewname = None
		self._preferredloclist = None
		self._dnsprofilename = None
		self._drop = None
		self._cachebypass = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def actionname(self) :
		r"""Name of the dns action.
		"""
		try :
			return self._actionname
		except Exception as e:
			raise e

	@actionname.setter
	def actionname(self, actionname) :
		r"""Name of the dns action.
		"""
		try :
			self._actionname = actionname
		except Exception as e:
			raise e

	@property
	def actiontype(self) :
		r"""The type of DNS action that is being configured.<br/>Possible values = ViewName, GslbPrefLoc, noop, Drop, Cache_Bypass, Rewrite_Response.
		"""
		try :
			return self._actiontype
		except Exception as e:
			raise e

	@actiontype.setter
	def actiontype(self, actiontype) :
		r"""The type of DNS action that is being configured.<br/>Possible values = ViewName, GslbPrefLoc, noop, Drop, Cache_Bypass, Rewrite_Response
		"""
		try :
			self._actiontype = actiontype
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""List of IP address to be returned in case of rewrite_response actiontype. They can be of IPV4 or IPV6 type.
		In case of set command We will remove all the IP address previously present in the action and will add new once given in set dns action command.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""List of IP address to be returned in case of rewrite_response actiontype. They can be of IPV4 or IPV6 type.
		In case of set command We will remove all the IP address previously present in the action and will add new once given in set dns action command.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Time to live, in seconds.<br/>Default value: 3600<br/>Maximum length =  2147483647.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Time to live, in seconds.<br/>Default value: 3600<br/>Maximum length =  2147483647
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def viewname(self) :
		r"""The view name that must be used for the given action.
		"""
		try :
			return self._viewname
		except Exception as e:
			raise e

	@viewname.setter
	def viewname(self, viewname) :
		r"""The view name that must be used for the given action.
		"""
		try :
			self._viewname = viewname
		except Exception as e:
			raise e

	@property
	def preferredloclist(self) :
		r"""The location list in priority order used for the given action.<br/>Minimum length =  1.
		"""
		try :
			return self._preferredloclist
		except Exception as e:
			raise e

	@preferredloclist.setter
	def preferredloclist(self, preferredloclist) :
		r"""The location list in priority order used for the given action.<br/>Minimum length =  1
		"""
		try :
			self._preferredloclist = preferredloclist
		except Exception as e:
			raise e

	@property
	def dnsprofilename(self) :
		r"""Name of the DNS profile to be associated with the transaction for which the action is chosen.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._dnsprofilename
		except Exception as e:
			raise e

	@dnsprofilename.setter
	def dnsprofilename(self, dnsprofilename) :
		r"""Name of the DNS profile to be associated with the transaction for which the action is chosen.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._dnsprofilename = dnsprofilename
		except Exception as e:
			raise e

	@property
	def drop(self) :
		r"""The dns packet must be dropped.<br/>Possible values = YES, NO.
		"""
		try :
			return self._drop
		except Exception as e:
			raise e

	@property
	def cachebypass(self) :
		r"""By pass dns cache for this.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cachebypass
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether DNS action is default or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(dnsaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsaction
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.actionname is not None :
				return str(self.actionname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = dnsaction()
		addresource.actionname = resource.actionname
		addresource.actiontype = resource.actiontype
		addresource.ipaddress = resource.ipaddress
		addresource.ttl = resource.ttl
		addresource.viewname = resource.viewname
		addresource.preferredloclist = resource.preferredloclist
		addresource.dnsprofilename = resource.dnsprofilename
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add dnsaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsaction() for _ in range(len(resource))]
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
		deleteresource = dnsaction()
		deleteresource.actionname = resource.actionname
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnsaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.actionname = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].actionname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsaction() for _ in range(len(resource))]
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
		updateresource = dnsaction()
		updateresource.actionname = resource.actionname
		updateresource.ipaddress = resource.ipaddress
		updateresource.ttl = resource.ttl
		updateresource.viewname = resource.viewname
		updateresource.preferredloclist = resource.preferredloclist
		updateresource.dnsprofilename = resource.dnsprofilename
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update dnsaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnsaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnsaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnsaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.actionname = resource
				else :
					unsetresource.actionname = resource.actionname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].actionname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnsaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].actionname = resource[i].actionname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnsaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnsaction()
					obj.actionname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnsaction() for _ in range(len(name))]
						obj = [dnsaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnsaction()
							obj[i].actionname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnsaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnsaction resources configured on NetScaler.
		"""
		try :
			obj = dnsaction()
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
		r""" Use this API to count filtered the set of dnsaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cachebypass:
		YES = "YES"
		NO = "NO"

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

	class Actiontype:
		ViewName = "ViewName"
		GslbPrefLoc = "GslbPrefLoc"
		noop = "noop"
		Drop = "Drop"
		Cache_Bypass = "Cache_Bypass"
		Rewrite_Response = "Rewrite_Response"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Drop:
		YES = "YES"
		NO = "NO"

class dnsaction_response(base_response) :
	def __init__(self, length=1) :
		self.dnsaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsaction = [dnsaction() for _ in range(length)]

