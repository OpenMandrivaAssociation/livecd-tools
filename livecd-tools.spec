# NOTE: This package is fully arched due to dependency sensitivity.
# Please do not remove archfulness on Requires/Provides.

%define debug_package %{nil}

%global min_dnf_ver 4.0
%global min_pykickstart_ver 2.25

Name:          livecd-tools
Summary:       Tools for building live CDs
Version:       26.0
Release:       3
License:       GPLv2
Group:         System/Base
URL:           https://github.com/livecd-tools/livecd-tools
Source0:       https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz

# Patches backported from upstream

# Mageia specific patches
Patch1001:     1001-livecd-tools-18-dracut_conf.patch
Patch1002:     1002-livecd-tools-18-force-dracut-also-for-initrd.patch
Patch1003:     1003-livecd-tools-24-extra_filesystems.patch
Patch1004:     1004-livecd-tools-24-disable-efi.patch


BuildRequires: python-devel
BuildRequires: %{_bindir}/pod2man
BuildRequires: /bin/sed

Requires:      python-imgcreate%{?_isa} = %{version}-%{release}

%ifarch %{ix86} %{x86_64}
Requires:      livecd-iso-to-mediums = %{version}-%{release}
%endif

%description
Tools for generating live CDs on Fedora based systems including
derived distributions such as RHEL, CentOS and others. See
http://fedoraproject.org/wiki/FedoraLiveCD for more details.

This package is patched to support building live images on
OpenMandriva systems.

%package -n python-imgcreate-sysdeps
Summary:       Common system dependencies for python-imgcreate
Group:         System/Base
Requires:      coreutils
Requires:      xorriso
Requires:      isomd5sum
Requires:      parted
Requires:      util-linux
Requires:      dosfstools
Requires:      e2fsprogs
# mkefiboot from lorax, disabled by patch1004
#Requires:      lorax >= 18.3
Requires:      rsync
%ifarch %{ix86} %{x86_64} ppc ppc64
Recommends:    hfsplus-tools
%endif
%ifarch %{ix86} %{x86_64}
Requires:      syslinux
%endif
%ifarch ppc
Requires:      yaboot
%endif
Requires:      dumpet
Recommends:    sssd-client
Requires:      cryptsetup
Requires:      squashfs-tools
#Requires:      policycoreutils

%description -n python-imgcreate-sysdeps
This package describes the common system dependencies for
python-imgcreate.

%package -n python-imgcreate
Summary:       Python 3 modules for building system images
Group:         Development/Python
Requires:      python-imgcreate-sysdeps%{?_isa} = %{version}-%{release}
Requires:      python-parted
Requires:      python-dnf >= %{min_dnf_ver}
Requires:      python-kickstart >= %{min_pykickstart_ver}
Requires:      python-six
Requires:      python-selinux
Requires:      python-dbus

%description -n python-imgcreate
Python 3 modules that can be used for building images for things
like live image or appliances.


%ifarch %{ix86} %{x86_64}
%package -n livecd-iso-to-mediums
Summary:       Tools for installing ISOs to different mediums
Group:         System/Base
Requires:      python-imgcreate-sysdeps%{?_isa} = %{version}-%{release}
Provides:      livecd-iso-to-disk = %{version}-%{release}
Requires:      extlinux
Requires:      pxelinux


%description -n livecd-iso-to-mediums
Tools for installing Live CD ISOs to different mediums
(e.g. USB sticks, hard drives, PXE boot, etc.)
%endif

%prep
%autosetup -p1

%build
# Nothing to do


%install
%make_install PYTHON=python3 SED_PROGRAM=/bin/sed

# Delete installed docs, we'll grab them later
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%ifnarch %{ix86} %{x86_64}
# livecd-iso-to-mediums doesn't work without syslinux
rm -rfv %{buildroot}%{_bindir}/livecd-iso-to-*
rm -rfv %{buildroot}%{_mandir}/man8/livecd-iso-to-*
%endif

%files
%license COPYING
%doc AUTHORS README HACKING
%doc config/livecd-fedora-minimal.ks
%doc config/livecd-mageia-minimal-*.ks
%{_bindir}/livecd-creator
%{_bindir}/image-creator
%{_bindir}/liveimage-mount
%{_bindir}/editliveos
%{_bindir}/mkbiarch
%{_mandir}/man8/livecd-creator.8*
%{_mandir}/man8/mkbiarch.8*


%files -n python-imgcreate-sysdeps
# No files because empty metapackage


%files -n python-imgcreate
%license COPYING
%doc API
%{python3_sitelib}/imgcreate

%ifarch %{ix86} %{x86_64}
%files -n livecd-iso-to-mediums
%license COPYING
%{_bindir}/livecd-iso-to-disk
%{_mandir}/man8/livecd-iso-to-disk.8*
%{_bindir}/livecd-iso-to-pxeboot
%endif
