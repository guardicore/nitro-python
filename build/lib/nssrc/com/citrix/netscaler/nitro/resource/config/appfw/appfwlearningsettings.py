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

class appfwlearningsettings(base_resource) :
	""" Configuration for learning settings resource. """
	def __init__(self) :
		self._profilename = None
		self._starturlminthreshold = None
		self._starturlpercentthreshold = None
		self._cookieconsistencyminthreshold = None
		self._cookieconsistencypercentthreshold = None
		self._csrftagminthreshold = None
		self._csrftagpercentthreshold = None
		self._fieldconsistencyminthreshold = None
		self._fieldconsistencypercentthreshold = None
		self._crosssitescriptingminthreshold = None
		self._crosssitescriptingpercentthreshold = None
		self._sqlinjectionminthreshold = None
		self._sqlinjectionpercentthreshold = None
		self._fieldformatminthreshold = None
		self._fieldformatpercentthreshold = None
		self._creditcardnumberminthreshold = None
		self._creditcardnumberpercentthreshold = None
		self._contenttypeminthreshold = None
		self._contenttypepercentthreshold = None
		self._xmlwsiminthreshold = None
		self._xmlwsipercentthreshold = None
		self._xmlattachmentminthreshold = None
		self._xmlattachmentpercentthreshold = None
		self._fieldformatautodeploygraceperiod = None
		self._sqlinjectionautodeploygraceperiod = None
		self._crosssitescriptingautodeploygraceperiod = None
		self._starturlautodeploygraceperiod = None
		self._cookieconsistencyautodeploygraceperiod = None
		self._csrftagautodeploygraceperiod = None
		self._fieldconsistencyautodeploygraceperiod = None
		self._contenttypeautodeploygraceperiod = None
		self.___count = None

	@property
	def profilename(self) :
		r"""Name of the profile.<br/>Minimum length =  1.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		r"""Name of the profile.<br/>Minimum length =  1
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def starturlminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn start URLs.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._starturlminthreshold
		except Exception as e:
			raise e

	@starturlminthreshold.setter
	def starturlminthreshold(self, starturlminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn start URLs.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._starturlminthreshold = starturlminthreshold
		except Exception as e:
			raise e

	@property
	def starturlpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular start URL pattern for the learning engine to learn that start URL.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._starturlpercentthreshold
		except Exception as e:
			raise e

	@starturlpercentthreshold.setter
	def starturlpercentthreshold(self, starturlpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular start URL pattern for the learning engine to learn that start URL.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._starturlpercentthreshold = starturlpercentthreshold
		except Exception as e:
			raise e

	@property
	def cookieconsistencyminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn cookies.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._cookieconsistencyminthreshold
		except Exception as e:
			raise e

	@cookieconsistencyminthreshold.setter
	def cookieconsistencyminthreshold(self, cookieconsistencyminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn cookies.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._cookieconsistencyminthreshold = cookieconsistencyminthreshold
		except Exception as e:
			raise e

	@property
	def cookieconsistencypercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular cookie pattern for the learning engine to learn that cookie.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._cookieconsistencypercentthreshold
		except Exception as e:
			raise e

	@cookieconsistencypercentthreshold.setter
	def cookieconsistencypercentthreshold(self, cookieconsistencypercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular cookie pattern for the learning engine to learn that cookie.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._cookieconsistencypercentthreshold = cookieconsistencypercentthreshold
		except Exception as e:
			raise e

	@property
	def csrftagminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn cross-site request forgery (CSRF) tags.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._csrftagminthreshold
		except Exception as e:
			raise e

	@csrftagminthreshold.setter
	def csrftagminthreshold(self, csrftagminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn cross-site request forgery (CSRF) tags.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._csrftagminthreshold = csrftagminthreshold
		except Exception as e:
			raise e

	@property
	def csrftagpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular CSRF tag for the learning engine to learn that CSRF tag.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._csrftagpercentthreshold
		except Exception as e:
			raise e

	@csrftagpercentthreshold.setter
	def csrftagpercentthreshold(self, csrftagpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular CSRF tag for the learning engine to learn that CSRF tag.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._csrftagpercentthreshold = csrftagpercentthreshold
		except Exception as e:
			raise e

	@property
	def fieldconsistencyminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn field consistency information.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._fieldconsistencyminthreshold
		except Exception as e:
			raise e

	@fieldconsistencyminthreshold.setter
	def fieldconsistencyminthreshold(self, fieldconsistencyminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn field consistency information.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._fieldconsistencyminthreshold = fieldconsistencyminthreshold
		except Exception as e:
			raise e

	@property
	def fieldconsistencypercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular field consistency pattern for the learning engine to learn that field consistency pattern.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._fieldconsistencypercentthreshold
		except Exception as e:
			raise e

	@fieldconsistencypercentthreshold.setter
	def fieldconsistencypercentthreshold(self, fieldconsistencypercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular field consistency pattern for the learning engine to learn that field consistency pattern.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._fieldconsistencypercentthreshold = fieldconsistencypercentthreshold
		except Exception as e:
			raise e

	@property
	def crosssitescriptingminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn HTML cross-site scripting patterns.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._crosssitescriptingminthreshold
		except Exception as e:
			raise e

	@crosssitescriptingminthreshold.setter
	def crosssitescriptingminthreshold(self, crosssitescriptingminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn HTML cross-site scripting patterns.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._crosssitescriptingminthreshold = crosssitescriptingminthreshold
		except Exception as e:
			raise e

	@property
	def crosssitescriptingpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular cross-site scripting pattern for the learning engine to learn that cross-site scripting pattern.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._crosssitescriptingpercentthreshold
		except Exception as e:
			raise e

	@crosssitescriptingpercentthreshold.setter
	def crosssitescriptingpercentthreshold(self, crosssitescriptingpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular cross-site scripting pattern for the learning engine to learn that cross-site scripting pattern.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._crosssitescriptingpercentthreshold = crosssitescriptingpercentthreshold
		except Exception as e:
			raise e

	@property
	def sqlinjectionminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn HTML SQL injection patterns.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._sqlinjectionminthreshold
		except Exception as e:
			raise e

	@sqlinjectionminthreshold.setter
	def sqlinjectionminthreshold(self, sqlinjectionminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn HTML SQL injection patterns.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._sqlinjectionminthreshold = sqlinjectionminthreshold
		except Exception as e:
			raise e

	@property
	def sqlinjectionpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular HTML SQL injection pattern for the learning engine to learn that HTML SQL injection pattern.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._sqlinjectionpercentthreshold
		except Exception as e:
			raise e

	@sqlinjectionpercentthreshold.setter
	def sqlinjectionpercentthreshold(self, sqlinjectionpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular HTML SQL injection pattern for the learning engine to learn that HTML SQL injection pattern.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._sqlinjectionpercentthreshold = sqlinjectionpercentthreshold
		except Exception as e:
			raise e

	@property
	def fieldformatminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn field formats.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._fieldformatminthreshold
		except Exception as e:
			raise e

	@fieldformatminthreshold.setter
	def fieldformatminthreshold(self, fieldformatminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn field formats.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._fieldformatminthreshold = fieldformatminthreshold
		except Exception as e:
			raise e

	@property
	def fieldformatpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular web form field pattern for the learning engine to recommend a field format for that form field.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._fieldformatpercentthreshold
		except Exception as e:
			raise e

	@fieldformatpercentthreshold.setter
	def fieldformatpercentthreshold(self, fieldformatpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular web form field pattern for the learning engine to recommend a field format for that form field.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._fieldformatpercentthreshold = fieldformatpercentthreshold
		except Exception as e:
			raise e

	@property
	def creditcardnumberminthreshold(self) :
		r"""Minimum threshold to learn Credit Card information.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._creditcardnumberminthreshold
		except Exception as e:
			raise e

	@creditcardnumberminthreshold.setter
	def creditcardnumberminthreshold(self, creditcardnumberminthreshold) :
		r"""Minimum threshold to learn Credit Card information.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._creditcardnumberminthreshold = creditcardnumberminthreshold
		except Exception as e:
			raise e

	@property
	def creditcardnumberpercentthreshold(self) :
		r"""Minimum threshold in percent to learn Credit Card information.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._creditcardnumberpercentthreshold
		except Exception as e:
			raise e

	@creditcardnumberpercentthreshold.setter
	def creditcardnumberpercentthreshold(self, creditcardnumberpercentthreshold) :
		r"""Minimum threshold in percent to learn Credit Card information.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._creditcardnumberpercentthreshold = creditcardnumberpercentthreshold
		except Exception as e:
			raise e

	@property
	def contenttypeminthreshold(self) :
		r"""Minimum threshold to learn Content Type information.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._contenttypeminthreshold
		except Exception as e:
			raise e

	@contenttypeminthreshold.setter
	def contenttypeminthreshold(self, contenttypeminthreshold) :
		r"""Minimum threshold to learn Content Type information.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._contenttypeminthreshold = contenttypeminthreshold
		except Exception as e:
			raise e

	@property
	def contenttypepercentthreshold(self) :
		r"""Minimum threshold in percent to learn Content Type information.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._contenttypepercentthreshold
		except Exception as e:
			raise e

	@contenttypepercentthreshold.setter
	def contenttypepercentthreshold(self, contenttypepercentthreshold) :
		r"""Minimum threshold in percent to learn Content Type information.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._contenttypepercentthreshold = contenttypepercentthreshold
		except Exception as e:
			raise e

	@property
	def xmlwsiminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn web services interoperability (WSI) information.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._xmlwsiminthreshold
		except Exception as e:
			raise e

	@xmlwsiminthreshold.setter
	def xmlwsiminthreshold(self, xmlwsiminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn web services interoperability (WSI) information.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._xmlwsiminthreshold = xmlwsiminthreshold
		except Exception as e:
			raise e

	@property
	def xmlwsipercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular pattern for the learning engine to learn a web services interoperability (WSI) pattern.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._xmlwsipercentthreshold
		except Exception as e:
			raise e

	@xmlwsipercentthreshold.setter
	def xmlwsipercentthreshold(self, xmlwsipercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular pattern for the learning engine to learn a web services interoperability (WSI) pattern.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._xmlwsipercentthreshold = xmlwsipercentthreshold
		except Exception as e:
			raise e

	@property
	def xmlattachmentminthreshold(self) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn XML attachment patterns.<br/>Default value: 1<br/>Minimum length =  1.
		"""
		try :
			return self._xmlattachmentminthreshold
		except Exception as e:
			raise e

	@xmlattachmentminthreshold.setter
	def xmlattachmentminthreshold(self, xmlattachmentminthreshold) :
		r"""Minimum number of application firewall sessions that the learning engine must observe to learn XML attachment patterns.<br/>Default value: 1<br/>Minimum length =  1
		"""
		try :
			self._xmlattachmentminthreshold = xmlattachmentminthreshold
		except Exception as e:
			raise e

	@property
	def xmlattachmentpercentthreshold(self) :
		r"""Minimum percentage of application firewall sessions that must contain a particular XML attachment pattern for the learning engine to learn that XML attachment pattern.<br/>Default value: 0<br/>Maximum length =  100.
		"""
		try :
			return self._xmlattachmentpercentthreshold
		except Exception as e:
			raise e

	@xmlattachmentpercentthreshold.setter
	def xmlattachmentpercentthreshold(self, xmlattachmentpercentthreshold) :
		r"""Minimum percentage of application firewall sessions that must contain a particular XML attachment pattern for the learning engine to learn that XML attachment pattern.<br/>Default value: 0<br/>Maximum length =  100
		"""
		try :
			self._xmlattachmentpercentthreshold = xmlattachmentpercentthreshold
		except Exception as e:
			raise e

	@property
	def fieldformatautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._fieldformatautodeploygraceperiod
		except Exception as e:
			raise e

	@fieldformatautodeploygraceperiod.setter
	def fieldformatautodeploygraceperiod(self, fieldformatautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._fieldformatautodeploygraceperiod = fieldformatautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def sqlinjectionautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._sqlinjectionautodeploygraceperiod
		except Exception as e:
			raise e

	@sqlinjectionautodeploygraceperiod.setter
	def sqlinjectionautodeploygraceperiod(self, sqlinjectionautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._sqlinjectionautodeploygraceperiod = sqlinjectionautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def crosssitescriptingautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._crosssitescriptingautodeploygraceperiod
		except Exception as e:
			raise e

	@crosssitescriptingautodeploygraceperiod.setter
	def crosssitescriptingautodeploygraceperiod(self, crosssitescriptingautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._crosssitescriptingautodeploygraceperiod = crosssitescriptingautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def starturlautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._starturlautodeploygraceperiod
		except Exception as e:
			raise e

	@starturlautodeploygraceperiod.setter
	def starturlautodeploygraceperiod(self, starturlautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._starturlautodeploygraceperiod = starturlautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def cookieconsistencyautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._cookieconsistencyautodeploygraceperiod
		except Exception as e:
			raise e

	@cookieconsistencyautodeploygraceperiod.setter
	def cookieconsistencyautodeploygraceperiod(self, cookieconsistencyautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._cookieconsistencyautodeploygraceperiod = cookieconsistencyautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def csrftagautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._csrftagautodeploygraceperiod
		except Exception as e:
			raise e

	@csrftagautodeploygraceperiod.setter
	def csrftagautodeploygraceperiod(self, csrftagautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._csrftagautodeploygraceperiod = csrftagautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def fieldconsistencyautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._fieldconsistencyautodeploygraceperiod
		except Exception as e:
			raise e

	@fieldconsistencyautodeploygraceperiod.setter
	def fieldconsistencyautodeploygraceperiod(self, fieldconsistencyautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._fieldconsistencyautodeploygraceperiod = fieldconsistencyautodeploygraceperiod
		except Exception as e:
			raise e

	@property
	def contenttypeautodeploygraceperiod(self) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200.
		"""
		try :
			return self._contenttypeautodeploygraceperiod
		except Exception as e:
			raise e

	@contenttypeautodeploygraceperiod.setter
	def contenttypeautodeploygraceperiod(self, contenttypeautodeploygraceperiod) :
		r"""The number of minutes after the threshold hit alert the learned rule will be deployed.<br/>Default value: 10080<br/>Minimum length =  5<br/>Maximum length =  43200
		"""
		try :
			self._contenttypeautodeploygraceperiod = contenttypeautodeploygraceperiod
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwlearningsettings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwlearningsettings
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.profilename is not None :
				return str(self.profilename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = appfwlearningsettings()
		updateresource.profilename = resource.profilename
		updateresource.starturlminthreshold = resource.starturlminthreshold
		updateresource.starturlpercentthreshold = resource.starturlpercentthreshold
		updateresource.cookieconsistencyminthreshold = resource.cookieconsistencyminthreshold
		updateresource.cookieconsistencypercentthreshold = resource.cookieconsistencypercentthreshold
		updateresource.csrftagminthreshold = resource.csrftagminthreshold
		updateresource.csrftagpercentthreshold = resource.csrftagpercentthreshold
		updateresource.fieldconsistencyminthreshold = resource.fieldconsistencyminthreshold
		updateresource.fieldconsistencypercentthreshold = resource.fieldconsistencypercentthreshold
		updateresource.crosssitescriptingminthreshold = resource.crosssitescriptingminthreshold
		updateresource.crosssitescriptingpercentthreshold = resource.crosssitescriptingpercentthreshold
		updateresource.sqlinjectionminthreshold = resource.sqlinjectionminthreshold
		updateresource.sqlinjectionpercentthreshold = resource.sqlinjectionpercentthreshold
		updateresource.fieldformatminthreshold = resource.fieldformatminthreshold
		updateresource.fieldformatpercentthreshold = resource.fieldformatpercentthreshold
		updateresource.creditcardnumberminthreshold = resource.creditcardnumberminthreshold
		updateresource.creditcardnumberpercentthreshold = resource.creditcardnumberpercentthreshold
		updateresource.contenttypeminthreshold = resource.contenttypeminthreshold
		updateresource.contenttypepercentthreshold = resource.contenttypepercentthreshold
		updateresource.xmlwsiminthreshold = resource.xmlwsiminthreshold
		updateresource.xmlwsipercentthreshold = resource.xmlwsipercentthreshold
		updateresource.xmlattachmentminthreshold = resource.xmlattachmentminthreshold
		updateresource.xmlattachmentpercentthreshold = resource.xmlattachmentpercentthreshold
		updateresource.fieldformatautodeploygraceperiod = resource.fieldformatautodeploygraceperiod
		updateresource.sqlinjectionautodeploygraceperiod = resource.sqlinjectionautodeploygraceperiod
		updateresource.crosssitescriptingautodeploygraceperiod = resource.crosssitescriptingautodeploygraceperiod
		updateresource.starturlautodeploygraceperiod = resource.starturlautodeploygraceperiod
		updateresource.cookieconsistencyautodeploygraceperiod = resource.cookieconsistencyautodeploygraceperiod
		updateresource.csrftagautodeploygraceperiod = resource.csrftagautodeploygraceperiod
		updateresource.fieldconsistencyautodeploygraceperiod = resource.fieldconsistencyautodeploygraceperiod
		updateresource.contenttypeautodeploygraceperiod = resource.contenttypeautodeploygraceperiod
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update appfwlearningsettings.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ appfwlearningsettings() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of appfwlearningsettings resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = appfwlearningsettings()
				if type(resource) !=  type(unsetresource):
					unsetresource.profilename = resource
				else :
					unsetresource.profilename = resource.profilename
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ appfwlearningsettings() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].profilename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ appfwlearningsettings() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].profilename = resource[i].profilename
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the appfwlearningsettings resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = appfwlearningsettings()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = appfwlearningsettings()
					obj.profilename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [appfwlearningsettings() for _ in range(len(name))]
						obj = [appfwlearningsettings() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = appfwlearningsettings()
							obj[i].profilename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of appfwlearningsettings resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwlearningsettings()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the appfwlearningsettings resources configured on NetScaler.
		"""
		try :
			obj = appfwlearningsettings()
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
		r""" Use this API to count filtered the set of appfwlearningsettings resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwlearningsettings()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class appfwlearningsettings_response(base_response) :
	def __init__(self, length=1) :
		self.appfwlearningsettings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwlearningsettings = [appfwlearningsettings() for _ in range(length)]

