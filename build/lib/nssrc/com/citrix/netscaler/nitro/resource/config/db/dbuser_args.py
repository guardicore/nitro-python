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


class dbuser_args :
	r""" Provides additional arguments required for fetching the dbuser resource.
	"""
	def __init__(self) :
		self._loggedin = None

	@property
	def loggedin(self) :
		r"""Display the names of all database users currently logged on to the Citrix ADC.
		"""
		try :
			return self._loggedin
		except Exception as e:
			raise e

	@loggedin.setter
	def loggedin(self, loggedin) :
		r"""Display the names of all database users currently logged on to the Citrix ADC.
		"""
		try :
			self._loggedin = loggedin
		except Exception as e:
			raise e

