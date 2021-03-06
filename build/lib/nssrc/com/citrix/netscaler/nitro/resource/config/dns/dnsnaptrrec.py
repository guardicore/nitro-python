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

class dnsnaptrrec(base_resource) :
	""" Configuration for NAPTR record resource. """
	def __init__(self) :
		self._domain = None
		self._order = None
		self._preference = None
		self._flags = None
		self._services = None
		self._regexp = None
		self._replacement = None
		self._ttl = None
		self._recordid = None
		self._ecssubnet = None
		self._type = None
		self._nodeid = None
		self._authtype = None
		self._vservername = None
		self.___count = None

	@property
	def domain(self) :
		r"""Name of the domain for the NAPTR record.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		r"""Name of the domain for the NAPTR record.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def order(self) :
		r"""An integer specifying the order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of Rules. The ordering is from lowest to highest.<br/>Maximum length =  65535.
		"""
		try :
			return self._order
		except Exception as e:
			raise e

	@order.setter
	def order(self, order) :
		r"""An integer specifying the order in which the NAPTR records MUST be processed in order to accurately represent the ordered list of Rules. The ordering is from lowest to highest.<br/>Maximum length =  65535
		"""
		try :
			self._order = order
		except Exception as e:
			raise e

	@property
	def preference(self) :
		r"""An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the number, higher the preference.<br/>Maximum length =  65535.
		"""
		try :
			return self._preference
		except Exception as e:
			raise e

	@preference.setter
	def preference(self, preference) :
		r"""An integer specifying the preference of this NAPTR among NAPTR records having same order. lower the number, higher the preference.<br/>Maximum length =  65535
		"""
		try :
			self._preference = preference
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""flags for this NAPTR.<br/>Maximum length =  255.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@flags.setter
	def flags(self, flags) :
		r"""flags for this NAPTR.<br/>Maximum length =  255
		"""
		try :
			self._flags = flags
		except Exception as e:
			raise e

	@property
	def services(self) :
		r"""Service Parameters applicable to this delegation path.<br/>Maximum length =  255.
		"""
		try :
			return self._services
		except Exception as e:
			raise e

	@services.setter
	def services(self, services) :
		r"""Service Parameters applicable to this delegation path.<br/>Maximum length =  255
		"""
		try :
			self._services = services
		except Exception as e:
			raise e

	@property
	def regexp(self) :
		r"""The regular expression, that specifies the substitution expression for this NAPTR.<br/>Maximum length =  255.
		"""
		try :
			return self._regexp
		except Exception as e:
			raise e

	@regexp.setter
	def regexp(self, regexp) :
		r"""The regular expression, that specifies the substitution expression for this NAPTR.<br/>Maximum length =  255
		"""
		try :
			self._regexp = regexp
		except Exception as e:
			raise e

	@property
	def replacement(self) :
		r"""The replacement domain name for this NAPTR.<br/>Maximum length =  255.
		"""
		try :
			return self._replacement
		except Exception as e:
			raise e

	@replacement.setter
	def replacement(self, replacement) :
		r"""The replacement domain name for this NAPTR.<br/>Maximum length =  255
		"""
		try :
			self._replacement = replacement
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the Citrix ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the Citrix ADC uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def recordid(self) :
		r"""Unique, internally generated record ID. View the details of the naptr record to obtain its record ID. Records can be removed by either specifying the domain name and record id OR by specifying
		domain name and all other naptr record attributes as was supplied during the add command.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._recordid
		except Exception as e:
			raise e

	@recordid.setter
	def recordid(self, recordid) :
		r"""Unique, internally generated record ID. View the details of the naptr record to obtain its record ID. Records can be removed by either specifying the domain name and record id OR by specifying
		domain name and all other naptr record attributes as was supplied during the add command.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._recordid = recordid
		except Exception as e:
			raise e

	@property
	def ecssubnet(self) :
		r"""Subnet for which the cached NAPTR record need to be removed.
		"""
		try :
			return self._ecssubnet
		except Exception as e:
			raise e

	@ecssubnet.setter
	def ecssubnet(self, ecssubnet) :
		r"""Subnet for which the cached NAPTR record need to be removed.
		"""
		try :
			self._ecssubnet = ecssubnet
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of records to display. Available settings function as follows:
		* ADNS - Display all authoritative address records.
		* PROXY - Display all proxy address records.
		* ALL - Display all address records.<br/>Default value: ADNS<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of records to display. Available settings function as follows:
		* ADNS - Display all authoritative address records.
		* PROXY - Display all proxy address records.
		* ALL - Display all address records.<br/>Default value: ADNS<br/>Possible values = ALL, ADNS, PROXY
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
	def authtype(self) :
		r"""Authentication type.<br/>Possible values = ALL, ADNS, PROXY.
		"""
		try :
			return self._authtype
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		r"""Virtual server name.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnsnaptrrec_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnsnaptrrec
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.domain is not None :
				return str(self.domain)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = dnsnaptrrec()
		addresource.domain = resource.domain
		addresource.order = resource.order
		addresource.preference = resource.preference
		addresource.flags = resource.flags
		addresource.services = resource.services
		addresource.regexp = resource.regexp
		addresource.replacement = resource.replacement
		addresource.ttl = resource.ttl
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add dnsnaptrrec.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnsnaptrrec() for _ in range(len(resource))]
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
		deleteresource = dnsnaptrrec()
		deleteresource.domain = resource.domain
		deleteresource.order = resource.order
		deleteresource.recordid = resource.recordid
		deleteresource.ecssubnet = resource.ecssubnet
		deleteresource.preference = resource.preference
		deleteresource.flags = resource.flags
		deleteresource.services = resource.services
		deleteresource.regexp = resource.regexp
		deleteresource.replacement = resource.replacement
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnsnaptrrec.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnsnaptrrec()
				if type(resource) !=  type(deleteresource):
					deleteresource.domain = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsnaptrrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].domain = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnsnaptrrec() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnsnaptrrec resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnsnaptrrec()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnsnaptrrec()
					obj.domain = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnsnaptrrec() for _ in range(len(name))]
						obj = [dnsnaptrrec() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnsnaptrrec()
							obj[i].domain = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the dnsnaptrrec resources that are configured on netscaler.
	# This uses dnsnaptrrec_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = dnsnaptrrec()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnsnaptrrec resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnaptrrec()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnsnaptrrec resources configured on NetScaler.
		"""
		try :
			obj = dnsnaptrrec()
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
		r""" Use this API to count filtered the set of dnsnaptrrec resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnsnaptrrec()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Authtype:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

	class Type:
		ALL = "ALL"
		ADNS = "ADNS"
		PROXY = "PROXY"

class dnsnaptrrec_response(base_response) :
	def __init__(self, length=1) :
		self.dnsnaptrrec = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnsnaptrrec = [dnsnaptrrec() for _ in range(length)]

