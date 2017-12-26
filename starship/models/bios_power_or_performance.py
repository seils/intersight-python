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


class BiosPowerOrPerformance(object):
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
        'adjacent_cache_line_prefetch': 'str',
        'cpu_performance': 'str',
        'hardware_prefetch': 'str',
        'ip_prefetch': 'str',
        'streamer_prefetch': 'str'
    }

    attribute_map = {
        'adjacent_cache_line_prefetch': 'AdjacentCacheLinePrefetch',
        'cpu_performance': 'CpuPerformance',
        'hardware_prefetch': 'HardwarePrefetch',
        'ip_prefetch': 'IpPrefetch',
        'streamer_prefetch': 'StreamerPrefetch'
    }

    def __init__(self, adjacent_cache_line_prefetch='platform-default', cpu_performance='platform-default', hardware_prefetch='platform-default', ip_prefetch='platform-default', streamer_prefetch='platform-default'):
        """
        BiosPowerOrPerformance - a model defined in Swagger
        """

        self._adjacent_cache_line_prefetch = None
        self._cpu_performance = None
        self._hardware_prefetch = None
        self._ip_prefetch = None
        self._streamer_prefetch = None

        if adjacent_cache_line_prefetch is not None:
          self.adjacent_cache_line_prefetch = adjacent_cache_line_prefetch
        if cpu_performance is not None:
          self.cpu_performance = cpu_performance
        if hardware_prefetch is not None:
          self.hardware_prefetch = hardware_prefetch
        if ip_prefetch is not None:
          self.ip_prefetch = ip_prefetch
        if streamer_prefetch is not None:
          self.streamer_prefetch = streamer_prefetch

    @property
    def adjacent_cache_line_prefetch(self):
        """
        Gets the adjacent_cache_line_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting Adjacent Cache Line Prefetcher configuration  

        :return: The adjacent_cache_line_prefetch of this BiosPowerOrPerformance.
        :rtype: str
        """
        return self._adjacent_cache_line_prefetch

    @adjacent_cache_line_prefetch.setter
    def adjacent_cache_line_prefetch(self, adjacent_cache_line_prefetch):
        """
        Sets the adjacent_cache_line_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting Adjacent Cache Line Prefetcher configuration  

        :param adjacent_cache_line_prefetch: The adjacent_cache_line_prefetch of this BiosPowerOrPerformance.
        :type: str
        """
        allowed_values = ["platform-default", "enabled", "disabled"]
        if adjacent_cache_line_prefetch not in allowed_values:
            raise ValueError(
                "Invalid value for `adjacent_cache_line_prefetch` ({0}), must be one of {1}"
                .format(adjacent_cache_line_prefetch, allowed_values)
            )

        self._adjacent_cache_line_prefetch = adjacent_cache_line_prefetch

    @property
    def cpu_performance(self):
        """
        Gets the cpu_performance of this BiosPowerOrPerformance.
        BIOS Token for setting CPU Performance configuration  

        :return: The cpu_performance of this BiosPowerOrPerformance.
        :rtype: str
        """
        return self._cpu_performance

    @cpu_performance.setter
    def cpu_performance(self, cpu_performance):
        """
        Sets the cpu_performance of this BiosPowerOrPerformance.
        BIOS Token for setting CPU Performance configuration  

        :param cpu_performance: The cpu_performance of this BiosPowerOrPerformance.
        :type: str
        """
        allowed_values = ["platform-default", "custom", "enterprise", "high-throughput", "hpc"]
        if cpu_performance not in allowed_values:
            raise ValueError(
                "Invalid value for `cpu_performance` ({0}), must be one of {1}"
                .format(cpu_performance, allowed_values)
            )

        self._cpu_performance = cpu_performance

    @property
    def hardware_prefetch(self):
        """
        Gets the hardware_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting Hardware Prefetcher configuration  

        :return: The hardware_prefetch of this BiosPowerOrPerformance.
        :rtype: str
        """
        return self._hardware_prefetch

    @hardware_prefetch.setter
    def hardware_prefetch(self, hardware_prefetch):
        """
        Sets the hardware_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting Hardware Prefetcher configuration  

        :param hardware_prefetch: The hardware_prefetch of this BiosPowerOrPerformance.
        :type: str
        """
        allowed_values = ["platform-default", "enabled", "disabled"]
        if hardware_prefetch not in allowed_values:
            raise ValueError(
                "Invalid value for `hardware_prefetch` ({0}), must be one of {1}"
                .format(hardware_prefetch, allowed_values)
            )

        self._hardware_prefetch = hardware_prefetch

    @property
    def ip_prefetch(self):
        """
        Gets the ip_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting DCU IP Prefetcher configuration  

        :return: The ip_prefetch of this BiosPowerOrPerformance.
        :rtype: str
        """
        return self._ip_prefetch

    @ip_prefetch.setter
    def ip_prefetch(self, ip_prefetch):
        """
        Sets the ip_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting DCU IP Prefetcher configuration  

        :param ip_prefetch: The ip_prefetch of this BiosPowerOrPerformance.
        :type: str
        """
        allowed_values = ["platform-default", "enabled", "disabled"]
        if ip_prefetch not in allowed_values:
            raise ValueError(
                "Invalid value for `ip_prefetch` ({0}), must be one of {1}"
                .format(ip_prefetch, allowed_values)
            )

        self._ip_prefetch = ip_prefetch

    @property
    def streamer_prefetch(self):
        """
        Gets the streamer_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting DCU Streamer Prefetch configuration   

        :return: The streamer_prefetch of this BiosPowerOrPerformance.
        :rtype: str
        """
        return self._streamer_prefetch

    @streamer_prefetch.setter
    def streamer_prefetch(self, streamer_prefetch):
        """
        Sets the streamer_prefetch of this BiosPowerOrPerformance.
        BIOS Token for setting DCU Streamer Prefetch configuration   

        :param streamer_prefetch: The streamer_prefetch of this BiosPowerOrPerformance.
        :type: str
        """
        allowed_values = ["platform-default", "enabled", "disabled"]
        if streamer_prefetch not in allowed_values:
            raise ValueError(
                "Invalid value for `streamer_prefetch` ({0}), must be one of {1}"
                .format(streamer_prefetch, allowed_values)
            )

        self._streamer_prefetch = streamer_prefetch

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
        if not isinstance(other, BiosPowerOrPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
