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


class VmediaMapping(object):
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
        'authentication_protocol': 'str',
        'device_type': 'str',
        'host_name': 'str',
        'mount_options': 'str',
        'mount_protocol': 'str',
        'password': 'str',
        'remote_file': 'str',
        'remote_path': 'str',
        'username': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'authentication_protocol': 'AuthenticationProtocol',
        'device_type': 'DeviceType',
        'host_name': 'HostName',
        'mount_options': 'MountOptions',
        'mount_protocol': 'MountProtocol',
        'password': 'Password',
        'remote_file': 'RemoteFile',
        'remote_path': 'RemotePath',
        'username': 'Username',
        'volume_name': 'VolumeName'
    }

    def __init__(self, authentication_protocol='none', device_type='Cdd', host_name=None, mount_options=None, mount_protocol='Nfs', password=None, remote_file=None, remote_path=None, username=None, volume_name=None):
        """
        VmediaMapping - a model defined in Swagger
        """

        self._authentication_protocol = None
        self._device_type = None
        self._host_name = None
        self._mount_options = None
        self._mount_protocol = None
        self._password = None
        self._remote_file = None
        self._remote_path = None
        self._username = None
        self._volume_name = None

        if authentication_protocol is not None:
          self.authentication_protocol = authentication_protocol
        if device_type is not None:
          self.device_type = device_type
        if host_name is not None:
          self.host_name = host_name
        if mount_options is not None:
          self.mount_options = mount_options
        if mount_protocol is not None:
          self.mount_protocol = mount_protocol
        if password is not None:
          self.password = password
        if remote_file is not None:
          self.remote_file = remote_file
        if remote_path is not None:
          self.remote_path = remote_path
        if username is not None:
          self.username = username
        if volume_name is not None:
          self.volume_name = volume_name

    @property
    def authentication_protocol(self):
        """
        Gets the authentication_protocol of this VmediaMapping.
        Type of Authentication protocol when CIFS is used for communication with the remote server  

        :return: The authentication_protocol of this VmediaMapping.
        :rtype: str
        """
        return self._authentication_protocol

    @authentication_protocol.setter
    def authentication_protocol(self, authentication_protocol):
        """
        Sets the authentication_protocol of this VmediaMapping.
        Type of Authentication protocol when CIFS is used for communication with the remote server  

        :param authentication_protocol: The authentication_protocol of this VmediaMapping.
        :type: str
        """
        allowed_values = ["none", "ntlm", "ntlmi", "ntlmv2", "ntlmv2i", "ntlmssp", "ntlmsspi"]
        if authentication_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_protocol` ({0}), must be one of {1}"
                .format(authentication_protocol, allowed_values)
            )

        self._authentication_protocol = authentication_protocol

    @property
    def device_type(self):
        """
        Gets the device_type of this VmediaMapping.
        Type of remote vMedia device. Accepted values are CDD, HDD  

        :return: The device_type of this VmediaMapping.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this VmediaMapping.
        Type of remote vMedia device. Accepted values are CDD, HDD  

        :param device_type: The device_type of this VmediaMapping.
        :type: str
        """
        allowed_values = ["Cdd", "Hdd"]
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def host_name(self):
        """
        Gets the host_name of this VmediaMapping.
        IP address or hostname of the remote server  

        :return: The host_name of this VmediaMapping.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this VmediaMapping.
        IP address or hostname of the remote server  

        :param host_name: The host_name of this VmediaMapping.
        :type: str
        """

        self._host_name = host_name

    @property
    def mount_options(self):
        """
        Gets the mount_options of this VmediaMapping.
        Mount options for the vMedia mount type  

        :return: The mount_options of this VmediaMapping.
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this VmediaMapping.
        Mount options for the vMedia mount type  

        :param mount_options: The mount_options of this VmediaMapping.
        :type: str
        """

        self._mount_options = mount_options

    @property
    def mount_protocol(self):
        """
        Gets the mount_protocol of this VmediaMapping.
        Protocol to use to communicate with the remote server. Accepted values are NFS, CIFS, HTTP, HTTPS  

        :return: The mount_protocol of this VmediaMapping.
        :rtype: str
        """
        return self._mount_protocol

    @mount_protocol.setter
    def mount_protocol(self, mount_protocol):
        """
        Sets the mount_protocol of this VmediaMapping.
        Protocol to use to communicate with the remote server. Accepted values are NFS, CIFS, HTTP, HTTPS  

        :param mount_protocol: The mount_protocol of this VmediaMapping.
        :type: str
        """
        allowed_values = ["Nfs", "Cifs", "Http", "Https"]
        if mount_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `mount_protocol` ({0}), must be one of {1}"
                .format(mount_protocol, allowed_values)
            )

        self._mount_protocol = mount_protocol

    @property
    def password(self):
        """
        Gets the password of this VmediaMapping.
        Password associated with the username  

        :return: The password of this VmediaMapping.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this VmediaMapping.
        Password associated with the username  

        :param password: The password of this VmediaMapping.
        :type: str
        """

        self._password = password

    @property
    def remote_file(self):
        """
        Gets the remote_file of this VmediaMapping.
        Name of the ISO or other images  

        :return: The remote_file of this VmediaMapping.
        :rtype: str
        """
        return self._remote_file

    @remote_file.setter
    def remote_file(self, remote_file):
        """
        Sets the remote_file of this VmediaMapping.
        Name of the ISO or other images  

        :param remote_file: The remote_file of this VmediaMapping.
        :type: str
        """

        self._remote_file = remote_file

    @property
    def remote_path(self):
        """
        Gets the remote_path of this VmediaMapping.
        Path to the location of the image on the remote server  

        :return: The remote_path of this VmediaMapping.
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """
        Sets the remote_path of this VmediaMapping.
        Path to the location of the image on the remote server  

        :param remote_path: The remote_path of this VmediaMapping.
        :type: str
        """

        self._remote_path = remote_path

    @property
    def username(self):
        """
        Gets the username of this VmediaMapping.
        Username to log in to the remote server  

        :return: The username of this VmediaMapping.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this VmediaMapping.
        Username to log in to the remote server  

        :param username: The username of this VmediaMapping.
        :type: str
        """

        self._username = username

    @property
    def volume_name(self):
        """
        Gets the volume_name of this VmediaMapping.
        Identity of the image for vMedia mapping   

        :return: The volume_name of this VmediaMapping.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this VmediaMapping.
        Identity of the image for vMedia mapping   

        :param volume_name: The volume_name of this VmediaMapping.
        :type: str
        """

        self._volume_name = volume_name

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
        if not isinstance(other, VmediaMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
