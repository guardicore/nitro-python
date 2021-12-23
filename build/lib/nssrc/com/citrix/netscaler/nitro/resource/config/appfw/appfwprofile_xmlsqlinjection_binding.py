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

class appfwprofile_xmlsqlinjection_binding(base_resource) :
	""" Binding class showing the xmlsqlinjection that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._xmlsqlinjection = None
		self._isregex_xmlsql = None
		self._as_scan_location_xmlsql = None
		self._state = None
		self._comment = None
		self._isautodeployed = None
		self._alertonly = None
		self._name = None
		self._resourceid = None
		self._ruletype = None
		self.___count = None

	@property
	def as_scan_location_xmlsql(self) :
		r"""Location of SQL injection exception - XML Element or Attribute.<br/>Possible values = ELEMENT, ATTRIBUTE.
		"""
		try :
			return self._as_scan_location_xmlsql
		except Exception as e:
			raise e

	@as_scan_location_xmlsql.setter
	def as_scan_location_xmlsql(self, as_scan_location_xmlsql) :
		r"""Location of SQL injection exception - XML Element or Attribute.<br/>Possible values = ELEMENT, ATTRIBUTE
		"""
		try :
			self._as_scan_location_xmlsql = as_scan_location_xmlsql
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def resourceid(self) :
		r"""A "id" that identifies the rule.
		"""
		try :
			return self._resourceid
		except Exception as e:
			raise e

	@resourceid.setter
	def resourceid(self, resourceid) :
		r"""A "id" that identifies the rule.
		"""
		try :
			self._resourceid = resourceid
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def xmlsqlinjection(self) :
		r"""Exempt the specified URL from the XML SQL injection check. 
		An XML SQL injection exemption (relaxation) consists of the following items:
		* Name. Name to exempt, as a string or a PCRE-format regular expression.
		* ISREGEX flag. REGEX if URL is a regular expression, NOTREGEX if URL is a fixed string.
		* Location. ELEMENT if the injection is located in an XML element, ATTRIBUTE if located in an XML attribute.
		"""
		try :
			return self._xmlsqlinjection
		except Exception as e:
			raise e

	@xmlsqlinjection.setter
	def xmlsqlinjection(self, xmlsqlinjection) :
		r"""Exempt the specified URL from the XML SQL injection check. 
		An XML SQL injection exemption (relaxation) consists of the following items:
		* Name. Name to exempt, as a string or a PCRE-format regular expression.
		* ISREGEX flag. REGEX if URL is a regular expression, NOTREGEX if URL is a fixed string.
		* Location. ELEMENT if the injection is located in an XML element, ATTRIBUTE if located in an XML attribute.
		"""
		try :
			self._xmlsqlinjection = xmlsqlinjection
		except Exception as e:
			raise e

	@property
	def alertonly(self) :
		r"""Send SNMP alert?.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._alertonly
		except Exception as e:
			raise e

	@alertonly.setter
	def alertonly(self, alertonly) :
		r"""Send SNMP alert?.<br/>Possible values = ON, OFF
		"""
		try :
			self._alertonly = alertonly
		except Exception as e:
			raise e

	@property
	def isregex_xmlsql(self) :
		r"""Is the XML SQL Injection exempted field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX.
		"""
		try :
			return self._isregex_xmlsql
		except Exception as e:
			raise e

	@isregex_xmlsql.setter
	def isregex_xmlsql(self, isregex_xmlsql) :
		r"""Is the XML SQL Injection exempted field name a regular expression?.<br/>Possible values = REGEX, NOTREGEX
		"""
		try :
			self._isregex_xmlsql = isregex_xmlsql
		except Exception as e:
			raise e

	@property
	def ruletype(self) :
		r"""Specifies rule type of binding.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._ruletype
		except Exception as e:
			raise e

	@ruletype.setter
	def ruletype(self, ruletype) :
		r"""Specifies rule type of binding.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._ruletype = ruletype
		except Exception as e:
			raise e

	@property
	def isautodeployed(self) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED.
		"""
		try :
			return self._isautodeployed
		except Exception as e:
			raise e

	@isautodeployed.setter
	def isautodeployed(self, isautodeployed) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED
		"""
		try :
			self._isautodeployed = isautodeployed
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_xmlsqlinjection_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_xmlsqlinjection_binding
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
		addresource = appfwprofile_xmlsqlinjection_binding()
		addresource.name = resource.name
		addresource.comment = resource.comment
		addresource.state = resource.state
		addresource.xmlsqlinjection = resource.xmlsqlinjection
		addresource.isregex_xmlsql = resource.isregex_xmlsql
		addresource.as_scan_location_xmlsql = resource.as_scan_location_xmlsql
		addresource.isautodeployed = resource.isautodeployed
		addresource.resourceid = resource.resourceid
		addresource.ruletype = resource.ruletype
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_xmlsqlinjection_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = appfwprofile_xmlsqlinjection_binding()
		deleteresource.name = resource.name
		deleteresource.xmlsqlinjection = resource.xmlsqlinjection
		deleteresource.as_scan_location_xmlsql = resource.as_scan_location_xmlsql
		deleteresource.ruletype = resource.ruletype
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_xmlsqlinjection_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch appfwprofile_xmlsqlinjection_binding resources.
		"""
		try :
			if not name :
				obj = appfwprofile_xmlsqlinjection_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = appfwprofile_xmlsqlinjection_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of appfwprofile_xmlsqlinjection_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmlsqlinjection_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count appfwprofile_xmlsqlinjection_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_xmlsqlinjection_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of appfwprofile_xmlsqlinjection_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmlsqlinjection_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Jsonmaxarraylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlsql:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxelementdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxdocumentlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattachmentsizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class As_value_type_cmd:
		Keyword = "Keyword"
		SpecialString = "SpecialString"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementchildrencheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxobjectkeylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxentityexpansionscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"
		URL = "URL"

	class Alertonly:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_cmd:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isvalueregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Filetype:
		pdf = "pdf"
		msdoc = "msdoc"
		text = "text"
		image = "image"
		any = "any"

	class Jsonmaxobjectkeycountcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_cmd:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnodescheck:
		ON = "ON"
		OFF = "OFF"

	class Ruletype:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class Xmlmaxchardatalengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlminfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_cmd:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Jsonmaxstringlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_value_type_sql:
		Keyword = "Keyword"
		SpecialString = "SpecialString"
		Wildchar = "Wildchar"

	class Isregex_fileuploadtypes_url:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isregex_xmlxss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmladditionalsoapheaders:
		ON = "ON"
		OFF = "OFF"

	class Isautodeployed:
		AUTODEPLOYED = "AUTODEPLOYED"
		NOTAUTODEPLOYED = "NOTAUTODEPLOYED"

	class Xmlmaxattributescheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxcontainerdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Action:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"
		xout = "xout"

	class As_value_type_xss:
		Tag = "Tag"
		Attribute = "Attribute"
		Pattern = "Pattern"

	class Xmlblockexternalentities:
		ON = "ON"
		OFF = "OFF"

class appfwprofile_xmlsqlinjection_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_xmlsqlinjection_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_xmlsqlinjection_binding = [appfwprofile_xmlsqlinjection_binding() for _ in range(length)]

