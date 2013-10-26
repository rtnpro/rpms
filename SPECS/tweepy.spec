Name:           tweepy
Version:        2.0
Release:        1%{?dist}
Summary:        Twitter library for python
Source0:        http://pypi.python.org/packages/source/t/%{name}/%{name}-%{version}.tar.gz
Patch0:         tweepy-2.0-docs.patch
License:        MIT
Group:          Development/Libraries
URL:            http://pypi.python.org/pypi/tweepy/
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools python-simplejson
Requires:       python-simplejson

%description
A library for accessing the Twitter.com API. Supports OAuth, covers the
entire API, and streaming API.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info

%changelog
* Fri Jun 28 2013 rtnpro <rtnpro@gmail.com> 2.0-1
- Update to tweepy v2.0

* Mon Feb 21 2011 rtnpro <rtnpro@gmail.com> 1.7.1-3
- Added LICENSE, removed unnecessary macros

* Sat Feb 05 2011 rtnpro <rtnpro@gmail.com> 1.7.1-2
- Some fixes in the SPEC file

* Fri Feb 04 2011 rtnpro <rtnpro@gmail.com> 1.7.1-1
- Intial RPM package for tweepy
