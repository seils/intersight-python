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


class PolicyConfigResultContext(object):
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
        'entity_data': 'object',
        'entity_moid': 'str',
        'entity_name': 'str',
        'entity_type': 'str'
    }

    attribute_map = {
        'entity_data': 'EntityData',
        'entity_moid': 'EntityMoid',
        'entity_name': 'EntityName',
        'entity_type': 'EntityType'
    }

    def __init__(self, entity_data=None, entity_moid=None, entity_name=None, entity_type=None):
        """
        PolicyConfigResultContext - a model defined in Swagger
        """

        self._entity_data = None
        self._entity_moid = None
        self._entity_name = None
        self._entity_type = None

        if entity_data is not None:
          self.entity_data = entity_data
        if entity_moid is not None:
          self.entity_moid = entity_moid
        if entity_name is not None:
          self.entity_name = entity_name
        if entity_type is not None:
          self.entity_type = entity_type

    @property
    def entity_data(self):
        """
        Gets the entity_data of this PolicyConfigResultContext.

        :return: The entity_data of this PolicyConfigResultContext.
        :rtype: object
        """
        return self._entity_data

    @entity_data.setter
    def entity_data(self, entity_data):
        """
        Sets the entity_data of this PolicyConfigResultContext.

        :param entity_data: The entity_data of this PolicyConfigResultContext.
        :type: object
        """

        self._entity_data = entity_data

    @property
    def entity_moid(self):
        """
        Gets the entity_moid of this PolicyConfigResultContext.

        :return: The entity_moid of this PolicyConfigResultContext.
        :rtype: str
        """
        return self._entity_moid

    @entity_moid.setter
    def entity_moid(self, entity_moid):
        """
        Sets the entity_moid of this PolicyConfigResultContext.

        :param entity_moid: The entity_moid of this PolicyConfigResultContext.
        :type: str
        """

        self._entity_moid = entity_moid

    @property
    def entity_name(self):
        """
        Gets the entity_name of this PolicyConfigResultContext.

        :return: The entity_name of this PolicyConfigResultContext.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this PolicyConfigResultContext.

        :param entity_name: The entity_name of this PolicyConfigResultContext.
        :type: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this PolicyConfigResultContext.

        :return: The entity_type of this PolicyConfigResultContext.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this PolicyConfigResultContext.

        :param entity_type: The entity_type of this PolicyConfigResultContext.
        :type: str
        """

        self._entity_type = entity_type

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
        if not isinstance(other, PolicyConfigResultContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
