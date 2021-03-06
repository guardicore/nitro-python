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

class sslcert(base_resource) :
	""" Configuration for cerificate resource. """
	def __init__(self) :
		self._certfile = None
		self._reqfile = None
		self._certtype = None
		self._keyfile = None
		self._keyform = None
		self._pempassphrase = None
		self._days = None
		self._subjectaltname = None
		self._certform = None
		self._cacert = None
		self._cacertform = None
		self._cakey = None
		self._cakeyform = None
		self._caserial = None

	@property
	def certfile(self) :
		r"""Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._certfile
		except Exception as e:
			raise e

	@certfile.setter
	def certfile(self, certfile) :
		r"""Name for and, optionally, path to the generated certificate file. /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._certfile = certfile
		except Exception as e:
			raise e

	@property
	def reqfile(self) :
		r"""Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path.<br/>Maximum length =  63.
		"""
		try :
			return self._reqfile
		except Exception as e:
			raise e

	@reqfile.setter
	def reqfile(self, reqfile) :
		r"""Name for and, optionally, path to the certificate-signing request (CSR). /nsconfig/ssl/ is the default path.<br/>Maximum length =  63
		"""
		try :
			self._reqfile = reqfile
		except Exception as e:
			raise e

	@property
	def certtype(self) :
		r"""Type of certificate to generate. Specify one of the following:
		* ROOT_CERT - Self-signed Root-CA certificate. You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates.
		* INTM_CERT - Intermediate-CA certificate.
		* CLNT_CERT - End-user client certificate used for client authentication.
		* SRVR_CERT - SSL server certificate used on SSL servers for end-to-end encryption.<br/>Possible values = ROOT_CERT, INTM_CERT, CLNT_CERT, SRVR_CERT.
		"""
		try :
			return self._certtype
		except Exception as e:
			raise e

	@certtype.setter
	def certtype(self, certtype) :
		r"""Type of certificate to generate. Specify one of the following:
		* ROOT_CERT - Self-signed Root-CA certificate. You must specify the key file name. The generated Root-CA certificate can be used for signing end-user client or server certificates or to create Intermediate-CA certificates.
		* INTM_CERT - Intermediate-CA certificate.
		* CLNT_CERT - End-user client certificate used for client authentication.
		* SRVR_CERT - SSL server certificate used on SSL servers for end-to-end encryption.<br/>Possible values = ROOT_CERT, INTM_CERT, CLNT_CERT, SRVR_CERT
		"""
		try :
			self._certtype = certtype
		except Exception as e:
			raise e

	@property
	def keyfile(self) :
		r"""Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.
		If the input key specified is an encrypted key, you are prompted to enter the PEM pass phrase that was used for encrypting the key.<br/>Maximum length =  63.
		"""
		try :
			return self._keyfile
		except Exception as e:
			raise e

	@keyfile.setter
	def keyfile(self, keyfile) :
		r"""Name for and, optionally, path to the private key. You can either use an existing RSA or DSA key that you own or create a new private key on the Citrix ADC. This file is required only when creating a self-signed Root-CA certificate. The key file is stored in the /nsconfig/ssl directory by default.
		If the input key specified is an encrypted key, you are prompted to enter the PEM pass phrase that was used for encrypting the key.<br/>Maximum length =  63
		"""
		try :
			self._keyfile = keyfile
		except Exception as e:
			raise e

	@property
	def keyform(self) :
		r"""Format in which the key is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._keyform
		except Exception as e:
			raise e

	@keyform.setter
	def keyform(self, keyform) :
		r"""Format in which the key is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._keyform = keyform
		except Exception as e:
			raise e

	@property
	def pempassphrase(self) :
		r""".<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._pempassphrase
		except Exception as e:
			raise e

	@pempassphrase.setter
	def pempassphrase(self, pempassphrase) :
		r""".<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._pempassphrase = pempassphrase
		except Exception as e:
			raise e

	@property
	def days(self) :
		r"""Number of days for which the certificate will be valid, beginning with the time and day (system time) of creation.<br/>Default value: 365<br/>Minimum length =  1<br/>Maximum length =  3650.
		"""
		try :
			return self._days
		except Exception as e:
			raise e

	@days.setter
	def days(self, days) :
		r"""Number of days for which the certificate will be valid, beginning with the time and day (system time) of creation.<br/>Default value: 365<br/>Minimum length =  1<br/>Maximum length =  3650
		"""
		try :
			self._days = days
		except Exception as e:
			raise e

	@property
	def subjectaltname(self) :
		r"""Subject Alternative Name (SAN) is an extension to X.509 that allows various values to be associated with a security certificate using a subjectAltName field. These values are called "Subject Alternative Names" (SAN). Names include:
		1. Email addresses
		2. IP addresses
		3. URIs
		4. DNS names (This is usually also provided as the Common Name RDN within the Subject field of the main certificate.)
		5. directory names (alternative Distinguished Names to that given in the Subject).<br/>Minimum length =  1.
		"""
		try :
			return self._subjectaltname
		except Exception as e:
			raise e

	@subjectaltname.setter
	def subjectaltname(self, subjectaltname) :
		r"""Subject Alternative Name (SAN) is an extension to X.509 that allows various values to be associated with a security certificate using a subjectAltName field. These values are called "Subject Alternative Names" (SAN). Names include:
		1. Email addresses
		2. IP addresses
		3. URIs
		4. DNS names (This is usually also provided as the Common Name RDN within the Subject field of the main certificate.)
		5. directory names (alternative Distinguished Names to that given in the Subject).<br/>Minimum length =  1
		"""
		try :
			self._subjectaltname = subjectaltname
		except Exception as e:
			raise e

	@property
	def certform(self) :
		r"""Format in which the certificate is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._certform
		except Exception as e:
			raise e

	@certform.setter
	def certform(self, certform) :
		r"""Format in which the certificate is stored on the appliance.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._certform = certform
		except Exception as e:
			raise e

	@property
	def cacert(self) :
		r"""Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates.<br/>Maximum length =  63.
		"""
		try :
			return self._cacert
		except Exception as e:
			raise e

	@cacert.setter
	def cacert(self, cacert) :
		r"""Name of the CA certificate file that issues and signs the Intermediate-CA certificate or the end-user client and server certificates.<br/>Maximum length =  63
		"""
		try :
			self._cacert = cacert
		except Exception as e:
			raise e

	@property
	def cacertform(self) :
		r"""Format of the CA certificate.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._cacertform
		except Exception as e:
			raise e

	@cacertform.setter
	def cacertform(self, cacertform) :
		r"""Format of the CA certificate.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._cacertform = cacertform
		except Exception as e:
			raise e

	@property
	def cakey(self) :
		r"""Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key.<br/>Maximum length =  63.
		"""
		try :
			return self._cakey
		except Exception as e:
			raise e

	@cakey.setter
	def cakey(self, cakey) :
		r"""Private key, associated with the CA certificate that is used to sign the Intermediate-CA certificate or the end-user client and server certificate. If the CA key file is password protected, the user is prompted to enter the pass phrase that was used to encrypt the key.<br/>Maximum length =  63
		"""
		try :
			self._cakey = cakey
		except Exception as e:
			raise e

	@property
	def cakeyform(self) :
		r"""Format for the CA certificate.<br/>Default value: PEM<br/>Possible values = DER, PEM.
		"""
		try :
			return self._cakeyform
		except Exception as e:
			raise e

	@cakeyform.setter
	def cakeyform(self, cakeyform) :
		r"""Format for the CA certificate.<br/>Default value: PEM<br/>Possible values = DER, PEM
		"""
		try :
			self._cakeyform = cakeyform
		except Exception as e:
			raise e

	@property
	def caserial(self) :
		r"""Serial number file maintained for the CA certificate. This file contains the serial number of the next certificate to be issued or signed by the CA. If the specified file does not exist, a new file is created, with /nsconfig/ssl/ as the default path. If you do not specify a proper path for the existing serial file, a new serial file is created. This might change the certificate serial numbers assigned by the CA certificate to each of the certificates it signs.<br/>Maximum length =  63.
		"""
		try :
			return self._caserial
		except Exception as e:
			raise e

	@caserial.setter
	def caserial(self, caserial) :
		r"""Serial number file maintained for the CA certificate. This file contains the serial number of the next certificate to be issued or signed by the CA. If the specified file does not exist, a new file is created, with /nsconfig/ssl/ as the default path. If you do not specify a proper path for the existing serial file, a new serial file is created. This might change the certificate serial numbers assigned by the CA certificate to each of the certificates it signs.<br/>Maximum length =  63
		"""
		try :
			self._caserial = caserial
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcert_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcert
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
		r""" Use this API to create sslcert.
		"""
		try :
			if type(resource) is not list :
				createresource = sslcert()
				createresource.certfile = resource.certfile
				createresource.reqfile = resource.reqfile
				createresource.certtype = resource.certtype
				createresource.keyfile = resource.keyfile
				createresource.keyform = resource.keyform
				createresource.pempassphrase = resource.pempassphrase
				createresource.days = resource.days
				createresource.subjectaltname = resource.subjectaltname
				createresource.certform = resource.certform
				createresource.cacert = resource.cacert
				createresource.cacertform = resource.cacertform
				createresource.cakey = resource.cakey
				createresource.cakeyform = resource.cakeyform
				createresource.caserial = resource.caserial
				return createresource.perform_operation(client,"create")
		except Exception as e :
			raise e

	class Keyform:
		DER = "DER"
		PEM = "PEM"

	class Cacertform:
		DER = "DER"
		PEM = "PEM"

	class Certtype:
		ROOT_CERT = "ROOT_CERT"
		INTM_CERT = "INTM_CERT"
		CLNT_CERT = "CLNT_CERT"
		SRVR_CERT = "SRVR_CERT"

	class Certform:
		DER = "DER"
		PEM = "PEM"

	class Cakeyform:
		DER = "DER"
		PEM = "PEM"

class sslcert_response(base_response) :
	def __init__(self, length=1) :
		self.sslcert = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcert = [sslcert() for _ in range(length)]

