%define    name   xlogical
%define    longname  XLogical
%define    majorversion   1.0
%define    subversion 8
%define    version %{majorversion}_%{subversion}
%define    sourceversion %{majorversion}-%{subversion}

%define    release %mkrel 9 

Summary:   %{longname} - A puzzle game
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{sourceversion}.tar.bz2
Source1:   %{name}-16.png
Source2:   %{name}-32.png
Source3:   %{name}-48.png
Patch0:    xlogical-c++-compil.patch
Patch1:    xlogical-gcc43.patch
Group:     Games/Puzzles
License: GPLv2+
URL:        https://changeling.ixionstudios.com/xlogical/
BuildRoot: %_tmppath/%{name}-build
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: autoconf2.5
BuildRequires: automake1.4

%description
XLogical is a puzzle game based on an Amiga game developed
by Rainbow Arts called Logical. It features ray-traced graphics,
music, and sound effects. The game is addictive, requiring
parallel thinking and quick reflexes.

%prep
%setup -n %{name}-%{sourceversion} -q
%patch0 -p0 -b .nanar
%patch1 -p1 -b .gcc43

%build

rm -f config.* configure

aclocal-1.4
autoconf
automake-1.4 -a

%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --localstatedir=%{_localstatedir}/lib

%make

%install
%makeinstall bindir=%buildroot%_gamesbindir datadir=%buildroot%_gamesdatadir localstatedir=%buildroot%{_localstatedir}/lib

install -D -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A puzzle game
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF

%files
%defattr(-,root,games)
%doc README COPYING ChangeLog AUTHORS NEWS TODO LICENSE
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%dir %{_localstatedir}/lib/%{name}
%{_localstatedir}/lib/%{name}/xlogical.scores
%{_liconsdir}/*.png
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_datadir}/applications/mandriva-%{name}.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Fri May 22 2009 Samuel Verschelde <stormi@mandriva.org> 1.0_8-9mdv2010.0
+ Revision: 378776
- fix autotools order

* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.0_8-8mdv2010.0
+ Revision: 375762
- fix highscores

* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.0_8-7mdv2010.0
+ Revision: 375700
- fix paths
- fix build
- fix Group and category

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild
    - drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.0_8-3mdv2008.1
+ Revision: 136608
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix autoconf-2.5x path
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Mon Jan 15 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0_8-3mdv2007.0
+ Revision: 108980
- buildrequires
- rebuild

* Sat Sep 09 2006 Olivier Thauvin <nanardon@mandriva.org> 1.0_8-2mdv2007.0
+ Revision: 60632
- fix menu (use summary macros)

* Sun Jul 16 2006 Olivier Thauvin <nanardon@mandriva.org> 1.0_8-1mdv2007.0
+ Revision: 41284
- fix patch to make it compil (couriousous)
- 1.0-8
- Import xlogical

* Wed Jun 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0-7.cvs20030522.4mdk
- rebuild
- fix build

