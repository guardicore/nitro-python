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


class policyevaluation_args :
	r""" Provides additional arguments required for fetching the policyevaluation resource.
	"""
	def __init__(self) :
		self._expression = None
		self._action = None
		self._type = None
		self._input = None

	@property
	def expression(self) :
		r"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			return self._expression
		except Exception as e:
			raise e

	@expression.setter
	def expression(self, expression) :
		r"""Expression string. For example: http.req.body(100).contains("this").
		"""
		try :
			self._expression = expression
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Rewrite action name. Supported rewrite action types are:
		-delete
		-delete_all
		-delete_http_header
		-insert_after
		-insert_after_all
		-insert_before
		-insert_before_all
		-insert_http_header
		-replace
		-replace_all
		.<br/>Minimum length =  1.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		r"""Rewrite action name. Supported rewrite action types are:
		-delete
		-delete_all
		-delete_http_header
		-insert_after
		-insert_after_all
		-insert_before
		-insert_before_all
		-insert_http_header
		-replace
		-replace_all
		.<br/>Minimum length =  1
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Indicates request or response input packet.<br/>Possible values = HTTP_REQ, HTTP_RES, TEXT.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Indicates request or response input packet.<br/>Possible values = HTTP_REQ, HTTP_RES, TEXT
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def input(self) :
		r"""Text representation of input packet.
		"""
		try :
			return self._input
		except Exception as e:
			raise e

	@input.setter
	def input(self, input) :
		r"""Text representation of input packet.
		"""
		try :
			self._input = input
		except Exception as e:
			raise e

	class Type:
		HTTP_REQ = "HTTP_REQ"
		HTTP_RES = "HTTP_RES"
		TEXT = "TEXT"

