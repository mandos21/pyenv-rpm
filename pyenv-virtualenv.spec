Name: pyenv-virtualenv
Version: 1.2.1
Release: 2%{?dist}
BuildArch: noarch
Summary: A pyenv plugin to manage virtualenv environments
License: MIT
URL: https://github.com/pyenv/%{name}
Requires: pyenv >= 2.3.14
Requires: bash

Source0: https://github.com/pyenv/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

%description

The pyenv-virtualenv plugin for pyenv provides a `pyenv virtualenv`
command to create pyenv-compatible virtualenv environments for Python
on UNIX-like systems.

%prep
%setup

%install
PLUGIN_DIR=%{buildroot}/usr/share/pyenv/plugins/%{name}
mkdir -p ${PLUGIN_DIR}
cp -r bin libexec ${PLUGIN_DIR}

%files
%doc LICENSE
%doc README.md
/usr/share/pyenv/plugins/%{name}
