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

class videooptimizationglobaldetection_binding(base_resource):
	""" Binding class showing the resources that can be bound to videooptimizationglobaldetection_binding. 
	"""
	def __init__(self) :
		self.videooptimizationglobaldetection_videooptimizationdetectionpolicy_binding = []

	@property
	def videooptimizationglobaldetection_videooptimizationdetectionpolicy_bindings(self) :
		r"""videooptimizationdetectionpolicy that can be bound to videooptimizationglobaldetection.
		"""
		try :
			return self._videooptimizationglobaldetection_videooptimizationdetectionpolicy_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationglobaldetection_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationglobaldetection_binding
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
	def get(self, service) :
		r""" Use this API to fetch a videooptimizationglobaldetection_binding resource .
		"""
		try :
			obj = videooptimizationglobaldetection_binding()
			response = obj.get_resource(service)
			return response

		except Exception as e:
			raise e

class videooptimizationglobaldetection_binding_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationglobaldetection_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationglobaldetection_binding = [videooptimizationglobaldetection_binding() for _ in range(length)]

