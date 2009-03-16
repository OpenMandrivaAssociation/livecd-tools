%define debug_package %{nil}

Summary: Tools for building live CD's
Name: livecd-tools
Version: 022
Release: %mkrel 1
License: GPLv2
Group: System/Base
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
Patch0: fix-libdir-in-python.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
Requires: yum >= 3.2.18
Requires: mkisofs
Requires: squashfs-tools
Requires: pykickstart >= 0.96
Requires: dosfstools >= 2.11-8
Requires: isomd5sum
Requires: python-urlgrabber
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc ppc64
Requires: yaboot
%endif
BuildRequires: python


%description
Tools for generating live CD's on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%prep
%setup -q
%patch0 -p0

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
%doc AUTHORS COPYING README HACKING API
%doc config/livecd-fedora-minimal.ks
%{_mandir}/man*/*
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator
%dir %{py_platsitedir}/imgcreate
%{py_platsitedir}/imgcreate/*.py
%{py_platsitedir}/imgcreate/*.pyo
%{py_platsitedir}/imgcreate/*.pyc
