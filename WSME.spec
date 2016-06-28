#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WSME
Version  : 0.8.0
Release  : 19
URL      : https://pypi.python.org/packages/source/W/WSME/WSME-0.8.0.tar.gz
Source0  : https://pypi.python.org/packages/source/W/WSME/WSME-0.8.0.tar.gz
Summary  : Simplify the writing of REST APIs, and extend them with additional protocols.
Group    : Development/Tools
License  : MIT
Requires: WSME-python
BuildRequires : Flask
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : docutils-python
BuildRequires : flask-python
BuildRequires : itsdangerous-python
BuildRequires : jinja2-python
BuildRequires : markupsafe-python
BuildRequires : netaddr
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
BuildRequires : simplegeneric-python
BuildRequires : six
BuildRequires : six-python
BuildRequires : sqlalchemy-python
BuildRequires : webtest-python
BuildRequires : werkzeug-python

%description
Web Services Made Easy
======================
Introduction
------------
Web Services Made Easy (WSME) simplifies the writing of REST web services
by providing simple yet powerful typing, removing the need to directly
manipulate the request and the response objects.

%package python
Summary: python components for the WSME package.
Group: Default
Provides: wsme-python

%description python
python components for the WSME package.


%prep
%setup -q -n WSME-0.8.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m nose || :
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
