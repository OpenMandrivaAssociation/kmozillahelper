Name:           kmozillahelper
License:        MIT
Group:          Graphical desktop/KDE 
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Mozilla KDE Integration
Version:        0.6.2
Release:        %mkrel 1
Url:            http://www.opensuse.org/
Source:         kmozillahelper-%{version}.tar.bz2
Patch0:         kmozillahelper-use-firefox.patch

BuildRequires:  kde4-macros
BuildRequires:  kdelibs4-devel

Provides:       mozilla-xulrunner191-kde4 = %version-release
Provides:       mozilla-xulrunner-kde4 = %version-release

%description
Package providing integration of Mozilla applications with KDE.

%files
%defattr(-,root,root)
%_prefix/lib/mozilla/kmozillahelper
%_kde_appsdir/kmozillahelper/kmozillahelper.notifyrc
%exclude %_prefix/src/debug/kmozillahelper

#--------------------------------------------------------------------

%prep
%setup -qn kmozillahelper
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

