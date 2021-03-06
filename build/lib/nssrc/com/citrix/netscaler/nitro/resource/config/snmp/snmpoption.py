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

class snmpoption(base_resource) :
	""" Configuration for SNMP option resource. """
	def __init__(self) :
		self._snmpset = None
		self._snmptraplogging = None
		self._partitionnameintrap = None
		self._snmptraplogginglevel = None

	@property
	def snmpset(self) :
		r"""Accept SNMP SET requests sent to the Citrix ADC, and allow SNMP managers to write values to MIB objects that are configured for write access.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snmpset
		except Exception as e:
			raise e

	@snmpset.setter
	def snmpset(self, snmpset) :
		r"""Accept SNMP SET requests sent to the Citrix ADC, and allow SNMP managers to write values to MIB objects that are configured for write access.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snmpset = snmpset
		except Exception as e:
			raise e

	@property
	def snmptraplogging(self) :
		r"""Log any SNMP trap events (for SNMP alarms in which logging is enabled) even if no trap listeners are configured. With the default setting, SNMP trap events are logged if at least one trap listener is configured on the appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snmptraplogging
		except Exception as e:
			raise e

	@snmptraplogging.setter
	def snmptraplogging(self, snmptraplogging) :
		r"""Log any SNMP trap events (for SNMP alarms in which logging is enabled) even if no trap listeners are configured. With the default setting, SNMP trap events are logged if at least one trap listener is configured on the appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snmptraplogging = snmptraplogging
		except Exception as e:
			raise e

	@property
	def partitionnameintrap(self) :
		r"""Send partition name as a varbind in traps. By default the partition names are not sent as a varbind.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._partitionnameintrap
		except Exception as e:
			raise e

	@partitionnameintrap.setter
	def partitionnameintrap(self, partitionnameintrap) :
		r"""Send partition name as a varbind in traps. By default the partition names are not sent as a varbind.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._partitionnameintrap = partitionnameintrap
		except Exception as e:
			raise e

	@property
	def snmptraplogginglevel(self) :
		r"""Audit log level of SNMP trap logs. The default value is INFORMATIONAL.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.
		"""
		try :
			return self._snmptraplogginglevel
		except Exception as e:
			raise e

	@snmptraplogginglevel.setter
	def snmptraplogginglevel(self, snmptraplogginglevel) :
		r"""Audit log level of SNMP trap logs. The default value is INFORMATIONAL.<br/>Default value: INFORMATIONAL<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG
		"""
		try :
			self._snmptraplogginglevel = snmptraplogginglevel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(snmpoption_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.snmpoption
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
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = snmpoption()
		updateresource.snmpset = resource.snmpset
		updateresource.snmptraplogging = resource.snmptraplogging
		updateresource.partitionnameintrap = resource.partitionnameintrap
		updateresource.snmptraplogginglevel = resource.snmptraplogginglevel
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update snmpoption.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of snmpoption resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = snmpoption()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the snmpoption resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = snmpoption()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Snmptraplogginglevel:
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"

	class Snmptraplogging:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snmpset:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Partitionnameintrap:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class snmpoption_response(base_response) :
	def __init__(self, length=1) :
		self.snmpoption = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.snmpoption = [snmpoption() for _ in range(length)]

