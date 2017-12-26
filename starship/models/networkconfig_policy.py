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


class NetworkconfigPolicy(object):
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
        'account_moid': 'str',
        'ancestors': 'list[MoMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoMoRef',
        'tags': 'list[MoTag]',
        'id': 'str',
        'description': 'str',
        'name': 'str',
        'account': 'MoMoRef',
        'alternate_ipv4dns_server': 'str',
        'alternate_ipv6dns_server': 'str',
        'dynamic_dns_domain': 'str',
        'enable_dynamic_dns': 'bool',
        'enable_ipv4dns_from_dhcp': 'bool',
        'enable_ipv6dns_from_dhcp': 'bool',
        'enable_vlan': 'bool',
        'preferred_ipv4dns_server': 'str',
        'preferred_ipv6dns_server': 'str',
        'priority': 'int',
        'profile': 'MoMoRef',
        'vlan_id': 'int'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'id': 'Id',
        'description': 'Description',
        'name': 'Name',
        'account': 'Account',
        'alternate_ipv4dns_server': 'AlternateIpv4dnsServer',
        'alternate_ipv6dns_server': 'AlternateIpv6dnsServer',
        'dynamic_dns_domain': 'DynamicDnsDomain',
        'enable_dynamic_dns': 'EnableDynamicDns',
        'enable_ipv4dns_from_dhcp': 'EnableIpv4dnsFromDhcp',
        'enable_ipv6dns_from_dhcp': 'EnableIpv6dnsFromDhcp',
        'enable_vlan': 'EnableVlan',
        'preferred_ipv4dns_server': 'PreferredIpv4dnsServer',
        'preferred_ipv6dns_server': 'PreferredIpv6dnsServer',
        'priority': 'Priority',
        'profile': 'Profile',
        'vlan_id': 'VlanId'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, description=None, name=None, account=None, alternate_ipv4dns_server=None, alternate_ipv6dns_server=None, dynamic_dns_domain=None, enable_dynamic_dns=None, enable_ipv4dns_from_dhcp=None, enable_ipv6dns_from_dhcp=None, enable_vlan=None, preferred_ipv4dns_server=None, preferred_ipv6dns_server=None, priority=None, profile=None, vlan_id=None):
        """
        NetworkconfigPolicy - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._id = None
        self._description = None
        self._name = None
        self._account = None
        self._alternate_ipv4dns_server = None
        self._alternate_ipv6dns_server = None
        self._dynamic_dns_domain = None
        self._enable_dynamic_dns = None
        self._enable_ipv4dns_from_dhcp = None
        self._enable_ipv6dns_from_dhcp = None
        self._enable_vlan = None
        self._preferred_ipv4dns_server = None
        self._preferred_ipv6dns_server = None
        self._priority = None
        self._profile = None
        self._vlan_id = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if id is not None:
          self.id = id
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if account is not None:
          self.account = account
        if alternate_ipv4dns_server is not None:
          self.alternate_ipv4dns_server = alternate_ipv4dns_server
        if alternate_ipv6dns_server is not None:
          self.alternate_ipv6dns_server = alternate_ipv6dns_server
        if dynamic_dns_domain is not None:
          self.dynamic_dns_domain = dynamic_dns_domain
        if enable_dynamic_dns is not None:
          self.enable_dynamic_dns = enable_dynamic_dns
        if enable_ipv4dns_from_dhcp is not None:
          self.enable_ipv4dns_from_dhcp = enable_ipv4dns_from_dhcp
        if enable_ipv6dns_from_dhcp is not None:
          self.enable_ipv6dns_from_dhcp = enable_ipv6dns_from_dhcp
        if enable_vlan is not None:
          self.enable_vlan = enable_vlan
        if preferred_ipv4dns_server is not None:
          self.preferred_ipv4dns_server = preferred_ipv4dns_server
        if preferred_ipv6dns_server is not None:
          self.preferred_ipv6dns_server = preferred_ipv6dns_server
        if priority is not None:
          self.priority = priority
        if profile is not None:
          self.profile = profile
        if vlan_id is not None:
          self.vlan_id = vlan_id

    @property
    def account_moid(self):
        """
        Gets the account_moid of this NetworkconfigPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this NetworkconfigPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this NetworkconfigPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this NetworkconfigPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this NetworkconfigPolicy.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this NetworkconfigPolicy.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this NetworkconfigPolicy.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this NetworkconfigPolicy.
        The time when this managed object was created.  

        :return: The create_time of this NetworkconfigPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this NetworkconfigPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this NetworkconfigPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this NetworkconfigPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this NetworkconfigPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this NetworkconfigPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this NetworkconfigPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this NetworkconfigPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this NetworkconfigPolicy.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this NetworkconfigPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this NetworkconfigPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this NetworkconfigPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this NetworkconfigPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this NetworkconfigPolicy.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this NetworkconfigPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this NetworkconfigPolicy.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this NetworkconfigPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this NetworkconfigPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this NetworkconfigPolicy.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this NetworkconfigPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this NetworkconfigPolicy.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this NetworkconfigPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this NetworkconfigPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this NetworkconfigPolicy.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this NetworkconfigPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this NetworkconfigPolicy.
        A unique identifier of this Managed Object instance.  

        :return: The id of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NetworkconfigPolicy.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this NetworkconfigPolicy.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this NetworkconfigPolicy.
        Description of the policy.  

        :return: The description of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this NetworkconfigPolicy.
        Description of the policy.  

        :param description: The description of this NetworkconfigPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this NetworkconfigPolicy.
        Name of the policy.   

        :return: The name of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NetworkconfigPolicy.
        Name of the policy.   

        :param name: The name of this NetworkconfigPolicy.
        :type: str
        """

        self._name = name

    @property
    def account(self):
        """
        Gets the account of this NetworkconfigPolicy.
        Relationship to the account. 

        :return: The account of this NetworkconfigPolicy.
        :rtype: MoMoRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this NetworkconfigPolicy.
        Relationship to the account. 

        :param account: The account of this NetworkconfigPolicy.
        :type: MoMoRef
        """

        self._account = account

    @property
    def alternate_ipv4dns_server(self):
        """
        Gets the alternate_ipv4dns_server of this NetworkconfigPolicy.
        IP address of the secondary DNS server  

        :return: The alternate_ipv4dns_server of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._alternate_ipv4dns_server

    @alternate_ipv4dns_server.setter
    def alternate_ipv4dns_server(self, alternate_ipv4dns_server):
        """
        Sets the alternate_ipv4dns_server of this NetworkconfigPolicy.
        IP address of the secondary DNS server  

        :param alternate_ipv4dns_server: The alternate_ipv4dns_server of this NetworkconfigPolicy.
        :type: str
        """

        self._alternate_ipv4dns_server = alternate_ipv4dns_server

    @property
    def alternate_ipv6dns_server(self):
        """
        Gets the alternate_ipv6dns_server of this NetworkconfigPolicy.
        IP address of the secondary DNS server  

        :return: The alternate_ipv6dns_server of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._alternate_ipv6dns_server

    @alternate_ipv6dns_server.setter
    def alternate_ipv6dns_server(self, alternate_ipv6dns_server):
        """
        Sets the alternate_ipv6dns_server of this NetworkconfigPolicy.
        IP address of the secondary DNS server  

        :param alternate_ipv6dns_server: The alternate_ipv6dns_server of this NetworkconfigPolicy.
        :type: str
        """

        self._alternate_ipv6dns_server = alternate_ipv6dns_server

    @property
    def dynamic_dns_domain(self):
        """
        Gets the dynamic_dns_domain of this NetworkconfigPolicy.
        The domain name appended to a hostname for a Dynamic DNS(DDNS) update. If left blank, only a hostname is sent to the DDNS update request  

        :return: The dynamic_dns_domain of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._dynamic_dns_domain

    @dynamic_dns_domain.setter
    def dynamic_dns_domain(self, dynamic_dns_domain):
        """
        Sets the dynamic_dns_domain of this NetworkconfigPolicy.
        The domain name appended to a hostname for a Dynamic DNS(DDNS) update. If left blank, only a hostname is sent to the DDNS update request  

        :param dynamic_dns_domain: The dynamic_dns_domain of this NetworkconfigPolicy.
        :type: str
        """

        self._dynamic_dns_domain = dynamic_dns_domain

    @property
    def enable_dynamic_dns(self):
        """
        Gets the enable_dynamic_dns of this NetworkconfigPolicy.
        If enabled, updates the resource records to the DNS from Cisco IMC  

        :return: The enable_dynamic_dns of this NetworkconfigPolicy.
        :rtype: bool
        """
        return self._enable_dynamic_dns

    @enable_dynamic_dns.setter
    def enable_dynamic_dns(self, enable_dynamic_dns):
        """
        Sets the enable_dynamic_dns of this NetworkconfigPolicy.
        If enabled, updates the resource records to the DNS from Cisco IMC  

        :param enable_dynamic_dns: The enable_dynamic_dns of this NetworkconfigPolicy.
        :type: bool
        """

        self._enable_dynamic_dns = enable_dynamic_dns

    @property
    def enable_ipv4dns_from_dhcp(self):
        """
        Gets the enable_ipv4dns_from_dhcp of this NetworkconfigPolicy.
        If enabled, Cisco IMC retrieves the DNS server addresses from DHCP  

        :return: The enable_ipv4dns_from_dhcp of this NetworkconfigPolicy.
        :rtype: bool
        """
        return self._enable_ipv4dns_from_dhcp

    @enable_ipv4dns_from_dhcp.setter
    def enable_ipv4dns_from_dhcp(self, enable_ipv4dns_from_dhcp):
        """
        Sets the enable_ipv4dns_from_dhcp of this NetworkconfigPolicy.
        If enabled, Cisco IMC retrieves the DNS server addresses from DHCP  

        :param enable_ipv4dns_from_dhcp: The enable_ipv4dns_from_dhcp of this NetworkconfigPolicy.
        :type: bool
        """

        self._enable_ipv4dns_from_dhcp = enable_ipv4dns_from_dhcp

    @property
    def enable_ipv6dns_from_dhcp(self):
        """
        Gets the enable_ipv6dns_from_dhcp of this NetworkconfigPolicy.
        If enabled, Cisco IMC retrieves the DNS server addresses from DHCP  

        :return: The enable_ipv6dns_from_dhcp of this NetworkconfigPolicy.
        :rtype: bool
        """
        return self._enable_ipv6dns_from_dhcp

    @enable_ipv6dns_from_dhcp.setter
    def enable_ipv6dns_from_dhcp(self, enable_ipv6dns_from_dhcp):
        """
        Sets the enable_ipv6dns_from_dhcp of this NetworkconfigPolicy.
        If enabled, Cisco IMC retrieves the DNS server addresses from DHCP  

        :param enable_ipv6dns_from_dhcp: The enable_ipv6dns_from_dhcp of this NetworkconfigPolicy.
        :type: bool
        """

        self._enable_ipv6dns_from_dhcp = enable_ipv6dns_from_dhcp

    @property
    def enable_vlan(self):
        """
        Gets the enable_vlan of this NetworkconfigPolicy.
        If enabled, Cisco IMC is connected to a virual LAN  

        :return: The enable_vlan of this NetworkconfigPolicy.
        :rtype: bool
        """
        return self._enable_vlan

    @enable_vlan.setter
    def enable_vlan(self, enable_vlan):
        """
        Sets the enable_vlan of this NetworkconfigPolicy.
        If enabled, Cisco IMC is connected to a virual LAN  

        :param enable_vlan: The enable_vlan of this NetworkconfigPolicy.
        :type: bool
        """

        self._enable_vlan = enable_vlan

    @property
    def preferred_ipv4dns_server(self):
        """
        Gets the preferred_ipv4dns_server of this NetworkconfigPolicy.
        IP address of the primary DNS server  

        :return: The preferred_ipv4dns_server of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._preferred_ipv4dns_server

    @preferred_ipv4dns_server.setter
    def preferred_ipv4dns_server(self, preferred_ipv4dns_server):
        """
        Sets the preferred_ipv4dns_server of this NetworkconfigPolicy.
        IP address of the primary DNS server  

        :param preferred_ipv4dns_server: The preferred_ipv4dns_server of this NetworkconfigPolicy.
        :type: str
        """

        self._preferred_ipv4dns_server = preferred_ipv4dns_server

    @property
    def preferred_ipv6dns_server(self):
        """
        Gets the preferred_ipv6dns_server of this NetworkconfigPolicy.
        IP address of the primary DNS server  

        :return: The preferred_ipv6dns_server of this NetworkconfigPolicy.
        :rtype: str
        """
        return self._preferred_ipv6dns_server

    @preferred_ipv6dns_server.setter
    def preferred_ipv6dns_server(self, preferred_ipv6dns_server):
        """
        Sets the preferred_ipv6dns_server of this NetworkconfigPolicy.
        IP address of the primary DNS server  

        :param preferred_ipv6dns_server: The preferred_ipv6dns_server of this NetworkconfigPolicy.
        :type: str
        """

        self._preferred_ipv6dns_server = preferred_ipv6dns_server

    @property
    def priority(self):
        """
        Gets the priority of this NetworkconfigPolicy.
        Priority associated with the specified VLAN ID. Allowed values range from 0 to 7  

        :return: The priority of this NetworkconfigPolicy.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this NetworkconfigPolicy.
        Priority associated with the specified VLAN ID. Allowed values range from 0 to 7  

        :param priority: The priority of this NetworkconfigPolicy.
        :type: int
        """

        self._priority = priority

    @property
    def profile(self):
        """
        Gets the profile of this NetworkconfigPolicy.
        Relationship to the profile object. 

        :return: The profile of this NetworkconfigPolicy.
        :rtype: MoMoRef
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """
        Sets the profile of this NetworkconfigPolicy.
        Relationship to the profile object. 

        :param profile: The profile of this NetworkconfigPolicy.
        :type: MoMoRef
        """

        self._profile = profile

    @property
    def vlan_id(self):
        """
        Gets the vlan_id of this NetworkconfigPolicy.
        VLAN ID assigned to Cisco IMC   

        :return: The vlan_id of this NetworkconfigPolicy.
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """
        Sets the vlan_id of this NetworkconfigPolicy.
        VLAN ID assigned to Cisco IMC   

        :param vlan_id: The vlan_id of this NetworkconfigPolicy.
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
        if not isinstance(other, NetworkconfigPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
