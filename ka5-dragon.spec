%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		dragon
Summary:	Dragon Player
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Multimedia
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	249ba185726ca02ba03425a970d8e319
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	kf5-solid-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	phonon-qt5-devel >= 4.6.60
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dragon Player is a very simple Phonon-based media player. It was
originally developed by Max Howell and called Codeine. I ported it to
KDE 4.0 and on Max's suggestion renamed it to Video Player (probably,
I might still rename it.)

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/sr
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/dragonplayerrc
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/dragonpart.so
%{_desktopdir}/org.kde.dragonplayer.desktop
%{_iconsdir}/hicolor/128x128/apps/dragonplayer.png
%{_iconsdir}/hicolor/16x16/apps/dragonplayer.png
%{_iconsdir}/hicolor/22x22/apps/dragonplayer.png
%{_iconsdir}/hicolor/32x32/apps/dragonplayer.png
%{_iconsdir}/hicolor/48x48/apps/dragonplayer.png
%{_iconsdir}/hicolor/64x64/apps/dragonplayer.png
%{_iconsdir}/hicolor/scalable/apps/dragonplayer.svgz
%{_iconsdir}/oxygen/16x16/actions/player-volume-muted.png
%{_iconsdir}/oxygen/22x22/actions/player-volume-muted.png
%{_iconsdir}/oxygen/32x32/actions/player-volume-muted.png
%{_iconsdir}/oxygen/48x48/actions/player-volume-muted.png
%{_iconsdir}/oxygen/scalable/actions/player-volume-muted.svgz
%{_datadir}/kservices5/ServiceMenus/dragonplayer_play_dvd.desktop
%{_datadir}/kservices5/dragonplayer_part.desktop
%lang(ca) %{_mandir}/ca/man1/dragon.1*
%lang(de) %{_mandir}/de/man1/dragon.1*
%lang(es) %{_mandir}/es/man1/dragon.1*
%lang(et) %{_mandir}/et/man1/dragon.1*
%lang(fr) %{_mandir}/fr/man1/dragon.1*
%lang(it) %{_mandir}/it/man1/dragon.1*
%{_mandir}/man1/dragon.1*
%lang(nl) %{_mandir}/nl/man1/dragon.1*
%lang(pt) %{_mandir}/pt/man1/dragon.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/dragon.1*
%lang(sr) %{_mandir}/sr/man1/dragon.1*
%lang(sv) %{_mandir}/sv/man1/dragon.1*
%lang(tr) %{_mandir}/tr/man1/dragon.1*
%lang(uk) %{_mandir}/uk/man1/dragon.1*
%{_datadir}/metainfo/org.kde.dragonplayer.appdata.xml
%{_datadir}/solid/actions/dragonplayer-openaudiocd.desktop
%{_datadir}/solid/actions/dragonplayer-opendvd.desktop
