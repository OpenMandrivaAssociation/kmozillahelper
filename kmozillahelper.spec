Name:           kmozillahelper
License:        MIT
Group:          Graphical desktop/KDE 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Mozilla KDE Integration
Version:        0.6
Release:        %mkrel 1
Url:            http://www.opensuse.org/
Source:         kmozillahelper-%{version}.tar.bz2
Provides:       mozilla-xulrunner191-kde4 = %version-release
Provides:       mozilla-xulrunner-kde4 = %version-release

%description
Package providing integration of Mozilla applications with KDE.

%prep
%setup -qn kmozillahelper

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_libdir/mozilla/kmozillahelper
%_kde_appsdir/kmozillahelper/kmozillahelper.notifyrc
%exclude %_prefix/src/debug/kmozillahelper

