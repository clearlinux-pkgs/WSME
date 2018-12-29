#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WSME
Version  : 0.9.3
Release  : 33
URL      : http://pypi.debian.net/WSME/WSME-0.9.3.tar.gz
Source0  : http://pypi.debian.net/WSME/WSME-0.9.3.tar.gz
Summary  : Simplify the writing of REST APIs, and extend them with additional protocols.
Group    : Development/Tools
License  : MIT
Requires: WSME-license = %{version}-%{release}
Requires: WSME-python = %{version}-%{release}
Requires: WSME-python3 = %{version}-%{release}
Requires: Pygments
Requires: Sphinx
Requires: WSME
Requires: WebOb
Requires: netaddr
Requires: pecan
Requires: pytz
Requires: simplegeneric
Requires: six
BuildRequires : Babel
BuildRequires : Flask
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : WSME
BuildRequires : WebOb-python
BuildRequires : buildreq-distutils3
BuildRequires : docutils-python
BuildRequires : flask-python
BuildRequires : itsdangerous-python
BuildRequires : jinja2-python
BuildRequires : markupsafe-python
BuildRequires : netaddr
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : pytz-python
BuildRequires : simplegeneric-python
BuildRequires : six
BuildRequires : six-python
BuildRequires : sqlalchemy-python
BuildRequires : webtest-python
BuildRequires : werkzeug-python

%description
======================
        
        Introduction
        ------------
        
        Web Services Made Easy (WSME) simplifies the writing of REST web services
        by providing simple yet powerful typing, removing the need to directly
        manipulate the request and the response objects.
        
        WSME can work standalone or on top of your favorite Python web
        (micro)framework, so you can use both your preferred way of routing your REST

%package license
Summary: license components for the WSME package.
Group: Default

%description license
license components for the WSME package.


%package python
Summary: python components for the WSME package.
Group: Default
Requires: WSME-python3 = %{version}-%{release}
Provides: wsme-python

%description python
python components for the WSME package.


%package python3
Summary: python3 components for the WSME package.
Group: Default
Requires: python3-core

%description python3
python3 components for the WSME package.


%prep
%setup -q -n WSME-0.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541280911
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m nose || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WSME
cp LICENSE %{buildroot}/usr/share/package-licenses/WSME/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WSME/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
