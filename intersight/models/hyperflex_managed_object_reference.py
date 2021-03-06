# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class HyperflexManagedObjectReference(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'val': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'val': 'Val'
    }

    def __init__(self, type=None, val=None):
        """
        HyperflexManagedObjectReference - a model defined in Swagger
        """

        self._type = None
        self._val = None

        if type is not None:
          self.type = type
        if val is not None:
          self.val = val

    @property
    def type(self):
        """
        Gets the type of this HyperflexManagedObjectReference.

        :return: The type of this HyperflexManagedObjectReference.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HyperflexManagedObjectReference.

        :param type: The type of this HyperflexManagedObjectReference.
        :type: str
        """

        self._type = type

    @property
    def val(self):
        """
        Gets the val of this HyperflexManagedObjectReference.

        :return: The val of this HyperflexManagedObjectReference.
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val):
        """
        Sets the val of this HyperflexManagedObjectReference.

        :param val: The val of this HyperflexManagedObjectReference.
        :type: str
        """

        self._val = val

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
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, HyperflexManagedObjectReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
