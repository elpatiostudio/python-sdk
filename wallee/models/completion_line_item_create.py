# coding: utf-8
import pprint
import six
from enum import Enum



class CompletionLineItemCreate:

    swagger_types = {
    
        'amount': 'float',
        'quantity': 'float',
        'unique_id': 'str',
    }

    attribute_map = {
        'amount': 'amount','quantity': 'quantity','unique_id': 'uniqueId',
    }

    
    _amount = None
    _quantity = None
    _unique_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount')

        self.quantity = kwargs.get('quantity')

        self.unique_id = kwargs.get('unique_id')

        

    
    @property
    def amount(self):
        """Gets the amount of this CompletionLineItemCreate.

            The total amount of the line item including any tax.

        :return: The amount of this CompletionLineItemCreate.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CompletionLineItemCreate.

            The total amount of the line item including any tax.

        :param amount: The amount of this CompletionLineItemCreate.
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount
    
    @property
    def quantity(self):
        """Gets the quantity of this CompletionLineItemCreate.

            The quantity of the line item which should be completed.

        :return: The quantity of this CompletionLineItemCreate.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CompletionLineItemCreate.

            The quantity of the line item which should be completed.

        :param quantity: The quantity of this CompletionLineItemCreate.
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity
    
    @property
    def unique_id(self):
        """Gets the unique_id of this CompletionLineItemCreate.

            The unique id identifies the line item on which the capture is applied on.

        :return: The unique_id of this CompletionLineItemCreate.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this CompletionLineItemCreate.

            The unique id identifies the line item on which the capture is applied on.

        :param unique_id: The unique_id of this CompletionLineItemCreate.
        :type: str
        """
        if unique_id is None:
            raise ValueError("Invalid value for `unique_id`, must not be `None`")

        self._unique_id = unique_id
    

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
        if issubclass(CompletionLineItemCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CompletionLineItemCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
