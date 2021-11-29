Summary:	Mozilla KDE Integration
Name:		kmozillahelper
Version:	5.0.6
Release:	1
License:	MIT
Group:		Graphical desktop/KDE
Url:		http://www.opensuse.org/
Source0:	kmozillahelper-%{version}.tar.gz

BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5I18n)

%description
Package providing integration of Mozilla applications with KDE.

%files
%{_prefix}/lib/mozilla/kmozillahelper
%{_datadir}/knotifications5/kmozillahelper.notifyrc
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

