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

class locationfile6(base_resource) :
	""" Configuration for location file6 resource. """
	def __init__(self) :
		self._Locationfile = None
		self._format = None
		self._src = None
		self.___count = None

	@property
	def Locationfile(self) :
		r"""Name of the IPv6 location file, with or without absolute path. If the path is not included, the default path (/var/netscaler/locdb) is assumed. In a high availability setup, the static database must be stored in the same location on both Citrix ADCs.<br/>Minimum length =  1.
		"""
		try :
			return self._Locationfile
		except Exception as e:
			raise e

	@Locationfile.setter
	def Locationfile(self, Locationfile) :
		r"""Name of the IPv6 location file, with or without absolute path. If the path is not included, the default path (/var/netscaler/locdb) is assumed. In a high availability setup, the static database must be stored in the same location on both Citrix ADCs.<br/>Minimum length =  1
		"""
		try :
			self._Locationfile = Locationfile
		except Exception as e:
			raise e

	@property
	def format(self) :
		r"""Format of the IPv6 location file. Required for the Citrix ADC to identify how to read the location file.<br/>Default value: netscaler6<br/>Possible values = netscaler6, geoip-country6.
		"""
		try :
			return self._format
		except Exception as e:
			raise e

	@format.setter
	def format(self, format) :
		r"""Format of the IPv6 location file. Required for the Citrix ADC to identify how to read the location file.<br/>Default value: netscaler6<br/>Possible values = netscaler6, geoip-country6
		"""
		try :
			self._format = format
		except Exception as e:
			raise e

	@property
	def src(self) :
		r"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		r"""URL \(protocol, host, path, and file name\) from where the location file will be imported.
		NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(locationfile6_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.locationfile6
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
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = locationfile6()
		addresource.Locationfile = resource.Locationfile
		addresource.format = resource.format
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add locationfile6.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ locationfile6() for _ in range(len(resource))]
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
		deleteresource = locationfile6()
		return deleteresource

	@classmethod
	def delete(cls, client, resource="") :
		r""" Use this API to delete locationfile6.
		"""
		try :
			if type(resource) is not list :
				deleteresource = locationfile6()
				return deleteresource.delete_resource(client)
			else :
				if (resource and len(resource) > 0) :
					deleteresources = [ locationfile6() for _ in range(len(resource))]
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		r""" Use this API to Import locationfile6.
		"""
		try :
			if type(resource) is not list :
				Importresource = locationfile6()
				Importresource.Locationfile = resource.Locationfile
				Importresource.src = resource.src
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ locationfile6() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].Locationfile = resource[i].Locationfile
						Importresources[i].src = resource[i].src
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the locationfile6 resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = locationfile6()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of locationfile6 resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = locationfile6()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the locationfile6 resources configured on NetScaler.
		"""
		try :
			obj = locationfile6()
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
		r""" Use this API to count filtered the set of locationfile6 resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = locationfile6()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Format:
		netscaler6 = "netscaler6"
		geoip_country6 = "geoip-country6"

class locationfile6_response(base_response) :
	def __init__(self, length=1) :
		self.locationfile6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.locationfile6 = [locationfile6() for _ in range(length)]

