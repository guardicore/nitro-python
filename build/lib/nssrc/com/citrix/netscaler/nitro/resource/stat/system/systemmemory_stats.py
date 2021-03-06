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

class systemmemory_stats(base_resource) :
	r""" Statistics for Global system memory stats resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._cacmemmaxmemlimitpcnt = 0
		self._cacmemmaxmemlimit = 0
		self._shmemerrallocfailed = 0
		self._shmemallocpcnt = 0
		self._shmemallocinmb = 0
		self._shmemtotinmb = 0
		self._memtotallocfailed = 0
		self._memtotfree = 0
		self._memusagepcnt = 0
		self._memtotuseinmb = 0
		self._memtotallocpcnt = 0
		self._memtotallocmb = 0
		self._memtotinmb = 0
		self._memtotavail = 0
		self._cacmemmaxsyslimitmb = 0

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
	def memtotallocpcnt(self) :
		r"""Currently allocated memory in percent.
		"""
		try :
			return self._memtotallocpcnt
		except Exception as e:
			raise e

	@property
	def memtotfree(self) :
		r"""Total Free PE Memory in the System.
		"""
		try :
			return self._memtotfree
		except Exception as e:
			raise e

	@property
	def shmemallocpcnt(self) :
		r"""Shared memory insue percent.
		"""
		try :
			return self._shmemallocpcnt
		except Exception as e:
			raise e

	@property
	def cacmemmaxmemlimitpcnt(self) :
		r"""Integrated Cache memory insue percent.
		"""
		try :
			return self._cacmemmaxmemlimitpcnt
		except Exception as e:
			raise e

	@property
	def shmemallocinmb(self) :
		r"""Shared memory insue, in megabytes.
		"""
		try :
			return self._shmemallocinmb
		except Exception as e:
			raise e

	@property
	def memtotuseinmb(self) :
		r"""Total Citrix ADC Memory in use, in megabytes.
		"""
		try :
			return self._memtotuseinmb
		except Exception as e:
			raise e

	@property
	def cacmemmaxmemlimit(self) :
		r"""Integrated Cache memory insue, in megabytes.
		"""
		try :
			return self._cacmemmaxmemlimit
		except Exception as e:
			raise e

	@property
	def memusagepcnt(self) :
		r"""Percentage of memory utilization on Citrix ADC.
		"""
		try :
			return self._memusagepcnt
		except Exception as e:
			raise e

	@property
	def memtotinmb(self) :
		r"""Total memory available (grabbed) for use by packet engine (PE), in megabytes.
		"""
		try :
			return self._memtotinmb
		except Exception as e:
			raise e

	@property
	def cacmemmaxsyslimitmb(self) :
		r"""Integrated Cache memory, in megabytes.
		"""
		try :
			return self._cacmemmaxsyslimitmb
		except Exception as e:
			raise e

	@property
	def memtotallocfailed(self) :
		r"""Total system memory allocation failed.
		"""
		try :
			return self._memtotallocfailed
		except Exception as e:
			raise e

	@property
	def memtotallocmb(self) :
		r"""Currently allocated memory, in megabytes.
		"""
		try :
			return self._memtotallocmb
		except Exception as e:
			raise e

	@property
	def shmemerrallocfailed(self) :
		r"""Total shared memory allocation failed.
		"""
		try :
			return self._shmemerrallocfailed
		except Exception as e:
			raise e

	@property
	def memtotavail(self) :
		r"""Total system memory available for PE to grab from the system.
		"""
		try :
			return self._memtotavail
		except Exception as e:
			raise e

	@property
	def shmemtotinmb(self) :
		r"""Total shared memory allowed to allocate, in megabytes.
		"""
		try :
			return self._shmemtotinmb
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemmemory_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemmemory
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all systemmemory_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = systemmemory_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class systemmemory_response(base_response) :
	def __init__(self, length=1) :
		self.systemmemory = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemmemory = [systemmemory_stats() for _ in range(length)]

