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

class servicegroup(base_resource) :
	""" Configuration for service group resource. """
	def __init__(self) :
		self._servicegroupname = None
		self._servicetype = None
		self._cachetype = None
		self._td = None
		self._maxclient = None
		self._maxreq = None
		self._cacheable = None
		self._cip = None
		self._cipheader = None
		self._usip = None
		self._pathmonitor = None
		self._pathmonitorindv = None
		self._useproxyport = None
		self._healthmonitor = None
		self._sc = None
		self._sp = None
		self._rtspsessionidremap = None
		self._clttimeout = None
		self._svrtimeout = None
		self._cka = None
		self._tcpb = None
		self._cmp = None
		self._maxbandwidth = None
		self._monthreshold = None
		self._state = None
		self._downstateflush = None
		self._tcpprofilename = None
		self._httpprofilename = None
		self._comment = None
		self._appflowlog = None
		self._netprofile = None
		self._autoscale = None
		self._memberport = None
		self._autodisablegraceful = None
		self._autodisabledelay = None
		self._monconnectionclose = None
		self._servername = None
		self._port = None
		self._weight = None
		self._customserverid = None
		self._serverid = None
		self._hashid = None
		self._nameserver = None
		self._dbsttl = None
		self._monitor_name_svc = None
		self._dup_weight = None
		self._delay = None
		self._graceful = None
		self._includemembers = None
		self._newname = None
		self._numofconnections = None
		self._serviceconftype = None
		self._value = None
		self._svrstate = None
		self._ip = None
		self._monstatcode = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._statechangetimemsec = None
		self._stateupdatereason = None
		self._clmonowner = None
		self._clmonview = None
		self._groupcount = None
		self._serviceipstr = None
		self._servicegroupeffectivestate = None
		self._nodefaultbindings = None
		self._svcitmactsvcs = None
		self._svcitmboundsvcs = None
		self._monuserstatusmesg = None
		self.___count = None

	@property
	def servicegroupname(self) :
		r"""Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the name is created.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the service group. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the name is created.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol used to exchange data with the service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, MONGO, MONGO_TLS, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, USER_TCP, USER_SSL_TCP, QUIC, IPFIX, LOGSTREAM, LOGSTREAM_SSL, MQTT, MQTT_TLS, QUIC_BRIDGE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol used to exchange data with the service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, MONGO, MONGO_TLS, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX, SSL_FIX, USER_TCP, USER_SSL_TCP, QUIC, IPFIX, LOGSTREAM, LOGSTREAM_SSL, MQTT, MQTT_TLS, QUIC_BRIDGE
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def cachetype(self) :
		r"""Cache type supported by the cache server.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD.
		"""
		try :
			return self._cachetype
		except Exception as e:
			raise e

	@cachetype.setter
	def cachetype(self, cachetype) :
		r"""Cache type supported by the cache server.<br/>Possible values = TRANSPARENT, REVERSE, FORWARD
		"""
		try :
			self._cachetype = cachetype
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		r"""Maximum number of simultaneous open connections for the service group.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	@maxclient.setter
	def maxclient(self, maxclient) :
		r"""Maximum number of simultaneous open connections for the service group.<br/>Maximum length =  4294967294
		"""
		try :
			self._maxclient = maxclient
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""Maximum number of requests that can be sent on a persistent connection to the service group. 
		Note: Connection requests beyond this value are rejected.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""Maximum number of requests that can be sent on a persistent connection to the service group. 
		Note: Connection requests beyond this value are rejected.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		r"""Use the transparent cache redirection virtual server to forward the request to the cache server.
		Note: Do not set this parameter if you set the Cache Type.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@cacheable.setter
	def cacheable(self, cacheable) :
		r"""Use the transparent cache redirection virtual server to forward the request to the cache server.
		Note: Do not set this parameter if you set the Cache Type.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._cacheable = cacheable
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Insert the Client IP header in requests forwarded to the service.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""Insert the Client IP header in requests forwarded to the service.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def usip(self) :
		r"""Use client's IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@usip.setter
	def usip(self, usip) :
		r"""Use client's IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections.<br/>Possible values = YES, NO
		"""
		try :
			self._usip = usip
		except Exception as e:
			raise e

	@property
	def pathmonitor(self) :
		r"""Path monitoring for clustering.<br/>Possible values = YES, NO.
		"""
		try :
			return self._pathmonitor
		except Exception as e:
			raise e

	@pathmonitor.setter
	def pathmonitor(self, pathmonitor) :
		r"""Path monitoring for clustering.<br/>Possible values = YES, NO
		"""
		try :
			self._pathmonitor = pathmonitor
		except Exception as e:
			raise e

	@property
	def pathmonitorindv(self) :
		r"""Individual Path monitoring decisions.<br/>Possible values = YES, NO.
		"""
		try :
			return self._pathmonitorindv
		except Exception as e:
			raise e

	@pathmonitorindv.setter
	def pathmonitorindv(self, pathmonitorindv) :
		r"""Individual Path monitoring decisions.<br/>Possible values = YES, NO
		"""
		try :
			self._pathmonitorindv = pathmonitorindv
		except Exception as e:
			raise e

	@property
	def useproxyport(self) :
		r"""Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection. 
		Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.<br/>Possible values = YES, NO.
		"""
		try :
			return self._useproxyport
		except Exception as e:
			raise e

	@useproxyport.setter
	def useproxyport(self, useproxyport) :
		r"""Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection. 
		Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.<br/>Possible values = YES, NO
		"""
		try :
			self._useproxyport = useproxyport
		except Exception as e:
			raise e

	@property
	def healthmonitor(self) :
		r"""Monitor the health of this service.  Available settings function as follows:
		YES - Send probes to check the health of the service.
		NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._healthmonitor
		except Exception as e:
			raise e

	@healthmonitor.setter
	def healthmonitor(self, healthmonitor) :
		r"""Monitor the health of this service.  Available settings function as follows:
		YES - Send probes to check the health of the service.
		NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._healthmonitor = healthmonitor
		except Exception as e:
			raise e

	@property
	def sc(self) :
		r"""State of the SureConnect feature for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@sc.setter
	def sc(self, sc) :
		r"""State of the SureConnect feature for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sc = sc
		except Exception as e:
			raise e

	@property
	def sp(self) :
		r"""Enable surge protection for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	@sp.setter
	def sp(self, sp) :
		r"""Enable surge protection for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sp = sp
		except Exception as e:
			raise e

	@property
	def rtspsessionidremap(self) :
		r"""Enable RTSP session ID mapping for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._rtspsessionidremap
		except Exception as e:
			raise e

	@rtspsessionidremap.setter
	def rtspsessionidremap(self, rtspsessionidremap) :
		r"""Enable RTSP session ID mapping for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._rtspsessionidremap = rtspsessionidremap
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def svrtimeout(self) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._svrtimeout
		except Exception as e:
			raise e

	@svrtimeout.setter
	def svrtimeout(self, svrtimeout) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000
		"""
		try :
			self._svrtimeout = svrtimeout
		except Exception as e:
			raise e

	@property
	def cka(self) :
		r"""Enable client keep-alive for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cka
		except Exception as e:
			raise e

	@cka.setter
	def cka(self, cka) :
		r"""Enable client keep-alive for the service group.<br/>Possible values = YES, NO
		"""
		try :
			self._cka = cka
		except Exception as e:
			raise e

	@property
	def tcpb(self) :
		r"""Enable TCP buffering for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tcpb
		except Exception as e:
			raise e

	@tcpb.setter
	def tcpb(self, tcpb) :
		r"""Enable TCP buffering for the service group.<br/>Possible values = YES, NO
		"""
		try :
			self._tcpb = tcpb
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		r"""Enable compression for the specified service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@cmp.setter
	def cmp(self, cmp) :
		r"""Enable compression for the specified service.<br/>Possible values = YES, NO
		"""
		try :
			self._cmp = cmp
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		r"""Maximum bandwidth, in Kbps, allocated for all the services in the service group.<br/>Maximum length =  4294967287.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@maxbandwidth.setter
	def maxbandwidth(self, maxbandwidth) :
		r"""Maximum bandwidth, in Kbps, allocated for all the services in the service group.<br/>Maximum length =  4294967287
		"""
		try :
			self._maxbandwidth = maxbandwidth
		except Exception as e:
			raise e

	@property
	def monthreshold(self) :
		r"""Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.<br/>Maximum length =  65535.
		"""
		try :
			return self._monthreshold
		except Exception as e:
			raise e

	@monthreshold.setter
	def monthreshold(self, monthreshold) :
		r"""Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.<br/>Maximum length =  65535
		"""
		try :
			self._monthreshold = monthreshold
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		r"""Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		r"""Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		r"""Name of the TCP profile that contains TCP configuration settings for the service group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		r"""Name of the TCP profile that contains TCP configuration settings for the service group.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def httpprofilename(self) :
		r"""Name of the HTTP profile that contains HTTP configuration settings for the service group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._httpprofilename
		except Exception as e:
			raise e

	@httpprofilename.setter
	def httpprofilename(self, httpprofilename) :
		r"""Name of the HTTP profile that contains HTTP configuration settings for the service group.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._httpprofilename = httpprofilename
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any information about the service group.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any information about the service group.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging of AppFlow information for the specified service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable logging of AppFlow information for the specified service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		r"""Network profile for the service group.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		r"""Network profile for the service group.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def autoscale(self) :
		r"""Auto scale option for a servicegroup.<br/>Default value: DISABLED<br/>Possible values = DISABLED, DNS, POLICY, CLOUD, API.
		"""
		try :
			return self._autoscale
		except Exception as e:
			raise e

	@autoscale.setter
	def autoscale(self, autoscale) :
		r"""Auto scale option for a servicegroup.<br/>Default value: DISABLED<br/>Possible values = DISABLED, DNS, POLICY, CLOUD, API
		"""
		try :
			self._autoscale = autoscale
		except Exception as e:
			raise e

	@property
	def memberport(self) :
		r"""member port.
		"""
		try :
			return self._memberport
		except Exception as e:
			raise e

	@memberport.setter
	def memberport(self, memberport) :
		r"""member port.
		"""
		try :
			self._memberport = memberport
		except Exception as e:
			raise e

	@property
	def autodisablegraceful(self) :
		r"""Indicates graceful shutdown of the service. System will wait for all outstanding connections to this service to be closed before disabling the service.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._autodisablegraceful
		except Exception as e:
			raise e

	@autodisablegraceful.setter
	def autodisablegraceful(self, autodisablegraceful) :
		r"""Indicates graceful shutdown of the service. System will wait for all outstanding connections to this service to be closed before disabling the service.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._autodisablegraceful = autodisablegraceful
		except Exception as e:
			raise e

	@property
	def autodisabledelay(self) :
		r"""The time allowed (in seconds) for a graceful shutdown. During this period, new connections or requests will continue to be sent to this service for clients who already have a persistent session on the system. Connections or requests from fresh or new clients who do not yet have a persistence sessions on the system will not be sent to the service. Instead, they will be load balanced among other available services. After the delay time expires, no new requests or connections will be sent to the service.
		"""
		try :
			return self._autodisabledelay
		except Exception as e:
			raise e

	@autodisabledelay.setter
	def autodisabledelay(self, autodisabledelay) :
		r"""The time allowed (in seconds) for a graceful shutdown. During this period, new connections or requests will continue to be sent to this service for clients who already have a persistent session on the system. Connections or requests from fresh or new clients who do not yet have a persistence sessions on the system will not be sent to the service. Instead, they will be load balanced among other available services. After the delay time expires, no new requests or connections will be sent to the service.
		"""
		try :
			self._autodisabledelay = autodisabledelay
		except Exception as e:
			raise e

	@property
	def monconnectionclose(self) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: NONE<br/>Possible values = RESET, FIN.
		"""
		try :
			return self._monconnectionclose
		except Exception as e:
			raise e

	@monconnectionclose.setter
	def monconnectionclose(self, monconnectionclose) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: NONE<br/>Possible values = RESET, FIN
		"""
		try :
			self._monconnectionclose = monconnectionclose
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the server to which to bind the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the server to which to bind the service group.<br/>Minimum length =  1
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Server port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Server port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def customserverid(self) :
		r"""The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.<br/>Default value: "None".
		"""
		try :
			return self._customserverid
		except Exception as e:
			raise e

	@customserverid.setter
	def customserverid(self, customserverid) :
		r"""The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.<br/>Default value: "None"
		"""
		try :
			self._customserverid = customserverid
		except Exception as e:
			raise e

	@property
	def serverid(self) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			return self._serverid
		except Exception as e:
			raise e

	@serverid.setter
	def serverid(self, serverid) :
		r"""The  identifier for the service. This is used when the persistency type is set to Custom Server ID.
		"""
		try :
			self._serverid = serverid
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		r"""The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum length =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		r"""The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum length =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def nameserver(self) :
		r"""Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use the global nameserver.
		"""
		try :
			return self._nameserver
		except Exception as e:
			raise e

	@nameserver.setter
	def nameserver(self, nameserver) :
		r"""Specify the nameserver to which the query for bound domain needs to be sent. If not specified, use the global nameserver.
		"""
		try :
			self._nameserver = nameserver
		except Exception as e:
			raise e

	@property
	def dbsttl(self) :
		r"""Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0.
		"""
		try :
			return self._dbsttl
		except Exception as e:
			raise e

	@dbsttl.setter
	def dbsttl(self, dbsttl) :
		r"""Specify the TTL for DNS record for domain based service.The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0
		"""
		try :
			self._dbsttl = dbsttl
		except Exception as e:
			raise e

	@property
	def monitor_name_svc(self) :
		r"""Name of the monitor bound to the service group. Used to assign a weight to the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitor_name_svc
		except Exception as e:
			raise e

	@monitor_name_svc.setter
	def monitor_name_svc(self, monitor_name_svc) :
		r"""Name of the monitor bound to the service group. Used to assign a weight to the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitor_name_svc = monitor_name_svc
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		r"""weight of the monitor that is bound to servicegroup.<br/>Minimum length =  1.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@dup_weight.setter
	def dup_weight(self, dup_weight) :
		r"""weight of the monitor that is bound to servicegroup.<br/>Minimum length =  1
		"""
		try :
			self._dup_weight = dup_weight
		except Exception as e:
			raise e

	@property
	def delay(self) :
		r"""Time, in seconds, allocated for a shutdown of the services in the service group. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
		"""
		try :
			return self._delay
		except Exception as e:
			raise e

	@delay.setter
	def delay(self, delay) :
		r"""Time, in seconds, allocated for a shutdown of the services in the service group. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE).
		"""
		try :
			self._delay = delay
		except Exception as e:
			raise e

	@property
	def graceful(self) :
		r"""Wait for all existing connections to the service to terminate before shutting down the service.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._graceful
		except Exception as e:
			raise e

	@graceful.setter
	def graceful(self, graceful) :
		r"""Wait for all existing connections to the service to terminate before shutting down the service.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._graceful = graceful
		except Exception as e:
			raise e

	@property
	def includemembers(self) :
		r"""Display the members of the listed service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			return self._includemembers
		except Exception as e:
			raise e

	@includemembers.setter
	def includemembers(self, includemembers) :
		r"""Display the members of the listed service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			self._includemembers = includemembers
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the service group.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numofconnections(self) :
		r"""This will tell the number of client side connections are still open.
		"""
		try :
			return self._numofconnections
		except Exception as e:
			raise e

	@property
	def serviceconftype(self) :
		r"""The configuration type of the service group.
		"""
		try :
			return self._serviceconftype
		except Exception as e:
			raise e

	@property
	def value(self) :
		r"""SSL Status.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		r"""The state of the service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""IP Address.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		r"""Time when last state change occurred. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def stateupdatereason(self) :
		r"""Checks state update reason on the secondary node.
		"""
		try :
			return self._stateupdatereason
		except Exception as e:
			raise e

	@property
	def clmonowner(self) :
		r"""Tells the mon owner of the service.
		"""
		try :
			return self._clmonowner
		except Exception as e:
			raise e

	@property
	def clmonview(self) :
		r"""Tells the view id of the monitoring owner.
		"""
		try :
			return self._clmonview
		except Exception as e:
			raise e

	@property
	def groupcount(self) :
		r"""Servicegroup Count.
		"""
		try :
			return self._groupcount
		except Exception as e:
			raise e

	@property
	def serviceipstr(self) :
		r"""This field has been intorduced to show the dbs services ip.
		"""
		try :
			return self._serviceipstr
		except Exception as e:
			raise e

	@property
	def servicegroupeffectivestate(self) :
		r"""Indicates the effective servicegroup state based on the state of the bound service items.If all services are UP the effective state is UP, if all are DOWN its DOWN,if all are OFS its OFS.If atleast one serviceis UP and rest are either DOWN or OFS, the effective state is PARTIAL-UP.If atleast one bound service is DOWN and rest are OFS the effective state is PARTIAL DOWN.<br/>Possible values = UP, DOWN, OUT OF SERVICE, PARTIAL-UP, PARTIAL-DOWN.
		"""
		try :
			return self._servicegroupeffectivestate
		except Exception as e:
			raise e

	@property
	def nodefaultbindings(self) :
		r"""to determine if the configuration is from stylebooks.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nodefaultbindings
		except Exception as e:
			raise e

	@property
	def svcitmactsvcs(self) :
		r"""This gives the total active service items for an FQDN for SRV type server binding.
		"""
		try :
			return self._svcitmactsvcs
		except Exception as e:
			raise e

	@property
	def svcitmboundsvcs(self) :
		r"""This gives the total bound items for an FQDN for SRV type server binding.
		"""
		try :
			return self._svcitmboundsvcs
		except Exception as e:
			raise e

	@property
	def monuserstatusmesg(self) :
		r"""This field has been introduced to show user monitor failure reasons.
		"""
		try :
			return self._monuserstatusmesg
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(servicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.servicegroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = servicegroup()
		addresource.servicegroupname = resource.servicegroupname
		addresource.servicetype = resource.servicetype
		addresource.cachetype = resource.cachetype
		addresource.td = resource.td
		addresource.maxclient = resource.maxclient
		addresource.maxreq = resource.maxreq
		addresource.cacheable = resource.cacheable
		addresource.cip = resource.cip
		addresource.cipheader = resource.cipheader
		addresource.usip = resource.usip
		addresource.pathmonitor = resource.pathmonitor
		addresource.pathmonitorindv = resource.pathmonitorindv
		addresource.useproxyport = resource.useproxyport
		addresource.healthmonitor = resource.healthmonitor
		addresource.sc = resource.sc
		addresource.sp = resource.sp
		addresource.rtspsessionidremap = resource.rtspsessionidremap
		addresource.clttimeout = resource.clttimeout
		addresource.svrtimeout = resource.svrtimeout
		addresource.cka = resource.cka
		addresource.tcpb = resource.tcpb
		addresource.cmp = resource.cmp
		addresource.maxbandwidth = resource.maxbandwidth
		addresource.monthreshold = resource.monthreshold
		addresource.state = resource.state
		addresource.downstateflush = resource.downstateflush
		addresource.tcpprofilename = resource.tcpprofilename
		addresource.httpprofilename = resource.httpprofilename
		addresource.comment = resource.comment
		addresource.appflowlog = resource.appflowlog
		addresource.netprofile = resource.netprofile
		addresource.autoscale = resource.autoscale
		addresource.memberport = resource.memberport
		addresource.autodisablegraceful = resource.autodisablegraceful
		addresource.autodisabledelay = resource.autodisabledelay
		addresource.monconnectionclose = resource.monconnectionclose
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add servicegroup.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ servicegroup() for _ in range(len(resource))]
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
		deleteresource = servicegroup()
		deleteresource.servicegroupname = resource.servicegroupname
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete servicegroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = servicegroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.servicegroupname = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ servicegroup() for _ in range(len(resource))]
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
		updateresource = servicegroup()
		updateresource.servicegroupname = resource.servicegroupname
		updateresource.servername = resource.servername
		updateresource.port = resource.port
		updateresource.weight = resource.weight
		updateresource.customserverid = resource.customserverid
		updateresource.serverid = resource.serverid
		updateresource.hashid = resource.hashid
		updateresource.nameserver = resource.nameserver
		updateresource.dbsttl = resource.dbsttl
		updateresource.monitor_name_svc = resource.monitor_name_svc
		updateresource.dup_weight = resource.dup_weight
		updateresource.maxclient = resource.maxclient
		updateresource.maxreq = resource.maxreq
		updateresource.healthmonitor = resource.healthmonitor
		updateresource.cacheable = resource.cacheable
		updateresource.cip = resource.cip
		updateresource.cipheader = resource.cipheader
		updateresource.usip = resource.usip
		updateresource.pathmonitor = resource.pathmonitor
		updateresource.pathmonitorindv = resource.pathmonitorindv
		updateresource.useproxyport = resource.useproxyport
		updateresource.sc = resource.sc
		updateresource.sp = resource.sp
		updateresource.rtspsessionidremap = resource.rtspsessionidremap
		updateresource.clttimeout = resource.clttimeout
		updateresource.svrtimeout = resource.svrtimeout
		updateresource.cka = resource.cka
		updateresource.tcpb = resource.tcpb
		updateresource.cmp = resource.cmp
		updateresource.maxbandwidth = resource.maxbandwidth
		updateresource.monthreshold = resource.monthreshold
		updateresource.downstateflush = resource.downstateflush
		updateresource.tcpprofilename = resource.tcpprofilename
		updateresource.httpprofilename = resource.httpprofilename
		updateresource.comment = resource.comment
		updateresource.appflowlog = resource.appflowlog
		updateresource.netprofile = resource.netprofile
		updateresource.autodisablegraceful = resource.autodisablegraceful
		updateresource.autodisabledelay = resource.autodisabledelay
		updateresource.monconnectionclose = resource.monconnectionclose
		updateresource.autoscale = resource.autoscale
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update servicegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ servicegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of servicegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = servicegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.servicegroupname = resource
				else :
					unsetresource.servicegroupname = resource.servicegroupname
					unsetresource.servername = resource.servername
					unsetresource.port = resource.port
					unsetresource.weight = resource.weight
					unsetresource.customserverid = resource.customserverid
					unsetresource.serverid = resource.serverid
					unsetresource.hashid = resource.hashid
					unsetresource.nameserver = resource.nameserver
					unsetresource.dbsttl = resource.dbsttl
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i].servicegroupname
							unsetresources[i].servername = resource[i].servername
							unsetresources[i].port = resource[i].port
							unsetresources[i].weight = resource[i].weight
							unsetresources[i].customserverid = resource[i].customserverid
							unsetresources[i].serverid = resource[i].serverid
							unsetresources[i].hashid = resource[i].hashid
							unsetresources[i].nameserver = resource[i].nameserver
							unsetresources[i].dbsttl = resource[i].dbsttl
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable servicegroup.
		"""
		try :
			if type(resource) is not list :
				enableresource = servicegroup()
				if type(resource) !=  type(enableresource):
					enableresource.servicegroupname = resource
				else :
					enableresource.servicegroupname = resource.servicegroupname
					enableresource.servername = resource.servername
					enableresource.port = resource.port
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicegroupname = resource[i].servicegroupname
							enableresources[i].servername = resource[i].servername
							enableresources[i].port = resource[i].port
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable servicegroup.
		"""
		try :
			if type(resource) is not list :
				disableresource = servicegroup()
				if type(resource) !=  type(disableresource):
					disableresource.servicegroupname = resource
				else :
					disableresource.servicegroupname = resource.servicegroupname
					disableresource.servername = resource.servername
					disableresource.port = resource.port
					disableresource.delay = resource.delay
					disableresource.graceful = resource.graceful
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ servicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicegroupname = resource[i].servicegroupname
							disableresources[i].servername = resource[i].servername
							disableresources[i].port = resource[i].port
							disableresources[i].delay = resource[i].delay
							disableresources[i].graceful = resource[i].graceful
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_servicegroupname) :
		r""" Use this API to rename a servicegroup resource.
		"""
		try :
			renameresource = servicegroup()
			if type(resource) == cls :
				renameresource.servicegroupname = resource.servicegroupname
			else :
				renameresource.servicegroupname = resource
			return renameresource.rename_resource(client,new_servicegroupname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the servicegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = servicegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = servicegroup()
					obj.servicegroupname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [servicegroup() for _ in range(len(name))]
						obj = [servicegroup() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = servicegroup()
							obj[i].servicegroupname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the servicegroup resources that are configured on netscaler.
	# This uses servicegroup_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = servicegroup()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of servicegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the servicegroup resources configured on NetScaler.
		"""
		try :
			obj = servicegroup()
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
		r""" Use this API to count filtered the set of servicegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = servicegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sp:
		ON = "ON"
		OFF = "OFF"

	class Sc:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cachetype:
		TRANSPARENT = "TRANSPARENT"
		REVERSE = "REVERSE"
		FORWARD = "FORWARD"

	class Nodefaultbindings:
		YES = "YES"
		NO = "NO"

	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		DTLS = "DTLS"
		NNTP = "NNTP"
		RPCSVR = "RPCSVR"
		DNS = "DNS"
		ADNS = "ADNS"
		SNMP = "SNMP"
		RTSP = "RTSP"
		DHCPRA = "DHCPRA"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		DNS_TCP = "DNS_TCP"
		ADNS_TCP = "ADNS_TCP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"
		MONGO = "MONGO"
		MONGO_TLS = "MONGO_TLS"
		RADIUS = "RADIUS"
		RADIUSListener = "RADIUSListener"
		RDP = "RDP"
		DIAMETER = "DIAMETER"
		SSL_DIAMETER = "SSL_DIAMETER"
		TFTP = "TFTP"
		SMPP = "SMPP"
		PPTP = "PPTP"
		GRE = "GRE"
		SYSLOGTCP = "SYSLOGTCP"
		SYSLOGUDP = "SYSLOGUDP"
		FIX = "FIX"
		SSL_FIX = "SSL_FIX"
		USER_TCP = "USER_TCP"
		USER_SSL_TCP = "USER_SSL_TCP"
		QUIC = "QUIC"
		IPFIX = "IPFIX"
		LOGSTREAM = "LOGSTREAM"
		LOGSTREAM_SSL = "LOGSTREAM_SSL"
		MQTT = "MQTT"
		MQTT_TLS = "MQTT_TLS"
		QUIC_BRIDGE = "QUIC_BRIDGE"

	class Svrstate:
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

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class Useproxyport:
		YES = "YES"
		NO = "NO"

	class Usip:
		YES = "YES"
		NO = "NO"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Monconnectionclose:
		RESET = "RESET"
		FIN = "FIN"

	class Servicegroupeffectivestate:
		UP = "UP"
		DOWN = "DOWN"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		PARTIAL_UP = "PARTIAL-UP"
		PARTIAL_DOWN = "PARTIAL-DOWN"

	class Pathmonitor:
		YES = "YES"
		NO = "NO"

	class Autoscale:
		DISABLED = "DISABLED"
		DNS = "DNS"
		POLICY = "POLICY"
		CLOUD = "CLOUD"
		API = "API"

	class Tcpb:
		YES = "YES"
		NO = "NO"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pathmonitorindv:
		YES = "YES"
		NO = "NO"

	class Autodisablegraceful:
		YES = "YES"
		NO = "NO"

	class Healthmonitor:
		YES = "YES"
		NO = "NO"

	class Cka:
		YES = "YES"
		NO = "NO"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmp:
		YES = "YES"
		NO = "NO"

	class Rtspsessionidremap:
		ON = "ON"
		OFF = "OFF"

	class Graceful:
		YES = "YES"
		NO = "NO"

class servicegroup_response(base_response) :
	def __init__(self, length=1) :
		self.servicegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.servicegroup = [servicegroup() for _ in range(length)]

