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

class appfwjsoncontenttype(base_resource) :
	""" Configuration for JSON content type resource. """
	def __init__(self) :
		self._jsoncontenttypevalue = None
		self._isregex = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def jsoncontenttypevalue(self) :
		r"""Content type to be classified as JSON.<br/>Minimum length =  1.
		"""
		try :
			return self._jsoncontenttypevalue
		except Exception as e:
			raise e

	@jsoncontenttypevalue.setter
	def jsoncontenttypevalue(self, jsoncontenttypevalue) :
		r"""Content type to be classified as JSON.<br/>Minimum length =  1
		"""
		try :
			self._jsoncontenttypevalue = jsoncontenttypevalue
		except Exception as e:
			raise e

	@property
	def isregex(self) :
		r"""Is json content type a regular expression?.<br/>Default value: NOTREGEX<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isregex
		except Exception as e:
			raise e

	@isregex.setter
	def isregex(self, isregex) :
		r"""Is json content type a regular expression?.<br/>Default value: NOTREGEX<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isregex = isregex
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if jsoncontenttype is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(appfwjsoncontenttype_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwjsoncontenttype
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.jsoncontenttypevalue is not None :
				return str(self.jsoncontenttypevalue)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = appfwjsoncontenttype()
		addresource.jsoncontenttypevalue = resource.jsoncontenttypevalue
		addresource.isregex = resource.isregex
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add appfwjsoncontenttype.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ appfwjsoncontenttype() for _ in range(len(resource))]
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
		deleteresource = appfwjsoncontenttype()
		deleteresource.jsoncontenttypevalue = resource.jsoncontenttypevalue
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete appfwjsoncontenttype.
		"""
		try :
			if type(resource) is not list :
				deleteresource = appfwjsoncontenttype()
				if type(resource) !=  type(deleteresource):
					deleteresource.jsoncontenttypevalue = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwjsoncontenttype() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].jsoncontenttypevalue = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ appfwjsoncontenttype() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwjsoncontenttype resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwjsoncontenttype()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = appfwjsoncontenttype()
					obj.jsoncontenttypevalue = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [appfwjsoncontenttype() for _ in range(len(name))]
						obj = [appfwjsoncontenttype() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = appfwjsoncontenttype()
							obj[i].jsoncontenttypevalue = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of appfwjsoncontenttype resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwjsoncontenttype()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the appfwjsoncontenttype resources configured on NetScaler.
		"""
		try :
			obj = appfwjsoncontenttype()
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
		r""" Use this API to count filtered the set of appfwjsoncontenttype resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwjsoncontenttype()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

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

class appfwjsoncontenttype_response(base_response) :
	def __init__(self, length=1) :
		self.appfwjsoncontenttype = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwjsoncontenttype = [appfwjsoncontenttype() for _ in range(length)]

