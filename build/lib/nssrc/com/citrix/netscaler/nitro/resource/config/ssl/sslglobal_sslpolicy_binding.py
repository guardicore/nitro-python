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

class sslglobal_sslpolicy_binding(base_resource) :
	""" Binding class showing the sslpolicy that can be bound to sslglobal.
	"""
	def __init__(self) :
		self._policyname = None
		self._type = None
		self._priority = None
		self._globalbindtype = None
		self._gotopriorityexpression = None
		self._invoke = None
		self._labeltype = None
		self._labelname = None
		self.___count = None

	@property
	def priority(self) :
		r"""The priority of the policy binding.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""The priority of the policy binding.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def globalbindtype(self) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL.
		"""
		try :
			return self._globalbindtype
		except Exception as e:
			raise e

	@globalbindtype.setter
	def globalbindtype(self, globalbindtype) :
		r""".<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL
		"""
		try :
			self._globalbindtype = globalbindtype
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""The name for the SSL policy.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""The name for the SSL policy.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def labelname(self) :
		r"""Name of the virtual server or user-defined policy label to invoke if the policy evaluates to TRUE.
		"""
		try :
			return self._labelname
		except Exception as e:
			raise e

	@labelname.setter
	def labelname(self, labelname) :
		r"""Name of the virtual server or user-defined policy label to invoke if the policy evaluates to TRUE.
		"""
		try :
			self._labelname = labelname
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* An expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		* If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@gotopriorityexpression.setter
	def gotopriorityexpression(self, gotopriorityexpression) :
		r"""Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
		* NEXT - Evaluate the policy with the next higher priority number.
		* END - End policy evaluation.
		* USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
		* An expression that evaluates to a number.
		If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
		* If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
		* If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
		* If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
		An UNDEF event is triggered if:
		* The expression is invalid.
		* The expression evaluates to a priority number that is numerically lower than the current policy's priority.
		* The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.
		"""
		try :
			self._gotopriorityexpression = gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		r"""Invoke policies bound to a virtual server, service, or policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@invoke.setter
	def invoke(self, invoke) :
		r"""Invoke policies bound to a virtual server, service, or policy label. After the invoked policies are evaluated, the flow returns to the policy with the next priority.
		"""
		try :
			self._invoke = invoke
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Global bind point to which the policy is bound.<br/>Possible values = CONTROL_OVERRIDE, CONTROL_DEFAULT, DATA_OVERRIDE, DATA_DEFAULT, HTTPQUIC_CONTROL_OVERRIDE, HTTPQUIC_CONTROL_DEFAULT, HTTPQUIC_DATA_OVERRIDE, HTTPQUIC_DATA_DEFAULT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Global bind point to which the policy is bound.<br/>Possible values = CONTROL_OVERRIDE, CONTROL_DEFAULT, DATA_OVERRIDE, DATA_DEFAULT, HTTPQUIC_CONTROL_OVERRIDE, HTTPQUIC_CONTROL_DEFAULT, HTTPQUIC_DATA_OVERRIDE, HTTPQUIC_DATA_DEFAULT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""Type of policy label to invoke. Specify virtual server for a policy label associated with a virtual server, or policy label for a user-defined policy label.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@labeltype.setter
	def labeltype(self, labeltype) :
		r"""Type of policy label to invoke. Specify virtual server for a policy label associated with a virtual server, or policy label for a user-defined policy label.
		"""
		try :
			self._labeltype = labeltype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslglobal_sslpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslglobal_sslpolicy_binding
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
		addresource = sslglobal_sslpolicy_binding()
		addresource.policyname = resource.policyname
		addresource.priority = resource.priority
		addresource.gotopriorityexpression = resource.gotopriorityexpression
		addresource.type = resource.type
		addresource.invoke = resource.invoke
		addresource.labeltype = resource.labeltype
		addresource.labelname = resource.labelname
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [sslglobal_sslpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = sslglobal_sslpolicy_binding()
		deleteresource.policyname = resource.policyname
		deleteresource.type = resource.type
		deleteresource.priority = resource.priority
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [sslglobal_sslpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		r""" Use this API to fetch a sslglobal_sslpolicy_binding resources.
		"""
		try :
			obj = sslglobal_sslpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		r""" Use this API to fetch filtered set of sslglobal_sslpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslglobal_sslpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		r""" Use this API to count sslglobal_sslpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = sslglobal_sslpolicy_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		r""" Use this API to count the filtered set of sslglobal_sslpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslglobal_sslpolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Globalbindtype:
		SYSTEM_GLOBAL = "SYSTEM_GLOBAL"
		VPN_GLOBAL = "VPN_GLOBAL"
		RNAT_GLOBAL = "RNAT_GLOBAL"

	class Type:
		CONTROL_OVERRIDE = "CONTROL_OVERRIDE"
		CONTROL_DEFAULT = "CONTROL_DEFAULT"
		DATA_OVERRIDE = "DATA_OVERRIDE"
		DATA_DEFAULT = "DATA_DEFAULT"
		HTTPQUIC_CONTROL_OVERRIDE = "HTTPQUIC_CONTROL_OVERRIDE"
		HTTPQUIC_CONTROL_DEFAULT = "HTTPQUIC_CONTROL_DEFAULT"
		HTTPQUIC_DATA_OVERRIDE = "HTTPQUIC_DATA_OVERRIDE"
		HTTPQUIC_DATA_DEFAULT = "HTTPQUIC_DATA_DEFAULT"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

class sslglobal_sslpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslglobal_sslpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslglobal_sslpolicy_binding = [sslglobal_sslpolicy_binding() for _ in range(length)]

