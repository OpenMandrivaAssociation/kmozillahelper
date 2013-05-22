Summary:	Mozilla KDE Integration
Name:		kmozillahelper
Version:	0.6.3
Release:	3
License:	MIT
Group:		Graphical desktop/KDE 
Url:		http://www.opensuse.org/
Source0:	kmozillahelper-%{version}.tar.bz2

BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel

Provides:	mozilla-xulrunner191-kde4 = %{version}-release
Provides:	mozilla-xulrunner-kde4 = %{version}-release

%description
Package providing integration of Mozilla applications with KDE.

%files
%{_prefix}/lib/mozilla/kmozillahelper
%{_kde_appsdir}/kmozillahelper/kmozillahelper.notifyrc

#--------------------------------------------------------------------

%prep
%setup -qn kmozillahelper

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

