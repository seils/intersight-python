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


class HyperflexNodeProfile(object):
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
        'src_template': 'MoMoRef',
        'type': 'str',
        'assigned_server': 'MoMoRef',
        'cluster_profile': 'MoMoRef',
        'esx_data_ip': 'str',
        'esx_mgmt_ip': 'str',
        'hxdp_data_ip': 'str',
        'hxdp_mgmt_ip': 'str'
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
        'src_template': 'SrcTemplate',
        'type': 'Type',
        'assigned_server': 'AssignedServer',
        'cluster_profile': 'ClusterProfile',
        'esx_data_ip': 'EsxDataIp',
        'esx_mgmt_ip': 'EsxMgmtIp',
        'hxdp_data_ip': 'HxdpDataIp',
        'hxdp_mgmt_ip': 'HxdpMgmtIp'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, id=None, description=None, name=None, src_template=None, type='instance', assigned_server=None, cluster_profile=None, esx_data_ip=None, esx_mgmt_ip=None, hxdp_data_ip=None, hxdp_mgmt_ip=None):
        """
        HyperflexNodeProfile - a model defined in Swagger
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
        self._src_template = None
        self._type = None
        self._assigned_server = None
        self._cluster_profile = None
        self._esx_data_ip = None
        self._esx_mgmt_ip = None
        self._hxdp_data_ip = None
        self._hxdp_mgmt_ip = None

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
        if src_template is not None:
          self.src_template = src_template
        if type is not None:
          self.type = type
        if assigned_server is not None:
          self.assigned_server = assigned_server
        if cluster_profile is not None:
          self.cluster_profile = cluster_profile
        if esx_data_ip is not None:
          self.esx_data_ip = esx_data_ip
        if esx_mgmt_ip is not None:
          self.esx_mgmt_ip = esx_mgmt_ip
        if hxdp_data_ip is not None:
          self.hxdp_data_ip = hxdp_data_ip
        if hxdp_mgmt_ip is not None:
          self.hxdp_mgmt_ip = hxdp_mgmt_ip

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexNodeProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexNodeProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this HyperflexNodeProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexNodeProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this HyperflexNodeProfile.
        :rtype: list[MoMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexNodeProfile.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this HyperflexNodeProfile.
        :type: list[MoMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexNodeProfile.
        The time when this managed object was created.  

        :return: The create_time of this HyperflexNodeProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexNodeProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this HyperflexNodeProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexNodeProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this HyperflexNodeProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexNodeProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this HyperflexNodeProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexNodeProfile.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexNodeProfile.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this HyperflexNodeProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexNodeProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexNodeProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this HyperflexNodeProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexNodeProfile.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this HyperflexNodeProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexNodeProfile.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this HyperflexNodeProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexNodeProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this HyperflexNodeProfile.
        :rtype: MoMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexNodeProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this HyperflexNodeProfile.
        :type: MoMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexNodeProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this HyperflexNodeProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexNodeProfile.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this HyperflexNodeProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this HyperflexNodeProfile.
        A unique identifier of this Managed Object instance.  

        :return: The id of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HyperflexNodeProfile.
        A unique identifier of this Managed Object instance.  

        :param id: The id of this HyperflexNodeProfile.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this HyperflexNodeProfile.
        Description of the profile.  

        :return: The description of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this HyperflexNodeProfile.
        Description of the profile.  

        :param description: The description of this HyperflexNodeProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this HyperflexNodeProfile.
        Name of the profile.  

        :return: The name of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this HyperflexNodeProfile.
        Name of the profile.  

        :param name: The name of this HyperflexNodeProfile.
        :type: str
        """

        self._name = name

    @property
    def src_template(self):
        """
        Gets the src_template of this HyperflexNodeProfile.

        :return: The src_template of this HyperflexNodeProfile.
        :rtype: MoMoRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this HyperflexNodeProfile.

        :param src_template: The src_template of this HyperflexNodeProfile.
        :type: MoMoRef
        """

        self._src_template = src_template

    @property
    def type(self):
        """
        Gets the type of this HyperflexNodeProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this HyperflexNodeProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this HyperflexNodeProfile.
        :type: str
        """
        allowed_values = ["instance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def assigned_server(self):
        """
        Gets the assigned_server of this HyperflexNodeProfile.

        :return: The assigned_server of this HyperflexNodeProfile.
        :rtype: MoMoRef
        """
        return self._assigned_server

    @assigned_server.setter
    def assigned_server(self, assigned_server):
        """
        Sets the assigned_server of this HyperflexNodeProfile.

        :param assigned_server: The assigned_server of this HyperflexNodeProfile.
        :type: MoMoRef
        """

        self._assigned_server = assigned_server

    @property
    def cluster_profile(self):
        """
        Gets the cluster_profile of this HyperflexNodeProfile.

        :return: The cluster_profile of this HyperflexNodeProfile.
        :rtype: MoMoRef
        """
        return self._cluster_profile

    @cluster_profile.setter
    def cluster_profile(self, cluster_profile):
        """
        Sets the cluster_profile of this HyperflexNodeProfile.

        :param cluster_profile: The cluster_profile of this HyperflexNodeProfile.
        :type: MoMoRef
        """

        self._cluster_profile = cluster_profile

    @property
    def esx_data_ip(self):
        """
        Gets the esx_data_ip of this HyperflexNodeProfile.

        :return: The esx_data_ip of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._esx_data_ip

    @esx_data_ip.setter
    def esx_data_ip(self, esx_data_ip):
        """
        Sets the esx_data_ip of this HyperflexNodeProfile.

        :param esx_data_ip: The esx_data_ip of this HyperflexNodeProfile.
        :type: str
        """

        self._esx_data_ip = esx_data_ip

    @property
    def esx_mgmt_ip(self):
        """
        Gets the esx_mgmt_ip of this HyperflexNodeProfile.

        :return: The esx_mgmt_ip of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._esx_mgmt_ip

    @esx_mgmt_ip.setter
    def esx_mgmt_ip(self, esx_mgmt_ip):
        """
        Sets the esx_mgmt_ip of this HyperflexNodeProfile.

        :param esx_mgmt_ip: The esx_mgmt_ip of this HyperflexNodeProfile.
        :type: str
        """

        self._esx_mgmt_ip = esx_mgmt_ip

    @property
    def hxdp_data_ip(self):
        """
        Gets the hxdp_data_ip of this HyperflexNodeProfile.

        :return: The hxdp_data_ip of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._hxdp_data_ip

    @hxdp_data_ip.setter
    def hxdp_data_ip(self, hxdp_data_ip):
        """
        Sets the hxdp_data_ip of this HyperflexNodeProfile.

        :param hxdp_data_ip: The hxdp_data_ip of this HyperflexNodeProfile.
        :type: str
        """

        self._hxdp_data_ip = hxdp_data_ip

    @property
    def hxdp_mgmt_ip(self):
        """
        Gets the hxdp_mgmt_ip of this HyperflexNodeProfile.

        :return: The hxdp_mgmt_ip of this HyperflexNodeProfile.
        :rtype: str
        """
        return self._hxdp_mgmt_ip

    @hxdp_mgmt_ip.setter
    def hxdp_mgmt_ip(self, hxdp_mgmt_ip):
        """
        Sets the hxdp_mgmt_ip of this HyperflexNodeProfile.

        :param hxdp_mgmt_ip: The hxdp_mgmt_ip of this HyperflexNodeProfile.
        :type: str
        """

        self._hxdp_mgmt_ip = hxdp_mgmt_ip

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
        if not isinstance(other, HyperflexNodeProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
