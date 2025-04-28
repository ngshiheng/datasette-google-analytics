# CHANGELOG


## v0.1.2 (2025-04-28)

### Bug Fixes

- Streamline release workflow and update version handling in setup.py
  ([`e57e489`](https://github.com/ngshiheng/datasette-google-analytics/commit/e57e4893d9e649d1cb5e51c87afc2d3f1f2063e2))

- Update pip install command to use non-editable mode for dependencies
  ([`7996281`](https://github.com/ngshiheng/datasette-google-analytics/commit/7996281ac71e63918fa53d97e83c542e2d287ff7))

### Chores

- Remove CHANGELOG file and environment setting from publish workflow
  ([`392699d`](https://github.com/ngshiheng/datasette-google-analytics/commit/392699d299c0f28b295ab461e10ff8c2ce4c077c))

### Continuous Integration

- Add GitHub Actions workflows for publishing
  ([`1d045be`](https://github.com/ngshiheng/datasette-google-analytics/commit/1d045be2b6dc7c289c8ee4cd75d17e4b3b64ade9))

- Simplify dependency installation in release workflow
  ([`d371fbf`](https://github.com/ngshiheng/datasette-google-analytics/commit/d371fbf1efbc4c7a6a8755968dd25c68ec67c082))

- Update release workflow to use semantic release and publish to PyPI
  ([`ecb6f5a`](https://github.com/ngshiheng/datasette-google-analytics/commit/ecb6f5a9bfdd60c65ed6f6432349ccdd5c19925e))


## v0.1.1 (2025-04-28)

### Bug Fixes

- Add package_data to include HTML templates in the distribution
  ([`c675e4a`](https://github.com/ngshiheng/datasette-google-analytics/commit/c675e4a85b0773993c7aa49265420924516083ab))


## v0.1.0 (2025-04-28)

### Chores

- Add .gitignore
  ([`7433763`](https://github.com/ngshiheng/datasette-google-analytics/commit/743376312da83a7864837f5cef756366a42f93ff))

- Add LICENSE
  ([`adfdf3e`](https://github.com/ngshiheng/datasette-google-analytics/commit/adfdf3e06f3f779f3254d9452fb702bd771d2d9d))

- Fix build requirements in setup.py by adding missing comma for wheel
  ([`b9719e2`](https://github.com/ngshiheng/datasette-google-analytics/commit/b9719e2a5c3145f477015070ebfbe6c90766e266))

- Update setup.py to include long description and project URLs
  ([`26b87db`](https://github.com/ngshiheng/datasette-google-analytics/commit/26b87db6620928065e6aef095a947b94d9d83259))

### Continuous Integration

- Add id to Python Semantic Release step
  ([`447d77b`](https://github.com/ngshiheng/datasette-google-analytics/commit/447d77b67a25de24fd4fe8c5915c258b8276df24))

- Add semantic release configuration and update setup.py for build requirements
  ([`9789882`](https://github.com/ngshiheng/datasette-google-analytics/commit/978988235a1a12e4f303693968196ef44f3a6c4d))

- Add workflow for testing across multiple Python versions
  ([`4cb258e`](https://github.com/ngshiheng/datasette-google-analytics/commit/4cb258eb3d37278c359fc4c7ce570a1ea48a99ab))

- Remove unnecessary permissions and password from release workflow
  ([`64c398e`](https://github.com/ngshiheng/datasette-google-analytics/commit/64c398ecfd3272ff7d103ad4f2e2937eb50bc1cf))

- Simplify workflow triggers to only respond to push events
  ([`011728d`](https://github.com/ngshiheng/datasette-google-analytics/commit/011728d05b4c2c1d06e84f6ae28ff9ab9d9eb2f5))

- Update Python version matrix to remove 3.8 and enforce minimum Python 3.9 requirement
  ([`4f9f033`](https://github.com/ngshiheng/datasette-google-analytics/commit/4f9f033d70ce215e532578c1892c365b2e4d0364))

- Update release workflow permissions to include contents write access
  ([`9ef4909`](https://github.com/ngshiheng/datasette-google-analytics/commit/9ef4909d2a35874534a8a3a804504ac552cc677c))

- Update workflows to use Python 3.13 and improve dependency management
  ([`b72c168`](https://github.com/ngshiheng/datasette-google-analytics/commit/b72c168c7fd53647f85432d9ffd10607b3d92b17))

### Documentation

- Add development setup instructions
  ([`93cdfe6`](https://github.com/ngshiheng/datasette-google-analytics/commit/93cdfe614a121ee6cfe87564583e01c7ad6de4f4))

- Update README with installation and usage instructions
  ([`ce05cb8`](https://github.com/ngshiheng/datasette-google-analytics/commit/ce05cb80f894a64ef7c654ac985ba43410e4daa6))

### Features

- Enhance plugin with template support
  ([`0862d97`](https://github.com/ngshiheng/datasette-google-analytics/commit/0862d97d2e8d3df88e21088602cde0673091d219))

- Implement Google Analytics 4 tracking functionality
  ([`9fec949`](https://github.com/ngshiheng/datasette-google-analytics/commit/9fec949a4bb385024f0c8961c62defee42c9c7dc))

- Init
  ([`d917c92`](https://github.com/ngshiheng/datasette-google-analytics/commit/d917c9231cf3ae54b9e71eef4ea80d272352092c))

### Testing

- Add tests for plugin
  ([`9387cbf`](https://github.com/ngshiheng/datasette-google-analytics/commit/9387cbf9b1d8d79c66a76600156a0fa3f9a5dcde))
