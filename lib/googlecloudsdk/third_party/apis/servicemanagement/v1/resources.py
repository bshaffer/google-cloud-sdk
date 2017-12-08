# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://servicemanagement.googleapis.com/v1/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  OPERATIONS = (
      'operations',
      'operations/{operationsId}',
      [
          'operations/{operationsId}',
      ],
      [u'operationsId'])
  SERVICES = (
      'services',
      'services/{serviceName}',
      [
          'services/{serviceName}',
      ],
      [u'serviceName'])
  SERVICES_CONFIGS = (
      'services.configs',
      'services/{serviceName}/configs/{configId}',
      [
          'services/{serviceName}/configs/{configId}',
      ],
      [u'serviceName', u'configId'])
  SERVICES_CUSTOMERSETTINGS = (
      'services.customerSettings',
      'services/{serviceName}/customerSettings/{customerId}',
      [
          'services/{serviceName}/customerSettings/{customerId}',
      ],
      [u'serviceName', u'customerId'])
  SERVICES_PROJECTSETTINGS = (
      'services.projectSettings',
      'services/{serviceName}/projectSettings/{consumerProjectId}',
      [
          'services/{serviceName}/projectSettings/{consumerProjectId}',
      ],
      [u'serviceName', u'consumerProjectId'])
  SERVICES_ROLLOUTS = (
      'services.rollouts',
      'services/{serviceName}/rollouts/{rolloutId}',
      [
          'services/{serviceName}/rollouts/{rolloutId}',
      ],
      [u'serviceName', u'rolloutId'])

  def __init__(self, collection_name, path, flat_paths, params):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params