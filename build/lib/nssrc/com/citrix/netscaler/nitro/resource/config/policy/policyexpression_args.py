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


class policyexpression_args :
	r""" Provides additional arguments required for fetching the policyexpression resource.
	"""
	def __init__(self) :
		self._type = None

	@property
	def type(self) :
		r"""Type of expression. Can be a classic or default syntax (advanced) expression.<br/>Possible values = CLASSIC, ADVANCED.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of expression. Can be a classic or default syntax (advanced) expression.<br/>Possible values = CLASSIC, ADVANCED
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	class Type:
		CLASSIC = "CLASSIC"
		ADVANCED = "ADVANCED"

