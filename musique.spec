%global	debug_package	%{nil}

Summary:	Lightweight music player
Name:	musique
Version:	1.12
Release:	1
Group:	Sound
License:	GPLv3+
Url:		https://flavio.tordini.org/musique
Source0:	https://github.com/flaviotordini/musique/archive/%{name}-%{version}.tar.bz2
Patch0:		musique-taglib2.patch
BuildRequires:	make
BuildRequires:	qmake-qt6
BuildRequires:	qt6-qttools-linguist-tools
BuildRequires:	qt6-qtdeclarative
BuildRequires:	pkgconfig(mpv)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6QmlIntegration)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(taglib)
Requires:	mpv

%description
Musique is a lightweight and versatile music player for QT6.

%files
%doc CHANGES
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/locale/*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# No equivalent of %%qmake_qt5 for Qt6: open code it...
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -Wl,-Bsymbolic-functions"
/usr/bin/qmake-qt6 \
%if "lib64" != "lib"
	libsuff=64 \
%endif
	QMAKE_CFLAGS="$CFLAGS" \
	QMAKE_CFLAGS_RELEASE="$CFLAGS" \
	QMAKE_CFLAGS_OPTIMIZE="$CFLAGS" \
	QMAKE_CFLAGS_OPTIMIZE_FULL="$CFLAGS" \
	QMAKE_CXXFLAGS="$CXXFLAGS" \
	QMAKE_CXXFLAGS_RELEASE="$CXXFLAGS" \
	QMAKE_LFLAGS="$LDFLAGS" \
	QMAKE_LFLAGS_RELEASE="$LDFLAGS" \
	QMAKE_LRELEASE="%{_libdir}/qt6/bin/lrelease" \
	PREFIX=%{_prefix}
	
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}
