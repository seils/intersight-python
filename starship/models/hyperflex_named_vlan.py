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


class HyperflexNamedVlan(object):
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
        'name': 'str',
        'vlan_id': 'int'
    }

    attribute_map = {
        'name': 'Name',
        'vlan_id': 'VlanId'
    }

    def __init__(self, name=None, vlan_id=None):
        """
        HyperflexNamedVlan - a model defined in Swagger
        """

        self._name = None
        self._vlan_id = None

        if name is not None:
          self.name = name
        if vlan_id is not None:
          self.vlan_id = vlan_id

    @property
    def name(self):
        """
        Gets the name of this HyperflexNamedVlan.

        :return: The name of this HyperflexNamedVlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexNamedVlan.

        :param name: The name of this HyperflexNamedVlan.
        :type: str
        """

        self._name = name

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this HyperflexNamedVlan.

        :return: The vlan_id of this HyperflexNamedVlan.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this HyperflexNamedVlan.

        :param vlan_id: The vlan_id of this HyperflexNamedVlan.
        :type: int
        """

        self._vlan_id = vlan_id

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
        if not isinstance(other, HyperflexNamedVlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
