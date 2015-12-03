##
# Portions Copyright (c) Microsoft Corporation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# THIS CODE IS PROVIDED *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
# ANY IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR
# PURPOSE, MERCHANTABLITY OR NON-INFRINGEMENT.
#
# See the Apache Version 2.0 License for specific language governing
# permissions and limitations under the License.
##
{
  'targets': [
    {
      'target_name': 'edge_coreclr',
      'win_delay_load_hook': 'false',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags+': [
        '-DHAVE_CORECLR'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-DHAVE_CORECLR'
        ]
      },
      'conditions': [
        [
          'OS=="win"',
          {
            'conditions': [
              [
                '"<!(node -e "var whereis = require(\'./tools/whereis\'); console.log(whereis(\'dnx.exe\'));")"!=""',
                {
                  'sources+': [
                    'src/common/v8synchronizationcontext.cpp',
                    'src/common/edge.cpp',
                    'src/CoreCLREmbedding/coreclrembedding.cpp',
                    'src/CoreCLREmbedding/coreclrfunc.cpp',
                    'src/CoreCLREmbedding/coreclrnodejsfunc.cpp',
                    'src/CoreCLREmbedding/coreclrfuncinvokecontext.cpp',
                    'src/CoreCLREmbedding/coreclrnodejsfuncinvokecontext.cpp',
                    'src/common/utils.cpp'
                  ]
                }
              ]
            ]
          },
          {
            'conditions': [
              [
                '"<!(echo -n `which dnx`)"!=""',
                {
                  'sources+': [
                    'src/common/v8synchronizationcontext.cpp',
                    'src/common/edge.cpp',
                    'src/CoreCLREmbedding/coreclrembedding.cpp',
                    'src/CoreCLREmbedding/coreclrfunc.cpp',
                    'src/CoreCLREmbedding/coreclrnodejsfunc.cpp',
                    'src/CoreCLREmbedding/coreclrfuncinvokecontext.cpp',
                    'src/CoreCLREmbedding/coreclrnodejsfuncinvokecontext.cpp',
                    'src/common/utils.cpp'
                  ]
                }
              ]
            ]
          }
        ]
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/wd4506',
                '/DHAVE_CORECLR',
                '/EHsc'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248',
                'shlwapi.lib'
              ]
            }
          }
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': 3,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/wd4506',
                '/DHAVE_CORECLR',
                '/EHsc'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248',
                'shlwapi.lib'
              ]
            }
          }
        }
      }
    },
    {
      'target_name': 'edge_nativeclr',
      'win_delay_load_hook': 'false',
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'cflags+': [
        '-DHAVE_NATIVECLR'
      ],
      'xcode_settings': {
        'OTHER_CFLAGS': [
          '-DHAVE_NATIVECLR'
        ]
      },
      'conditions': [
        [
          'OS=="win"',
          {
            'sources+': [
              'src/dotnet/utils.cpp',
              'src/dotnet/clrfunc.cpp',
              'src/dotnet/clrfuncinvokecontext.cpp',
              'src/dotnet/nodejsfunc.cpp',
              'src/dotnet/nodejsfuncinvokecontext.cpp',
              'src/dotnet/persistentdisposecontext.cpp',
              'src/dotnet/clrfuncreflectionwrap.cpp',
              'src/dotnet/clractioncontext.cpp',
              'src/common/v8synchronizationcontext.cpp',
              'src/common/edge.cpp'
            ]
          }
        ]
      ],
      'configurations': {
        'Release': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
                '/DHAVE_NATIVECLR'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        },
        'Debug': {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # this is out of range and will generate a warning and skip adding RuntimeLibrary property:
              'RuntimeLibrary': -1,
              # this is out of range and will generate a warning and skip adding RuntimeTypeInfo property:
              'RuntimeTypeInfo': -1,
              'BasicRuntimeChecks': -1,
              'ExceptionHandling': '0',
              'AdditionalOptions': [
                '/clr',
                '/wd4506',
                '/DHAVE_NATIVECLR'
              ]
            },
            'VCLinkerTool': {
              'AdditionalOptions': [
                '/ignore:4248'
              ]
            }
          }
        }
      }
    }
  ]
}
