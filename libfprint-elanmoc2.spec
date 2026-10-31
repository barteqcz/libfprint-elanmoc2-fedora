Name:           libfprint-elanmoc2
Version:        1.94.9
Release:        %autorelease
Summary:        Toolkit for fingerprint scanners with ELAN MOC support
License:        LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/Depau/libfprint
Source0:        %{url}/-/archive/elanmoc2/libfprint-elanmoc2.tar.gz

ExcludeArch:    s390 s390x

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros

Provides:       libfprint = %{version}-%{release}
Provides:       libfprint%{?_isa} = %{version}-%{release}
Obsoletes:      libfprint

%description
Fork of libfprint with support for ELAN 0C4C and 0C00 Match-on-Chip fingerprint readers. Replaces the stock libfprint package.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libfprint-devel = %{version}-%{release}
Provides:       libfprint-devel%{?_isa} = %{version}-%{release}
Obsoletes:      libfprint-devel

%description devel
Development files for applications using libfprint.

%prep
%autosetup -n libfprint-elanmoc2

%build
%meson -Ddrivers=all -Dinstalled-tests=false -Ddoc=false
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libfprint-2.so.*
%{_libdir}/girepository-1.0/FPrint-2.0.typelib
%{_udevhwdbdir}/60-autosuspend-libfprint-2.hwdb
%{_udevrulesdir}/70-libfprint-2.rules
%{_datadir}/metainfo/org.freedesktop.libfprint.metainfo.xml

%files devel
%{_includedir}/libfprint-2/
%{_libdir}/libfprint-2.so
%{_libdir}/pkgconfig/libfprint-2.pc
%{_datadir}/gir-1.0/FPrint-2.0.gir

%changelog
%autochangelog
