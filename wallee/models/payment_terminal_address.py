# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalAddress:

    swagger_types = {
    
        'city': 'str',
        'country': 'str',
        'dependent_locality': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'mobile_phone_number': 'str',
        'organization_name': 'str',
        'phone_number': 'str',
        'post_code': 'str',
        'postal_state': 'str',
        'salutation': 'str',
        'sorting_code': 'str',
        'street': 'str',
    }

    attribute_map = {
        'city': 'city','country': 'country','dependent_locality': 'dependentLocality','email_address': 'emailAddress','family_name': 'familyName','given_name': 'givenName','mobile_phone_number': 'mobilePhoneNumber','organization_name': 'organizationName','phone_number': 'phoneNumber','post_code': 'postCode','postal_state': 'postalState','salutation': 'salutation','sorting_code': 'sortingCode','street': 'street',
    }

    
    _city = None
    _country = None
    _dependent_locality = None
    _email_address = None
    _family_name = None
    _given_name = None
    _mobile_phone_number = None
    _organization_name = None
    _phone_number = None
    _post_code = None
    _postal_state = None
    _salutation = None
    _sorting_code = None
    _street = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.city = kwargs.get('city', None)
        self.country = kwargs.get('country', None)
        self.dependent_locality = kwargs.get('dependent_locality', None)
        self.email_address = kwargs.get('email_address', None)
        self.family_name = kwargs.get('family_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.mobile_phone_number = kwargs.get('mobile_phone_number', None)
        self.organization_name = kwargs.get('organization_name', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.post_code = kwargs.get('post_code', None)
        self.postal_state = kwargs.get('postal_state', None)
        self.salutation = kwargs.get('salutation', None)
        self.sorting_code = kwargs.get('sorting_code', None)
        self.street = kwargs.get('street', None)
        

    
    @property
    def city(self):
        """Gets the city of this PaymentTerminalAddress.

            

        :return: The city of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PaymentTerminalAddress.

            

        :param city: The city of this PaymentTerminalAddress.
        :type: str
        """

        self._city = city
    
    @property
    def country(self):
        """Gets the country of this PaymentTerminalAddress.

            

        :return: The country of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PaymentTerminalAddress.

            

        :param country: The country of this PaymentTerminalAddress.
        :type: str
        """

        self._country = country
    
    @property
    def dependent_locality(self):
        """Gets the dependent_locality of this PaymentTerminalAddress.

            

        :return: The dependent_locality of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._dependent_locality

    @dependent_locality.setter
    def dependent_locality(self, dependent_locality):
        """Sets the dependent_locality of this PaymentTerminalAddress.

            

        :param dependent_locality: The dependent_locality of this PaymentTerminalAddress.
        :type: str
        """

        self._dependent_locality = dependent_locality
    
    @property
    def email_address(self):
        """Gets the email_address of this PaymentTerminalAddress.

            

        :return: The email_address of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this PaymentTerminalAddress.

            

        :param email_address: The email_address of this PaymentTerminalAddress.
        :type: str
        """

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this PaymentTerminalAddress.

            

        :return: The family_name of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this PaymentTerminalAddress.

            

        :param family_name: The family_name of this PaymentTerminalAddress.
        :type: str
        """

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this PaymentTerminalAddress.

            

        :return: The given_name of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this PaymentTerminalAddress.

            

        :param given_name: The given_name of this PaymentTerminalAddress.
        :type: str
        """

        self._given_name = given_name
    
    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this PaymentTerminalAddress.

            

        :return: The mobile_phone_number of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this PaymentTerminalAddress.

            

        :param mobile_phone_number: The mobile_phone_number of this PaymentTerminalAddress.
        :type: str
        """

        self._mobile_phone_number = mobile_phone_number
    
    @property
    def organization_name(self):
        """Gets the organization_name of this PaymentTerminalAddress.

            

        :return: The organization_name of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this PaymentTerminalAddress.

            

        :param organization_name: The organization_name of this PaymentTerminalAddress.
        :type: str
        """

        self._organization_name = organization_name
    
    @property
    def phone_number(self):
        """Gets the phone_number of this PaymentTerminalAddress.

            

        :return: The phone_number of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this PaymentTerminalAddress.

            

        :param phone_number: The phone_number of this PaymentTerminalAddress.
        :type: str
        """

        self._phone_number = phone_number
    
    @property
    def post_code(self):
        """Gets the post_code of this PaymentTerminalAddress.

            

        :return: The post_code of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this PaymentTerminalAddress.

            

        :param post_code: The post_code of this PaymentTerminalAddress.
        :type: str
        """

        self._post_code = post_code
    
    @property
    def postal_state(self):
        """Gets the postal_state of this PaymentTerminalAddress.

            

        :return: The postal_state of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._postal_state

    @postal_state.setter
    def postal_state(self, postal_state):
        """Sets the postal_state of this PaymentTerminalAddress.

            

        :param postal_state: The postal_state of this PaymentTerminalAddress.
        :type: str
        """

        self._postal_state = postal_state
    
    @property
    def salutation(self):
        """Gets the salutation of this PaymentTerminalAddress.

            

        :return: The salutation of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """Sets the salutation of this PaymentTerminalAddress.

            

        :param salutation: The salutation of this PaymentTerminalAddress.
        :type: str
        """

        self._salutation = salutation
    
    @property
    def sorting_code(self):
        """Gets the sorting_code of this PaymentTerminalAddress.

            The sorting code identifies the post office at which the post box is located in.

        :return: The sorting_code of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._sorting_code

    @sorting_code.setter
    def sorting_code(self, sorting_code):
        """Sets the sorting_code of this PaymentTerminalAddress.

            The sorting code identifies the post office at which the post box is located in.

        :param sorting_code: The sorting_code of this PaymentTerminalAddress.
        :type: str
        """

        self._sorting_code = sorting_code
    
    @property
    def street(self):
        """Gets the street of this PaymentTerminalAddress.

            

        :return: The street of this PaymentTerminalAddress.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this PaymentTerminalAddress.

            

        :param street: The street of this PaymentTerminalAddress.
        :type: str
        """

        self._street = street
    

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
            elif isinstance(value, Enum):
                result[attr] = value.value
            else:
                result[attr] = value
        if issubclass(PaymentTerminalAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
