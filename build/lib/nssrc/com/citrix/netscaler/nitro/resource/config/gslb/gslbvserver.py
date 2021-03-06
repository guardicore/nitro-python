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

class gslbvserver(base_resource) :
	""" Configuration for Global Server Load Balancing Virtual Server resource. """
	def __init__(self) :
		self._name = None
		self._servicetype = None
		self._iptype = None
		self._dnsrecordtype = None
		self._lbmethod = None
		self._backupsessiontimeout = None
		self._backuplbmethod = None
		self._netmask = None
		self._v6netmasklen = None
		self._rule = None
		self._tolerance = None
		self._persistencetype = None
		self._persistenceid = None
		self._persistmask = None
		self._v6persistmasklen = None
		self._timeout = None
		self._edr = None
		self._ecs = None
		self._ecsaddrvalidation = None
		self._mir = None
		self._disableprimaryondown = None
		self._dynamicweight = None
		self._state = None
		self._considereffectivestate = None
		self._comment = None
		self._somethod = None
		self._sopersistence = None
		self._sopersistencetimeout = None
		self._sothreshold = None
		self._sobackupaction = None
		self._appflowlog = None
		self._backupvserver = None
		self._servicename = None
		self._weight = None
		self._domainname = None
		self._ttl = None
		self._backupip = None
		self._cookie_domain = None
		self._cookietimeout = None
		self._sitedomainttl = None
		self._newname = None
		self._curstate = None
		self._status = None
		self._lbrrreason = None
		self._iscname = None
		self._sitepersistence = None
		self._totalservices = None
		self._activeservices = None
		self._statechangetimesec = None
		self._statechangetimemsec = None
		self._tickssincelaststatechange = None
		self._health = None
		self._policyname = None
		self._priority = None
		self._gotopriorityexpression = None
		self._type = None
		self._vsvrbindsvcip = None
		self._vsvrbindsvcport = None
		self._servername = None
		self._nodefaultbindings = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.
		CLI Users:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol used by services bound to the virtual server.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol used by services bound to the virtual server.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def iptype(self) :
		r"""The IP type for this GSLB vserver.<br/>Default value: IPV4<br/>Possible values = IPV4, IPV6.
		"""
		try :
			return self._iptype
		except Exception as e:
			raise e

	@iptype.setter
	def iptype(self, iptype) :
		r"""The IP type for this GSLB vserver.<br/>Default value: IPV4<br/>Possible values = IPV4, IPV6
		"""
		try :
			self._iptype = iptype
		except Exception as e:
			raise e

	@property
	def dnsrecordtype(self) :
		r"""DNS record type to associate with the GSLB virtual server's domain name.<br/>Default value: A<br/>Possible values = A, AAAA, CNAME, NAPTR.
		"""
		try :
			return self._dnsrecordtype
		except Exception as e:
			raise e

	@dnsrecordtype.setter
	def dnsrecordtype(self, dnsrecordtype) :
		r"""DNS record type to associate with the GSLB virtual server's domain name.<br/>Default value: A<br/>Possible values = A, AAAA, CNAME, NAPTR
		"""
		try :
			self._dnsrecordtype = dnsrecordtype
		except Exception as e:
			raise e

	@property
	def lbmethod(self) :
		r"""Load balancing method for the GSLB virtual server.<br/>Default value: LEASTCONNECTION<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API.
		"""
		try :
			return self._lbmethod
		except Exception as e:
			raise e

	@lbmethod.setter
	def lbmethod(self, lbmethod) :
		r"""Load balancing method for the GSLB virtual server.<br/>Default value: LEASTCONNECTION<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API
		"""
		try :
			self._lbmethod = lbmethod
		except Exception as e:
			raise e

	@property
	def backupsessiontimeout(self) :
		r"""A non zero value enables the feature whose minimum value is 2 minutes. The feature can be disabled by setting the value to zero. The created session is in effect for a specific client per domain.<br/>Maximum length =  1440.
		"""
		try :
			return self._backupsessiontimeout
		except Exception as e:
			raise e

	@backupsessiontimeout.setter
	def backupsessiontimeout(self, backupsessiontimeout) :
		r"""A non zero value enables the feature whose minimum value is 2 minutes. The feature can be disabled by setting the value to zero. The created session is in effect for a specific client per domain.<br/>Maximum length =  1440
		"""
		try :
			self._backupsessiontimeout = backupsessiontimeout
		except Exception as e:
			raise e

	@property
	def backuplbmethod(self) :
		r"""Backup load balancing method. Becomes operational if the primary load balancing method fails or cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static proximity.<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API.
		"""
		try :
			return self._backuplbmethod
		except Exception as e:
			raise e

	@backuplbmethod.setter
	def backuplbmethod(self, backuplbmethod) :
		r"""Backup load balancing method. Becomes operational if the primary load balancing method fails or cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static proximity.<br/>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD, API
		"""
		try :
			self._backuplbmethod = backuplbmethod
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""IPv4 network mask for use in the SOURCEIPHASH load balancing method.<br/>Minimum length =  1.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""IPv4 network mask for use in the SOURCEIPHASH load balancing method.<br/>Minimum length =  1
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def v6netmasklen(self) :
		r"""Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the SOURCEIPHASH load balancing method.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6netmasklen
		except Exception as e:
			raise e

	@v6netmasklen.setter
	def v6netmasklen(self, v6netmasklen) :
		r"""Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the SOURCEIPHASH load balancing method.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6netmasklen = v6netmasklen
		except Exception as e:
			raise e

	@property
	def rule(self) :
		r"""Expression, or name of a named expression, against which traffic is evaluated.
		This field is applicable only if gslb method or gslb backup method are set to API.
		The following requirements apply only to the Citrix ADC CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "none".
		"""
		try :
			return self._rule
		except Exception as e:
			raise e

	@rule.setter
	def rule(self, rule) :
		r"""Expression, or name of a named expression, against which traffic is evaluated.
		This field is applicable only if gslb method or gslb backup method are set to API.
		The following requirements apply only to the Citrix ADC CLI:
		* If the expression includes one or more spaces, enclose the entire expression in double quotation marks.
		* If the expression itself includes double quotation marks, escape the quotations by using the \ character. 
		* Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.<br/>Default value: "none"
		"""
		try :
			self._rule = rule
		except Exception as e:
			raise e

	@property
	def tolerance(self) :
		r"""Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a site's RTT deviates from the lowest RTT by more than the specified tolerance, the site is not considered when the Citrix ADC makes a GSLB decision. The appliance implements the round robin method of global server load balancing between sites whose RTT values are within the specified tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the site with the lowest RTT.<br/>Maximum length =  100.
		"""
		try :
			return self._tolerance
		except Exception as e:
			raise e

	@tolerance.setter
	def tolerance(self, tolerance) :
		r"""Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a site's RTT deviates from the lowest RTT by more than the specified tolerance, the site is not considered when the Citrix ADC makes a GSLB decision. The appliance implements the round robin method of global server load balancing between sites whose RTT values are within the specified tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the site with the lowest RTT.<br/>Maximum length =  100
		"""
		try :
			self._tolerance = tolerance
		except Exception as e:
			raise e

	@property
	def persistencetype(self) :
		r"""Use source IP address based persistence for the virtual server. 
		After the load balancing method selects a service for the first packet, the IP address received in response to the DNS query is used for subsequent requests from the same client.<br/>Possible values = SOURCEIP, NONE.
		"""
		try :
			return self._persistencetype
		except Exception as e:
			raise e

	@persistencetype.setter
	def persistencetype(self, persistencetype) :
		r"""Use source IP address based persistence for the virtual server. 
		After the load balancing method selects a service for the first packet, the IP address received in response to the DNS query is used for subsequent requests from the same client.<br/>Possible values = SOURCEIP, NONE
		"""
		try :
			self._persistencetype = persistencetype
		except Exception as e:
			raise e

	@property
	def persistenceid(self) :
		r"""The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites to identify the GSLB virtual server, and is required if source IP address based or spill over based persistence is enabled on the virtual server.<br/>Maximum length =  65535.
		"""
		try :
			return self._persistenceid
		except Exception as e:
			raise e

	@persistenceid.setter
	def persistenceid(self, persistenceid) :
		r"""The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites to identify the GSLB virtual server, and is required if source IP address based or spill over based persistence is enabled on the virtual server.<br/>Maximum length =  65535
		"""
		try :
			self._persistenceid = persistenceid
		except Exception as e:
			raise e

	@property
	def persistmask(self) :
		r"""The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.<br/>Minimum length =  1.
		"""
		try :
			return self._persistmask
		except Exception as e:
			raise e

	@persistmask.setter
	def persistmask(self, persistmask) :
		r"""The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.<br/>Minimum length =  1
		"""
		try :
			self._persistmask = persistmask
		except Exception as e:
			raise e

	@property
	def v6persistmasklen(self) :
		r"""Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128.
		"""
		try :
			return self._v6persistmasklen
		except Exception as e:
			raise e

	@v6persistmasklen.setter
	def v6persistmasklen(self, v6persistmasklen) :
		r"""Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  128
		"""
		try :
			self._v6persistmasklen = v6persistmasklen
		except Exception as e:
			raise e

	@property
	def timeout(self) :
		r"""Idle time, in minutes, after which a persistence entry is cleared.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._timeout
		except Exception as e:
			raise e

	@timeout.setter
	def timeout(self, timeout) :
		r"""Idle time, in minutes, after which a persistence entry is cleared.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._timeout = timeout
		except Exception as e:
			raise e

	@property
	def edr(self) :
		r"""Send clients an empty DNS response when the GSLB virtual server is DOWN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._edr
		except Exception as e:
			raise e

	@edr.setter
	def edr(self, edr) :
		r"""Send clients an empty DNS response when the GSLB virtual server is DOWN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._edr = edr
		except Exception as e:
			raise e

	@property
	def ecs(self) :
		r"""If enabled, respond with EDNS Client Subnet (ECS) option in the response for a DNS query with ECS. The ECS address will be used for persistence and spillover persistence (if enabled) instead of the LDNS address. Persistence mask is ignored if ECS is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ecs
		except Exception as e:
			raise e

	@ecs.setter
	def ecs(self, ecs) :
		r"""If enabled, respond with EDNS Client Subnet (ECS) option in the response for a DNS query with ECS. The ECS address will be used for persistence and spillover persistence (if enabled) instead of the LDNS address. Persistence mask is ignored if ECS is enabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ecs = ecs
		except Exception as e:
			raise e

	@property
	def ecsaddrvalidation(self) :
		r"""Validate if ECS address is a private or unroutable address and in such cases, use the LDNS IP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ecsaddrvalidation
		except Exception as e:
			raise e

	@ecsaddrvalidation.setter
	def ecsaddrvalidation(self, ecsaddrvalidation) :
		r"""Validate if ECS address is a private or unroutable address and in such cases, use the LDNS IP.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ecsaddrvalidation = ecsaddrvalidation
		except Exception as e:
			raise e

	@property
	def mir(self) :
		r"""Include multiple IP addresses in the DNS responses sent to clients.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._mir
		except Exception as e:
			raise e

	@mir.setter
	def mir(self, mir) :
		r"""Include multiple IP addresses in the DNS responses sent to clients.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._mir = mir
		except Exception as e:
			raise e

	@property
	def disableprimaryondown(self) :
		r"""Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to the UP state. Used when spillover is configured for the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._disableprimaryondown
		except Exception as e:
			raise e

	@disableprimaryondown.setter
	def disableprimaryondown(self, disableprimaryondown) :
		r"""Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to the UP state. Used when spillover is configured for the virtual server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._disableprimaryondown = disableprimaryondown
		except Exception as e:
			raise e

	@property
	def dynamicweight(self) :
		r"""Specify if the appliance should consider the service count, service weights, or ignore both when using weight-based load balancing methods. The state of the number of services bound to the virtual server help the appliance to select the service.<br/>Default value: DISABLED<br/>Possible values = SERVICECOUNT, SERVICEWEIGHT, DISABLED.
		"""
		try :
			return self._dynamicweight
		except Exception as e:
			raise e

	@dynamicweight.setter
	def dynamicweight(self, dynamicweight) :
		r"""Specify if the appliance should consider the service count, service weights, or ignore both when using weight-based load balancing methods. The state of the number of services bound to the virtual server help the appliance to select the service.<br/>Default value: DISABLED<br/>Possible values = SERVICECOUNT, SERVICEWEIGHT, DISABLED
		"""
		try :
			self._dynamicweight = dynamicweight
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""State of the GSLB virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""State of the GSLB virtual server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def considereffectivestate(self) :
		r"""If the primary state of all bound GSLB services is DOWN, consider the effective states of all the GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To disregard the effective state, set the parameter to NONE. 
		The effective state of a GSLB service is the ability of the corresponding virtual server to serve traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP state.<br/>Default value: NONE<br/>Possible values = NONE, STATE_ONLY.
		"""
		try :
			return self._considereffectivestate
		except Exception as e:
			raise e

	@considereffectivestate.setter
	def considereffectivestate(self, considereffectivestate) :
		r"""If the primary state of all bound GSLB services is DOWN, consider the effective states of all the GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To disregard the effective state, set the parameter to NONE. 
		The effective state of a GSLB service is the ability of the corresponding virtual server to serve traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP state.<br/>Default value: NONE<br/>Possible values = NONE, STATE_ONLY
		"""
		try :
			self._considereffectivestate = considereffectivestate
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments that you might want to associate with the GSLB virtual server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments that you might want to associate with the GSLB virtual server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def somethod(self) :
		r"""Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:
		* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.
		* DYNAMICCONNECTION - Spillover occurs when the number of client connections at the GSLB virtual server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of the bound GSLB services.
		* BANDWIDTH - Spillover occurs when the bandwidth consumed by the GSLB virtual server's incoming and outgoing traffic exceeds the threshold. 
		* HEALTH - Spillover occurs when the percentage of weights of the GSLB services that are UP drops below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN. 
		* NONE - Spillover does not occur.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE.
		"""
		try :
			return self._somethod
		except Exception as e:
			raise e

	@somethod.setter
	def somethod(self, somethod) :
		r"""Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:
		* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.
		* DYNAMICCONNECTION - Spillover occurs when the number of client connections at the GSLB virtual server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of the bound GSLB services.
		* BANDWIDTH - Spillover occurs when the bandwidth consumed by the GSLB virtual server's incoming and outgoing traffic exceeds the threshold. 
		* HEALTH - Spillover occurs when the percentage of weights of the GSLB services that are UP drops below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN. 
		* NONE - Spillover does not occur.<br/>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE
		"""
		try :
			self._somethod = somethod
		except Exception as e:
			raise e

	@property
	def sopersistence(self) :
		r"""If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sopersistence
		except Exception as e:
			raise e

	@sopersistence.setter
	def sopersistence(self, sopersistence) :
		r"""If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sopersistence = sopersistence
		except Exception as e:
			raise e

	@property
	def sopersistencetimeout(self) :
		r"""Timeout for spillover persistence, in minutes.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440.
		"""
		try :
			return self._sopersistencetimeout
		except Exception as e:
			raise e

	@sopersistencetimeout.setter
	def sopersistencetimeout(self, sopersistencetimeout) :
		r"""Timeout for spillover persistence, in minutes.<br/>Default value: 2<br/>Minimum length =  2<br/>Maximum length =  1440
		"""
		try :
			self._sopersistencetimeout = sopersistencetimeout
		except Exception as e:
			raise e

	@property
	def sothreshold(self) :
		r"""Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).<br/>Minimum length =  1<br/>Maximum length =  4294967287.
		"""
		try :
			return self._sothreshold
		except Exception as e:
			raise e

	@sothreshold.setter
	def sothreshold(self, sothreshold) :
		r"""Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).<br/>Minimum length =  1<br/>Maximum length =  4294967287
		"""
		try :
			self._sothreshold = sothreshold
		except Exception as e:
			raise e

	@property
	def sobackupaction(self) :
		r"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT.
		"""
		try :
			return self._sobackupaction
		except Exception as e:
			raise e

	@sobackupaction.setter
	def sobackupaction(self, sobackupaction) :
		r"""Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.<br/>Possible values = DROP, ACCEPT, REDIRECT
		"""
		try :
			self._sobackupaction = sobackupaction
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable logging appflow flow information.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def backupvserver(self) :
		r"""Name of the backup GSLB virtual server to which the appliance should to forward requests if the status of the primary GSLB virtual server is down or exceeds its spillover threshold.<br/>Minimum length =  1.
		"""
		try :
			return self._backupvserver
		except Exception as e:
			raise e

	@backupvserver.setter
	def backupvserver(self, backupvserver) :
		r"""Name of the backup GSLB virtual server to which the appliance should to forward requests if the status of the primary GSLB virtual server is down or exceeds its spillover threshold.<br/>Minimum length =  1
		"""
		try :
			self._backupvserver = backupvserver
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""Name of the GSLB service for which to change the weight.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		r"""Name of the GSLB service for which to change the weight.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the GSLB service.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the GSLB service.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def domainname(self) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._domainname
		except Exception as e:
			raise e

	@domainname.setter
	def domainname(self, domainname) :
		r"""Domain name for which to change the time to live (TTL) and/or backup service IP address.<br/>Minimum length =  1
		"""
		try :
			self._domainname = domainname
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Time to live (TTL) for the domain.<br/>Minimum length =  1.
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@ttl.setter
	def ttl(self, ttl) :
		r"""Time to live (TTL) for the domain.<br/>Minimum length =  1
		"""
		try :
			self._ttl = ttl
		except Exception as e:
			raise e

	@property
	def backupip(self) :
		r"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.<br/>Minimum length =  1.
		"""
		try :
			return self._backupip
		except Exception as e:
			raise e

	@backupip.setter
	def backupip(self, backupip) :
		r"""The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.<br/>Minimum length =  1
		"""
		try :
			self._backupip = backupip
		except Exception as e:
			raise e

	@property
	def cookie_domain(self) :
		r"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.<br/>Minimum length =  1.
		"""
		try :
			return self._cookie_domain
		except Exception as e:
			raise e

	@cookie_domain.setter
	def cookie_domain(self, cookie_domain) :
		r"""The cookie domain for the GSLB site. Used when inserting the GSLB site cookie in the HTTP response.<br/>Minimum length =  1
		"""
		try :
			self._cookie_domain = cookie_domain
		except Exception as e:
			raise e

	@property
	def cookietimeout(self) :
		r"""Timeout, in minutes, for the GSLB site cookie.<br/>Maximum length =  1440.
		"""
		try :
			return self._cookietimeout
		except Exception as e:
			raise e

	@cookietimeout.setter
	def cookietimeout(self, cookietimeout) :
		r"""Timeout, in minutes, for the GSLB site cookie.<br/>Maximum length =  1440
		"""
		try :
			self._cookietimeout = cookietimeout
		except Exception as e:
			raise e

	@property
	def sitedomainttl(self) :
		r"""TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._sitedomainttl
		except Exception as e:
			raise e

	@sitedomainttl.setter
	def sitedomainttl(self, sitedomainttl) :
		r"""TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server.<br/>Minimum length =  1
		"""
		try :
			self._sitedomainttl = sitedomainttl
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the GSLB virtual server.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the GSLB virtual server.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""State of the gslb vserver.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Current status of the gslb vserver. During the initial phase if the configured lb method is not round robin , the vserver will adopt round robin to distribute traffic for a predefined number of requests.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def lbrrreason(self) :
		r"""Reason why a vserver is in RR. The following are the reasons:
		1  - MEP is DOWN (GSLB)
		2  - LB method has changed
		3  - Bound service's state changed to UP
		4  - A new service is bound
		5  - Startup RR factor has changed
		6  - LB feature is enabled
		7  - Load monitor is not active on a service
		8  - Vserver is Enabled
		9  - SSL feature is Enabled
		10 - All bound services have reached threshold. Using effective state to load balance (GSLB)
		11 - Primary state of bound services are not UP. Using effective state to load balance (GSLB)
		12 - No LB decision can be made as all bound services have either reached threshold or are not UP (GSLB)
		13 - All load monitors are active
		.
		"""
		try :
			return self._lbrrreason
		except Exception as e:
			raise e

	@property
	def iscname(self) :
		r"""is cname feature set on vserver.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._iscname
		except Exception as e:
			raise e

	@property
	def sitepersistence(self) :
		r"""Type of Site Persistence set.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE.
		"""
		try :
			return self._sitepersistence
		except Exception as e:
			raise e

	@property
	def totalservices(self) :
		r"""Total number of services bound to the vserver.
		"""
		try :
			return self._totalservices
		except Exception as e:
			raise e

	@property
	def activeservices(self) :
		r"""Total number of active services bound to the vserver.
		"""
		try :
			return self._activeservices
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		r"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		r"""Time at which last state change happened. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def tickssincelaststatechange(self) :
		r"""Time in 10 millisecond ticks since the last state change.
		"""
		try :
			return self._tickssincelaststatechange
		except Exception as e:
			raise e

	@property
	def health(self) :
		r"""Health of vserver based on percentage of weights of active svcs/all svcs. This does not consider administratively disabled svcs.
		"""
		try :
			return self._health
		except Exception as e:
			raise e

	@property
	def policyname(self) :
		r"""Name of the policy bound to the GSLB vserver.
		"""
		try :
			return self._policyname
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority.<br/>Minimum value =  1<br/>Maximum value =  2147483647.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def gotopriorityexpression(self) :
		r"""Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.
		o	If gotoPriorityExpression is not present or if it is equal to END then the policy bank evaluation ends here
		o	Else if the gotoPriorityExpression is equal to NEXT then the next policy in the priority order is evaluated.
		o	Else gotoPriorityExpression is evaluated. The result of gotoPriorityExpression (which has to be a number) is processed as follows:
		-	An UNDEF event is triggered if
		.	gotoPriorityExpression cannot be evaluated
		.	gotoPriorityExpression evaluates to number which is smaller than the maximum priority in the policy bank but is not same as any policy's priority
		.	gotoPriorityExpression evaluates to a priority that is smaller than the current policy's priority
		-	If the gotoPriorityExpression evaluates to the priority of the current policy then the next policy in the priority order is evaluated.
		-	If the gotoPriorityExpression evaluates to the priority of a policy further ahead in the list then that policy will be evaluated next.
		This field is applicable only to rewrite and responder policies.
		"""
		try :
			return self._gotopriorityexpression
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""The bindpoint to which the policy is bound.<br/>Possible values = REQUEST, RESPONSE, MQTT_JUMBO_REQ.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@property
	def vsvrbindsvcip(self) :
		r"""used for showing the ip of bound entities.
		"""
		try :
			return self._vsvrbindsvcip
		except Exception as e:
			raise e

	@property
	def vsvrbindsvcport(self) :
		r"""used for showing ports of bound entities.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._vsvrbindsvcport
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""This field is used to display server name in case of GSLB servicegroup binding to GSLB vserver .
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@property
	def nodefaultbindings(self) :
		r"""to determine if the configuration will have default ssl CIPHER and ECC curve bindings.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nodefaultbindings
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbvserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbvserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = gslbvserver()
		addresource.name = resource.name
		addresource.servicetype = resource.servicetype
		addresource.iptype = resource.iptype
		addresource.dnsrecordtype = resource.dnsrecordtype
		addresource.lbmethod = resource.lbmethod
		addresource.backupsessiontimeout = resource.backupsessiontimeout
		addresource.backuplbmethod = resource.backuplbmethod
		addresource.netmask = resource.netmask
		addresource.v6netmasklen = resource.v6netmasklen
		addresource.rule = resource.rule
		addresource.tolerance = resource.tolerance
		addresource.persistencetype = resource.persistencetype
		addresource.persistenceid = resource.persistenceid
		addresource.persistmask = resource.persistmask
		addresource.v6persistmasklen = resource.v6persistmasklen
		addresource.timeout = resource.timeout
		addresource.edr = resource.edr
		addresource.ecs = resource.ecs
		addresource.ecsaddrvalidation = resource.ecsaddrvalidation
		addresource.mir = resource.mir
		addresource.disableprimaryondown = resource.disableprimaryondown
		addresource.dynamicweight = resource.dynamicweight
		addresource.state = resource.state
		addresource.considereffectivestate = resource.considereffectivestate
		addresource.comment = resource.comment
		addresource.somethod = resource.somethod
		addresource.sopersistence = resource.sopersistence
		addresource.sopersistencetimeout = resource.sopersistencetimeout
		addresource.sothreshold = resource.sothreshold
		addresource.sobackupaction = resource.sobackupaction
		addresource.appflowlog = resource.appflowlog
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add gslbvserver.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ gslbvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = gslbvserver()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete gslbvserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = gslbvserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = gslbvserver()
		updateresource.name = resource.name
		updateresource.iptype = resource.iptype
		updateresource.dnsrecordtype = resource.dnsrecordtype
		updateresource.backupvserver = resource.backupvserver
		updateresource.backupsessiontimeout = resource.backupsessiontimeout
		updateresource.lbmethod = resource.lbmethod
		updateresource.backuplbmethod = resource.backuplbmethod
		updateresource.netmask = resource.netmask
		updateresource.v6netmasklen = resource.v6netmasklen
		updateresource.tolerance = resource.tolerance
		updateresource.persistencetype = resource.persistencetype
		updateresource.persistenceid = resource.persistenceid
		updateresource.persistmask = resource.persistmask
		updateresource.v6persistmasklen = resource.v6persistmasklen
		updateresource.timeout = resource.timeout
		updateresource.edr = resource.edr
		updateresource.ecs = resource.ecs
		updateresource.ecsaddrvalidation = resource.ecsaddrvalidation
		updateresource.mir = resource.mir
		updateresource.disableprimaryondown = resource.disableprimaryondown
		updateresource.dynamicweight = resource.dynamicweight
		updateresource.considereffectivestate = resource.considereffectivestate
		updateresource.somethod = resource.somethod
		updateresource.sopersistence = resource.sopersistence
		updateresource.sopersistencetimeout = resource.sopersistencetimeout
		updateresource.sothreshold = resource.sothreshold
		updateresource.sobackupaction = resource.sobackupaction
		updateresource.servicename = resource.servicename
		updateresource.weight = resource.weight
		updateresource.domainname = resource.domainname
		updateresource.ttl = resource.ttl
		updateresource.backupip = resource.backupip
		updateresource.cookie_domain = resource.cookie_domain
		updateresource.cookietimeout = resource.cookietimeout
		updateresource.sitedomainttl = resource.sitedomainttl
		updateresource.comment = resource.comment
		updateresource.appflowlog = resource.appflowlog
		updateresource.rule = resource.rule
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update gslbvserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ gslbvserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of gslbvserver resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbvserver()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable gslbvserver.
		"""
		try :
			if type(resource) is not list :
				enableresource = gslbvserver()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable gslbvserver.
		"""
		try :
			if type(resource) is not list :
				disableresource = gslbvserver()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ gslbvserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a gslbvserver resource.
		"""
		try :
			renameresource = gslbvserver()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the gslbvserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbvserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = gslbvserver()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [gslbvserver() for _ in range(len(name))]
						obj = [gslbvserver() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = gslbvserver()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of gslbvserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the gslbvserver resources configured on NetScaler.
		"""
		try :
			obj = gslbvserver()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of gslbvserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbvserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Backuplbmethod:
		ROUNDROBIN = "ROUNDROBIN"
		LEASTCONNECTION = "LEASTCONNECTION"
		LEASTRESPONSETIME = "LEASTRESPONSETIME"
		SOURCEIPHASH = "SOURCEIPHASH"
		LEASTBANDWIDTH = "LEASTBANDWIDTH"
		LEASTPACKETS = "LEASTPACKETS"
		STATICPROXIMITY = "STATICPROXIMITY"
		RTT = "RTT"
		CUSTOMLOAD = "CUSTOMLOAD"
		API = "API"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		RADIUS = "RADIUS"
		RDP = "RDP"
		RTSP = "RTSP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"

	class Sopersistence:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Edr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sitepersistence:
		ConnectionProxy = "ConnectionProxy"
		HTTPRedirect = "HTTPRedirect"
		NONE = "NONE"

	class Considereffectivestate:
		NONE = "NONE"
		STATE_ONLY = "STATE_ONLY"

	class Iscname:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Persistencetype:
		SOURCEIP = "SOURCEIP"
		NONE = "NONE"

	class Iptype:
		IPV4 = "IPV4"
		IPV6 = "IPV6"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nodefaultbindings:
		YES = "YES"
		NO = "NO"

	class Dnsrecordtype:
		A = "A"
		AAAA = "AAAA"
		CNAME = "CNAME"
		NAPTR = "NAPTR"

	class Ecsaddrvalidation:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sobackupaction:
		DROP = "DROP"
		ACCEPT = "ACCEPT"
		REDIRECT = "REDIRECT"

	class Type:
		REQUEST = "REQUEST"
		RESPONSE = "RESPONSE"
		MQTT_JUMBO_REQ = "MQTT_JUMBO_REQ"

	class Disableprimaryondown:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Mir:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Somethod:
		CONNECTION = "CONNECTION"
		DYNAMICCONNECTION = "DYNAMICCONNECTION"
		BANDWIDTH = "BANDWIDTH"
		HEALTH = "HEALTH"
		NONE = "NONE"

	class Lbmethod:
		ROUNDROBIN = "ROUNDROBIN"
		LEASTCONNECTION = "LEASTCONNECTION"
		LEASTRESPONSETIME = "LEASTRESPONSETIME"
		SOURCEIPHASH = "SOURCEIPHASH"
		LEASTBANDWIDTH = "LEASTBANDWIDTH"
		LEASTPACKETS = "LEASTPACKETS"
		STATICPROXIMITY = "STATICPROXIMITY"
		RTT = "RTT"
		CUSTOMLOAD = "CUSTOMLOAD"
		API = "API"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Curstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Dynamicweight:
		SERVICECOUNT = "SERVICECOUNT"
		SERVICEWEIGHT = "SERVICEWEIGHT"
		DISABLED = "DISABLED"

	class Ecs:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class gslbvserver_response(base_response) :
	def __init__(self, length=1) :
		self.gslbvserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbvserver = [gslbvserver() for _ in range(length)]

