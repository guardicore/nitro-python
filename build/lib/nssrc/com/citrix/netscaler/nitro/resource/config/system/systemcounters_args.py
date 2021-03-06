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


class systemcounters_args :
	r""" Provides additional arguments required for fetching the systemcounters resource.
	"""
	def __init__(self) :
		self._countergroup = None
		self._datasource = None

	@property
	def countergroup(self) :
		r"""Specify the (counter) group name which contains all the counters specific tot his particular group.
		"""
		try :
			return self._countergroup
		except Exception as e:
			raise e

	@countergroup.setter
	def countergroup(self, countergroup) :
		r"""Specify the (counter) group name which contains all the counters specific tot his particular group.
		"""
		try :
			self._countergroup = countergroup
		except Exception as e:
			raise e

	@property
	def datasource(self) :
		r"""Specifies the source which contains all the stored counter values.
		"""
		try :
			return self._datasource
		except Exception as e:
			raise e

	@datasource.setter
	def datasource(self, datasource) :
		r"""Specifies the source which contains all the stored counter values.
		"""
		try :
			self._datasource = datasource
		except Exception as e:
			raise e

