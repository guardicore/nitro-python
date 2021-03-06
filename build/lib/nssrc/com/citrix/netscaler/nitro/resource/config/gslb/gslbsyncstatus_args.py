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


class gslbsyncstatus_args :
	r""" Provides additional arguments required for fetching the gslbsyncstatus resource.
	"""
	def __init__(self) :
		self._summary = None

	@property
	def summary(self) :
		r"""sync status summary to be displayed in one line (Success/Failure), in case of Failure stating reason for failure.
		"""
		try :
			return self._summary
		except Exception as e:
			raise e

	@summary.setter
	def summary(self, summary) :
		r"""sync status summary to be displayed in one line (Success/Failure), in case of Failure stating reason for failure.
		"""
		try :
			self._summary = summary
		except Exception as e:
			raise e

