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

class nshardware(base_resource) :
	""" Configuration for hardware resource. """

		#------- Read only Parameter ---------

	def __init__(self) :
		self._hwdescription = None
		self._sysid = None
		self._manufactureday = None
		self._manufacturemonth = None
		self._manufactureyear = None
		self._cpufrequncy = None
		self._hostid = None
		self._host = None
		self._serialno = None
		self._encodedserialno = None
		self._netscaleruuid = None
		self._bmcrevision = None

	@property
	def hwdescription(self) :
		r"""Hardware and it's ports detail.
		"""
		try :
			return self._hwdescription
		except Exception as e:
			raise e

	@property
	def sysid(self) :
		r"""System id.
		"""
		try :
			return self._sysid
		except Exception as e:
			raise e

	@property
	def manufactureday(self) :
		r"""Manufacturing day.
		"""
		try :
			return self._manufactureday
		except Exception as e:
			raise e

	@property
	def manufacturemonth(self) :
		r"""Manufacturing month.
		"""
		try :
			return self._manufacturemonth
		except Exception as e:
			raise e

	@property
	def manufactureyear(self) :
		r"""Manufacturing year.
		"""
		try :
			return self._manufactureyear
		except Exception as e:
			raise e

	@property
	def cpufrequncy(self) :
		r"""CPU Frequency.
		"""
		try :
			return self._cpufrequncy
		except Exception as e:
			raise e

	@property
	def hostid(self) :
		r"""host id.
		"""
		try :
			return self._hostid
		except Exception as e:
			raise e

	@property
	def host(self) :
		r"""host id.
		"""
		try :
			return self._host
		except Exception as e:
			raise e

	@property
	def serialno(self) :
		r"""Serial no.
		"""
		try :
			return self._serialno
		except Exception as e:
			raise e

	@property
	def encodedserialno(self) :
		r"""Encoded serial no.
		"""
		try :
			return self._encodedserialno
		except Exception as e:
			raise e

	@property
	def netscaleruuid(self) :
		r"""Citrix ADC UUID.
		"""
		try :
			return self._netscaleruuid
		except Exception as e:
			raise e

	@property
	def bmcrevision(self) :
		r"""BMC Firmware Revision.
		"""
		try :
			return self._bmcrevision
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshardware_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshardware
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
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nshardware resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshardware()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nshardware_response(base_response) :
	def __init__(self, length=1) :
		self.nshardware = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshardware = [nshardware() for _ in range(length)]

