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

class sslrsakey(base_resource) :
	""" Configuration for RSA key resource. """
	def __init__(self) :
		self._keyfile = None
		self._bits = None
		self._exponent = None
		self._keyform = None
		self._des = None
		self._des3 = None
		self._aes256 = None
		self._password = None
		self._pkcs8 = None

	@property
	def keyfile(self) :
		r"""Name for and, optionally, path to the RSA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		r"""Name for and, optionally, path to the RSA key file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def bits(self) :
		r"""Size, in bits, of the RSA key.<br/>Minimum length =  512<br/>Maximum length =  4096.
		"""
		try :
			return self._bits
		except Exception as e:
			raise e

	@bits.setter
	def bits(self, bits) :
		r"""Size, in bits, of the RSA key.<br/>Minimum length =  512<br/>Maximum length =  4096
		"""
		try :
			self._bits = bits
		except Exception as e:
			raise e

	@property
	def exponent(self) :
		r"""Public exponent for the RSA key. The exponent is part of the cipher algorithm and is required for creating the RSA key.<br/>Default value: F4<br/>Possible values = 3, F4.
		"""
		try :
			return self._exponent
		except Exception as e:
			raise e

	@exponent.setter
	def exponent(self, exponent) :
		r"""Public exponent for the RSA key. The exponent is part of the cipher algorithm and is required for creating the RSA key.<br/>Default value: F4<br/>Possible values = 3, F4
		"""
		try :
			self._exponent = exponent
		except Exception as e:
			raise e

	@property
	def keyform(self) :
		r"""Format in which the RSA key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._keyform
		except Exception as e:
			raise e

	@keyform.setter
	def keyform(self, keyform) :
		r"""Format in which the RSA key file is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._keyform = keyform
		except Exception as e:
			raise e

	@property
	def des(self) :
		r"""Encrypt the generated RSA key by using the DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			return self._des
		except Exception as e:
			raise e

	@des.setter
	def des(self, des) :
		r"""Encrypt the generated RSA key by using the DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			self._des = des
		except Exception as e:
			raise e

	@property
	def des3(self) :
		r"""Encrypt the generated RSA key by using the Triple-DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			return self._des3
		except Exception as e:
			raise e

	@des3.setter
	def des3(self, des3) :
		r"""Encrypt the generated RSA key by using the Triple-DES algorithm. On the command line, you are prompted to enter the pass phrase (password) that is used to encrypt the key.
		"""
		try :
			self._des3 = des3
		except Exception as e:
			raise e

	@property
	def aes256(self) :
		r"""Encrypt the generated RSA key by using the AES algorithm.
		"""
		try :
			return self._aes256
		except Exception as e:
			raise e

	@aes256.setter
	def aes256(self, aes256) :
		r"""Encrypt the generated RSA key by using the AES algorithm.
		"""
		try :
			self._aes256 = aes256
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Pass phrase to use for encryption if DES or DES3 option is selected.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Pass phrase to use for encryption if DES or DES3 option is selected.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def pkcs8(self) :
		r"""Create the private key in PKCS#8 format.
		"""
		try :
			return self._pkcs8
		except Exception as e:
			raise e

	@pkcs8.setter
	def pkcs8(self, pkcs8) :
		r"""Create the private key in PKCS#8 format.
		"""
		try :
			self._pkcs8 = pkcs8
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslrsakey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslrsakey
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
	def create(cls, client, resource) :
		r""" Use this API to create sslrsakey.
		"""
		try :
			if type(resource) is not list :
				createresource = sslrsakey()
				createresource.keyfile = resource.keyfile
				createresource.bits = resource.bits
				createresource.exponent = resource.exponent
				createresource.keyform = resource.keyform
				createresource.des = resource.des
				createresource.des3 = resource.des3
				createresource.aes256 = resource.aes256
				createresource.password = resource.password
				createresource.pkcs8 = resource.pkcs8
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	class Keyform:
		DER = "DER"
		PEM = "PEM"

	class Exponent:
		_3 = "3"
		F4 = "F4"

class sslrsakey_response(base_response) :
	def __init__(self, length=1) :
		self.sslrsakey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslrsakey = [sslrsakey() for _ in range(length)]

