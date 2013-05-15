%{!?python_sitelib: %define python_sitelib %(%{__python} -c "import distutils.sysconfig as d; print d.get_python_lib()")}

%define debug_package %{nil}

Summary:	Tools for building live CDs
Name:		livecd-tools
Version:	18.8
Release:	19
Epoch:		1
License:	GPLv2
Group:		System/Base
URL:		http://git.fedorahosted.org/git/livecd
# To make source tar ball:
# git clone git://git.fedorahosted.org/livecd
# cd livecd
# make dist
# scp livecd*.tar.bz2 fedorahosted.org:livecd
Source0:	http://fedorahosted.org/releases/l/i/livecd/%{name}-%{version}.tar.bz2
Source1:	arch.py
Patch0:		livecd-tools-18.8.urpmi.rosa.patch
Patch1:		livecd-tools-18.8.noyum.patch
Patch2:		livecd-tools-18.8.more.fixes.patch
Patch3:		livecd-tools-18.8.localboot.patch
Patch4:		livecd-tools-18.8.revert.patch
Patch5:		livecd-tools-18.8.sgb2.patch
Patch6:		livecd-tools-18.8.safemode.patch
Patch7:         livecd-tools-18.8.fs_nls.patch
Requires:	python-imgcreate = %{EVRD}
Requires:	mkisofs
Requires:	isomd5sum
Requires:	parted
Requires:	pyparted
Requires:	util-linux
Requires:	dosfstools
Requires:	e2fsprogs
Requires:	lorax >= 18.3
Obsoletes:	livecd-iso-to-disk

%ifarch %{ix86} x86_64
Requires:	syslinux
%endif
Requires:	dumpet
BuildRequires:	python
BuildRequires:	/usr/bin/pod2man


%description 
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

%package -n python-imgcreate
Summary:	Python modules for building system images
Group:		System/Base
Requires:	util-linux
Requires:	coreutils
Requires:	e2fsprogs
Requires:	squashfs-tools
Requires:	pykickstart >= 0.96
Requires:	dosfstools >= 2.11-8
#Requires: system-config-keyboard >= 1.3.0
Requires:	python-urlgrabber
Requires:	python-selinux
Requires:	python-dbus
#Requires: policycoreutils

%description -n python-imgcreate
Python modules that can be used for building images for things
like live image or appliances.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT
%__install -m 0644 %{SOURCE1} %{buildroot}%{python_sitelib}/imgcreate/


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README HACKING
%doc config/livecd-fedora-minimal.ks
%{_mandir}/man*/*
%{_bindir}/livecd-creator
%{_bindir}/livecd-iso-to-disk
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/edit-livecd
%{_bindir}/mkbiarch
/usr/share/doc/livecd-tools*

%files -n python-imgcreate
%defattr(-,root,root,-)
%doc API COPYING
%dir %{python_sitelib}/imgcreate
%{python_sitelib}/imgcreate/*.py
%{python_sitelib}/imgcreate/*.pyo
%{python_sitelib}/imgcreate/*.pyc

%changelog
* Mon Aug 06 2012 Brian C. Lane <bcl@redhat.com> 18.8-1
- Version 18.8 (bcl)
- dracut needs to load vfat and msdos filesystems (bcl)
