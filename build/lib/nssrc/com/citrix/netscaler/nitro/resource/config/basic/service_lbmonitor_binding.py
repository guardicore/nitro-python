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

class service_lbmonitor_binding(base_resource) :
	""" Binding class showing the lbmonitor that can be bound to service.
	"""
	def __init__(self) :
		self._monitor_name = None
		self._monstate = None
		self._monitor_state = None
		self._dup_state = None
		self._weight = None
		self._dup_weight = None
		self._totalprobes = None
		self._totalfailedprobes = None
		self._failedprobes = None
		self._monstatcode = None
		self._lastresponse = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._responsetime = None
		self._monitortotalprobes = None
		self._monitortotalfailedprobes = None
		self._monitorcurrentfailedprobes = None
		self._passive = None
		self._name = None
		self.___count = None

	@property
	def weight(self) :
		r"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the monitor-service binding. When a monitor is UP, the weight assigned to its binding with the service determines how much the monitor contributes toward keeping the health of the service above the value configured for the Monitor Threshold parameter.<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the service to which to bind a policy or monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the service to which to bind a policy or monitor.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def passive(self) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			return self._passive
		except Exception as e:
			raise e

	@passive.setter
	def passive(self, passive) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			self._passive = passive
		except Exception as e:
			raise e

	@property
	def monitor_name(self) :
		r"""The monitor Names.
		"""
		try :
			return self._monitor_name
		except Exception as e:
			raise e

	@monitor_name.setter
	def monitor_name(self, monitor_name) :
		r"""The monitor Names.
		"""
		try :
			self._monitor_name = monitor_name
		except Exception as e:
			raise e

	@property
	def monstate(self) :
		r"""The configured state (enable/disable) of the monitor on this server.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monstate
		except Exception as e:
			raise e

	@monstate.setter
	def monstate(self, monstate) :
		r"""The configured state (enable/disable) of the monitor on this server.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monstate = monstate
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		r"""The weight of the monitor.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@property
	def responsetime(self) :
		r"""Response time of this monitor.
		"""
		try :
			return self._responsetime
		except Exception as e:
			raise e

	@property
	def totalfailedprobes(self) :
		r"""The total number of failed probs.
		"""
		try :
			return self._totalfailedprobes
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def lastresponse(self) :
		r"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
		except Exception as e:
			raise e

	@property
	def failedprobes(self) :
		r"""Number of the current failed monitoring probes.
		"""
		try :
			return self._failedprobes
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def totalprobes(self) :
		r"""The total number of probs sent.
		"""
		try :
			return self._totalprobes
		except Exception as e:
			raise e

	@property
	def monitor_state(self) :
		r"""The running state of the monitor on this service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._monitor_state
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		r"""Added this field for getting state value from table.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@property
	def monitortotalprobes(self) :
		r"""Total number of probes sent to monitor this service.
		"""
		try :
			return self._monitortotalprobes
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monitortotalfailedprobes(self) :
		r"""Total number of failed probes.
		"""
		try :
			return self._monitortotalfailedprobes
		except Exception as e:
			raise e

	@property
	def monitorcurrentfailedprobes(self) :
		r"""Total number of currently failed probes.
		"""
		try :
			return self._monitorcurrentfailedprobes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(service_lbmonitor_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.service_lbmonitor_binding
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
		addresource = service_lbmonitor_binding()
		addresource.name = resource.name
		addresource.monitor_name = resource.monitor_name
		addresource.monstate = resource.monstate
		addresource.weight = resource.weight
		addresource.passive = resource.passive
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [service_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = service_lbmonitor_binding()
		deleteresource.name = resource.name
		deleteresource.monitor_name = resource.monitor_name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [service_lbmonitor_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch service_lbmonitor_binding resources.
		"""
		try :
			if not name :
				obj = service_lbmonitor_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = service_lbmonitor_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of service_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count service_lbmonitor_binding resources configued on NetScaler.
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of service_lbmonitor_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = service_lbmonitor_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Monitor_state:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class service_lbmonitor_binding_response(base_response) :
	def __init__(self, length=1) :
		self.service_lbmonitor_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.service_lbmonitor_binding = [service_lbmonitor_binding() for _ in range(length)]

