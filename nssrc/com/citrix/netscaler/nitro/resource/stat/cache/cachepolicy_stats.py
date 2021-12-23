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

class cachepolicy_stats(base_resource) :
	r""" Statistics for Integrated Cache policy resource.
	"""
	def __init__(self) :
		self._policyname = None
		self._clearstats = None
		self._pipolicyhits = 0
		self._pipolicyhitsrate = 0
		self._pipolicyundefhits = 0
		self._pipolicyundefhitsrate = 0

	@property
	def policyname(self) :
		r"""Name of the cache policy for which to display statistics. If you do not set this parameter, statistics are shown for all cache policies.<br/>Minimum length =  1.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@policyname.setter
	def policyname(self, policyname) :
		r"""Name of the cache policy for which to display statistics. If you do not set this parameter, statistics are shown for all cache policies.
		"""
		try :
			self._policyname = policyname
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def pipolicyundefhitsrate(self) :
		r"""Rate (/s) counter for pipolicyundefhits.
		"""
		try :
			return self._pipolicyundefhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicyundefhits(self) :
		r"""Number of undef hits on the policy.
		"""
		try :
			return self._pipolicyundefhits
		except Exception as e:
			raise e

	@property
	def pipolicyhitsrate(self) :
		r"""Rate (/s) counter for pipolicyhits.
		"""
		try :
			return self._pipolicyhitsrate
		except Exception as e:
			raise e

	@property
	def pipolicyhits(self) :
		r"""Number of hits on the policy.
		"""
		try :
			return self._pipolicyhits
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cachepolicy_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cachepolicy
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.policyname is not None :
				return str(self.policyname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all cachepolicy_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = cachepolicy_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.policyname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class cachepolicy_response(base_response) :
	def __init__(self, length=1) :
		self.cachepolicy = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cachepolicy = [cachepolicy_stats() for _ in range(length)]
