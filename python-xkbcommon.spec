%undefine _debugsource_packages
Name:           python-xkbcommon
Version:        1.5.1
Release:        1
Summary:        Python bindings for libxkbcommon using cffi
License:        MIT

URL:            https://github.com/sde1000/python-xkbcommon
Source0:        https://files.pythonhosted.org/packages/source/p/xkbcommon/xkbcommon-%{version}.tar.gz

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(python3)
BuildRequires: python-cffi
Requires: python
Requires: python-cffi
Requires: libxkbcommon-utils
BuildSystem:  python

%description
Python bindings for libxkbcommon using cffi.

%files
%license LICENSE
%{python_sitelib}/xkbcommon-%{version}.dist-info
%{python_sitelib}/xkbcommon/
