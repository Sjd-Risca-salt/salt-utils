# -*- coding: utf-8 -*-
"""
Helper for pillarstack.

Usage (with jinja into pillarstack):

{{ __salt__['datautils.mtraverse'](dictA, dictB, 'my:path', None) }}
"""
# To be evaluate: push a shortcut into pillarstack for __stack__
from salt.utils.data import traverse_dict_and_list

def mtraverse(srca, srcb, path, default=None):
    """Try to search path into srca. If missing, try srcb. If no value is
    found return the default (or None).

    dic, dic, string, obj => obj

    Usage:
      mtraverse({'test': {'list': 2}}, {'test': 0}, 'test:list')
    """
    test = '2traverse_value_not_found'
    value = traverse_dict_and_list(srca, path, test)
    if value == test:
        value = traverse_dict_and_list(srcb, path, test)
    if value == test:
        return default
    return value
