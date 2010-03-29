%define debug_package %{nil}

Summary: Tools for building live CDs
Name: livecd-tools
Version: 031
Release: %mkrel 3
License: GPLv2
Group: System/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
Patch100: fix-libdir-in-python.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-imgcreate = %{version}-%{release}
Requires: mkisofs
Requires: isomd5sum
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc
Requires: yaboot
%endif
BuildRequires: python
BuildRequires: /usr/bin/pod2man
Patch0: 0001-Disable-iswmd-on-live-images-for-now.patch


%description 
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%package -n python-imgcreate
Summary: Python modules for building system images
Group: System/Base
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
Requires: yum >= 3.2.18
Requires: squashfs-tools
Requires: pykickstart >= 0.96
Requires: dosfstools >= 2.11-8
Requires: system-config-keyboard >= 1.3.0
Requires: python-urlgrabber
Requires: libselinux-python
Requires: dbus-python

%description -n python-imgcreate
Python modules that can be used for building images for things
like live image or appliances.


%prep
%setup -q
%patch100 -p0
%patch0 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv %{buildroot}/%{_docdir}/%{name}-%{version}/  %{buildroot}/%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README HACKING
%doc config/livecd-fedora-minimal.ks
%{_mandir}/man*/*
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator

%files -n python-imgcreate
%defattr(-,root,root,-)
%doc API
%dir %{py_platsitedir}/imgcreate
%{py_platsitedir}/imgcreate/*.py
%{py_platsitedir}/imgcreate/*.pyo
%{py_platsitedir}/imgcreate/*.pyc
