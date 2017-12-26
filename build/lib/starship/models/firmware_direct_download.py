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


class FirmwareDirectDownload(object):
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
        'upgradeoption': 'str'
    }

    attribute_map = {
        'upgradeoption': 'Upgradeoption'
    }

    def __init__(self, upgradeoption='sd_upgrade_full'):
        """
        FirmwareDirectDownload - a model defined in Swagger
        """

        self._upgradeoption = None

        if upgradeoption is not None:
          self.upgradeoption = upgradeoption

    @property
    def upgradeoption(self):
        """
        Gets the upgradeoption of this FirmwareDirectDownload.
        Customer can download the image on the microsd of the server from Cisco.com and upgrade later or do the download, upgrade in a single window   

        :return: The upgradeoption of this FirmwareDirectDownload.
        :rtype: str
        """
        return self._upgradeoption

    @upgradeoption.setter
    def upgradeoption(self, upgradeoption):
        """
        Sets the upgradeoption of this FirmwareDirectDownload.
        Customer can download the image on the microsd of the server from Cisco.com and upgrade later or do the download, upgrade in a single window   

        :param upgradeoption: The upgradeoption of this FirmwareDirectDownload.
        :type: str
        """
        allowed_values = ["sd_upgrade_full", "sd_download_only", "sd_upgrade_only"]
        if upgradeoption not in allowed_values:
            raise ValueError(
                "Invalid value for `upgradeoption` ({0}), must be one of {1}"
                .format(upgradeoption, allowed_values)
            )

        self._upgradeoption = upgradeoption

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
        if not isinstance(other, FirmwareDirectDownload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
