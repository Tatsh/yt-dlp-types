local utils = import 'utils.libjsonnet';

(import 'defaults.libjsonnet') + {
  // Project-specific
  description: 'PEP 561 type stubs for yt-dlp.',
  keywords: ['pep561', 'stubs', 'types', 'yt-dlp'],
  project_name: 'yt-dlp-types',
  version: '0.0.16',
  citation+: {
    'date-released': '2025-04-12',
  },
  want_docs: false,
  want_tests: false,
  stubs_only: true,
  primary_module: 'yt_dlp-stubs',
  pyproject+: {
    tool+: {
      poetry+: {
        group+: {
          dev+: {
            dependencies+: {
              'yt-dlp': '>=2023.6.22,<2026.0.0',
            },
          },
        },
      },
    },
  },
  // Common
  authors: [
    {
      'family-names': 'Udvare',
      'given-names': 'Andrew',
      email: 'audvare@gmail.com',
      name: '%s %s' % [self['given-names'], self['family-names']],
    },
  ],
  local funding_name = '%s2' % std.asciiLower(self.github_username),
  github_username: 'Tatsh',
  github+: {
    funding+: {
      ko_fi: funding_name,
      liberapay: funding_name,
      patreon: funding_name,
    },
  },
}
