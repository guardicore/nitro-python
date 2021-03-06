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

class lbparameter(base_resource) :
	""" Configuration for LB parameter resource. """
	def __init__(self) :
		self._httponlycookieflag = None
		self._usesecuredpersistencecookie = None
		self._useencryptedpersistencecookie = None
		self._cookiepassphrase = None
		self._consolidatedlconn = None
		self._useportforhashlb = None
		self._preferdirectroute = None
		self._startuprrfactor = None
		self._monitorskipmaxclient = None
		self._monitorconnectionclose = None
		self._vserverspecificmac = None
		self._allowboundsvcremoval = None
		self._retainservicestate = None
		self._dbsttl = None
		self._maxpipelinenat = None
		self._literaladccookieattribute = None
		self._computedadccookieattribute = None
		self._storemqttclientidandusername = None
		self._dropmqttjumbomessage = None
		self._lbhashalgorithm = None
		self._lbhashfingers = None
		self._sessionsthreshold = None
		self._builtin = None
		self._feature = None
		self._adccookieattributewarningmsg = None
		self._lbhashalgowinsize = None

	@property
	def httponlycookieflag(self) :
		r"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._httponlycookieflag
		except Exception as e:
			raise e

	@httponlycookieflag.setter
	def httponlycookieflag(self, httponlycookieflag) :
		r"""Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute limits the scope of a cookie to HTTP requests and helps mitigate the risk of cross-site scripting attacks.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._httponlycookieflag = httponlycookieflag
		except Exception as e:
			raise e

	@property
	def usesecuredpersistencecookie(self) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._usesecuredpersistencecookie
		except Exception as e:
			raise e

	@usesecuredpersistencecookie.setter
	def usesecuredpersistencecookie(self, usesecuredpersistencecookie) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._usesecuredpersistencecookie = usesecuredpersistencecookie
		except Exception as e:
			raise e

	@property
	def useencryptedpersistencecookie(self) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._useencryptedpersistencecookie
		except Exception as e:
			raise e

	@useencryptedpersistencecookie.setter
	def useencryptedpersistencecookie(self, useencryptedpersistencecookie) :
		r"""Encode persistence cookie values using SHA2 hash.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._useencryptedpersistencecookie = useencryptedpersistencecookie
		except Exception as e:
			raise e

	@property
	def cookiepassphrase(self) :
		r"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			return self._cookiepassphrase
		except Exception as e:
			raise e

	@cookiepassphrase.setter
	def cookiepassphrase(self, cookiepassphrase) :
		r"""Use this parameter to specify the passphrase used to generate secured persistence cookie value. It specifies the passphrase with a maximum of 31 characters.
		"""
		try :
			self._cookiepassphrase = cookiepassphrase
		except Exception as e:
			raise e

	@property
	def consolidatedlconn(self) :
		r"""To find the service with the fewest connections, the virtual server uses the consolidated connection statistics from all the packet engines. The NO setting allows consideration of only the number of connections on the packet engine that received the new connection.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._consolidatedlconn
		except Exception as e:
			raise e

	@consolidatedlconn.setter
	def consolidatedlconn(self, consolidatedlconn) :
		r"""To find the service with the fewest connections, the virtual server uses the consolidated connection statistics from all the packet engines. The NO setting allows consideration of only the number of connections on the packet engine that received the new connection.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._consolidatedlconn = consolidatedlconn
		except Exception as e:
			raise e

	@property
	def useportforhashlb(self) :
		r"""Include the port number of the service when creating a hash for hash based load balancing methods. With the NO setting, only the IP address of the service is considered when creating a hash.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._useportforhashlb
		except Exception as e:
			raise e

	@useportforhashlb.setter
	def useportforhashlb(self, useportforhashlb) :
		r"""Include the port number of the service when creating a hash for hash based load balancing methods. With the NO setting, only the IP address of the service is considered when creating a hash.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._useportforhashlb = useportforhashlb
		except Exception as e:
			raise e

	@property
	def preferdirectroute(self) :
		r"""Perform route lookup for traffic received by the Citrix ADC, and forward the traffic according to configured routes. Do not set this parameter if you want a wildcard virtual server to direct packets received by the appliance to an intermediary device, such as a firewall, even if their destination is directly connected to the appliance. Route lookup is performed after the packets have been processed and returned by the intermediary device.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._preferdirectroute
		except Exception as e:
			raise e

	@preferdirectroute.setter
	def preferdirectroute(self, preferdirectroute) :
		r"""Perform route lookup for traffic received by the Citrix ADC, and forward the traffic according to configured routes. Do not set this parameter if you want a wildcard virtual server to direct packets received by the appliance to an intermediary device, such as a firewall, even if their destination is directly connected to the appliance. Route lookup is performed after the packets have been processed and returned by the intermediary device.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._preferdirectroute = preferdirectroute
		except Exception as e:
			raise e

	@property
	def startuprrfactor(self) :
		r"""Number of requests, per service, for which to apply the round robin load balancing method before switching to the configured load balancing method, thus allowing services to ramp up gradually to full load. Until the specified number of requests is distributed, the Citrix ADC is said to be implementing the slow start mode (or startup round robin). Implemented for a virtual server when one of the following is true:
		* The virtual server is newly created.
		* One or more services are newly bound to the virtual server. 
		* One or more services bound to the virtual server are enabled.
		* The load balancing method is changed.
		This parameter applies to all the load balancing virtual servers configured on the Citrix ADC, except for those virtual servers for which the virtual server-level slow start parameters (New Service Startup Request Rate and Increment Interval) are configured. If the global slow start parameter and the slow start parameters for a given virtual server are not set, the appliance implements a default slow start for the virtual server, as follows:
		* For a newly configured virtual server, the appliance implements slow start for the first 100 requests received by the virtual server.
		* For an existing virtual server, if one or more services are newly bound or newly enabled, or if the load balancing method is changed, the appliance dynamically computes the number of requests for which to implement startup round robin. It obtains this number by multiplying the request rate by the number of bound services (it includes services that are marked as DOWN). For example, if the current request rate is 20 requests/s and ten services are bound to the virtual server, the appliance performs startup round robin for 200 requests.
		Not applicable to a virtual server for which a hash based load balancing method is configured.
		"""
		try :
			return self._startuprrfactor
		except Exception as e:
			raise e

	@startuprrfactor.setter
	def startuprrfactor(self, startuprrfactor) :
		r"""Number of requests, per service, for which to apply the round robin load balancing method before switching to the configured load balancing method, thus allowing services to ramp up gradually to full load. Until the specified number of requests is distributed, the Citrix ADC is said to be implementing the slow start mode (or startup round robin). Implemented for a virtual server when one of the following is true:
		* The virtual server is newly created.
		* One or more services are newly bound to the virtual server. 
		* One or more services bound to the virtual server are enabled.
		* The load balancing method is changed.
		This parameter applies to all the load balancing virtual servers configured on the Citrix ADC, except for those virtual servers for which the virtual server-level slow start parameters (New Service Startup Request Rate and Increment Interval) are configured. If the global slow start parameter and the slow start parameters for a given virtual server are not set, the appliance implements a default slow start for the virtual server, as follows:
		* For a newly configured virtual server, the appliance implements slow start for the first 100 requests received by the virtual server.
		* For an existing virtual server, if one or more services are newly bound or newly enabled, or if the load balancing method is changed, the appliance dynamically computes the number of requests for which to implement startup round robin. It obtains this number by multiplying the request rate by the number of bound services (it includes services that are marked as DOWN). For example, if the current request rate is 20 requests/s and ten services are bound to the virtual server, the appliance performs startup round robin for 200 requests.
		Not applicable to a virtual server for which a hash based load balancing method is configured.
		"""
		try :
			self._startuprrfactor = startuprrfactor
		except Exception as e:
			raise e

	@property
	def monitorskipmaxclient(self) :
		r"""When a monitor initiates a connection to a service, do not check to determine whether the number of connections to the service has reached the limit specified by the service's Max Clients setting. Enables monitoring to continue even if the service has reached its connection limit.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._monitorskipmaxclient
		except Exception as e:
			raise e

	@monitorskipmaxclient.setter
	def monitorskipmaxclient(self, monitorskipmaxclient) :
		r"""When a monitor initiates a connection to a service, do not check to determine whether the number of connections to the service has reached the limit specified by the service's Max Clients setting. Enables monitoring to continue even if the service has reached its connection limit.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._monitorskipmaxclient = monitorskipmaxclient
		except Exception as e:
			raise e

	@property
	def monitorconnectionclose(self) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: FIN<br/>Possible values = RESET, FIN.
		"""
		try :
			return self._monitorconnectionclose
		except Exception as e:
			raise e

	@monitorconnectionclose.setter
	def monitorconnectionclose(self, monitorconnectionclose) :
		r"""Close monitoring connections by sending the service a connection termination message with the specified bit set.<br/>Default value: FIN<br/>Possible values = RESET, FIN
		"""
		try :
			self._monitorconnectionclose = monitorconnectionclose
		except Exception as e:
			raise e

	@property
	def vserverspecificmac(self) :
		r"""Allow a MAC-mode virtual server to accept traffic returned by an intermediary device, such as a firewall, to which the traffic was previously forwarded by another MAC-mode virtual server. The second virtual server can then distribute that traffic across the destination server farm. Also useful when load balancing Branch Repeater appliances.
		Note: The second virtual server can also send the traffic to another set of intermediary devices, such as another set of firewalls. If necessary, you can configure multiple MAC-mode virtual servers to pass traffic successively through multiple sets of intermediary devices.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._vserverspecificmac
		except Exception as e:
			raise e

	@vserverspecificmac.setter
	def vserverspecificmac(self, vserverspecificmac) :
		r"""Allow a MAC-mode virtual server to accept traffic returned by an intermediary device, such as a firewall, to which the traffic was previously forwarded by another MAC-mode virtual server. The second virtual server can then distribute that traffic across the destination server farm. Also useful when load balancing Branch Repeater appliances.
		Note: The second virtual server can also send the traffic to another set of intermediary devices, such as another set of firewalls. If necessary, you can configure multiple MAC-mode virtual servers to pass traffic successively through multiple sets of intermediary devices.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._vserverspecificmac = vserverspecificmac
		except Exception as e:
			raise e

	@property
	def allowboundsvcremoval(self) :
		r"""This is used, to enable/disable the option of svc/svcgroup removal, if it is bound to one or more vserver. If it is enabled, the svc/svcgroup can be removed, even if it bound to vservers. If disabled, an error will be thrown, when the user tries to remove a svc/svcgroup without unbinding from its vservers.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._allowboundsvcremoval
		except Exception as e:
			raise e

	@allowboundsvcremoval.setter
	def allowboundsvcremoval(self, allowboundsvcremoval) :
		r"""This is used, to enable/disable the option of svc/svcgroup removal, if it is bound to one or more vserver. If it is enabled, the svc/svcgroup can be removed, even if it bound to vservers. If disabled, an error will be thrown, when the user tries to remove a svc/svcgroup without unbinding from its vservers.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._allowboundsvcremoval = allowboundsvcremoval
		except Exception as e:
			raise e

	@property
	def retainservicestate(self) :
		r"""This option is used to retain the original state of service or servicegroup member when an enable server command is issued.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._retainservicestate
		except Exception as e:
			raise e

	@retainservicestate.setter
	def retainservicestate(self, retainservicestate) :
		r"""This option is used to retain the original state of service or servicegroup member when an enable server command is issued.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._retainservicestate = retainservicestate
		except Exception as e:
			raise e

	@property
	def dbsttl(self) :
		r"""Specify the TTL for DNS record for domain based service. The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0.
		"""
		try :
			return self._dbsttl
		except Exception as e:
			raise e

	@dbsttl.setter
	def dbsttl(self, dbsttl) :
		r"""Specify the TTL for DNS record for domain based service. The default value of ttl is 0 which indicates to use the TTL received in DNS response for monitors.<br/>Default value: 0
		"""
		try :
			self._dbsttl = dbsttl
		except Exception as e:
			raise e

	@property
	def maxpipelinenat(self) :
		r"""Maximum number of concurrent requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. This parameter is applicable to ANY service type and all UDP service types (except DNS) and only when "svrTimeout" is set to zero. A value of 0 (zero) applies no limit to the number of concurrent requests allowed on a single client connection.
		"""
		try :
			return self._maxpipelinenat
		except Exception as e:
			raise e

	@maxpipelinenat.setter
	def maxpipelinenat(self, maxpipelinenat) :
		r"""Maximum number of concurrent requests to allow on a single client connection, which is identified by the <clientip:port>-<vserver ip:port> tuple. This parameter is applicable to ANY service type and all UDP service types (except DNS) and only when "svrTimeout" is set to zero. A value of 0 (zero) applies no limit to the number of concurrent requests allowed on a single client connection.
		"""
		try :
			self._maxpipelinenat = maxpipelinenat
		except Exception as e:
			raise e

	@property
	def literaladccookieattribute(self) :
		r"""String configured as LiteralADCCookieAttribute will be appended as attribute for Citrix ADC cookie (for example: LB cookie persistence , GSLB site persistence, CS cookie persistence, LB group cookie persistence).
		Sample usage -
		set lb parameter -LiteralADCCookieAttribute ";SameSite=None".
		"""
		try :
			return self._literaladccookieattribute
		except Exception as e:
			raise e

	@literaladccookieattribute.setter
	def literaladccookieattribute(self, literaladccookieattribute) :
		r"""String configured as LiteralADCCookieAttribute will be appended as attribute for Citrix ADC cookie (for example: LB cookie persistence , GSLB site persistence, CS cookie persistence, LB group cookie persistence).
		Sample usage -
		set lb parameter -LiteralADCCookieAttribute ";SameSite=None".
		"""
		try :
			self._literaladccookieattribute = literaladccookieattribute
		except Exception as e:
			raise e

	@property
	def computedadccookieattribute(self) :
		r"""ComputedADCCookieAttribute accepts ns variable as input in form of string starting with $ (to understand how to configure ns variable, please check man add ns variable). policies can be configured to modify this variable for every transaction and the final value of the variable after policy evaluation will be appended as attribute to Citrix ADC cookie (for example: LB cookie persistence , GSLB sitepersistence, CS cookie persistence, LB group cookie persistence). Only one of ComputedADCCookieAttribute, LiteralADCCookieAttribute can be set.
		Sample usage -
		add ns variable lbvar -type TEXT(100) -scope Transaction
		add ns assignment lbassign -variable $lbvar -set "\\";SameSite=Strict\\""
		add rewrite policy lbpol <valid policy expression> lbassign
		bind rewrite global lbpol 100 next -type RES_OVERRIDE
		set lb param -ComputedADCCookieAttribute "$lbvar"
		For incoming client request, if above policy evaluates TRUE, then SameSite=Strict will be appended to ADC generated cookie.
		"""
		try :
			return self._computedadccookieattribute
		except Exception as e:
			raise e

	@computedadccookieattribute.setter
	def computedadccookieattribute(self, computedadccookieattribute) :
		r"""ComputedADCCookieAttribute accepts ns variable as input in form of string starting with $ (to understand how to configure ns variable, please check man add ns variable). policies can be configured to modify this variable for every transaction and the final value of the variable after policy evaluation will be appended as attribute to Citrix ADC cookie (for example: LB cookie persistence , GSLB sitepersistence, CS cookie persistence, LB group cookie persistence). Only one of ComputedADCCookieAttribute, LiteralADCCookieAttribute can be set.
		Sample usage -
		add ns variable lbvar -type TEXT(100) -scope Transaction
		add ns assignment lbassign -variable $lbvar -set "\\";SameSite=Strict\\""
		add rewrite policy lbpol <valid policy expression> lbassign
		bind rewrite global lbpol 100 next -type RES_OVERRIDE
		set lb param -ComputedADCCookieAttribute "$lbvar"
		For incoming client request, if above policy evaluates TRUE, then SameSite=Strict will be appended to ADC generated cookie.
		"""
		try :
			self._computedadccookieattribute = computedadccookieattribute
		except Exception as e:
			raise e

	@property
	def storemqttclientidandusername(self) :
		r"""This option allows to store the MQTT clientid and username in transactional logs.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._storemqttclientidandusername
		except Exception as e:
			raise e

	@storemqttclientidandusername.setter
	def storemqttclientidandusername(self, storemqttclientidandusername) :
		r"""This option allows to store the MQTT clientid and username in transactional logs.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._storemqttclientidandusername = storemqttclientidandusername
		except Exception as e:
			raise e

	@property
	def dropmqttjumbomessage(self) :
		r"""When this option is enabled, MQTT messages of length greater than 64k will be dropped and the client/server connections will be reset.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropmqttjumbomessage
		except Exception as e:
			raise e

	@dropmqttjumbomessage.setter
	def dropmqttjumbomessage(self, dropmqttjumbomessage) :
		r"""When this option is enabled, MQTT messages of length greater than 64k will be dropped and the client/server connections will be reset.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._dropmqttjumbomessage = dropmqttjumbomessage
		except Exception as e:
			raise e

	@property
	def lbhashalgorithm(self) :
		r"""This option dictates the hashing algorithm used for hash based LB methods (URLHASH, DOMAINHASH, SOURCEIPHASH, DESTINATIONIPHASH, SRCIPDESTIPHASH, SRCIPSRCPORTHASH, TOKEN, USER_TOKEN, CALLIDHASH).<br/>Default value: DEFAULT<br/>Possible values = DEFAULT, PRAC, JARH.
		"""
		try :
			return self._lbhashalgorithm
		except Exception as e:
			raise e

	@lbhashalgorithm.setter
	def lbhashalgorithm(self, lbhashalgorithm) :
		r"""This option dictates the hashing algorithm used for hash based LB methods (URLHASH, DOMAINHASH, SOURCEIPHASH, DESTINATIONIPHASH, SRCIPDESTIPHASH, SRCIPSRCPORTHASH, TOKEN, USER_TOKEN, CALLIDHASH).<br/>Default value: DEFAULT<br/>Possible values = DEFAULT, PRAC, JARH
		"""
		try :
			self._lbhashalgorithm = lbhashalgorithm
		except Exception as e:
			raise e

	@property
	def lbhashfingers(self) :
		r"""This option is used to specify the number of fingers to be used in PRAC and JARH algorithms for hash based LB methods. Increasing the number of fingers might give better distribution of traffic at the expense of additional memory.<br/>Default value: 256<br/>Minimum length =  1<br/>Maximum length =  1024.
		"""
		try :
			return self._lbhashfingers
		except Exception as e:
			raise e

	@lbhashfingers.setter
	def lbhashfingers(self, lbhashfingers) :
		r"""This option is used to specify the number of fingers to be used in PRAC and JARH algorithms for hash based LB methods. Increasing the number of fingers might give better distribution of traffic at the expense of additional memory.<br/>Default value: 256<br/>Minimum length =  1<br/>Maximum length =  1024
		"""
		try :
			self._lbhashfingers = lbhashfingers
		except Exception as e:
			raise e

	@property
	def sessionsthreshold(self) :
		r"""This option is used to get the upper-limit on the number of persistent sessions set by the administrator for this system.<br/>Minimum value =  1.
		"""
		try :
			return self._sessionsthreshold
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r""".<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@property
	def adccookieattributewarningmsg(self) :
		r"""Used to describe any configuration issue with respect to ns variable configured as part of set lb parameter.
		"""
		try :
			return self._adccookieattributewarningmsg
		except Exception as e:
			raise e

	@property
	def lbhashalgowinsize(self) :
		r"""This options allows to increase window size used in LB hashing algorithm(DEFAULT).<br/>Default value: 16.
		"""
		try :
			return self._lbhashalgowinsize
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lbparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lbparameter
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
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = lbparameter()
		updateresource.httponlycookieflag = resource.httponlycookieflag
		updateresource.usesecuredpersistencecookie = resource.usesecuredpersistencecookie
		updateresource.useencryptedpersistencecookie = resource.useencryptedpersistencecookie
		updateresource.cookiepassphrase = resource.cookiepassphrase
		updateresource.consolidatedlconn = resource.consolidatedlconn
		updateresource.useportforhashlb = resource.useportforhashlb
		updateresource.preferdirectroute = resource.preferdirectroute
		updateresource.startuprrfactor = resource.startuprrfactor
		updateresource.monitorskipmaxclient = resource.monitorskipmaxclient
		updateresource.monitorconnectionclose = resource.monitorconnectionclose
		updateresource.vserverspecificmac = resource.vserverspecificmac
		updateresource.allowboundsvcremoval = resource.allowboundsvcremoval
		updateresource.retainservicestate = resource.retainservicestate
		updateresource.dbsttl = resource.dbsttl
		updateresource.maxpipelinenat = resource.maxpipelinenat
		updateresource.literaladccookieattribute = resource.literaladccookieattribute
		updateresource.computedadccookieattribute = resource.computedadccookieattribute
		updateresource.storemqttclientidandusername = resource.storemqttclientidandusername
		updateresource.dropmqttjumbomessage = resource.dropmqttjumbomessage
		updateresource.lbhashalgorithm = resource.lbhashalgorithm
		updateresource.lbhashfingers = resource.lbhashfingers
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update lbparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of lbparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = lbparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the lbparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = lbparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Usesecuredpersistencecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropmqttjumbomessage:
		YES = "YES"
		NO = "NO"

	class Httponlycookieflag:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"
		APIGateway = "APIGateway"

	class Monitorconnectionclose:
		RESET = "RESET"
		FIN = "FIN"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Lbhashalgorithm:
		DEFAULT = "DEFAULT"
		PRAC = "PRAC"
		JARH = "JARH"

	class Allowboundsvcremoval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Retainservicestate:
		ON = "ON"
		OFF = "OFF"

	class Useportforhashlb:
		YES = "YES"
		NO = "NO"

	class Consolidatedlconn:
		YES = "YES"
		NO = "NO"

	class Vserverspecificmac:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Useencryptedpersistencecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Storemqttclientidandusername:
		YES = "YES"
		NO = "NO"

	class Monitorskipmaxclient:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Preferdirectroute:
		YES = "YES"
		NO = "NO"

class lbparameter_response(base_response) :
	def __init__(self, length=1) :
		self.lbparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lbparameter = [lbparameter() for _ in range(length)]

