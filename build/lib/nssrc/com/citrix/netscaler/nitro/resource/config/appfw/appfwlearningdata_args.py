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


class appfwlearningdata_args :
	r""" Provides additional arguments required for fetching the appfwlearningdata resource.
	"""
	def __init__(self) :
		self._profilename = None
		self._securitycheck = None

	@property
	def profilename(self) :
		r"""Name of the profile.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		r"""Name of the profile.
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def securitycheck(self) :
		r"""Name of the security check.<br/>Possible values = startURL, cookieConsistency, fieldConsistency, crossSiteScripting, SQLInjection, fieldFormat, CSRFtag, XMLDoSCheck, XMLWSICheck, XMLAttachmentCheck, TotalXMLRequests, creditCardNumber, ContentType.
		"""
		try :
			return self._securitycheck
		except Exception as e:
			raise e

	@securitycheck.setter
	def securitycheck(self, securitycheck) :
		r"""Name of the security check.<br/>Possible values = startURL, cookieConsistency, fieldConsistency, crossSiteScripting, SQLInjection, fieldFormat, CSRFtag, XMLDoSCheck, XMLWSICheck, XMLAttachmentCheck, TotalXMLRequests, creditCardNumber, ContentType
		"""
		try :
			self._securitycheck = securitycheck
		except Exception as e:
			raise e

	class Securitycheck:
		startURL = "startURL"
		cookieConsistency = "cookieConsistency"
		fieldConsistency = "fieldConsistency"
		crossSiteScripting = "crossSiteScripting"
		SQLInjection = "SQLInjection"
		fieldFormat = "fieldFormat"
		CSRFtag = "CSRFtag"
		XMLDoSCheck = "XMLDoSCheck"
		XMLWSICheck = "XMLWSICheck"
		XMLAttachmentCheck = "XMLAttachmentCheck"
		TotalXMLRequests = "TotalXMLRequests"
		creditCardNumber = "creditCardNumber"
		ContentType = "ContentType"

