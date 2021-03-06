import os
import json

from fxpt.fx_utils import message_box
from fxpt.fx_utils.utils import makeWritable


def load(filename, showError=True, alertNotExist=True):
    try:
        with open(filename, 'r') as f:
            obj = json.load(f)
    except IOError:
        if alertNotExist and not os.path.exists(filename):
            message_box.exception('Cannot load JSON file. File does not exists:\n{}'.format(filename))
        if showError:
            message_box.exception('Cannot load JSON file:\n{}'.format(filename))
        raise
    except ValueError:
        if showError:
            message_box.exception('Error parsing JSON file. Check syntax:\n{}'.format(filename))
        raise
    except StandardError:
        if showError:
            message_box.exception('Unexpected error loading JSON file:\n{}'.format(filename))
        raise

    return obj


def dump(filename, obj, showError=True):
    try:
        makeWritable(filename)
        with open(filename, 'w') as f:
            json.dump(obj, f, sort_keys=True, indent=4, separators=(',', ': '))
    except IOError:
        if showError:
            message_box.exception('Cannot save JSON file:\n{}'.format(filename))
        raise
    except StandardError:
        if showError:
            message_box.exception('Unexpected error saving JSON file:\n{}'.format(filename))
        raise
