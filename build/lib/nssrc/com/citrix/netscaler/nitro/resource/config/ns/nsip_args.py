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


class nsip_args :
	r""" Provides additional arguments required for fetching the nsip resource.
	"""
	def __init__(self) :
		self._type = None

	@property
	def type(self) :
		r"""Display the settings of all IPv4 addresses of a particular type.<br/>Default value: 0<br/>Possible values = SNIP, VIP, NSIP, GSLBsiteIP, CLIP.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Display the settings of all IPv4 addresses of a particular type.<br/>Default value: 0<br/>Possible values = SNIP, VIP, NSIP, GSLBsiteIP, CLIP
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	class Type:
		SNIP = "SNIP"
		VIP = "VIP"
		NSIP = "NSIP"
		GSLBsiteIP = "GSLBsiteIP"
		CLIP = "CLIP"

