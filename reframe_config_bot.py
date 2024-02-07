# WARNING: this file is intended as template and the __X__ template variables need to be replaced
# before it can act as a configuration file
# Once replaced, this is a config file for running tests after the build phase, by the bot

from eessi.testsuite.common_config import common_logging_config
from eessi.testsuite.constants import *  # noqa: F403


site_configuration = {
    'systems': [
        {
            'name': 'Testing in bot Build jobs for EESSI software Layer',
            'descr': 'Software-layer bot',
            'hostnames': ['.*'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'default',
                    'scheduler': 'local',
                    'launcher': 'mpirun',
                    'environs': ['default'],
                    'features': [FEATURES[CPU]],
                    'processor': {
                        'num_cpus': __NUM_CPUS__,
                        'num_sockets': __NUM_SOCKETS__,
                        'num_cpus_per_core': __NUM_CPUS_PER_CORE__,
                        'num_cpus_per_socket': __NUM_CPUS_PER_SOCKET__,
                    },
                    'resources': [
                        {
                            'name': 'memory',
                            'options': ['--mem={size}'],
                        }
                    ],
                    'max_jobs': 1
                    }
                ]
            }
        ],
    'environments': [
        {
            'name': 'default',
            'cc': 'cc',
            'cxx': '',
            'ftn': ''
            }
        ],
    'general': [
        {
            'purge_environment': True,
            'resolve_module_conflicts': False,  # avoid loading the module before submitting the job
            # Enable automatic detection of CPU architecture
            # See https://reframe-hpc.readthedocs.io/en/stable/configure.html#auto-detecting-processor-information
            'remote_detect': True,
        }
    ],
    'logging': common_logging_config(),
}
