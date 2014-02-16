Summary:	Mozilla KDE Integration
Name:		kmozillahelper
Version:	0.6.4
Release:	1
License:	MIT
Group:		Graphical desktop/KDE
Url:		http://www.opensuse.org/
Source0:	kmozillahelper-%{version}.tar.bz2
Patch0:		kmozillahelper-0.6.4-setwallpaper.patch

BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel

Provides:	mozilla-xulrunner191-kde4 = %{version}-%{release}
Provides:	mozilla-xulrunner-kde4 = %{version}-%{release}
Requires:	qt4-qtdbus

%description
Package providing integration of Mozilla applications with KDE.

%files
%{_prefix}/lib/mozilla/kmozillahelper
%{_kde_appsdir}/kmozillahelper/kmozillahelper.notifyrc

#--------------------------------------------------------------------

%prep
%setup -qn kmozillahelper
%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

