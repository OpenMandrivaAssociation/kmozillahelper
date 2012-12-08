Summary:	Mozilla KDE Integration
Name:		kmozillahelper
Version:	0.6.3
Release:	3
License:	MIT
Group:		Graphical desktop/KDE 
Url:		http://www.opensuse.org/
Source:		kmozillahelper-%{version}.tar.bz2

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

%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.3-2mdv2011.0
+ Revision: 666031
- mass rebuild

* Wed Mar 16 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.3-1
+ Revision: 645354
- New version 0.6.3
  	* Remove P0: Merged Upstream

* Sat Aug 14 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 0.6.2-2mdv2011.0
+ Revision: 569542
- rebuild with new KDE to fix mozilla startup issue

* Sat May 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.2-1mdv2010.1
+ Revision: 544852
- New version 0.6.2

* Sat Feb 20 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6-2mdv2010.1
+ Revision: 508668
- Use firefox as default and not MozillaFirefox

* Sun Jan 24 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6-1mdv2010.1
+ Revision: 495393
- add kdelibs4-devel as buildrequire
- add kde4-macros as buildrequire
- Fix file list
- import kmozillahelper


