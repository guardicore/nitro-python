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

class nsmode(base_resource) :
	""" Configuration for ns mode resource. """
	def __init__(self) :
		self._mode = None
		self._fr = None
		self._l2 = None
		self._usip = None
		self._cka = None
		self._tcpb = None
		self._mbf = None
		self._edge = None
		self._usnip = None
		self._l3 = None
		self._pmtud = None
		self._mediaclassification = None
		self._sradv = None
		self._dradv = None
		self._iradv = None
		self._sradv6 = None
		self._dradv6 = None
		self._bridgebpdus = None
		self._ulfd = None

	@property
	def mode(self) :
		r"""Mode to be enabled. Multiple modes can be specified by providing a blank space between each mode.<br/>Possible values = FR, FastRamp, L2, L2mode, L3, L3mode, USIP, UseSourceIP, CKA, ClientKeepAlive, TCPB, TCPBuffering, MBF, MACbasedforwarding, Edge, USNIP, SRADV, DRADV, IRADV, SRADV6, DRADV6, PMTUD, RISE_APBR, RISE_RHI, BridgeBPDUs, ULFD.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		r"""Mode to be enabled. Multiple modes can be specified by providing a blank space between each mode.<br/>Possible values = FR, FastRamp, L2, L2mode, L3, L3mode, USIP, UseSourceIP, CKA, ClientKeepAlive, TCPB, TCPBuffering, MBF, MACbasedforwarding, Edge, USNIP, SRADV, DRADV, IRADV, SRADV6, DRADV6, PMTUD, RISE_APBR, RISE_RHI, BridgeBPDUs, ULFD
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def fr(self) :
		r"""Fast Ramp.
		"""
		try :
			return self._fr
		except Exception as e:
			raise e

	@property
	def l2(self) :
		r"""Layer 2 mode.
		"""
		try :
			return self._l2
		except Exception as e:
			raise e

	@property
	def usip(self) :
		r"""Use Source IP.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@property
	def cka(self) :
		r"""Client Keep-alive.
		"""
		try :
			return self._cka
		except Exception as e:
			raise e

	@property
	def tcpb(self) :
		r"""TCP Buffering.
		"""
		try :
			return self._tcpb
		except Exception as e:
			raise e

	@property
	def mbf(self) :
		r"""MAC-based forwarding.
		"""
		try :
			return self._mbf
		except Exception as e:
			raise e

	@property
	def edge(self) :
		r"""Edge configuration.
		"""
		try :
			return self._edge
		except Exception as e:
			raise e

	@property
	def usnip(self) :
		r"""Use Subnet IP.
		"""
		try :
			return self._usnip
		except Exception as e:
			raise e

	@property
	def l3(self) :
		r"""Layer 3 mode (ip forwarding).
		"""
		try :
			return self._l3
		except Exception as e:
			raise e

	@property
	def pmtud(self) :
		r"""Path MTU Discovery.
		"""
		try :
			return self._pmtud
		except Exception as e:
			raise e

	@property
	def mediaclassification(self) :
		r"""mediaclassification.
		"""
		try :
			return self._mediaclassification
		except Exception as e:
			raise e

	@property
	def sradv(self) :
		r"""Static Route Advertisement.
		"""
		try :
			return self._sradv
		except Exception as e:
			raise e

	@property
	def dradv(self) :
		r"""Direct Route Advertisement.
		"""
		try :
			return self._dradv
		except Exception as e:
			raise e

	@property
	def iradv(self) :
		r"""Intranet Route Advertisement.
		"""
		try :
			return self._iradv
		except Exception as e:
			raise e

	@property
	def sradv6(self) :
		r"""Ipv6 Static Route Advertisement.
		"""
		try :
			return self._sradv6
		except Exception as e:
			raise e

	@property
	def dradv6(self) :
		r"""Ipv6 Direct Route Advertisement.
		"""
		try :
			return self._dradv6
		except Exception as e:
			raise e

	@property
	def bridgebpdus(self) :
		r"""BPDU Bridging Mode.
		"""
		try :
			return self._bridgebpdus
		except Exception as e:
			raise e

	@property
	def ulfd(self) :
		r"""Unified Logging Framework Mode for adding/removing ULF services.
		"""
		try :
			return self._ulfd
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsmode_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsmode
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
	def enable(cls, client, resource) :
		r""" Use this API to enable nsmode.
		"""
		try :
			if type(resource) is not list :
				enableresource = nsmode()
				enableresource.mode = resource.mode
				return enableresource.perform_operation(client,"enable")
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nsmode.
		"""
		try :
			if type(resource) is not list :
				disableresource = nsmode()
				disableresource.mode = resource.mode
				return disableresource.perform_operation(client,"disable")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsmode resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsmode()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Mode:
		FR = "FR"
		FastRamp = "FastRamp"
		L2 = "L2"
		L2mode = "L2mode"
		L3 = "L3"
		L3mode = "L3mode"
		USIP = "USIP"
		UseSourceIP = "UseSourceIP"
		CKA = "CKA"
		ClientKeepAlive = "ClientKeepAlive"
		TCPB = "TCPB"
		TCPBuffering = "TCPBuffering"
		MBF = "MBF"
		MACbasedforwarding = "MACbasedforwarding"
		Edge = "Edge"
		USNIP = "USNIP"
		SRADV = "SRADV"
		DRADV = "DRADV"
		IRADV = "IRADV"
		SRADV6 = "SRADV6"
		DRADV6 = "DRADV6"
		PMTUD = "PMTUD"
		RISE_APBR = "RISE_APBR"
		RISE_RHI = "RISE_RHI"
		BridgeBPDUs = "BridgeBPDUs"
		ULFD = "ULFD"

class nsmode_response(base_response) :
	def __init__(self, length=1) :
		self.nsmode = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsmode = [nsmode() for _ in range(length)]

