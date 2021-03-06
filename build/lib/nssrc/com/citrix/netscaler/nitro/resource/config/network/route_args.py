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


class route_args :
	r""" Provides additional arguments required for fetching the route resource.
	"""
	def __init__(self) :
		self._routetype = None
		self._detail = None

	@property
	def routetype(self) :
		r"""The type of routes to be shown.<br/>Possible values = CONNECTED, STATIC, DYNAMIC, OSPF, ISIS, RIP, BGP.
		"""
		try :
			return self._routetype
		except Exception as e:
			raise e

	@routetype.setter
	def routetype(self, routetype) :
		r"""The type of routes to be shown.<br/>Possible values = CONNECTED, STATIC, DYNAMIC, OSPF, ISIS, RIP, BGP
		"""
		try :
			self._routetype = routetype
		except Exception as e:
			raise e

	@property
	def detail(self) :
		r"""Display a detailed view.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		r"""Display a detailed view.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	class Routetype:
		CONNECTED = "CONNECTED"
		STATIC = "STATIC"
		DYNAMIC = "DYNAMIC"
		OSPF = "OSPF"
		ISIS = "ISIS"
		RIP = "RIP"
		BGP = "BGP"

