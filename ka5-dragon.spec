%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		dragon
######		Unknown group!
######		Unknown group!
Summary:	Dragon Player
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Multimedia
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	8e38c3c28338792910798eed0861f88a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.31.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.31.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.31.0
BuildRequires:	kf5-kcrash-devel >= 5.31.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.31.0
BuildRequires:	kf5-kdoctools-devel >= 5.31.0
BuildRequires:	kf5-ki18n-devel >= 5.31.0
BuildRequires:	kf5-kio-devel >= 5.31.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.31.0
BuildRequires:	kf5-knotifications-devel >= 5.31.0
BuildRequires:	kf5-kparts-devel >= 5.31.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.31.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.31.0
BuildRequires:	kf5-kxmlgui-devel >= 5.31.0
BuildRequires:	kf5-solid-devel >= 5.31.0
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/dragonplayerrc
%attr(755,root,root) %{_bindir}/dragon
%attr(755,root,root) %{_libdir}/qt5/plugins/dragonpart.so
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
#%{_iconsdir}/oxygen/scalable/actions/player-volume-muted.svgz
%{_datadir}/kservices5/ServiceMenus/dragonplayer_play_dvd.desktop
%{_datadir}/kservices5/dragonplayer_part.desktop
%dir %{_datadir}/kxmlgui5/dragonplayer
%{_datadir}/kxmlgui5/dragonplayer/dragonlogo.png
%{_datadir}/kxmlgui5/dragonplayer/dragonplayerui.rc
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
