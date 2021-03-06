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

class lsnappsprofile(base_resource) :
	""" Configuration for LSN Application Profile resource. """
	def __init__(self) :
		self._appsprofilename = None
		self._transportprotocol = None
		self._ippooling = None
		self._mapping = None
		self._filtering = None
		self._tcpproxy = None
		self._td = None
		self._l2info = None
		self.___count = None

	@property
	def appsprofilename(self) :
		r"""Name for the LSN application profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN application profile is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn application profile1" or 'lsn application profile1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._appsprofilename
		except Exception as e:
			raise e

	@appsprofilename.setter
	def appsprofilename(self, appsprofilename) :
		r"""Name for the LSN application profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN application profile is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn application profile1" or 'lsn application profile1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._appsprofilename = appsprofilename
		except Exception as e:
			raise e

	@property
	def transportprotocol(self) :
		r"""Name of the protocol for which the parameters of this LSN application profile applies.<br/>Possible values = TCP, UDP, ICMP.
		"""
		try :
			return self._transportprotocol
		except Exception as e:
			raise e

	@transportprotocol.setter
	def transportprotocol(self, transportprotocol) :
		r"""Name of the protocol for which the parameters of this LSN application profile applies.<br/>Possible values = TCP, UDP, ICMP
		"""
		try :
			self._transportprotocol = transportprotocol
		except Exception as e:
			raise e

	@property
	def ippooling(self) :
		r"""NAT IP address allocation options for sessions associated with the same subscriber.
		Available options function as follows:
		* Paired - The Citrix ADC allocates the same NAT IP address for all sessions associated with the same subscriber. When all the ports of a NAT IP address are used in LSN sessions (for same or multiple subscribers), the Citrix ADC ADC drops any new connection from the subscriber.
		* Random - The Citrix ADC allocates random NAT IP addresses, from the pool, for different sessions associated with the same subscriber.
		This parameter is applicable to dynamic NAT allocation only.<br/>Default value: RANDOM<br/>Possible values = PAIRED, RANDOM.
		"""
		try :
			return self._ippooling
		except Exception as e:
			raise e

	@ippooling.setter
	def ippooling(self, ippooling) :
		r"""NAT IP address allocation options for sessions associated with the same subscriber.
		Available options function as follows:
		* Paired - The Citrix ADC allocates the same NAT IP address for all sessions associated with the same subscriber. When all the ports of a NAT IP address are used in LSN sessions (for same or multiple subscribers), the Citrix ADC ADC drops any new connection from the subscriber.
		* Random - The Citrix ADC allocates random NAT IP addresses, from the pool, for different sessions associated with the same subscriber.
		This parameter is applicable to dynamic NAT allocation only.<br/>Default value: RANDOM<br/>Possible values = PAIRED, RANDOM
		"""
		try :
			self._ippooling = ippooling
		except Exception as e:
			raise e

	@property
	def mapping(self) :
		r"""Type of LSN mapping to apply to subsequent packets originating from the same subscriber IP address and port.
		Consider an example of an LSN mapping that includes the mapping of the subscriber IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
		Available options function as follows: 
		* ENDPOINT-INDEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same subscriber IP address and port (X:x) to any external IP address and port. 
		* ADDRESS-DEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same subscriber IP address and port (X:x) to the same external IP address (Y), regardless of the external port.
		* ADDRESS-PORT-DEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same internal IP address and port (X:x) to the same external IP address and port (Y:y) while the mapping is still active.<br/>Default value: ADDRESS-PORT-DEPENDENT<br/>Possible values = ENDPOINT-INDEPENDENT, ADDRESS-DEPENDENT, ADDRESS-PORT-DEPENDENT.
		"""
		try :
			return self._mapping
		except Exception as e:
			raise e

	@mapping.setter
	def mapping(self, mapping) :
		r"""Type of LSN mapping to apply to subsequent packets originating from the same subscriber IP address and port.
		Consider an example of an LSN mapping that includes the mapping of the subscriber IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
		Available options function as follows: 
		* ENDPOINT-INDEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same subscriber IP address and port (X:x) to any external IP address and port. 
		* ADDRESS-DEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same subscriber IP address and port (X:x) to the same external IP address (Y), regardless of the external port.
		* ADDRESS-PORT-DEPENDENT - Reuse the LSN mapping for subsequent packets sent from the same internal IP address and port (X:x) to the same external IP address and port (Y:y) while the mapping is still active.<br/>Default value: ADDRESS-PORT-DEPENDENT<br/>Possible values = ENDPOINT-INDEPENDENT, ADDRESS-DEPENDENT, ADDRESS-PORT-DEPENDENT
		"""
		try :
			self._mapping = mapping
		except Exception as e:
			raise e

	@property
	def filtering(self) :
		r"""Type of filter to apply to packets originating from external hosts.
		Consider an example of an LSN mapping that includes the mapping of subscriber IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
		Available options function as follows:
		* ENDPOINT INDEPENDENT - Filters out only packets not destined to the subscriber IP address and port X:x, regardless of the external host IP address and port source (Z:z).  The Citrix ADC forwards any packets destined to X:x.  In other words, sending packets from the subscriber to any external IP address is sufficient to allow packets from any external hosts to the subscriber.
		* ADDRESS DEPENDENT - Filters out packets not destined to subscriber IP address and port X:x.  In addition, the ADC filters out packets from Y:y destined for the subscriber (X:x) if the client has not previously sent packets to Y:anyport (external port independent). In other words, receiving packets from a specific external host requires that the subscriber first send packets to that specific external host's IP address.
		* ADDRESS PORT DEPENDENT (the default) - Filters out  packets not destined to subscriber IP address and port (X:x).  In addition, the Citrix ADC filters out packets from Y:y destined for the subscriber (X:x) if the subscriber has not previously sent packets to Y:y.  In other words, receiving packets from a specific external host requires that the subscriber first send packets first to that external IP address and port.<br/>Default value: ADDRESS-PORT-DEPENDENT<br/>Possible values = ENDPOINT-INDEPENDENT, ADDRESS-DEPENDENT, ADDRESS-PORT-DEPENDENT.
		"""
		try :
			return self._filtering
		except Exception as e:
			raise e

	@filtering.setter
	def filtering(self, filtering) :
		r"""Type of filter to apply to packets originating from external hosts.
		Consider an example of an LSN mapping that includes the mapping of subscriber IP:port (X:x), NAT IP:port (N:n), and external host IP:port (Y:y).
		Available options function as follows:
		* ENDPOINT INDEPENDENT - Filters out only packets not destined to the subscriber IP address and port X:x, regardless of the external host IP address and port source (Z:z).  The Citrix ADC forwards any packets destined to X:x.  In other words, sending packets from the subscriber to any external IP address is sufficient to allow packets from any external hosts to the subscriber.
		* ADDRESS DEPENDENT - Filters out packets not destined to subscriber IP address and port X:x.  In addition, the ADC filters out packets from Y:y destined for the subscriber (X:x) if the client has not previously sent packets to Y:anyport (external port independent). In other words, receiving packets from a specific external host requires that the subscriber first send packets to that specific external host's IP address.
		* ADDRESS PORT DEPENDENT (the default) - Filters out  packets not destined to subscriber IP address and port (X:x).  In addition, the Citrix ADC filters out packets from Y:y destined for the subscriber (X:x) if the subscriber has not previously sent packets to Y:y.  In other words, receiving packets from a specific external host requires that the subscriber first send packets first to that external IP address and port.<br/>Default value: ADDRESS-PORT-DEPENDENT<br/>Possible values = ENDPOINT-INDEPENDENT, ADDRESS-DEPENDENT, ADDRESS-PORT-DEPENDENT
		"""
		try :
			self._filtering = filtering
		except Exception as e:
			raise e

	@property
	def tcpproxy(self) :
		r"""Enable TCP proxy, which enables the Citrix ADC to optimize the  TCP traffic by using Layer 4 features.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpproxy
		except Exception as e:
			raise e

	@tcpproxy.setter
	def tcpproxy(self, tcpproxy) :
		r"""Enable TCP proxy, which enables the Citrix ADC to optimize the  TCP traffic by using Layer 4 features.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpproxy = tcpproxy
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""ID of the traffic domain through which the Citrix ADC sends the outbound traffic after performing LSN. 
		If you do not specify an ID, the ADC sends the outbound traffic through the default traffic domain, which has an ID of 0.<br/>Default value: 4095.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""ID of the traffic domain through which the Citrix ADC sends the outbound traffic after performing LSN. 
		If you do not specify an ID, the ADC sends the outbound traffic through the default traffic domain, which has an ID of 0.<br/>Default value: 4095
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def l2info(self) :
		r"""Enable l2info by creating natpcbs for LSN, which enables the Citrix ADC to use L2CONN/MBF with LSN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._l2info
		except Exception as e:
			raise e

	@l2info.setter
	def l2info(self, l2info) :
		r"""Enable l2info by creating natpcbs for LSN, which enables the Citrix ADC to use L2CONN/MBF with LSN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._l2info = l2info
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnappsprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnappsprofile
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.appsprofilename is not None :
				return str(self.appsprofilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = lsnappsprofile()
		addresource.appsprofilename = resource.appsprofilename
		addresource.transportprotocol = resource.transportprotocol
		addresource.ippooling = resource.ippooling
		addresource.mapping = resource.mapping
		addresource.filtering = resource.filtering
		addresource.tcpproxy = resource.tcpproxy
		addresource.td = resource.td
		addresource.l2info = resource.l2info
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lsnappsprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lsnappsprofile() for _ in range(len(resource))]
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
		deleteresource = lsnappsprofile()
		deleteresource.appsprofilename = resource.appsprofilename
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lsnappsprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lsnappsprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.appsprofilename = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnappsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].appsprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lsnappsprofile() for _ in range(len(resource))]
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
		updateresource = lsnappsprofile()
		updateresource.appsprofilename = resource.appsprofilename
		updateresource.ippooling = resource.ippooling
		updateresource.mapping = resource.mapping
		updateresource.filtering = resource.filtering
		updateresource.tcpproxy = resource.tcpproxy
		updateresource.td = resource.td
		updateresource.l2info = resource.l2info
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lsnappsprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lsnappsprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lsnappsprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lsnappsprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.appsprofilename = resource
				else :
					unsetresource.appsprofilename = resource.appsprofilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnappsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].appsprofilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ lsnappsprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].appsprofilename = resource[i].appsprofilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lsnappsprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lsnappsprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lsnappsprofile()
					obj.appsprofilename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lsnappsprofile() for _ in range(len(name))]
						obj = [lsnappsprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lsnappsprofile()
							obj[i].appsprofilename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lsnappsprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnappsprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lsnappsprofile resources configured on NetScaler.
		"""
		try :
			obj = lsnappsprofile()
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
		r""" Use this API to count filtered the set of lsnappsprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnappsprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Mapping:
		ENDPOINT_INDEPENDENT = "ENDPOINT-INDEPENDENT"
		ADDRESS_DEPENDENT = "ADDRESS-DEPENDENT"
		ADDRESS_PORT_DEPENDENT = "ADDRESS-PORT-DEPENDENT"

	class L2info:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Filtering:
		ENDPOINT_INDEPENDENT = "ENDPOINT-INDEPENDENT"
		ADDRESS_DEPENDENT = "ADDRESS-DEPENDENT"
		ADDRESS_PORT_DEPENDENT = "ADDRESS-PORT-DEPENDENT"

	class Ippooling:
		PAIRED = "PAIRED"
		RANDOM = "RANDOM"

	class Tcpproxy:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Transportprotocol:
		TCP = "TCP"
		UDP = "UDP"
		ICMP = "ICMP"

class lsnappsprofile_response(base_response) :
	def __init__(self, length=1) :
		self.lsnappsprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnappsprofile = [lsnappsprofile() for _ in range(length)]

