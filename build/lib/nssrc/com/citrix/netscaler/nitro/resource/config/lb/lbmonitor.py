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

class lbmonitor(base_resource) :
	""" Configuration for monitor resource. """
	def __init__(self) :
		self._monitorname = None
		self._type = None
		self._action = None
		self._respcode = None
		self._httprequest = None
		self._rtsprequest = None
		self._customheaders = None
		self._maxforwards = None
		self._sipmethod = None
		self._sipuri = None
		self._sipreguri = None
		self._send = None
		self._recv = None
		self._query = None
		self._querytype = None
		self._scriptname = None
		self._scriptargs = None
		self._dispatcherip = None
		self._dispatcherport = None
		self._username = None
		self._password = None
		self._secondarypassword = None
		self._logonpointname = None
		self._lasversion = None
		self._radkey = None
		self._radnasid = None
		self._radnasip = None
		self._radaccounttype = None
		self._radframedip = None
		self._radapn = None
		self._radmsisdn = None
		self._radaccountsession = None
		self._lrtm = None
		self._deviation = None
		self._units1 = None
		self._interval = None
		self._units3 = None
		self._resptimeout = None
		self._units4 = None
		self._resptimeoutthresh = None
		self._retries = None
		self._failureretries = None
		self._alertretries = None
		self._successretries = None
		self._downtime = None
		self._units2 = None
		self._destip = None
		self._destport = None
		self._state = None
		self._reverse = None
		self._transparent = None
		self._iptunnel = None
		self._tos = None
		self._tosid = None
		self._secure = None
		self._validatecred = None
		self._domain = None
		self._ipaddress = None
		self._group = None
		self._filename = None
		self._basedn = None
		self._binddn = None
		self._filter = None
		self._attribute = None
		self._database = None
		self._oraclesid = None
		self._sqlquery = None
		self._evalrule = None
		self._mssqlprotocolversion = None
		self._Snmpoid = None
		self._snmpcommunity = None
		self._snmpthreshold = None
		self._snmpversion = None
		self._metrictable = None
		self._application = None
		self._sitepath = None
		self._storename = None
		self._storefrontacctservice = None
		self._hostname = None
		self._netprofile = None
		self._originhost = None
		self._originrealm = None
		self._hostipaddress = None
		self._vendorid = None
		self._productname = None
		self._firmwarerevision = None
		self._authapplicationid = None
		self._acctapplicationid = None
		self._inbandsecurityid = None
		self._supportedvendorids = None
		self._vendorspecificvendorid = None
		self._vendorspecificauthapplicationids = None
		self._vendorspecificacctapplicationids = None
		self._kcdaccount = None
		self._storedb = None
		self._storefrontcheckbackendservices = None
		self._trofscode = None
		self._trofsstring = None
		self._sslprofile = None
		self._mqttclientidentifier = None
		self._mqttversion = None
		self._metric = None
		self._metricthreshold = None
		self._metricweight = None
		self._servicename = None
		self._servicegroupname = None
		self._lrtmconf = None
		self._lrtmconfstr = None
		self._dynamicresponsetimeout = None
		self._dynamicinterval = None
		self._multimetrictable = None
		self._dup_state = None
		self._dup_weight = None
		self._weight = None
		self.___count = None

	@property
	def monitorname(self) :
		r"""Name for the monitor. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		CLI Users:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my monitor" or 'my monitor').<br/>Minimum length =  1.
		"""
		try :
			return self._monitorname
		except Exception as e:
			raise e

	@monitorname.setter
	def monitorname(self, monitorname) :
		r"""Name for the monitor. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		CLI Users:  If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my monitor" or 'my monitor').<br/>Minimum length =  1
		"""
		try :
			self._monitorname = monitorname
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, SIP-TCP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, SMPP, CITRIX-XNC-ECV, CITRIX-XDM, CITRIX-STA-SERVICE, CITRIX-STA-SERVICE-NHOP, MQTT, HTTP2.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of monitor that you want to create.<br/>Possible values = PING, TCP, HTTP, TCP-ECV, HTTP-ECV, UDP-ECV, DNS, FTP, LDNS-PING, LDNS-TCP, LDNS-DNS, RADIUS, USER, HTTP-INLINE, SIP-UDP, SIP-TCP, LOAD, FTP-EXTENDED, SMTP, SNMP, NNTP, MYSQL, MYSQL-ECV, MSSQL-ECV, ORACLE-ECV, LDAP, POP3, CITRIX-XML-SERVICE, CITRIX-WEB-INTERFACE, DNS-TCP, RTSP, ARP, CITRIX-AG, CITRIX-AAC-LOGINPAGE, CITRIX-AAC-LAS, CITRIX-XD-DDC, ND6, CITRIX-WI-EXTENDED, DIAMETER, RADIUS_ACCOUNTING, STOREFRONT, APPC, SMPP, CITRIX-XNC-ECV, CITRIX-XDM, CITRIX-STA-SERVICE, CITRIX-STA-SERVICE-NHOP, MQTT, HTTP2
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE) indicates that the service is down. A service monitored by an inline monitor is considered DOWN if the response code is not one of the codes that have been specified for the Response Code parameter. 
		Available settings function as follows: 
		* NONE - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.
		* LOG - Log the event in NSLOG or SYSLOG. 
		* DOWN - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.<br/>Default value: DOWN<br/>Possible values = NONE, LOG, DOWN.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		r"""Action to perform when the response to an inline monitor (a monitor of type HTTP-INLINE) indicates that the service is down. A service monitored by an inline monitor is considered DOWN if the response code is not one of the codes that have been specified for the Response Code parameter. 
		Available settings function as follows: 
		* NONE - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.
		* LOG - Log the event in NSLOG or SYSLOG. 
		* DOWN - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as DOWN. Also, log the event in NSLOG or SYSLOG.<br/>Default value: DOWN<br/>Possible values = NONE, LOG, DOWN
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def respcode(self) :
		r"""Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform the action indicated by the Action parameter.
		"""
		try :
			return self._respcode
		except Exception as e:
			raise e

	@respcode.setter
	def respcode(self, respcode) :
		r"""Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. HTTP monitors and RADIUS monitors mark the service as DOWN, while HTTP-INLINE monitors perform the action indicated by the Action parameter.
		"""
		try :
			self._respcode = respcode
		except Exception as e:
			raise e

	@property
	def httprequest(self) :
		r"""HTTP request to send to the server (for example, "HEAD /file.html").
		"""
		try :
			return self._httprequest
		except Exception as e:
			raise e

	@httprequest.setter
	def httprequest(self, httprequest) :
		r"""HTTP request to send to the server (for example, "HEAD /file.html").
		"""
		try :
			self._httprequest = httprequest
		except Exception as e:
			raise e

	@property
	def rtsprequest(self) :
		r"""RTSP request to send to the server (for example, "OPTIONS *").
		"""
		try :
			return self._rtsprequest
		except Exception as e:
			raise e

	@rtsprequest.setter
	def rtsprequest(self, rtsprequest) :
		r"""RTSP request to send to the server (for example, "OPTIONS *").
		"""
		try :
			self._rtsprequest = rtsprequest
		except Exception as e:
			raise e

	@property
	def customheaders(self) :
		r"""Custom header string to include in the monitoring probes.
		"""
		try :
			return self._customheaders
		except Exception as e:
			raise e

	@customheaders.setter
	def customheaders(self, customheaders) :
		r"""Custom header string to include in the monitoring probes.
		"""
		try :
			self._customheaders = customheaders
		except Exception as e:
			raise e

	@property
	def maxforwards(self) :
		r"""Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.<br/>Default value: 1<br/>Maximum length =  255.
		"""
		try :
			return self._maxforwards
		except Exception as e:
			raise e

	@maxforwards.setter
	def maxforwards(self, maxforwards) :
		r"""Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type SIP-UDP.<br/>Default value: 1<br/>Maximum length =  255
		"""
		try :
			self._maxforwards = maxforwards
		except Exception as e:
			raise e

	@property
	def sipmethod(self) :
		r"""SIP method to use for the query. Applicable only to monitors of type SIP-UDP.<br/>Possible values = OPTIONS, INVITE, REGISTER.
		"""
		try :
			return self._sipmethod
		except Exception as e:
			raise e

	@sipmethod.setter
	def sipmethod(self, sipmethod) :
		r"""SIP method to use for the query. Applicable only to monitors of type SIP-UDP.<br/>Possible values = OPTIONS, INVITE, REGISTER
		"""
		try :
			self._sipmethod = sipmethod
		except Exception as e:
			raise e

	@property
	def sipuri(self) :
		r"""SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP.<br/>Minimum length =  1.
		"""
		try :
			return self._sipuri
		except Exception as e:
			raise e

	@sipuri.setter
	def sipuri(self, sipuri) :
		r"""SIP URI string to send to the service (for example, sip:sip.test). Applicable only to monitors of type SIP-UDP.<br/>Minimum length =  1
		"""
		try :
			self._sipuri = sipuri
		except Exception as e:
			raise e

	@property
	def sipreguri(self) :
		r"""SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.<br/>Minimum length =  1.
		"""
		try :
			return self._sipreguri
		except Exception as e:
			raise e

	@sipreguri.setter
	def sipreguri(self, sipreguri) :
		r"""SIP user to be registered. Applicable only if the monitor is of type SIP-UDP and the SIP Method parameter is set to REGISTER.<br/>Minimum length =  1
		"""
		try :
			self._sipreguri = sipreguri
		except Exception as e:
			raise e

	@property
	def send(self) :
		r"""String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			return self._send
		except Exception as e:
			raise e

	@send.setter
	def send(self, send) :
		r"""String to send to the service. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			self._send = send
		except Exception as e:
			raise e

	@property
	def recv(self) :
		r"""String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			return self._recv
		except Exception as e:
			raise e

	@recv.setter
	def recv(self, recv) :
		r"""String expected from the server for the service to be marked as UP. Applicable to TCP-ECV, HTTP-ECV, and UDP-ECV monitors.
		"""
		try :
			self._recv = recv
		except Exception as e:
			raise e

	@property
	def query(self) :
		r"""Domain name to resolve as part of monitoring the DNS service (for example, example.com).
		"""
		try :
			return self._query
		except Exception as e:
			raise e

	@query.setter
	def query(self, query) :
		r"""Domain name to resolve as part of monitoring the DNS service (for example, example.com).
		"""
		try :
			self._query = query
		except Exception as e:
			raise e

	@property
	def querytype(self) :
		r"""Type of DNS record for which to send monitoring queries. Set to Address for querying A records, AAAA for querying AAAA records, and Zone for querying the SOA record.<br/>Possible values = Address, Zone, AAAA.
		"""
		try :
			return self._querytype
		except Exception as e:
			raise e

	@querytype.setter
	def querytype(self, querytype) :
		r"""Type of DNS record for which to send monitoring queries. Set to Address for querying A records, AAAA for querying AAAA records, and Zone for querying the SOA record.<br/>Possible values = Address, Zone, AAAA
		"""
		try :
			self._querytype = querytype
		except Exception as e:
			raise e

	@property
	def scriptname(self) :
		r"""Path and name of the script to execute. The script must be available on the Citrix ADC, in the /nsconfig/monitors/ directory.<br/>Minimum length =  1.
		"""
		try :
			return self._scriptname
		except Exception as e:
			raise e

	@scriptname.setter
	def scriptname(self, scriptname) :
		r"""Path and name of the script to execute. The script must be available on the Citrix ADC, in the /nsconfig/monitors/ directory.<br/>Minimum length =  1
		"""
		try :
			self._scriptname = scriptname
		except Exception as e:
			raise e

	@property
	def scriptargs(self) :
		r"""String of arguments for the script. The string is copied verbatim into the request.
		"""
		try :
			return self._scriptargs
		except Exception as e:
			raise e

	@scriptargs.setter
	def scriptargs(self, scriptargs) :
		r"""String of arguments for the script. The string is copied verbatim into the request.
		"""
		try :
			self._scriptargs = scriptargs
		except Exception as e:
			raise e

	@property
	def dispatcherip(self) :
		r"""IP address of the dispatcher to which to send the probe.
		"""
		try :
			return self._dispatcherip
		except Exception as e:
			raise e

	@dispatcherip.setter
	def dispatcherip(self, dispatcherip) :
		r"""IP address of the dispatcher to which to send the probe.
		"""
		try :
			self._dispatcherip = dispatcherip
		except Exception as e:
			raise e

	@property
	def dispatcherport(self) :
		r"""Port number on which the dispatcher listens for the monitoring probe.
		"""
		try :
			return self._dispatcherport
		except Exception as e:
			raise e

	@dispatcherport.setter
	def dispatcherport(self, dispatcherport) :
		r"""Port number on which the dispatcher listens for the monitoring probe.
		"""
		try :
			self._dispatcherport = dispatcherport
		except Exception as e:
			raise e

	@property
	def username(self) :
		r"""User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM server.<br/>Minimum length =  1.
		"""
		try :
			return self._username
		except Exception as e:
			raise e

	@username.setter
	def username(self, username) :
		r"""User name with which to probe the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC or CITRIX-XDM server.<br/>Minimum length =  1
		"""
		try :
			self._username = username
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server. Used in conjunction with the user name specified for the User Name parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Password that is required for logging on to the RADIUS, NNTP, FTP, FTP-EXTENDED, MYSQL, MSSQL, POP3, CITRIX-AG, CITRIX-XD-DDC, CITRIX-WI-EXTENDED, CITRIX-XNC-ECV or CITRIX-XDM server. Used in conjunction with the user name specified for the User Name parameter.<br/>Minimum length =  1
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def secondarypassword(self) :
		r"""Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.
		"""
		try :
			return self._secondarypassword
		except Exception as e:
			raise e

	@secondarypassword.setter
	def secondarypassword(self, secondarypassword) :
		r"""Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to CITRIX-AG monitors.
		"""
		try :
			self._secondarypassword = secondarypassword
		except Exception as e:
			raise e

	@property
	def logonpointname(self) :
		r"""Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.
		"""
		try :
			return self._logonpointname
		except Exception as e:
			raise e

	@logonpointname.setter
	def logonpointname(self, logonpointname) :
		r"""Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to CITRIX-AAC-LAS and CITRIX-AAC-LOGINPAGE monitors.
		"""
		try :
			self._logonpointname = logonpointname
		except Exception as e:
			raise e

	@property
	def lasversion(self) :
		r"""Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.
		"""
		try :
			return self._lasversion
		except Exception as e:
			raise e

	@lasversion.setter
	def lasversion(self, lasversion) :
		r"""Version number of the Citrix Advanced Access Control Logon Agent. Required by the CITRIX-AAC-LAS monitor.
		"""
		try :
			self._lasversion = lasversion
		except Exception as e:
			raise e

	@property
	def radkey(self) :
		r"""Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radkey
		except Exception as e:
			raise e

	@radkey.setter
	def radkey(self, radkey) :
		r"""Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radkey = radkey
		except Exception as e:
			raise e

	@property
	def radnasid(self) :
		r"""NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.<br/>Minimum length =  1.
		"""
		try :
			return self._radnasid
		except Exception as e:
			raise e

	@radnasid.setter
	def radnasid(self, radnasid) :
		r"""NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type RADIUS.<br/>Minimum length =  1
		"""
		try :
			self._radnasid = radnasid
		except Exception as e:
			raise e

	@property
	def radnasip(self) :
		r"""Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
		"""
		try :
			return self._radnasip
		except Exception as e:
			raise e

	@radnasip.setter
	def radnasip(self, radnasip) :
		r"""Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type RADIUS and RADIUS_ACCOUNTING.
		"""
		try :
			self._radnasip = radnasip
		except Exception as e:
			raise e

	@property
	def radaccounttype(self) :
		r"""Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Default value: 1<br/>Maximum length =  15.
		"""
		try :
			return self._radaccounttype
		except Exception as e:
			raise e

	@radaccounttype.setter
	def radaccounttype(self, radaccounttype) :
		r"""Account Type to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Default value: 1<br/>Maximum length =  15
		"""
		try :
			self._radaccounttype = radaccounttype
		except Exception as e:
			raise e

	@property
	def radframedip(self) :
		r"""Source ip with which the packet will go out . Applicable to monitors of type RADIUS_ACCOUNTING.
		"""
		try :
			return self._radframedip
		except Exception as e:
			raise e

	@radframedip.setter
	def radframedip(self, radframedip) :
		r"""Source ip with which the packet will go out . Applicable to monitors of type RADIUS_ACCOUNTING.
		"""
		try :
			self._radframedip = radframedip
		except Exception as e:
			raise e

	@property
	def radapn(self) :
		r"""Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radapn
		except Exception as e:
			raise e

	@radapn.setter
	def radapn(self, radapn) :
		r"""Called Station Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radapn = radapn
		except Exception as e:
			raise e

	@property
	def radmsisdn(self) :
		r"""Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radmsisdn
		except Exception as e:
			raise e

	@radmsisdn.setter
	def radmsisdn(self, radmsisdn) :
		r"""Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radmsisdn = radmsisdn
		except Exception as e:
			raise e

	@property
	def radaccountsession(self) :
		r"""Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1.
		"""
		try :
			return self._radaccountsession
		except Exception as e:
			raise e

	@radaccountsession.setter
	def radaccountsession(self, radaccountsession) :
		r"""Account Session ID to be used in Account Request Packet. Applicable to monitors of type RADIUS_ACCOUNTING.<br/>Minimum length =  1
		"""
		try :
			self._radaccountsession = radaccountsession
		except Exception as e:
			raise e

	@property
	def lrtm(self) :
		r"""Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lrtm
		except Exception as e:
			raise e

	@lrtm.setter
	def lrtm(self, lrtm) :
		r"""Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._lrtm = lrtm
		except Exception as e:
			raise e

	@property
	def deviation(self) :
		r"""Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.<br/>Maximum length =  20939.
		"""
		try :
			return self._deviation
		except Exception as e:
			raise e

	@deviation.setter
	def deviation(self, deviation) :
		r"""Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.<br/>Maximum length =  20939
		"""
		try :
			self._deviation = deviation
		except Exception as e:
			raise e

	@property
	def units1(self) :
		r"""Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units1
		except Exception as e:
			raise e

	@units1.setter
	def units1(self, units1) :
		r"""Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units1 = units1
		except Exception as e:
			raise e

	@property
	def interval(self) :
		r"""Time interval between two successive probes. Must be greater than the value of Response Time-out.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  20940.
		"""
		try :
			return self._interval
		except Exception as e:
			raise e

	@interval.setter
	def interval(self, interval) :
		r"""Time interval between two successive probes. Must be greater than the value of Response Time-out.<br/>Default value: 5<br/>Minimum length =  1<br/>Maximum length =  20940
		"""
		try :
			self._interval = interval
		except Exception as e:
			raise e

	@property
	def units3(self) :
		r"""monitor interval units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units3
		except Exception as e:
			raise e

	@units3.setter
	def units3(self, units3) :
		r"""monitor interval units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units3 = units3
		except Exception as e:
			raise e

	@property
	def resptimeout(self) :
		r"""Amount of time for which the appliance must wait before it marks a probe as FAILED.  Must be less than the value specified for the Interval parameter.
		Note: For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply. For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  20939.
		"""
		try :
			return self._resptimeout
		except Exception as e:
			raise e

	@resptimeout.setter
	def resptimeout(self, resptimeout) :
		r"""Amount of time for which the appliance must wait before it marks a probe as FAILED.  Must be less than the value specified for the Interval parameter.
		Note: For UDP-ECV monitors for which a receive string is not configured, response timeout does not apply. For UDP-ECV monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  20939
		"""
		try :
			self._resptimeout = resptimeout
		except Exception as e:
			raise e

	@property
	def units4(self) :
		r"""monitor response timeout units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units4
		except Exception as e:
			raise e

	@units4.setter
	def units4(self, units4) :
		r"""monitor response timeout units.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units4 = units4
		except Exception as e:
			raise e

	@property
	def resptimeoutthresh(self) :
		r"""Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.<br/>Maximum length =  100.
		"""
		try :
			return self._resptimeoutthresh
		except Exception as e:
			raise e

	@resptimeoutthresh.setter
	def resptimeoutthresh(self, resptimeoutthresh) :
		r"""Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.<br/>Maximum length =  100
		"""
		try :
			self._resptimeoutthresh = resptimeoutthresh
		except Exception as e:
			raise e

	@property
	def retries(self) :
		r"""Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._retries
		except Exception as e:
			raise e

	@retries.setter
	def retries(self, retries) :
		r"""Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.<br/>Default value: 3<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._retries = retries
		except Exception as e:
			raise e

	@property
	def failureretries(self) :
		r"""Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.<br/>Maximum length =  32.
		"""
		try :
			return self._failureretries
		except Exception as e:
			raise e

	@failureretries.setter
	def failureretries(self, failureretries) :
		r"""Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.<br/>Maximum length =  32
		"""
		try :
			self._failureretries = failureretries
		except Exception as e:
			raise e

	@property
	def alertretries(self) :
		r"""Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.<br/>Maximum length =  32.
		"""
		try :
			return self._alertretries
		except Exception as e:
			raise e

	@alertretries.setter
	def alertretries(self, alertretries) :
		r"""Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.<br/>Maximum length =  32
		"""
		try :
			self._alertretries = alertretries
		except Exception as e:
			raise e

	@property
	def successretries(self) :
		r"""Number of consecutive successful probes required to transition a service's state from DOWN to UP.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._successretries
		except Exception as e:
			raise e

	@successretries.setter
	def successretries(self, successretries) :
		r"""Number of consecutive successful probes required to transition a service's state from DOWN to UP.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._successretries = successretries
		except Exception as e:
			raise e

	@property
	def downtime(self) :
		r"""Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  20939.
		"""
		try :
			return self._downtime
		except Exception as e:
			raise e

	@downtime.setter
	def downtime(self, downtime) :
		r"""Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  20939
		"""
		try :
			self._downtime = downtime
		except Exception as e:
			raise e

	@property
	def units2(self) :
		r"""Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN.
		"""
		try :
			return self._units2
		except Exception as e:
			raise e

	@units2.setter
	def units2(self, units2) :
		r"""Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.<br/>Default value: SEC<br/>Possible values = SEC, MSEC, MIN
		"""
		try :
			self._units2 = units2
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		r"""IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type USER, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type PING.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		r"""TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type USER, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type PING.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""State of the monitor. The DISABLED setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to ENABLED. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""State of the monitor. The DISABLED setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to ENABLED. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def reverse(self) :
		r"""Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._reverse
		except Exception as e:
			raise e

	@reverse.setter
	def reverse(self, reverse) :
		r"""Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._reverse = reverse
		except Exception as e:
			raise e

	@property
	def transparent(self) :
		r"""The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._transparent
		except Exception as e:
			raise e

	@transparent.setter
	def transparent(self, transparent) :
		r"""The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._transparent = transparent
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		r"""Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@iptunnel.setter
	def iptunnel(self, iptunnel) :
		r"""Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._iptunnel = iptunnel
		except Exception as e:
			raise e

	@property
	def tos(self) :
		r"""Probe the service by encoding the destination IP address in the IP TOS (6) bits.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tos
		except Exception as e:
			raise e

	@tos.setter
	def tos(self, tos) :
		r"""Probe the service by encoding the destination IP address in the IP TOS (6) bits.<br/>Possible values = YES, NO
		"""
		try :
			self._tos = tos
		except Exception as e:
			raise e

	@property
	def tosid(self) :
		r"""The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._tosid
		except Exception as e:
			raise e

	@tosid.setter
	def tosid(self, tosid) :
		r"""The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._tosid = tosid
		except Exception as e:
			raise e

	@property
	def secure(self) :
		r"""Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._secure
		except Exception as e:
			raise e

	@secure.setter
	def secure(self, secure) :
		r"""Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a CITRIX-AG monitor, because a CITRIX-AG monitor uses a secure connection by default.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._secure = secure
		except Exception as e:
			raise e

	@property
	def validatecred(self) :
		r"""Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._validatecred
		except Exception as e:
			raise e

	@validatecred.setter
	def validatecred(self, validatecred) :
		r"""Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type CITRIX-XD-DDC.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._validatecred = validatecred
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED monitors for logging on to the DDC servers and Web Interface servers, respectively.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		r"""Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by CITRIX-XD-DDC and CITRIX-WI-EXTENDED monitors for logging on to the DDC servers and Web Interface servers, respectively.
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to DNS monitors.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def group(self) :
		r"""Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		r"""Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.<br/>Minimum length =  1
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

	@property
	def filename(self) :
		r"""Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to FTP-EXTENDED monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		r"""Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to FTP-EXTENDED monitors.<br/>Minimum length =  1
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def basedn(self) :
		r"""The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for LDAP service monitoring.<br/>Minimum length =  1.
		"""
		try :
			return self._basedn
		except Exception as e:
			raise e

	@basedn.setter
	def basedn(self, basedn) :
		r"""The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for LDAP service monitoring.<br/>Minimum length =  1
		"""
		try :
			self._basedn = basedn
		except Exception as e:
			raise e

	@property
	def binddn(self) :
		r"""The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._binddn
		except Exception as e:
			raise e

	@binddn.setter
	def binddn(self, binddn) :
		r"""The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to LDAP monitors.<br/>Minimum length =  1
		"""
		try :
			self._binddn = binddn
		except Exception as e:
			raise e

	@property
	def filter(self) :
		r"""Filter criteria for the LDAP query. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._filter
		except Exception as e:
			raise e

	@filter.setter
	def filter(self, filter) :
		r"""Filter criteria for the LDAP query. Optional.<br/>Minimum length =  1
		"""
		try :
			self._filter = filter
		except Exception as e:
			raise e

	@property
	def attribute(self) :
		r"""Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._attribute
		except Exception as e:
			raise e

	@attribute.setter
	def attribute(self, attribute) :
		r"""Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.<br/>Minimum length =  1
		"""
		try :
			self._attribute = attribute
		except Exception as e:
			raise e

	@property
	def database(self) :
		r"""Name of the database to connect to during authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._database
		except Exception as e:
			raise e

	@database.setter
	def database(self, database) :
		r"""Name of the database to connect to during authentication.<br/>Minimum length =  1
		"""
		try :
			self._database = database
		except Exception as e:
			raise e

	@property
	def oraclesid(self) :
		r"""Name of the service identifier that is used to connect to the Oracle database during authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._oraclesid
		except Exception as e:
			raise e

	@oraclesid.setter
	def oraclesid(self, oraclesid) :
		r"""Name of the service identifier that is used to connect to the Oracle database during authentication.<br/>Minimum length =  1
		"""
		try :
			self._oraclesid = oraclesid
		except Exception as e:
			raise e

	@property
	def sqlquery(self) :
		r"""SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.<br/>Minimum length =  1.
		"""
		try :
			return self._sqlquery
		except Exception as e:
			raise e

	@sqlquery.setter
	def sqlquery(self, sqlquery) :
		r"""SQL query for a MYSQL-ECV or MSSQL-ECV monitor. Sent to the database server after the server authenticates the connection.<br/>Minimum length =  1
		"""
		try :
			self._sqlquery = sqlquery
		except Exception as e:
			raise e

	@property
	def evalrule(self) :
		r"""Expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds. 
		For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").
		"""
		try :
			return self._evalrule
		except Exception as e:
			raise e

	@evalrule.setter
	def evalrule(self, evalrule) :
		r"""Expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds. 
		For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule MYSQL.RES.ROW(10) .TEXT_ELEM(2).EQ("MySQL").
		"""
		try :
			self._evalrule = evalrule
		except Exception as e:
			raise e

	@property
	def mssqlprotocolversion(self) :
		r"""Version of MSSQL server that is to be monitored.<br/>Default value: 70<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014.
		"""
		try :
			return self._mssqlprotocolversion
		except Exception as e:
			raise e

	@mssqlprotocolversion.setter
	def mssqlprotocolversion(self, mssqlprotocolversion) :
		r"""Version of MSSQL server that is to be monitored.<br/>Default value: 70<br/>Possible values = 70, 2000, 2000SP1, 2005, 2008, 2008R2, 2012, 2014
		"""
		try :
			self._mssqlprotocolversion = mssqlprotocolversion
		except Exception as e:
			raise e

	@property
	def Snmpoid(self) :
		r"""SNMP OID for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._Snmpoid
		except Exception as e:
			raise e

	@Snmpoid.setter
	def Snmpoid(self, Snmpoid) :
		r"""SNMP OID for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._Snmpoid = Snmpoid
		except Exception as e:
			raise e

	@property
	def snmpcommunity(self) :
		r"""Community name for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._snmpcommunity
		except Exception as e:
			raise e

	@snmpcommunity.setter
	def snmpcommunity(self, snmpcommunity) :
		r"""Community name for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._snmpcommunity = snmpcommunity
		except Exception as e:
			raise e

	@property
	def snmpthreshold(self) :
		r"""Threshold for SNMP monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._snmpthreshold
		except Exception as e:
			raise e

	@snmpthreshold.setter
	def snmpthreshold(self, snmpthreshold) :
		r"""Threshold for SNMP monitors.<br/>Minimum length =  1
		"""
		try :
			self._snmpthreshold = snmpthreshold
		except Exception as e:
			raise e

	@property
	def snmpversion(self) :
		r"""SNMP version to be used for SNMP monitors.<br/>Possible values = V1, V2.
		"""
		try :
			return self._snmpversion
		except Exception as e:
			raise e

	@snmpversion.setter
	def snmpversion(self, snmpversion) :
		r"""SNMP version to be used for SNMP monitors.<br/>Possible values = V1, V2
		"""
		try :
			self._snmpversion = snmpversion
		except Exception as e:
			raise e

	@property
	def metrictable(self) :
		r"""Metric table to which to bind metrics.<br/>Minimum length =  1<br/>Maximum length =  99.
		"""
		try :
			return self._metrictable
		except Exception as e:
			raise e

	@metrictable.setter
	def metrictable(self, metrictable) :
		r"""Metric table to which to bind metrics.<br/>Minimum length =  1<br/>Maximum length =  99
		"""
		try :
			self._metrictable = metrictable
		except Exception as e:
			raise e

	@property
	def application(self) :
		r"""Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.<br/>Minimum length =  1.
		"""
		try :
			return self._application
		except Exception as e:
			raise e

	@application.setter
	def application(self, application) :
		r"""Name of the application used to determine the state of the service. Applicable to monitors of type CITRIX-XML-SERVICE.<br/>Minimum length =  1
		"""
		try :
			self._application = application
		except Exception as e:
			raise e

	@property
	def sitepath(self) :
		r"""URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path, terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._sitepath
		except Exception as e:
			raise e

	@sitepath.setter
	def sitepath(self, sitepath) :
		r"""URL of the logon page. For monitors of type CITRIX-WEB-INTERFACE, to monitor a dynamic page under the site path, terminate the site path with a slash (/). Applicable to CITRIX-WEB-INTERFACE, CITRIX-WI-EXTENDED and CITRIX-XDM monitors.<br/>Minimum length =  1
		"""
		try :
			self._sitepath = sitepath
		except Exception as e:
			raise e

	@property
	def storename(self) :
		r"""Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument defining storefront service store name. Applicable to STOREFRONT monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._storename
		except Exception as e:
			raise e

	@storename.setter
	def storename(self, storename) :
		r"""Store Name. For monitors of type STOREFRONT, STORENAME is an optional argument defining storefront service store name. Applicable to STOREFRONT monitors.<br/>Minimum length =  1
		"""
		try :
			self._storename = storename
		except Exception as e:
			raise e

	@property
	def storefrontacctservice(self) :
		r"""Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._storefrontacctservice
		except Exception as e:
			raise e

	@storefrontacctservice.setter
	def storefrontacctservice(self, storefrontacctservice) :
		r"""Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._storefrontacctservice = storefrontacctservice
		except Exception as e:
			raise e

	@property
	def hostname(self) :
		r"""Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT monitors.<br/>Minimum length =  1.
		"""
		try :
			return self._hostname
		except Exception as e:
			raise e

	@hostname.setter
	def hostname(self, hostname) :
		r"""Hostname in the FQDN format (Example: porche.cars.org). Applicable to STOREFRONT monitors.<br/>Minimum length =  1
		"""
		try :
			self._hostname = hostname
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		r"""Name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		r"""Name of the network profile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def originhost(self) :
		r"""Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._originhost
		except Exception as e:
			raise e

	@originhost.setter
	def originhost(self, originhost) :
		r"""Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._originhost = originhost
		except Exception as e:
			raise e

	@property
	def originrealm(self) :
		r"""Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._originrealm
		except Exception as e:
			raise e

	@originrealm.setter
	def originrealm(self, originrealm) :
		r"""Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._originrealm = originrealm
		except Exception as e:
			raise e

	@property
	def hostipaddress(self) :
		r"""Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.<br/>Minimum length =  1.
		"""
		try :
			return self._hostipaddress
		except Exception as e:
			raise e

	@hostipaddress.setter
	def hostipaddress(self, hostipaddress) :
		r"""Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.<br/>Minimum length =  1
		"""
		try :
			self._hostipaddress = hostipaddress
		except Exception as e:
			raise e

	@property
	def vendorid(self) :
		r"""Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			return self._vendorid
		except Exception as e:
			raise e

	@vendorid.setter
	def vendorid(self, vendorid) :
		r"""Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			self._vendorid = vendorid
		except Exception as e:
			raise e

	@property
	def productname(self) :
		r"""Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1.
		"""
		try :
			return self._productname
		except Exception as e:
			raise e

	@productname.setter
	def productname(self, productname) :
		r"""Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Minimum length =  1
		"""
		try :
			self._productname = productname
		except Exception as e:
			raise e

	@property
	def firmwarerevision(self) :
		r"""Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			return self._firmwarerevision
		except Exception as e:
			raise e

	@firmwarerevision.setter
	def firmwarerevision(self, firmwarerevision) :
		r"""Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.
		"""
		try :
			self._firmwarerevision = firmwarerevision
		except Exception as e:
			raise e

	@property
	def authapplicationid(self) :
		r"""List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._authapplicationid
		except Exception as e:
			raise e

	@authapplicationid.setter
	def authapplicationid(self, authapplicationid) :
		r"""List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._authapplicationid = authapplicationid
		except Exception as e:
			raise e

	@property
	def acctapplicationid(self) :
		r"""List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._acctapplicationid
		except Exception as e:
			raise e

	@acctapplicationid.setter
	def acctapplicationid(self, acctapplicationid) :
		r"""List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._acctapplicationid = acctapplicationid
		except Exception as e:
			raise e

	@property
	def inbandsecurityid(self) :
		r"""Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Possible values = NO_INBAND_SECURITY, TLS.
		"""
		try :
			return self._inbandsecurityid
		except Exception as e:
			raise e

	@inbandsecurityid.setter
	def inbandsecurityid(self, inbandsecurityid) :
		r"""Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.<br/>Possible values = NO_INBAND_SECURITY, TLS
		"""
		try :
			self._inbandsecurityid = inbandsecurityid
		except Exception as e:
			raise e

	@property
	def supportedvendorids(self) :
		r"""List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._supportedvendorids
		except Exception as e:
			raise e

	@supportedvendorids.setter
	def supportedvendorids(self, supportedvendorids) :
		r"""List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.<br/>Minimum length =  1<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._supportedvendorids = supportedvendorids
		except Exception as e:
			raise e

	@property
	def vendorspecificvendorid(self) :
		r"""Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.<br/>Minimum length =  1.
		"""
		try :
			return self._vendorspecificvendorid
		except Exception as e:
			raise e

	@vendorspecificvendorid.setter
	def vendorspecificvendorid(self, vendorspecificvendorid) :
		r"""Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.<br/>Minimum length =  1
		"""
		try :
			self._vendorspecificvendorid = vendorspecificvendorid
		except Exception as e:
			raise e

	@property
	def vendorspecificauthapplicationids(self) :
		r"""List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._vendorspecificauthapplicationids
		except Exception as e:
			raise e

	@vendorspecificauthapplicationids.setter
	def vendorspecificauthapplicationids(self, vendorspecificauthapplicationids) :
		r"""List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._vendorspecificauthapplicationids = vendorspecificauthapplicationids
		except Exception as e:
			raise e

	@property
	def vendorspecificacctapplicationids(self) :
		r"""List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF.
		"""
		try :
			return self._vendorspecificacctapplicationids
		except Exception as e:
			raise e

	@vendorspecificacctapplicationids.setter
	def vendorspecificacctapplicationids(self, vendorspecificacctapplicationids) :
		r"""List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.<br/>Maximum length =  0xFFFFFFFF
		"""
		try :
			self._vendorspecificacctapplicationids = vendorspecificacctapplicationids
		except Exception as e:
			raise e

	@property
	def kcdaccount(self) :
		r"""KCD Account used by MSSQL monitor.<br/>Minimum length =  1<br/>Maximum length =  32.
		"""
		try :
			return self._kcdaccount
		except Exception as e:
			raise e

	@kcdaccount.setter
	def kcdaccount(self, kcdaccount) :
		r"""KCD Account used by MSSQL monitor.<br/>Minimum length =  1<br/>Maximum length =  32
		"""
		try :
			self._kcdaccount = kcdaccount
		except Exception as e:
			raise e

	@property
	def storedb(self) :
		r"""Store the database list populated with the responses to monitor probes. Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._storedb
		except Exception as e:
			raise e

	@storedb.setter
	def storedb(self, storedb) :
		r"""Store the database list populated with the responses to monitor probes. Used in database specific load balancing if MSSQL-ECV/MYSQL-ECV  monitor is configured.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._storedb = storedb
		except Exception as e:
			raise e

	@property
	def storefrontcheckbackendservices(self) :
		r"""This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._storefrontcheckbackendservices
		except Exception as e:
			raise e

	@storefrontcheckbackendservices.setter
	def storefrontcheckbackendservices(self, storefrontcheckbackendservices) :
		r"""This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._storefrontcheckbackendservices = storefrontcheckbackendservices
		except Exception as e:
			raise e

	@property
	def trofscode(self) :
		r"""Code expected when the server is under maintenance.
		"""
		try :
			return self._trofscode
		except Exception as e:
			raise e

	@trofscode.setter
	def trofscode(self, trofscode) :
		r"""Code expected when the server is under maintenance.
		"""
		try :
			self._trofscode = trofscode
		except Exception as e:
			raise e

	@property
	def trofsstring(self) :
		r"""String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.
		"""
		try :
			return self._trofsstring
		except Exception as e:
			raise e

	@trofsstring.setter
	def trofsstring(self, trofsstring) :
		r"""String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.
		"""
		try :
			self._trofsstring = trofsstring
		except Exception as e:
			raise e

	@property
	def sslprofile(self) :
		r"""SSL Profile associated with the monitor.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._sslprofile
		except Exception as e:
			raise e

	@sslprofile.setter
	def sslprofile(self, sslprofile) :
		r"""SSL Profile associated with the monitor.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._sslprofile = sslprofile
		except Exception as e:
			raise e

	@property
	def mqttclientidentifier(self) :
		r"""Client id to be used in Connect command.
		"""
		try :
			return self._mqttclientidentifier
		except Exception as e:
			raise e

	@mqttclientidentifier.setter
	def mqttclientidentifier(self, mqttclientidentifier) :
		r"""Client id to be used in Connect command.
		"""
		try :
			self._mqttclientidentifier = mqttclientidentifier
		except Exception as e:
			raise e

	@property
	def mqttversion(self) :
		r"""Version of MQTT protocol used in connect message, default is version 3.1.1 [4].<br/>Default value: 4<br/>Minimum length =  3.
		"""
		try :
			return self._mqttversion
		except Exception as e:
			raise e

	@mqttversion.setter
	def mqttversion(self, mqttversion) :
		r"""Version of MQTT protocol used in connect message, default is version 3.1.1 [4].<br/>Default value: 4<br/>Minimum length =  3
		"""
		try :
			self._mqttversion = mqttversion
		except Exception as e:
			raise e

	@property
	def metric(self) :
		r"""Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37.
		"""
		try :
			return self._metric
		except Exception as e:
			raise e

	@metric.setter
	def metric(self, metric) :
		r"""Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37
		"""
		try :
			self._metric = metric
		except Exception as e:
			raise e

	@property
	def metricthreshold(self) :
		r"""Threshold to be used for that metric.
		"""
		try :
			return self._metricthreshold
		except Exception as e:
			raise e

	@metricthreshold.setter
	def metricthreshold(self, metricthreshold) :
		r"""Threshold to be used for that metric.
		"""
		try :
			self._metricthreshold = metricthreshold
		except Exception as e:
			raise e

	@property
	def metricweight(self) :
		r"""The weight for the specified service metric with respect to others.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._metricweight
		except Exception as e:
			raise e

	@metricweight.setter
	def metricweight(self, metricweight) :
		r"""The weight for the specified service metric with respect to others.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._metricweight = metricweight
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""The name of the service to which the monitor is bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@servicename.setter
	def servicename(self, servicename) :
		r"""The name of the service to which the monitor is bound.<br/>Minimum length =  1
		"""
		try :
			self._servicename = servicename
		except Exception as e:
			raise e

	@property
	def servicegroupname(self) :
		r"""The name of the service group to which the monitor is to be bound.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""The name of the service group to which the monitor is to be bound.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def lrtmconf(self) :
		r"""State of LRTM configuration on the monitor.
		"""
		try :
			return self._lrtmconf
		except Exception as e:
			raise e

	@property
	def lrtmconfstr(self) :
		r"""State of LRTM configuration on the monitor as STRING.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lrtmconfstr
		except Exception as e:
			raise e

	@property
	def dynamicresponsetimeout(self) :
		r"""Response timeout of the DRTM enabled monitor , calculated dynamically based on the history and current response time.
		"""
		try :
			return self._dynamicresponsetimeout
		except Exception as e:
			raise e

	@property
	def dynamicinterval(self) :
		r"""Interval between monitoring probes for DRTM enabled monitor , calculated dynamically based monitor response time.
		"""
		try :
			return self._dynamicinterval
		except Exception as e:
			raise e

	@property
	def multimetrictable(self) :
		r"""Metric table to which to bind metrics, to be used only for output purposes.
		"""
		try :
			return self._multimetrictable
		except Exception as e:
			raise e

	@property
	def dup_state(self) :
		r""".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dup_state
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		r""".<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r""".<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbmonitor_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbmonitor
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.monitorname is not None :
				return str(self.monitorname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = lbmonitor()
		addresource.monitorname = resource.monitorname
		addresource.type = resource.type
		addresource.action = resource.action
		addresource.respcode = resource.respcode
		addresource.httprequest = resource.httprequest
		addresource.rtsprequest = resource.rtsprequest
		addresource.customheaders = resource.customheaders
		addresource.maxforwards = resource.maxforwards
		addresource.sipmethod = resource.sipmethod
		addresource.sipuri = resource.sipuri
		addresource.sipreguri = resource.sipreguri
		addresource.send = resource.send
		addresource.recv = resource.recv
		addresource.query = resource.query
		addresource.querytype = resource.querytype
		addresource.scriptname = resource.scriptname
		addresource.scriptargs = resource.scriptargs
		addresource.dispatcherip = resource.dispatcherip
		addresource.dispatcherport = resource.dispatcherport
		addresource.username = resource.username
		addresource.password = resource.password
		addresource.secondarypassword = resource.secondarypassword
		addresource.logonpointname = resource.logonpointname
		addresource.lasversion = resource.lasversion
		addresource.radkey = resource.radkey
		addresource.radnasid = resource.radnasid
		addresource.radnasip = resource.radnasip
		addresource.radaccounttype = resource.radaccounttype
		addresource.radframedip = resource.radframedip
		addresource.radapn = resource.radapn
		addresource.radmsisdn = resource.radmsisdn
		addresource.radaccountsession = resource.radaccountsession
		addresource.lrtm = resource.lrtm
		addresource.deviation = resource.deviation
		addresource.units1 = resource.units1
		addresource.interval = resource.interval
		addresource.units3 = resource.units3
		addresource.resptimeout = resource.resptimeout
		addresource.units4 = resource.units4
		addresource.resptimeoutthresh = resource.resptimeoutthresh
		addresource.retries = resource.retries
		addresource.failureretries = resource.failureretries
		addresource.alertretries = resource.alertretries
		addresource.successretries = resource.successretries
		addresource.downtime = resource.downtime
		addresource.units2 = resource.units2
		addresource.destip = resource.destip
		addresource.destport = resource.destport
		addresource.state = resource.state
		addresource.reverse = resource.reverse
		addresource.transparent = resource.transparent
		addresource.iptunnel = resource.iptunnel
		addresource.tos = resource.tos
		addresource.tosid = resource.tosid
		addresource.secure = resource.secure
		addresource.validatecred = resource.validatecred
		addresource.domain = resource.domain
		addresource.ipaddress = resource.ipaddress
		addresource.group = resource.group
		addresource.filename = resource.filename
		addresource.basedn = resource.basedn
		addresource.binddn = resource.binddn
		addresource.filter = resource.filter
		addresource.attribute = resource.attribute
		addresource.database = resource.database
		addresource.oraclesid = resource.oraclesid
		addresource.sqlquery = resource.sqlquery
		addresource.evalrule = resource.evalrule
		addresource.mssqlprotocolversion = resource.mssqlprotocolversion
		addresource.Snmpoid = resource.Snmpoid
		addresource.snmpcommunity = resource.snmpcommunity
		addresource.snmpthreshold = resource.snmpthreshold
		addresource.snmpversion = resource.snmpversion
		addresource.metrictable = resource.metrictable
		addresource.application = resource.application
		addresource.sitepath = resource.sitepath
		addresource.storename = resource.storename
		addresource.storefrontacctservice = resource.storefrontacctservice
		addresource.hostname = resource.hostname
		addresource.netprofile = resource.netprofile
		addresource.originhost = resource.originhost
		addresource.originrealm = resource.originrealm
		addresource.hostipaddress = resource.hostipaddress
		addresource.vendorid = resource.vendorid
		addresource.productname = resource.productname
		addresource.firmwarerevision = resource.firmwarerevision
		addresource.authapplicationid = resource.authapplicationid
		addresource.acctapplicationid = resource.acctapplicationid
		addresource.inbandsecurityid = resource.inbandsecurityid
		addresource.supportedvendorids = resource.supportedvendorids
		addresource.vendorspecificvendorid = resource.vendorspecificvendorid
		addresource.vendorspecificauthapplicationids = resource.vendorspecificauthapplicationids
		addresource.vendorspecificacctapplicationids = resource.vendorspecificacctapplicationids
		addresource.kcdaccount = resource.kcdaccount
		addresource.storedb = resource.storedb
		addresource.storefrontcheckbackendservices = resource.storefrontcheckbackendservices
		addresource.trofscode = resource.trofscode
		addresource.trofsstring = resource.trofsstring
		addresource.sslprofile = resource.sslprofile
		addresource.mqttclientidentifier = resource.mqttclientidentifier
		addresource.mqttversion = resource.mqttversion
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add lbmonitor.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ lbmonitor() for _ in range(len(resource))]
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
		deleteresource = lbmonitor()
		deleteresource.monitorname = resource.monitorname
		deleteresource.type = resource.type
		deleteresource.respcode = resource.respcode
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete lbmonitor.
		"""
		try :
			if type(resource) is not list :
				deleteresource = lbmonitor()
				if type(resource) !=  type(deleteresource):
					deleteresource.monitorname = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ lbmonitor() for _ in range(len(resource))]
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
		updateresource = lbmonitor()
		updateresource.monitorname = resource.monitorname
		updateresource.type = resource.type
		updateresource.action = resource.action
		updateresource.respcode = resource.respcode
		updateresource.httprequest = resource.httprequest
		updateresource.rtsprequest = resource.rtsprequest
		updateresource.customheaders = resource.customheaders
		updateresource.maxforwards = resource.maxforwards
		updateresource.sipmethod = resource.sipmethod
		updateresource.sipreguri = resource.sipreguri
		updateresource.sipuri = resource.sipuri
		updateresource.send = resource.send
		updateresource.recv = resource.recv
		updateresource.query = resource.query
		updateresource.querytype = resource.querytype
		updateresource.username = resource.username
		updateresource.password = resource.password
		updateresource.secondarypassword = resource.secondarypassword
		updateresource.logonpointname = resource.logonpointname
		updateresource.lasversion = resource.lasversion
		updateresource.radkey = resource.radkey
		updateresource.radnasid = resource.radnasid
		updateresource.radnasip = resource.radnasip
		updateresource.radaccounttype = resource.radaccounttype
		updateresource.radframedip = resource.radframedip
		updateresource.radapn = resource.radapn
		updateresource.radmsisdn = resource.radmsisdn
		updateresource.radaccountsession = resource.radaccountsession
		updateresource.lrtm = resource.lrtm
		updateresource.deviation = resource.deviation
		updateresource.units1 = resource.units1
		updateresource.scriptname = resource.scriptname
		updateresource.scriptargs = resource.scriptargs
		updateresource.validatecred = resource.validatecred
		updateresource.domain = resource.domain
		updateresource.dispatcherip = resource.dispatcherip
		updateresource.dispatcherport = resource.dispatcherport
		updateresource.interval = resource.interval
		updateresource.units3 = resource.units3
		updateresource.resptimeout = resource.resptimeout
		updateresource.units4 = resource.units4
		updateresource.resptimeoutthresh = resource.resptimeoutthresh
		updateresource.retries = resource.retries
		updateresource.failureretries = resource.failureretries
		updateresource.alertretries = resource.alertretries
		updateresource.successretries = resource.successretries
		updateresource.downtime = resource.downtime
		updateresource.units2 = resource.units2
		updateresource.destip = resource.destip
		updateresource.destport = resource.destport
		updateresource.state = resource.state
		updateresource.reverse = resource.reverse
		updateresource.transparent = resource.transparent
		updateresource.iptunnel = resource.iptunnel
		updateresource.tos = resource.tos
		updateresource.tosid = resource.tosid
		updateresource.secure = resource.secure
		updateresource.ipaddress = resource.ipaddress
		updateresource.group = resource.group
		updateresource.filename = resource.filename
		updateresource.basedn = resource.basedn
		updateresource.binddn = resource.binddn
		updateresource.filter = resource.filter
		updateresource.attribute = resource.attribute
		updateresource.database = resource.database
		updateresource.oraclesid = resource.oraclesid
		updateresource.sqlquery = resource.sqlquery
		updateresource.evalrule = resource.evalrule
		updateresource.Snmpoid = resource.Snmpoid
		updateresource.snmpcommunity = resource.snmpcommunity
		updateresource.snmpthreshold = resource.snmpthreshold
		updateresource.snmpversion = resource.snmpversion
		updateresource.metrictable = resource.metrictable
		updateresource.metric = resource.metric
		updateresource.metricthreshold = resource.metricthreshold
		updateresource.metricweight = resource.metricweight
		updateresource.application = resource.application
		updateresource.sitepath = resource.sitepath
		updateresource.storename = resource.storename
		updateresource.storefrontacctservice = resource.storefrontacctservice
		updateresource.storefrontcheckbackendservices = resource.storefrontcheckbackendservices
		updateresource.hostname = resource.hostname
		updateresource.netprofile = resource.netprofile
		updateresource.mssqlprotocolversion = resource.mssqlprotocolversion
		updateresource.originhost = resource.originhost
		updateresource.originrealm = resource.originrealm
		updateresource.hostipaddress = resource.hostipaddress
		updateresource.vendorid = resource.vendorid
		updateresource.productname = resource.productname
		updateresource.firmwarerevision = resource.firmwarerevision
		updateresource.authapplicationid = resource.authapplicationid
		updateresource.acctapplicationid = resource.acctapplicationid
		updateresource.inbandsecurityid = resource.inbandsecurityid
		updateresource.supportedvendorids = resource.supportedvendorids
		updateresource.vendorspecificvendorid = resource.vendorspecificvendorid
		updateresource.vendorspecificauthapplicationids = resource.vendorspecificauthapplicationids
		updateresource.vendorspecificacctapplicationids = resource.vendorspecificacctapplicationids
		updateresource.kcdaccount = resource.kcdaccount
		updateresource.storedb = resource.storedb
		updateresource.trofscode = resource.trofscode
		updateresource.trofsstring = resource.trofsstring
		updateresource.sslprofile = resource.sslprofile
		updateresource.mqttclientidentifier = resource.mqttclientidentifier
		updateresource.mqttversion = resource.mqttversion
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lbmonitor.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ lbmonitor() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lbmonitor resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbmonitor()
				unsetresource.monitorname = resource.monitorname
				unsetresource.type = resource.type
				unsetresource.ipaddress = resource.ipaddress
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) == cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].monitorname = resource[i].monitorname
							unsetresources[i].type = resource[i].type
							unsetresources[i].ipaddress = resource[i].ipaddress
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable lbmonitor.
		"""
		try :
			if type(resource) is not list :
				enableresource = lbmonitor()
				if type(resource) !=  type(enableresource):
					enableresource.monitorname = resource
				else :
					enableresource.servicename = resource.servicename
					enableresource.servicegroupname = resource.servicegroupname
					enableresource.monitorname = resource.monitorname
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicename = resource[i].servicename
							enableresources[i].servicegroupname = resource[i].servicegroupname
							enableresources[i].monitorname = resource[i].monitorname
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable lbmonitor.
		"""
		try :
			if type(resource) is not list :
				disableresource = lbmonitor()
				if type(resource) !=  type(disableresource):
					disableresource.monitorname = resource
				else :
					disableresource.servicename = resource.servicename
					disableresource.servicegroupname = resource.servicegroupname
					disableresource.monitorname = resource.monitorname
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].monitorname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ lbmonitor() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicename = resource[i].servicename
							disableresources[i].servicegroupname = resource[i].servicegroupname
							disableresources[i].monitorname = resource[i].monitorname
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbmonitor resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbmonitor()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = lbmonitor()
					obj.monitorname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [lbmonitor() for _ in range(len(name))]
						obj = [lbmonitor() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = lbmonitor()
							obj[i].monitorname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the lbmonitor resources that are configured on netscaler.
	# This uses lbmonitor_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of lbmonitor resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the lbmonitor resources configured on NetScaler.
		"""
		try :
			obj = lbmonitor()
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
		r""" Use this API to count filtered the set of lbmonitor resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lbmonitor()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Secure:
		YES = "YES"
		NO = "NO"

	class Iptunnel:
		YES = "YES"
		NO = "NO"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Validatecred:
		YES = "YES"
		NO = "NO"

	class Tos:
		YES = "YES"
		NO = "NO"

	class Units3:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Inbandsecurityid:
		NO_INBAND_SECURITY = "NO_INBAND_SECURITY"
		TLS = "TLS"

	class Storedb:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Transparent:
		YES = "YES"
		NO = "NO"

	class Lrtmconfstr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Units1:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Dup_state:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Storefrontacctservice:
		YES = "YES"
		NO = "NO"

	class Storefrontcheckbackendservices:
		YES = "YES"
		NO = "NO"

	class Units2:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Reverse:
		YES = "YES"
		NO = "NO"

	class Sipmethod:
		OPTIONS = "OPTIONS"
		INVITE = "INVITE"
		REGISTER = "REGISTER"

	class Units4:
		SEC = "SEC"
		MSEC = "MSEC"
		MIN = "MIN"

	class Action:
		NONE = "NONE"
		LOG = "LOG"
		DOWN = "DOWN"

	class Mssqlprotocolversion:
		_70 = "70"
		_2000 = "2000"
		_2000SP1 = "2000SP1"
		_2005 = "2005"
		_2008 = "2008"
		_2008R2 = "2008R2"
		_2012 = "2012"
		_2014 = "2014"

	class Type:
		PING = "PING"
		TCP = "TCP"
		HTTP = "HTTP"
		TCP_ECV = "TCP-ECV"
		HTTP_ECV = "HTTP-ECV"
		UDP_ECV = "UDP-ECV"
		DNS = "DNS"
		FTP = "FTP"
		LDNS_PING = "LDNS-PING"
		LDNS_TCP = "LDNS-TCP"
		LDNS_DNS = "LDNS-DNS"
		RADIUS = "RADIUS"
		USER = "USER"
		HTTP_INLINE = "HTTP-INLINE"
		SIP_UDP = "SIP-UDP"
		SIP_TCP = "SIP-TCP"
		LOAD = "LOAD"
		FTP_EXTENDED = "FTP-EXTENDED"
		SMTP = "SMTP"
		SNMP = "SNMP"
		NNTP = "NNTP"
		MYSQL = "MYSQL"
		MYSQL_ECV = "MYSQL-ECV"
		MSSQL_ECV = "MSSQL-ECV"
		ORACLE_ECV = "ORACLE-ECV"
		LDAP = "LDAP"
		POP3 = "POP3"
		CITRIX_XML_SERVICE = "CITRIX-XML-SERVICE"
		CITRIX_WEB_INTERFACE = "CITRIX-WEB-INTERFACE"
		DNS_TCP = "DNS-TCP"
		RTSP = "RTSP"
		ARP = "ARP"
		CITRIX_AG = "CITRIX-AG"
		CITRIX_AAC_LOGINPAGE = "CITRIX-AAC-LOGINPAGE"
		CITRIX_AAC_LAS = "CITRIX-AAC-LAS"
		CITRIX_XD_DDC = "CITRIX-XD-DDC"
		ND6 = "ND6"
		CITRIX_WI_EXTENDED = "CITRIX-WI-EXTENDED"
		DIAMETER = "DIAMETER"
		RADIUS_ACCOUNTING = "RADIUS_ACCOUNTING"
		STOREFRONT = "STOREFRONT"
		APPC = "APPC"
		SMPP = "SMPP"
		CITRIX_XNC_ECV = "CITRIX-XNC-ECV"
		CITRIX_XDM = "CITRIX-XDM"
		CITRIX_STA_SERVICE = "CITRIX-STA-SERVICE"
		CITRIX_STA_SERVICE_NHOP = "CITRIX-STA-SERVICE-NHOP"
		MQTT = "MQTT"
		HTTP2 = "HTTP2"

	class Snmpversion:
		V1 = "V1"
		V2 = "V2"

	class Lrtm:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Querytype:
		Address = "Address"
		Zone = "Zone"
		AAAA = "AAAA"

class lbmonitor_response(base_response) :
	def __init__(self, length=1) :
		self.lbmonitor = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbmonitor = [lbmonitor() for _ in range(length)]

