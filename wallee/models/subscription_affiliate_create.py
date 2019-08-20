# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractSubscriptionAffiliateUpdate


class SubscriptionAffiliateCreate(AbstractSubscriptionAffiliateUpdate):

    swagger_types = {
        'external_id': 'str',
        'reference': 'str',
        'state': 'CreationEntityState',
    }

    attribute_map = {
        'external_id': 'externalId',
        'reference': 'reference',
        'state': 'state',
    }

    
    _external_id = None
    _reference = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.external_id = kwargs.get('external_id')
        self.reference = kwargs.get('reference', None)
        self.state = kwargs.get('state', None)

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionAffiliateCreate.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this SubscriptionAffiliateCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionAffiliateCreate.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this SubscriptionAffiliateCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id

    @property
    def reference(self):
        """Gets the reference of this SubscriptionAffiliateCreate.

            

        :return: The reference of this SubscriptionAffiliateCreate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionAffiliateCreate.

            

        :param reference: The reference of this SubscriptionAffiliateCreate.
        :type: str
        """

        self._reference = reference

    @property
    def state(self):
        """Gets the state of this SubscriptionAffiliateCreate.

            

        :return: The state of this SubscriptionAffiliateCreate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionAffiliateCreate.

            

        :param state: The state of this SubscriptionAffiliateCreate.
        :type: CreationEntityState
        """

        self._state = state

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
        if issubclass(SubscriptionAffiliateCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionAffiliateCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other