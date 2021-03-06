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

class lsnstatic(base_resource) :
	""" Configuration for static mapping resource. """
	def __init__(self) :
		self._name = None
		self._transportprotocol = None
		self._subscrip = None
		self._subscrport = None
		self._network6 = None
		self._td = None
		self._natip = None
		self._natport = None
		self._destip = None
		self._dsttd = None
		self._nattype = None
		self._status = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the LSN static mapping entry. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn static1" or 'lsn static1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the LSN static mapping entry. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN group is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn static1" or 'lsn static1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def transportprotocol(self) :
		r"""Protocol for the LSN mapping entry.<br/>Possible values = TCP, UDP, ICMP, ALL.
		"""
		try :
			return self._transportprotocol
		except Exception as e:
			raise e

	@transportprotocol.setter
	def transportprotocol(self, transportprotocol) :
		r"""Protocol for the LSN mapping entry.<br/>Possible values = TCP, UDP, ICMP, ALL
		"""
		try :
			self._transportprotocol = transportprotocol
		except Exception as e:
			raise e

	@property
	def subscrip(self) :
		r"""IPv4(NAT44 & DS-Lite)/IPv6(NAT64) address of an LSN subscriber for the LSN static mapping entry.
		"""
		try :
			return self._subscrip
		except Exception as e:
			raise e

	@subscrip.setter
	def subscrip(self, subscrip) :
		r"""IPv4(NAT44 & DS-Lite)/IPv6(NAT64) address of an LSN subscriber for the LSN static mapping entry.
		"""
		try :
			self._subscrip = subscrip
		except Exception as e:
			raise e

	@property
	def subscrport(self) :
		r"""Port of the LSN subscriber for the LSN mapping entry. * represents all ports being used. Used in case of static wildcard.<br/>Maximum length =  65535<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._subscrport
		except Exception as e:
			raise e

	@subscrport.setter
	def subscrport(self, subscrport) :
		r"""Port of the LSN subscriber for the LSN mapping entry. * represents all ports being used. Used in case of static wildcard.<br/>Maximum length =  65535<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._subscrport = subscrport
		except Exception as e:
			raise e

	@property
	def network6(self) :
		r"""B4 address in DS-Lite setup.<br/>Minimum length =  1.
		"""
		try :
			return self._network6
		except Exception as e:
			raise e

	@network6.setter
	def network6(self, network6) :
		r"""B4 address in DS-Lite setup.<br/>Minimum length =  1
		"""
		try :
			self._network6 = network6
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""ID of the traffic domain to which the subscriber belongs. 
		If you do not specify an ID, the subscriber is assumed to be a part of the default traffic domain.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""ID of the traffic domain to which the subscriber belongs. 
		If you do not specify an ID, the subscriber is assumed to be a part of the default traffic domain.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def natip(self) :
		r"""IPv4 address, already existing on the Citrix ADC as type LSN, to be used as NAT IP address for this mapping entry.
		"""
		try :
			return self._natip
		except Exception as e:
			raise e

	@natip.setter
	def natip(self, natip) :
		r"""IPv4 address, already existing on the Citrix ADC as type LSN, to be used as NAT IP address for this mapping entry.
		"""
		try :
			self._natip = natip
		except Exception as e:
			raise e

	@property
	def natport(self) :
		r"""NAT port for this LSN mapping entry. * represents all ports being used. Used in case of static wildcard.<br/>Maximum length =  65535<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._natport
		except Exception as e:
			raise e

	@natport.setter
	def natport(self, natport) :
		r"""NAT port for this LSN mapping entry. * represents all ports being used. Used in case of static wildcard.<br/>Maximum length =  65535<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._natport = natport
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""Destination IP address for the LSN mapping entry.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		r"""Destination IP address for the LSN mapping entry.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def dsttd(self) :
		r"""ID of the traffic domain through which the destination IP address for this LSN mapping entry is reachable from the Citrix ADC.
		If you do not specify an ID, the destination IP address is assumed to be reachable through the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094.
		"""
		try :
			return self._dsttd
		except Exception as e:
			raise e

	@dsttd.setter
	def dsttd(self, dsttd) :
		r"""ID of the traffic domain through which the destination IP address for this LSN mapping entry is reachable from the Citrix ADC.
		If you do not specify an ID, the destination IP address is assumed to be reachable through the default traffic domain, which has an ID of 0.<br/>Default value: 0<br/>Maximum length =  4094
		"""
		try :
			self._dsttd = dsttd
		except Exception as e:
			raise e

	@property
	def nattype(self) :
		r"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite, NAT64.
		"""
		try :
			return self._nattype
		except Exception as e:
			raise e

	@nattype.setter
	def nattype(self, nattype) :
		r"""Type of sessions to be displayed.<br/>Possible values = NAT44, DS-Lite, NAT64
		"""
		try :
			self._nattype = nattype
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""The status of the Mapping. Status could be Inactive, if mapping addition failed due to already existing dynamic/static mapping, port allocation failure.<br/>Possible values = ACTIVE, INACTIVE.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnstatic_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnstatic
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
		addresource = lsnstatic()
		addresource.name = resource.name
		addresource.transportprotocol = resource.transportprotocol
		addresource.subscrip = resource.subscrip
		addresource.subscrport = resource.subscrport
		addresource.network6 = resource.network6
		addresource.td = resource.td
		addresource.natip = resource.natip
		addresource.natport = resource.natport
		addresource.destip = resource.destip
		addresource.dsttd = resource.dsttd
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lsnstatic.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnstatic() for _ in range(len(resource))]
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
		deleteresource = lsnstatic()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lsnstatic.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnstatic()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnstatic() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnstatic() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lsnstatic resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnstatic()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lsnstatic()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lsnstatic() for _ in range(len(name))]
						obj = [lsnstatic() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lsnstatic()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the lsnstatic resources that are configured on netscaler.
	# This uses lsnstatic_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lsnstatic resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lsnstatic resources configured on NetScaler.
		"""
		try :
			obj = lsnstatic()
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
		r""" Use this API to count filtered the set of lsnstatic resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnstatic()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Transportprotocol:
		TCP = "TCP"
		UDP = "UDP"
		ICMP = "ICMP"
		ALL = "ALL"

	class Status:
		ACTIVE = "ACTIVE"
		INACTIVE = "INACTIVE"

	class Nattype:
		NAT44 = "NAT44"
		DS_Lite = "DS-Lite"
		NAT64 = "NAT64"

class lsnstatic_response(base_response) :
	def __init__(self, length=1) :
		self.lsnstatic = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnstatic = [lsnstatic() for _ in range(length)]

