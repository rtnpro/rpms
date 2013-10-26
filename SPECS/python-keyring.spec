%global upstream_name keyring
%global tarball_version 0.3

Name:           python-keyring
Version:        3.0.5
Release:        1%{?dist}
Summary:        Python library to access the system keyring service

Source0:        http://pypi.python.org/packages/source/k/keyring/%{upstream_name}-%{tarball_version}.tar.gz
License:        Python
Group:          Development/Libraries
URL:            http://pypi.python.org/pypi/keyring
BuildArch:      noarch
BuildRequires:  python-devel
Obsoletes:      %{name}-kwallet < %{version}
Obsoletes:      %{name}-gnome < %{version}
Obsoletes:      %{name} < %{version}

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

The keyring services supported by the Python keyring lib:
* OSXKeychain: supports the Keychain service in Mac OS X.
* KDEKWallet: supports the KDE's Kwallet service.
* GnomeKeyring: for Gnome 2 environment.
* SecretServiceKeyring: for newer GNOME and KDE environments.
* WinVaultKeyring: supports the Windows Credential Vault

Besides these native password storing services provided by operating
systems. Python keyring lib also provides following build-in keyrings.
* Win32CryptoKeyring: for Windows 2k+.
* CryptedFileKeyring: a command line interface keyring base on PyCrypto.
* UncryptedFileKeyring: a keyring which leaves passwords directly in file.

%prep
%setup -q -n %{upstream_name}-%{tarball_version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt CHANGES.txt demo
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-*.egg-info

%changelog
* Tue Oct 22 2013 rtnpro <rtnpro@gmail.com>
- Bump to version 3.0.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 rtnpro <rtnpro@gmail.com> 0.7-1
- Python 3 is now supported. All tests now pass under Python 3.2 on Windows and
Linux (although Linux backend support is limited). Fixes #28.
- Extension modules on Mac and Windows replaced by pure-Python ctypes
implementations. Thanks to Jérôme Laheurte.
- WinVaultKeyring now supports multiple passwords for the same service.
Fixes #47.
- Most of the tests don't require user interaction anymore.
- Entries stored in Gnome Keyring appears now with a meaningful name if you try
to browser your keyring (for ex. with Seahorse)
- Tests from Gnome Keyring no longer pollute the user own keyring.
- keyring.util.escape now accepts only unicode strings. Don't try to encode
strings passed to it.

* Tue Nov 08 2011 rtnpro <rtnpro@gmail.com> 0.6.2-1
- fix compiling on OSX with XCode 4.0
- Gnome keyring should not be used if there is no DISPLAY or if the dbus is not around
    (https://bugs.launchpad.net/launchpadlib/+bug/752282).
- Added keyring.http for facilitating HTTP Auth using keyring.
- Add a utility to access the keyring from the command line.

* Mon Jan 10 2011 rtnpro <rtnpro@gmail.com> 0.5.1-1
- Remove a spurious KDE debug message when using KWallet
- Fix a bug that caused an exception if the user canceled the KWallet dialog

* Sun Nov 28 2010 rtnpro <rtnpro@gmail.com> 0.5-2
- Removed sub-packages: gnome and kwallet; removed "Requires: PyKDE4 PyQt4"

* Mon Nov 22 2010 rtnpro <rtnpro@gmail.com> 0.5-1
- RPM for keyring-0.5

* Mon Nov 01 2010 rtnpro <rtnpro@gmail.com> 0.4-1
- Updated rpm to python-keyring version 0.4

* Sat Oct 30 2010 rtnpro <rtnpro@gmail.com> 0.2-4
- Filtered gnome_keyring.so from the provides list, removed kdelibs-devel

* Sat Oct 02 2010 rtnpro <rtnpro@gmail.com> 0.2-3
- Updated dependencies to kdelibs4-devel, some cleanup

* Tue Aug 24 2010 rtnpro <rtnpro@gmail.com> 0.2-2
- Some updates according to bugzilla reviews

* Sat Jun 26 2010 rtnpro <rtnpro@gmail.com> 0.2-1.3
- Some cleanup

* Sat Jun 26 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.2
- add KWallet subpackage

* Mon Jun 21 2010 Felix Schwarz <felix.schwarz@oss.schwarz.eu> 0.2-1.1
- add build dependencies
- create subpackage for gnome, disable KWallet for now
- look for files in arch-dependend site-packages

* Tue May 25 2010 rtnpro <rtnpro@gmail.com> 0.2-1
- Incorporated some changes with reference to http://vcrhonek.fedorapeople.org/python-keyring/python-keyring.spec
- Fixed some rpmlint errors

* Wed May 19 2010 rtnpro <rtnpro@gmail.com> 0.2
- Initial RPM package


