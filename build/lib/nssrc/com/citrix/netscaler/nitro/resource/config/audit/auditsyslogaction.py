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

class auditsyslogaction(base_resource) :
	""" Configuration for system log action resource. """
	def __init__(self) :
		self._name = None
		self._serverip = None
		self._serverdomainname = None
		self._domainresolveretry = None
		self._lbvservername = None
		self._serverport = None
		self._loglevel = None
		self._dateformat = None
		self._logfacility = None
		self._tcp = None
		self._acl = None
		self._timezone = None
		self._userdefinedauditlog = None
		self._appflowexport = None
		self._lsn = None
		self._alg = None
		self._subscriberlog = None
		self._transport = None
		self._tcpprofilename = None
		self._maxlogdatasizetohold = None
		self._dns = None
		self._contentinspectionlog = None
		self._netprofile = None
		self._sslinterception = None
		self._urlfiltering = None
		self._domainresolvenow = None
		self._ip = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the syslog action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the syslog action is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my syslog action" or 'my syslog action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the syslog action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the syslog action is added.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my syslog action" or 'my syslog action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		r"""IP address of the syslog server.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address of the syslog server.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverdomainname(self) :
		r"""SYSLOG server name as a FQDN.  Mutually exclusive with serverIP/lbVserverName.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._serverdomainname
		except Exception as e:
			raise e

	@serverdomainname.setter
	def serverdomainname(self, serverdomainname) :
		r"""SYSLOG server name as a FQDN.  Mutually exclusive with serverIP/lbVserverName.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._serverdomainname = serverdomainname
		except Exception as e:
			raise e

	@property
	def domainresolveretry(self) :
		r"""Time, in seconds, for which the Citrix ADC waits before sending another DNS query to resolve the host name of the syslog server if the last query failed.<br/>Default value: 5<br/>Minimum length =  5<br/>Maximum length =  20939.
		"""
		try :
			return self._domainresolveretry
		except Exception as e:
			raise e

	@domainresolveretry.setter
	def domainresolveretry(self, domainresolveretry) :
		r"""Time, in seconds, for which the Citrix ADC waits before sending another DNS query to resolve the host name of the syslog server if the last query failed.<br/>Default value: 5<br/>Minimum length =  5<br/>Maximum length =  20939
		"""
		try :
			self._domainresolveretry = domainresolveretry
		except Exception as e:
			raise e

	@property
	def lbvservername(self) :
		r"""Name of the LB vserver. Mutually exclusive with syslog serverIP/serverName.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._lbvservername
		except Exception as e:
			raise e

	@lbvservername.setter
	def lbvservername(self, lbvservername) :
		r"""Name of the LB vserver. Mutually exclusive with syslog serverIP/serverName.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._lbvservername = lbvservername
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port on which the syslog server accepts connections.<br/>Minimum length =  1.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port on which the syslog server accepts connections.<br/>Minimum length =  1
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def loglevel(self) :
		r"""Audit log level, which specifies the types of events to log. 
		Available values function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE.
		"""
		try :
			return self._loglevel
		except Exception as e:
			raise e

	@loglevel.setter
	def loglevel(self, loglevel) :
		r"""Audit log level, which specifies the types of events to log. 
		Available values function as follows: 
		* ALL - All events.
		* EMERGENCY - Events that indicate an immediate crisis on the server.
		* ALERT - Events that might require action.
		* CRITICAL - Events that indicate an imminent server crisis.
		* ERROR - Events that indicate some type of error.
		* WARNING - Events that require action in the near future.
		* NOTICE - Events that the administrator should know about.
		* INFORMATIONAL - All but low-level events.
		* DEBUG - All events, in extreme detail.
		* NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE
		"""
		try :
			self._loglevel = loglevel
		except Exception as e:
			raise e

	@property
	def dateformat(self) :
		r"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY. -U.S. style month/date/year format.
		* DDMMYYYY - European style date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD.
		"""
		try :
			return self._dateformat
		except Exception as e:
			raise e

	@dateformat.setter
	def dateformat(self, dateformat) :
		r"""Format of dates in the logs.
		Supported formats are: 
		* MMDDYYYY. -U.S. style month/date/year format.
		* DDMMYYYY - European style date/month/year format.
		* YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD
		"""
		try :
			self._dateformat = dateformat
		except Exception as e:
			raise e

	@property
	def logfacility(self) :
		r"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the Citrix ADC itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7.
		"""
		try :
			return self._logfacility
		except Exception as e:
			raise e

	@logfacility.setter
	def logfacility(self, logfacility) :
		r"""Facility value, as defined in RFC 3164, assigned to the log message. 
		Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the Citrix ADC itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7
		"""
		try :
			self._logfacility = logfacility
		except Exception as e:
			raise e

	@property
	def tcp(self) :
		r"""Log TCP messages.<br/>Possible values = NONE, ALL.
		"""
		try :
			return self._tcp
		except Exception as e:
			raise e

	@tcp.setter
	def tcp(self, tcp) :
		r"""Log TCP messages.<br/>Possible values = NONE, ALL
		"""
		try :
			self._tcp = tcp
		except Exception as e:
			raise e

	@property
	def acl(self) :
		r"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._acl
		except Exception as e:
			raise e

	@acl.setter
	def acl(self, acl) :
		r"""Log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._acl = acl
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		r"""Time zone used for date and timestamps in the logs. 
		Supported settings are: 
		* GMT_TIME. Coordinated Universal time.
		* LOCAL_TIME. Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		r"""Time zone used for date and timestamps in the logs. 
		Supported settings are: 
		* GMT_TIME. Coordinated Universal time.
		* LOCAL_TIME. Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def userdefinedauditlog(self) :
		r"""Log user-configurable log messages to syslog. 
		Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO.
		"""
		try :
			return self._userdefinedauditlog
		except Exception as e:
			raise e

	@userdefinedauditlog.setter
	def userdefinedauditlog(self, userdefinedauditlog) :
		r"""Log user-configurable log messages to syslog. 
		Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO
		"""
		try :
			self._userdefinedauditlog = userdefinedauditlog
		except Exception as e:
			raise e

	@property
	def appflowexport(self) :
		r"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowexport
		except Exception as e:
			raise e

	@appflowexport.setter
	def appflowexport(self, appflowexport) :
		r"""Export log messages to AppFlow collectors.
		Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowexport = appflowexport
		except Exception as e:
			raise e

	@property
	def lsn(self) :
		r"""Log lsn info.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._lsn
		except Exception as e:
			raise e

	@lsn.setter
	def lsn(self, lsn) :
		r"""Log lsn info.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._lsn = lsn
		except Exception as e:
			raise e

	@property
	def alg(self) :
		r"""Log alg info.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._alg
		except Exception as e:
			raise e

	@alg.setter
	def alg(self, alg) :
		r"""Log alg info.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._alg = alg
		except Exception as e:
			raise e

	@property
	def subscriberlog(self) :
		r"""Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._subscriberlog
		except Exception as e:
			raise e

	@subscriberlog.setter
	def subscriberlog(self, subscriberlog) :
		r"""Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._subscriberlog = subscriberlog
		except Exception as e:
			raise e

	@property
	def transport(self) :
		r"""Transport type used to send auditlogs to syslog server. Default type is UDP.<br/>Possible values = TCP, UDP.
		"""
		try :
			return self._transport
		except Exception as e:
			raise e

	@transport.setter
	def transport(self, transport) :
		r"""Transport type used to send auditlogs to syslog server. Default type is UDP.<br/>Possible values = TCP, UDP
		"""
		try :
			self._transport = transport
		except Exception as e:
			raise e

	@property
	def tcpprofilename(self) :
		r"""Name of the TCP profile whose settings are to be applied to the audit server info to tune the TCP connection parameters.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._tcpprofilename
		except Exception as e:
			raise e

	@tcpprofilename.setter
	def tcpprofilename(self, tcpprofilename) :
		r"""Name of the TCP profile whose settings are to be applied to the audit server info to tune the TCP connection parameters.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._tcpprofilename = tcpprofilename
		except Exception as e:
			raise e

	@property
	def maxlogdatasizetohold(self) :
		r"""Max size of log data that can be held in NSB chain of server info.<br/>Default value: 500<br/>Minimum length =  50<br/>Maximum length =  25600.
		"""
		try :
			return self._maxlogdatasizetohold
		except Exception as e:
			raise e

	@maxlogdatasizetohold.setter
	def maxlogdatasizetohold(self, maxlogdatasizetohold) :
		r"""Max size of log data that can be held in NSB chain of server info.<br/>Default value: 500<br/>Minimum length =  50<br/>Maximum length =  25600
		"""
		try :
			self._maxlogdatasizetohold = maxlogdatasizetohold
		except Exception as e:
			raise e

	@property
	def dns(self) :
		r"""Log DNS related syslog messages.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dns
		except Exception as e:
			raise e

	@dns.setter
	def dns(self, dns) :
		r"""Log DNS related syslog messages.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dns = dns
		except Exception as e:
			raise e

	@property
	def contentinspectionlog(self) :
		r"""Log Content Inspection event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._contentinspectionlog
		except Exception as e:
			raise e

	@contentinspectionlog.setter
	def contentinspectionlog(self, contentinspectionlog) :
		r"""Log Content Inspection event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._contentinspectionlog = contentinspectionlog
		except Exception as e:
			raise e

	@property
	def netprofile(self) :
		r"""Name of the network profile.
		The SNIP configured in the network profile will be used as source IP while sending log messages.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._netprofile
		except Exception as e:
			raise e

	@netprofile.setter
	def netprofile(self, netprofile) :
		r"""Name of the network profile.
		The SNIP configured in the network profile will be used as source IP while sending log messages.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._netprofile = netprofile
		except Exception as e:
			raise e

	@property
	def sslinterception(self) :
		r"""Log SSL Interception event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslinterception
		except Exception as e:
			raise e

	@sslinterception.setter
	def sslinterception(self, sslinterception) :
		r"""Log SSL Interception event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslinterception = sslinterception
		except Exception as e:
			raise e

	@property
	def urlfiltering(self) :
		r"""Log URL filtering event information.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._urlfiltering
		except Exception as e:
			raise e

	@urlfiltering.setter
	def urlfiltering(self, urlfiltering) :
		r"""Log URL filtering event information.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._urlfiltering = urlfiltering
		except Exception as e:
			raise e

	@property
	def domainresolvenow(self) :
		r"""Immediately send a DNS query to resolve the server's domain name.
		"""
		try :
			return self._domainresolvenow
		except Exception as e:
			raise e

	@domainresolvenow.setter
	def domainresolvenow(self, domainresolvenow) :
		r"""Immediately send a DNS query to resolve the server's domain name.
		"""
		try :
			self._domainresolvenow = domainresolvenow
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""The resolved IP address of the syslog server.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(auditsyslogaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.auditsyslogaction
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
		addresource = auditsyslogaction()
		addresource.name = resource.name
		addresource.serverip = resource.serverip
		addresource.serverdomainname = resource.serverdomainname
		addresource.domainresolveretry = resource.domainresolveretry
		addresource.lbvservername = resource.lbvservername
		addresource.serverport = resource.serverport
		addresource.loglevel = resource.loglevel
		addresource.dateformat = resource.dateformat
		addresource.logfacility = resource.logfacility
		addresource.tcp = resource.tcp
		addresource.acl = resource.acl
		addresource.timezone = resource.timezone
		addresource.userdefinedauditlog = resource.userdefinedauditlog
		addresource.appflowexport = resource.appflowexport
		addresource.lsn = resource.lsn
		addresource.alg = resource.alg
		addresource.subscriberlog = resource.subscriberlog
		addresource.transport = resource.transport
		addresource.tcpprofilename = resource.tcpprofilename
		addresource.maxlogdatasizetohold = resource.maxlogdatasizetohold
		addresource.dns = resource.dns
		addresource.contentinspectionlog = resource.contentinspectionlog
		addresource.netprofile = resource.netprofile
		addresource.sslinterception = resource.sslinterception
		addresource.urlfiltering = resource.urlfiltering
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add auditsyslogaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ auditsyslogaction() for _ in range(len(resource))]
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
		deleteresource = auditsyslogaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete auditsyslogaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = auditsyslogaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditsyslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ auditsyslogaction() for _ in range(len(resource))]
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
		updateresource = auditsyslogaction()
		updateresource.name = resource.name
		updateresource.serverip = resource.serverip
		updateresource.serverdomainname = resource.serverdomainname
		updateresource.lbvservername = resource.lbvservername
		updateresource.domainresolveretry = resource.domainresolveretry
		updateresource.domainresolvenow = resource.domainresolvenow
		updateresource.serverport = resource.serverport
		updateresource.loglevel = resource.loglevel
		updateresource.dateformat = resource.dateformat
		updateresource.logfacility = resource.logfacility
		updateresource.tcp = resource.tcp
		updateresource.acl = resource.acl
		updateresource.timezone = resource.timezone
		updateresource.userdefinedauditlog = resource.userdefinedauditlog
		updateresource.appflowexport = resource.appflowexport
		updateresource.lsn = resource.lsn
		updateresource.alg = resource.alg
		updateresource.subscriberlog = resource.subscriberlog
		updateresource.tcpprofilename = resource.tcpprofilename
		updateresource.maxlogdatasizetohold = resource.maxlogdatasizetohold
		updateresource.dns = resource.dns
		updateresource.contentinspectionlog = resource.contentinspectionlog
		updateresource.netprofile = resource.netprofile
		updateresource.sslinterception = resource.sslinterception
		updateresource.urlfiltering = resource.urlfiltering
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update auditsyslogaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ auditsyslogaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of auditsyslogaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = auditsyslogaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditsyslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ auditsyslogaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the auditsyslogaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = auditsyslogaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = auditsyslogaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [auditsyslogaction() for _ in range(len(name))]
						obj = [auditsyslogaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = auditsyslogaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of auditsyslogaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditsyslogaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the auditsyslogaction resources configured on NetScaler.
		"""
		try :
			obj = auditsyslogaction()
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
		r""" Use this API to count filtered the set of auditsyslogaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = auditsyslogaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Timezone:
		GMT_TIME = "GMT_TIME"
		LOCAL_TIME = "LOCAL_TIME"

	class Acl:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Subscriberlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Logfacility:
		LOCAL0 = "LOCAL0"
		LOCAL1 = "LOCAL1"
		LOCAL2 = "LOCAL2"
		LOCAL3 = "LOCAL3"
		LOCAL4 = "LOCAL4"
		LOCAL5 = "LOCAL5"
		LOCAL6 = "LOCAL6"
		LOCAL7 = "LOCAL7"

	class Transport:
		TCP = "TCP"
		UDP = "UDP"

	class Sslinterception:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Urlfiltering:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dns:
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

	class Contentinspectionlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Userdefinedauditlog:
		YES = "YES"
		NO = "NO"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Dateformat:
		MMDDYYYY = "MMDDYYYY"
		DDMMYYYY = "DDMMYYYY"
		YYYYMMDD = "YYYYMMDD"

	class Lsn:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Alg:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Loglevel:
		ALL = "ALL"
		EMERGENCY = "EMERGENCY"
		ALERT = "ALERT"
		CRITICAL = "CRITICAL"
		ERROR = "ERROR"
		WARNING = "WARNING"
		NOTICE = "NOTICE"
		INFORMATIONAL = "INFORMATIONAL"
		DEBUG = "DEBUG"
		NONE = "NONE"

	class Tcp:
		NONE = "NONE"
		ALL = "ALL"

	class Appflowexport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class auditsyslogaction_response(base_response) :
	def __init__(self, length=1) :
		self.auditsyslogaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.auditsyslogaction = [auditsyslogaction() for _ in range(length)]

