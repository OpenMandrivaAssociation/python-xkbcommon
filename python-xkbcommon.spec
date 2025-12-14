%undefine _debugsource_packages
%define module xkbcommon
Name:           python-xkbcommon
Version:        1.5.1
Release:        2
Summary:        Python bindings for libxkbcommon using cffi
License:        MIT
URL:            https://github.com/sde1000/python-xkbcommon
Source0:        https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz

BuildSystem:  python
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(setuptools)
Requires: python
Requires: python-cffi
Requires: libxkbcommon-utils

%description
Python bindings for libxkbcommon using cffi.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/%{module}-%{version}.dist-info
%{python_sitearch}/%{module}
