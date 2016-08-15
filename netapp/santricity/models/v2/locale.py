# coding: utf-8

"""
Locale.py

 The Clear BSD License

 Copyright (c) – 2016, NetApp, Inc. All rights reserved.

 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the limitations in the disclaimer below) provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

 * Neither the name of NetApp, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from pprint import pformat
from six import iteritems


class Locale(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Locale - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'language': 'str',  
            'country': 'str',  
            'display_country': 'str',  
            'display_language': 'str',  
            'display_name': 'str',  
            'display_script': 'str',  
            'display_variant': 'str',  
            'extension_keys': 'list[str]',  
            'iso3_country': 'str',  
            'iso3_language': 'str',  
            'script': 'str',  
            'unicode_locale_attributes': 'list[str]',  
            'unicode_locale_keys': 'list[str]',  
            'variant': 'str'
        }

        self.attribute_map = {
            'language': 'language',  
            'country': 'country',  
            'display_country': 'displayCountry',  
            'display_language': 'displayLanguage',  
            'display_name': 'displayName',  
            'display_script': 'displayScript',  
            'display_variant': 'displayVariant',  
            'extension_keys': 'extensionKeys',  
            'iso3_country': 'iso3Country',  
            'iso3_language': 'iso3Language',  
            'script': 'script',  
            'unicode_locale_attributes': 'unicodeLocaleAttributes',  
            'unicode_locale_keys': 'unicodeLocaleKeys',  
            'variant': 'variant'
        }

        self._language = None
        self._country = None
        self._display_country = None
        self._display_language = None
        self._display_name = None
        self._display_script = None
        self._display_variant = None
        self._extension_keys = None
        self._iso3_country = None
        self._iso3_language = None
        self._script = None
        self._unicode_locale_attributes = None
        self._unicode_locale_keys = None
        self._variant = None

    @property
    def language(self):
        """
        Gets the language of this Locale.


        :return: The language of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this Locale.


        :param language: The language of this Locale.
        :type: str
        """
        self._language = language

    @property
    def country(self):
        """
        Gets the country of this Locale.


        :return: The country of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Locale.


        :param country: The country of this Locale.
        :type: str
        """
        self._country = country

    @property
    def display_country(self):
        """
        Gets the display_country of this Locale.


        :return: The display_country of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._display_country

    @display_country.setter
    def display_country(self, display_country):
        """
        Sets the display_country of this Locale.


        :param display_country: The display_country of this Locale.
        :type: str
        """
        self._display_country = display_country

    @property
    def display_language(self):
        """
        Gets the display_language of this Locale.


        :return: The display_language of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._display_language

    @display_language.setter
    def display_language(self, display_language):
        """
        Sets the display_language of this Locale.


        :param display_language: The display_language of this Locale.
        :type: str
        """
        self._display_language = display_language

    @property
    def display_name(self):
        """
        Gets the display_name of this Locale.


        :return: The display_name of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Locale.


        :param display_name: The display_name of this Locale.
        :type: str
        """
        self._display_name = display_name

    @property
    def display_script(self):
        """
        Gets the display_script of this Locale.


        :return: The display_script of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._display_script

    @display_script.setter
    def display_script(self, display_script):
        """
        Sets the display_script of this Locale.


        :param display_script: The display_script of this Locale.
        :type: str
        """
        self._display_script = display_script

    @property
    def display_variant(self):
        """
        Gets the display_variant of this Locale.


        :return: The display_variant of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._display_variant

    @display_variant.setter
    def display_variant(self, display_variant):
        """
        Sets the display_variant of this Locale.


        :param display_variant: The display_variant of this Locale.
        :type: str
        """
        self._display_variant = display_variant

    @property
    def extension_keys(self):
        """
        Gets the extension_keys of this Locale.


        :return: The extension_keys of this Locale.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._extension_keys

    @extension_keys.setter
    def extension_keys(self, extension_keys):
        """
        Sets the extension_keys of this Locale.


        :param extension_keys: The extension_keys of this Locale.
        :type: list[str]
        """
        self._extension_keys = extension_keys

    @property
    def iso3_country(self):
        """
        Gets the iso3_country of this Locale.


        :return: The iso3_country of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._iso3_country

    @iso3_country.setter
    def iso3_country(self, iso3_country):
        """
        Sets the iso3_country of this Locale.


        :param iso3_country: The iso3_country of this Locale.
        :type: str
        """
        self._iso3_country = iso3_country

    @property
    def iso3_language(self):
        """
        Gets the iso3_language of this Locale.


        :return: The iso3_language of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._iso3_language

    @iso3_language.setter
    def iso3_language(self, iso3_language):
        """
        Sets the iso3_language of this Locale.


        :param iso3_language: The iso3_language of this Locale.
        :type: str
        """
        self._iso3_language = iso3_language

    @property
    def script(self):
        """
        Gets the script of this Locale.


        :return: The script of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._script

    @script.setter
    def script(self, script):
        """
        Sets the script of this Locale.


        :param script: The script of this Locale.
        :type: str
        """
        self._script = script

    @property
    def unicode_locale_attributes(self):
        """
        Gets the unicode_locale_attributes of this Locale.


        :return: The unicode_locale_attributes of this Locale.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._unicode_locale_attributes

    @unicode_locale_attributes.setter
    def unicode_locale_attributes(self, unicode_locale_attributes):
        """
        Sets the unicode_locale_attributes of this Locale.


        :param unicode_locale_attributes: The unicode_locale_attributes of this Locale.
        :type: list[str]
        """
        self._unicode_locale_attributes = unicode_locale_attributes

    @property
    def unicode_locale_keys(self):
        """
        Gets the unicode_locale_keys of this Locale.


        :return: The unicode_locale_keys of this Locale.
        :rtype: list[str]
        :required/optional: optional
        """
        return self._unicode_locale_keys

    @unicode_locale_keys.setter
    def unicode_locale_keys(self, unicode_locale_keys):
        """
        Sets the unicode_locale_keys of this Locale.


        :param unicode_locale_keys: The unicode_locale_keys of this Locale.
        :type: list[str]
        """
        self._unicode_locale_keys = unicode_locale_keys

    @property
    def variant(self):
        """
        Gets the variant of this Locale.


        :return: The variant of this Locale.
        :rtype: str
        :required/optional: optional
        """
        return self._variant

    @variant.setter
    def variant(self, variant):
        """
        Sets the variant of this Locale.


        :param variant: The variant of this Locale.
        :type: str
        """
        self._variant = variant

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        if self is None:
           return None
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if self is None or other is None:
            return None
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

