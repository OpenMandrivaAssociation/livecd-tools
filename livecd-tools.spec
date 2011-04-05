%define debug_package %{nil}

Summary: Tools for building live CDs
Name: livecd-tools
Version: 031
Release: %mkrel 43
License: GPLv2
Group: System/Base
Buildarch: noarch
URL: http://git.fedoraproject.org/?p=hosted/livecd
Source0: %{name}-%{version}.tar.bz2
Patch100: fix-libdir-in-python.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: python-imgcreate = %{version}-%{release}
Requires: mkisofs
Requires: isomd5sum
Requires: parted
%ifarch %{ix86} x86_64
Requires: syslinux
%endif
%ifarch ppc
Requires: yaboot
%endif
BuildRequires: python
BuildRequires: perl
Patch0: 0001-Disable-iswmd-on-live-images-for-now.patch
Patch10: livecd-tools-031-menu-config.patch
Patch11: livecd-tools-031-dracut.patch
Patch12: livecd-tools-031-not-use-rhpl-python.patch
Patch13: livecd-tools-031-use-urpmi.patch
Patch14: livecd-tools-031-yum-not-needed.patch
Patch15: livecd-tools-031-parted-path.patch 
Patch16: livecd-tools-031-yum-option.patch
Patch17: livecd-tools-031-without-language-config.patch
Patch18: livecd-tools-031-mksquashfs-lzma.patch
Patch19: livecd-tools-031-iso-to-disk-oem.patch
Patch20: livecd-tools-031-post-packages.patch
Patch21: livecd-tools-031-lazy-umount.patch
Patch22: livecd-tools-031-timeout-before-losetup-d.patch
Patch23: livecd-tools-031-xz.patch
Patch24: livecd-tools-031-iso-to-disk-oem-man.patch
# (eugeni) a temporary workaround to allow mixing packages from different repos
Patch25: livecd-tools-031-no-verify.patch
Patch26: livecd-tools-031-urpmi-split-length.patch

#next patch
Patch27: livecd-tools-031-fdisk-unit-cylinder.patch
Patch28: livecd-tools-031-cp-progress-bar.patch

%description 
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

This package contains the patches required to allow building live images on
Mandriva systems.

%package -n python-imgcreate
Summary: Python modules for building system images
Group: System/Base
Requires: util-linux
Requires: coreutils
Requires: e2fsprogs
#Requires: yum >= 3.2.18
Requires: squashfs-tools
#Requires: python-kickstart >= 0.96
Requires: pykickstart >= 1.77-3
Requires: dosfstools >= 2.11-8
#Requires: system-config-keyboard >= 1.3.0
Requires: python-urlgrabber
Requires: dbus-python
Conflicts: livecd-tools < 0.31

%description -n python-imgcreate
Python modules that can be used for building images for things
like live image or appliances.

%package -n livecd-iso-to-disk
Summary: Script for copy iso to disk

%description -n livecd-iso-to-disk
Convert a live CD iso so that it's bootable off of a USB stick

%prep
%setup -q
#%patch100 -p0
%patch0 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
#%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1 -F 5
%patch26 -p1
%patch27 -p1
%patch28 -p1

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
%{_bindir}/livecd-iso-to-pxeboot
%{_bindir}/image-creator

%files -n python-imgcreate
%defattr(-,root,root,-)
%doc API
%dir %{py_sitedir}/imgcreate
%{py_sitedir}/imgcreate/*.py
%{py_sitedir}/imgcreate/*.pyo
%{py_sitedir}/imgcreate/*.pyc

%files -n livecd-iso-to-disk
%{_bindir}/livecd-iso-to-disk
