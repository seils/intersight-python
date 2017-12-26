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


class DeviceinfoSerialNumberInfoList(object):
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
        'count': 'int',
        'results': 'list[DeviceinfoSerialNumberInfo]'
    }

    attribute_map = {
        'count': 'Count',
        'results': 'Results'
    }

    def __init__(self, count=None, results=None):
        """
        DeviceinfoSerialNumberInfoList - a model defined in Swagger
        """

        self._count = None
        self._results = None

        if count is not None:
          self.count = count
        if results is not None:
          self.results = results

    @property
    def count(self):
        """
        Gets the count of this DeviceinfoSerialNumberInfoList.
        The number of deviceinfoSerialNumberInfos matching your request in total for all pages.

        :return: The count of this DeviceinfoSerialNumberInfoList.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this DeviceinfoSerialNumberInfoList.
        The number of deviceinfoSerialNumberInfos matching your request in total for all pages.

        :param count: The count of this DeviceinfoSerialNumberInfoList.
        :type: int
        """

        self._count = count

    @property
    def results(self):
        """
        Gets the results of this DeviceinfoSerialNumberInfoList.
        The array of deviceinfoSerialNumberInfos matching your request.

        :return: The results of this DeviceinfoSerialNumberInfoList.
        :rtype: list[DeviceinfoSerialNumberInfo]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this DeviceinfoSerialNumberInfoList.
        The array of deviceinfoSerialNumberInfos matching your request.

        :param results: The results of this DeviceinfoSerialNumberInfoList.
        :type: list[DeviceinfoSerialNumberInfo]
        """

        self._results = results

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
        if not isinstance(other, DeviceinfoSerialNumberInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
