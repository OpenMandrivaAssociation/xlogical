%define    name   xlogical
%define    longname  XLogical
%define    majorversion   1.0
%define    subversion 8
%define    version %{majorversion}_%{subversion}
%define    sourceversion %{majorversion}-%{subversion}

%define    release %mkrel 6

Summary:   %{longname} - A puzzle game
Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{sourceversion}.tar.bz2
Source1:   %{name}-16.png
Source2:   %{name}-32.png
Source3:   %{name}-48.png
Patch0:    xlogical-c++-compil.patch
Group:     Games/Arcade
License: GPL
URL:        http://changeling.ixionstudios.com/xlogical/
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

%build

rm -f config.* configure

aclocal-1.4
automake-1.4 -a
autoconf

%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir

%make

%install
%makeinstall bindir=%buildroot%_gamesbindir datadir=%buildroot%_gamesdatadir

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
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
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



