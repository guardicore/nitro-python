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

class protocolicmp_stats(base_resource) :
	r""" Statistics for icmp resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._icmptotrxpkts = 0
		self._icmprxpktsrate = 0
		self._icmptotrxbytes = 0
		self._icmprxbytesrate = 0
		self._icmptottxpkts = 0
		self._icmptxpktsrate = 0
		self._icmptottxbytes = 0
		self._icmptxbytesrate = 0
		self._icmptotrxechoreply = 0
		self._icmprxechoreplyrate = 0
		self._icmptottxechoreply = 0
		self._icmptxechoreplyrate = 0
		self._icmptotrxecho = 0
		self._icmprxechorate = 0
		self._icmptotdstiplookup = 0
		self._icmpcurratethreshold = 0
		self._icmptotportunreachablerx = 0
		self._icmptotportunreachabletx = 0
		self._icmptotneedfragrx = 0
		self._icmptotthresholdexceeds = 0
		self._icmptotpktsdropped = 0
		self._icmptotbadchecksum = 0
		self._icmptotnonfirstipfrag = 0
		self._icmptotinvalidbodylen = 0
		self._icmptotnotcpconn = 0
		self._icmptotnoudpconn = 0
		self._icmptotinvalidtcpseqno = 0
		self._icmptotinvalidnextmtuval = 0
		self._icmptotbignextmtu = 0
		self._icmptotinvalidprotocol = 0
		self._icmptotbadpmtuipchecksum = 0
		self._icmptotpmtunolink = 0
		self._icmptotpmtudiscoverydisabled = 0

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
	def icmprxechoreplyrate(self) :
		r"""Rate (/s) counter for icmptotrxechoreply.
		"""
		try :
			return self._icmprxechoreplyrate
		except Exception as e:
			raise e

	@property
	def icmptottxpkts(self) :
		r"""ICMP packets transmitted.
		"""
		try :
			return self._icmptottxpkts
		except Exception as e:
			raise e

	@property
	def icmptotinvalidnextmtuval(self) :
		r"""ICMP Fragmentation Needed error messages received in which the Maximum Transmission Unit (MTU) for the next hop is out of range. The range for the MTU is 576-1500.
		"""
		try :
			return self._icmptotinvalidnextmtuval
		except Exception as e:
			raise e

	@property
	def icmptotrxecho(self) :
		r"""ICMP Ping Echo Request and Echo Reply packets received.
		"""
		try :
			return self._icmptotrxecho
		except Exception as e:
			raise e

	@property
	def icmptotdstiplookup(self) :
		r"""Total number of MTU lookup on destination IP info received on a need fragmentation ICMP error message failed.
		"""
		try :
			return self._icmptotdstiplookup
		except Exception as e:
			raise e

	@property
	def icmptotnoudpconn(self) :
		r"""ICMP Need Fragmentation error messages received for UDP packets. The state of the connection for these packets is not maintained on the Citrix ADC.
		"""
		try :
			return self._icmptotnoudpconn
		except Exception as e:
			raise e

	@property
	def icmptotportunreachabletx(self) :
		r"""ICMP Port Unreachable error messages generated. This error is generated when there is no service is running on the port.
		"""
		try :
			return self._icmptotportunreachabletx
		except Exception as e:
			raise e

	@property
	def icmptotpmtudiscoverydisabled(self) :
		r"""ICMP Need Fragmentation error messages received when the PMTU Discovery mode is not enabled.
		"""
		try :
			return self._icmptotpmtudiscoverydisabled
		except Exception as e:
			raise e

	@property
	def icmptotbadpmtuipchecksum(self) :
		r"""ICMP Fragmentation Needed error messages received with an IP checksum error.
		"""
		try :
			return self._icmptotbadpmtuipchecksum
		except Exception as e:
			raise e

	@property
	def icmptotpmtunolink(self) :
		r"""ICMP Fragmentation Needed error messages received on a Protocol Control Block (PCB) with no link. The PCB maintains the state of the connection.
		"""
		try :
			return self._icmptotpmtunolink
		except Exception as e:
			raise e

	@property
	def icmptotinvalidprotocol(self) :
		r"""ICMP Fragmentation Needed error messages received that contain a protocol other than TCP and UDP.
		"""
		try :
			return self._icmptotinvalidprotocol
		except Exception as e:
			raise e

	@property
	def icmptotportunreachablerx(self) :
		r"""ICMP Port Unreachable error messages received. This error is generated when there is no service is running on the port.
		"""
		try :
			return self._icmptotportunreachablerx
		except Exception as e:
			raise e

	@property
	def icmptotneedfragrx(self) :
		r"""ICMP Fragmentation Needed error messages received for packets that need to be fragmented but for which Don't Fragment is specified the header.
		"""
		try :
			return self._icmptotneedfragrx
		except Exception as e:
			raise e

	@property
	def icmptxechoreplyrate(self) :
		r"""Rate (/s) counter for icmptottxechoreply.
		"""
		try :
			return self._icmptxechoreplyrate
		except Exception as e:
			raise e

	@property
	def icmptotnonfirstipfrag(self) :
		r"""ICMP Fragmentation Needed error messages received that were generated by an IP fragment other than the first one.
		"""
		try :
			return self._icmptotnonfirstipfrag
		except Exception as e:
			raise e

	@property
	def icmptotinvalidtcpseqno(self) :
		r"""ICMP Fragmentation Needed error messages received for packets that contain an invalid TCP address.
		"""
		try :
			return self._icmptotinvalidtcpseqno
		except Exception as e:
			raise e

	@property
	def icmprxbytesrate(self) :
		r"""Rate (/s) counter for icmptotrxbytes.
		"""
		try :
			return self._icmprxbytesrate
		except Exception as e:
			raise e

	@property
	def icmptotthresholdexceeds(self) :
		r"""Times the ICMP rate threshold is exceeded. If this counter continuously increases, first make sure the ICMP packets received are genuine. If they are, increase the current rate threshold.
		"""
		try :
			return self._icmptotthresholdexceeds
		except Exception as e:
			raise e

	@property
	def icmptottxechoreply(self) :
		r"""ICMP Ping echo replies transmitted.
		"""
		try :
			return self._icmptottxechoreply
		except Exception as e:
			raise e

	@property
	def icmptottxbytes(self) :
		r"""Bytes of ICMP data transmitted.
		"""
		try :
			return self._icmptottxbytes
		except Exception as e:
			raise e

	@property
	def icmptotrxbytes(self) :
		r"""Bytes of ICMP data received.
		"""
		try :
			return self._icmptotrxbytes
		except Exception as e:
			raise e

	@property
	def icmpcurratethreshold(self) :
		r"""Limit for ICMP packets handled every 10 milliseconds. Default value, 0, applies no limit.
		This is a configurable value using the set rateControl command.
		.
		"""
		try :
			return self._icmpcurratethreshold
		except Exception as e:
			raise e

	@property
	def icmptotbadchecksum(self) :
		r"""ICMP Fragmentation Needed error messages received with an ICMP checksum error.
		"""
		try :
			return self._icmptotbadchecksum
		except Exception as e:
			raise e

	@property
	def icmptotinvalidbodylen(self) :
		r"""ICMP Fragmentation Needed error messages received that specified an invalid body length.
		"""
		try :
			return self._icmptotinvalidbodylen
		except Exception as e:
			raise e

	@property
	def icmprxechorate(self) :
		r"""Rate (/s) counter for icmptotrxecho.
		"""
		try :
			return self._icmprxechorate
		except Exception as e:
			raise e

	@property
	def icmptotbignextmtu(self) :
		r"""ICMP Fragmentation Needed error messages received in which the value for the next MTU is higher than that of the current MTU.
		"""
		try :
			return self._icmptotbignextmtu
		except Exception as e:
			raise e

	@property
	def icmprxpktsrate(self) :
		r"""Rate (/s) counter for icmptotrxpkts.
		"""
		try :
			return self._icmprxpktsrate
		except Exception as e:
			raise e

	@property
	def icmptotpktsdropped(self) :
		r"""ICMP packets dropped because the rate threshold has been exceeded.
		"""
		try :
			return self._icmptotpktsdropped
		except Exception as e:
			raise e

	@property
	def icmptotrxechoreply(self) :
		r"""ICMP Ping echo replies received.
		"""
		try :
			return self._icmptotrxechoreply
		except Exception as e:
			raise e

	@property
	def icmptxpktsrate(self) :
		r"""Rate (/s) counter for icmptottxpkts.
		"""
		try :
			return self._icmptxpktsrate
		except Exception as e:
			raise e

	@property
	def icmptotrxpkts(self) :
		r"""ICMP packets received.
		"""
		try :
			return self._icmptotrxpkts
		except Exception as e:
			raise e

	@property
	def icmptotnotcpconn(self) :
		r"""ICMP Need Fragmentation error messages received for TCP packets. The state of the connection for these packets is not maintained on the Citrix ADC.
		"""
		try :
			return self._icmptotnotcpconn
		except Exception as e:
			raise e

	@property
	def icmptxbytesrate(self) :
		r"""Rate (/s) counter for icmptottxbytes.
		"""
		try :
			return self._icmptxbytesrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(protocolicmp_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.protocolicmp
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
		r""" Use this API to fetch the statistics of all protocolicmp_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = protocolicmp_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class protocolicmp_response(base_response) :
	def __init__(self, length=1) :
		self.protocolicmp = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.protocolicmp = [protocolicmp_stats() for _ in range(length)]

