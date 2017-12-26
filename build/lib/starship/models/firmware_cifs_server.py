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


class FirmwareCifsServer(object):
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
        'mount_options': 'str',
        'remote_file': 'str',
        'remote_ip': 'str',
        'remote_share': 'str'
    }

    attribute_map = {
        'mount_options': 'MountOptions',
        'remote_file': 'RemoteFile',
        'remote_ip': 'RemoteIp',
        'remote_share': 'RemoteShare'
    }

    def __init__(self, mount_options='none', remote_file=None, remote_ip=None, remote_share=None):
        """
        FirmwareCifsServer - a model defined in Swagger
        """

        self._mount_options = None
        self._remote_file = None
        self._remote_ip = None
        self._remote_share = None

        if mount_options is not None:
          self.mount_options = mount_options
        if remote_file is not None:
          self.remote_file = remote_file
        if remote_ip is not None:
          self.remote_ip = remote_ip
        if remote_share is not None:
          self.remote_share = remote_share

    @property
    def mount_options(self):
        """
        Gets the mount_options of this FirmwareCifsServer.
        Mount options of this image in the nfs server  

        :return: The mount_options of this FirmwareCifsServer.
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this FirmwareCifsServer.
        Mount options of this image in the nfs server  

        :param mount_options: The mount_options of this FirmwareCifsServer.
        :type: str
        """
        allowed_values = ["none", "ntlm", "ntlmi", "ntlmv2", "ntlmv2i", "ntlmssp", "ntlmsspi"]
        if mount_options not in allowed_values:
            raise ValueError(
                "Invalid value for `mount_options` ({0}), must be one of {1}"
                .format(mount_options, allowed_values)
            )

        self._mount_options = mount_options

    @property
    def remote_file(self):
        """
        Gets the remote_file of this FirmwareCifsServer.
        The filename of the image  

        :return: The remote_file of this FirmwareCifsServer.
        :rtype: str
        """
        return self._remote_file

    @remote_file.setter
    def remote_file(self, remote_file):
        """
        Sets the remote_file of this FirmwareCifsServer.
        The filename of the image  

        :param remote_file: The remote_file of this FirmwareCifsServer.
        :type: str
        """

        self._remote_file = remote_file

    @property
    def remote_ip(self):
        """
        Gets the remote_ip of this FirmwareCifsServer.
        The IP of a host (in the network) that has the image download thta can be mounted in BMC  

        :return: The remote_ip of this FirmwareCifsServer.
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        """
        Sets the remote_ip of this FirmwareCifsServer.
        The IP of a host (in the network) that has the image download thta can be mounted in BMC  

        :param remote_ip: The remote_ip of this FirmwareCifsServer.
        :type: str
        """

        self._remote_ip = remote_ip

    @property
    def remote_share(self):
        """
        Gets the remote_share of this FirmwareCifsServer.
        The directory where the image is stored   

        :return: The remote_share of this FirmwareCifsServer.
        :rtype: str
        """
        return self._remote_share

    @remote_share.setter
    def remote_share(self, remote_share):
        """
        Sets the remote_share of this FirmwareCifsServer.
        The directory where the image is stored   

        :param remote_share: The remote_share of this FirmwareCifsServer.
        :type: str
        """

        self._remote_share = remote_share

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
        if not isinstance(other, FirmwareCifsServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
