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

class dnskey(base_resource) :
	""" Configuration for dns key resource. """
	def __init__(self) :
		self._keyname = None
		self._publickey = None
		self._privatekey = None
		self._expires = None
		self._units1 = None
		self._notificationperiod = None
		self._units2 = None
		self._ttl = None
		self._password = None
		self._zonename = None
		self._keytype = None
		self._algorithm = None
		self._keysize = None
		self._filenameprefix = None
		self._src = None
		self.___count = None

	@property
	def keyname(self) :
		r"""Name of the public-private key pair to publish in the zone.<br/>Minimum length =  1.
		"""
		try :
			return self._keyname
		except Exception as e:
			raise e

	@keyname.setter
	def keyname(self, keyname) :
		r"""Name of the public-private key pair to publish in the zone.<br/>Minimum length =  1
		"""
		try :
			self._keyname = keyname
		except Exception as e:
			raise e

	@property
	def publickey(self) :
		r"""File name of the public key.
		"""
		try :
			return self._publickey
		except Exception as e:
			raise e

	@publickey.setter
	def publickey(self, publickey) :
		r"""File name of the public key.
		"""
		try :
			self._publickey = publickey
		except Exception as e:
			raise e

	@property
	def privatekey(self) :
		r"""File name of the private key.
		"""
		try :
			return self._privatekey
		except Exception as e:
			raise e

	@privatekey.setter
	def privatekey(self, privatekey) :
		r"""File name of the private key.
		"""
		try :
			self._privatekey = privatekey
		except Exception as e:
			raise e

	@property
	def expires(self) :
		r"""Time period for which to consider the key valid, after the key is used to sign a zone.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  32767.
		"""
		try :
			return self._expires
		except Exception as e:
			raise e

	@expires.setter
	def expires(self, expires) :
		r"""Time period for which to consider the key valid, after the key is used to sign a zone.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  32767
		"""
		try :
			self._expires = expires
		except Exception as e:
			raise e

	@property
	def units1(self) :
		r"""Units for the expiry period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS.
		"""
		try :
			return self._units1
		except Exception as e:
			raise e

	@units1.setter
	def units1(self, units1) :
		r"""Units for the expiry period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS
		"""
		try :
			self._units1 = units1
		except Exception as e:
			raise e

	@property
	def notificationperiod(self) :
		r"""Time at which to generate notification of key expiration, specified as number of days, hours, or minutes before expiry. Must be less than the expiry period. The notification is an SNMP trap sent to an SNMP manager. To enable the appliance to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  32767.
		"""
		try :
			return self._notificationperiod
		except Exception as e:
			raise e

	@notificationperiod.setter
	def notificationperiod(self, notificationperiod) :
		r"""Time at which to generate notification of key expiration, specified as number of days, hours, or minutes before expiry. Must be less than the expiry period. The notification is an SNMP trap sent to an SNMP manager. To enable the appliance to send the trap, enable the DNSKEY-EXPIRY SNMP alarm.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  32767
		"""
		try :
			self._notificationperiod = notificationperiod
		except Exception as e:
			raise e

	@property
	def units2(self) :
		r"""Units for the notification period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS.
		"""
		try :
			return self._units2
		except Exception as e:
			raise e

	@units2.setter
	def units2(self, units2) :
		r"""Units for the notification period.<br/>Default value: DAYS<br/>Possible values = MINUTES, HOURS, DAYS
		"""
		try :
			self._units2 = units2
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Time to Live (TTL), in seconds, for the DNSKEY resource record created in the zone. TTL is the time for which the record must be cached by the DNS proxies. If the TTL is not specified, either the DNS zone's minimum TTL or the default value of 3600 is used.<br/>Default value: 3600<br/>Maximum length =  2147483647.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Time to Live (TTL), in seconds, for the DNSKEY resource record created in the zone. TTL is the time for which the record must be cached by the DNS proxies. If the TTL is not specified, either the DNS zone's minimum TTL or the default value of 3600 is used.<br/>Default value: 3600<br/>Maximum length =  2147483647
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Passphrase for reading the encrypted public/private DNS keys.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Passphrase for reading the encrypted public/private DNS keys.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def zonename(self) :
		r"""Name of the zone for which to create a key.<br/>Minimum length =  1.
		"""
		try :
			return self._zonename
		except Exception as e:
			raise e

	@zonename.setter
	def zonename(self, zonename) :
		r"""Name of the zone for which to create a key.<br/>Minimum length =  1
		"""
		try :
			self._zonename = zonename
		except Exception as e:
			raise e

	@property
	def keytype(self) :
		r"""Type of key to create.<br/>Default value: NS_DNSKEY_ZSK<br/>Possible values = KSK, KeySigningKey, ZSK, ZoneSigningKey.
		"""
		try :
			return self._keytype
		except Exception as e:
			raise e

	@keytype.setter
	def keytype(self, keytype) :
		r"""Type of key to create.<br/>Default value: NS_DNSKEY_ZSK<br/>Possible values = KSK, KeySigningKey, ZSK, ZoneSigningKey
		"""
		try :
			self._keytype = keytype
		except Exception as e:
			raise e

	@property
	def algorithm(self) :
		r"""Algorithm to generate for zone signing.<br/>Default value: NS_DNSKEYALGO_RSASHA1<br/>Possible values = RSASHA1, RSASHA256, RSASHA512.
		"""
		try :
			return self._algorithm
		except Exception as e:
			raise e

	@algorithm.setter
	def algorithm(self, algorithm) :
		r"""Algorithm to generate for zone signing.<br/>Default value: NS_DNSKEYALGO_RSASHA1<br/>Possible values = RSASHA1, RSASHA256, RSASHA512
		"""
		try :
			self._algorithm = algorithm
		except Exception as e:
			raise e

	@property
	def keysize(self) :
		r"""Size of the key, in bits.<br/>Default value: 512<br/>Minimum length =  1<br/>Maximum length =  4096.
		"""
		try :
			return self._keysize
		except Exception as e:
			raise e

	@keysize.setter
	def keysize(self, keysize) :
		r"""Size of the key, in bits.<br/>Default value: 512<br/>Minimum length =  1<br/>Maximum length =  4096
		"""
		try :
			self._keysize = keysize
		except Exception as e:
			raise e

	@property
	def filenameprefix(self) :
		r"""Common prefix for the names of the generated public and private key files and the Delegation Signer (DS) resource record. During key generation, the .key, .private, and .ds suffixes are appended automatically to the file name prefix to produce the names of the public key, the private key, and the DS record, respectively.
		"""
		try :
			return self._filenameprefix
		except Exception as e:
			raise e

	@filenameprefix.setter
	def filenameprefix(self, filenameprefix) :
		r"""Common prefix for the names of the generated public and private key files and the Delegation Signer (DS) resource record. During key generation, the .key, .private, and .ds suffixes are appended automatically to the file name prefix to produce the names of the public key, the private key, and the DS record, respectively.
		"""
		try :
			self._filenameprefix = filenameprefix
		except Exception as e:
			raise e

	@property
	def src(self) :
		r"""URL (protocol, host, path, and file name) from where the DNS key file will be imported. NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access. This is a mandatory argument.<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._src
		except Exception as e:
			raise e

	@src.setter
	def src(self, src) :
		r"""URL (protocol, host, path, and file name) from where the DNS key file will be imported. NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access. This is a mandatory argument.<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._src = src
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(dnskey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.dnskey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.keyname is not None :
				return str(self.keyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = dnskey()
		addresource.keyname = resource.keyname
		addresource.publickey = resource.publickey
		addresource.privatekey = resource.privatekey
		addresource.expires = resource.expires
		addresource.units1 = resource.units1
		addresource.notificationperiod = resource.notificationperiod
		addresource.units2 = resource.units2
		addresource.ttl = resource.ttl
		addresource.password = resource.password
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add dnskey.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def create(cls, client, resource) :
		r""" Use this API to create dnskey.
		"""
		try :
			if type(resource) is not list :
				createresource = dnskey()
				createresource.zonename = resource.zonename
				createresource.keytype = resource.keytype
				createresource.algorithm = resource.algorithm
				createresource.keysize = resource.keysize
				createresource.filenameprefix = resource.filenameprefix
				createresource.password = resource.password
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].zonename = resource[i].zonename
						createresources[i].keytype = resource[i].keytype
						createresources[i].algorithm = resource[i].algorithm
						createresources[i].keysize = resource[i].keysize
						createresources[i].filenameprefix = resource[i].filenameprefix
						createresources[i].password = resource[i].password
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = dnskey()
		updateresource.keyname = resource.keyname
		updateresource.expires = resource.expires
		updateresource.units1 = resource.units1
		updateresource.notificationperiod = resource.notificationperiod
		updateresource.units2 = resource.units2
		updateresource.ttl = resource.ttl
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update dnskey.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of dnskey resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = dnskey()
				if type(resource) !=  type(unsetresource):
					unsetresource.keyname = resource
				else :
					unsetresource.keyname = resource.keyname
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].keyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].keyname = resource[i].keyname
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = dnskey()
		deleteresource.keyname = resource.keyname
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete dnskey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = dnskey()
				if type(resource) !=  type(deleteresource):
					deleteresource.keyname = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].keyname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ dnskey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def Import(cls, client, resource) :
		r""" Use this API to Import dnskey.
		"""
		try :
			if type(resource) is not list :
				Importresource = dnskey()
				Importresource.keyname = resource.keyname
				Importresource.src = resource.src
				return Importresource.perform_operation(client,"Import")
			else :
				if (resource and len(resource) > 0) :
					Importresources = [ dnskey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						Importresources[i].keyname = resource[i].keyname
						Importresources[i].src = resource[i].src
				result = cls.perform_operation_bulk_request(client, Importresources,"Import")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the dnskey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = dnskey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = dnskey()
					obj.keyname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [dnskey() for _ in range(len(name))]
						obj = [dnskey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = dnskey()
							obj[i].keyname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of dnskey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnskey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the dnskey resources configured on NetScaler.
		"""
		try :
			obj = dnskey()
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
		r""" Use this API to count filtered the set of dnskey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = dnskey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Algorithm:
		RSASHA1 = "RSASHA1"
		RSASHA256 = "RSASHA256"
		RSASHA512 = "RSASHA512"

	class Units1:
		MINUTES = "MINUTES"
		HOURS = "HOURS"
		DAYS = "DAYS"

	class Keytype:
		KSK = "KSK"
		KeySigningKey = "KeySigningKey"
		ZSK = "ZSK"
		ZoneSigningKey = "ZoneSigningKey"

	class Units2:
		MINUTES = "MINUTES"
		HOURS = "HOURS"
		DAYS = "DAYS"

class dnskey_response(base_response) :
	def __init__(self, length=1) :
		self.dnskey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.dnskey = [dnskey() for _ in range(length)]

