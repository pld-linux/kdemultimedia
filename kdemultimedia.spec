#
# Conditional build:
# --without	alsa	Set this option in case you don't want alsa.
#
# --with	esd	Set this option in case you want esd support.
#
# --with	nas 	Set this option if you want nas support.
#

%define         _state          snapshots
%define         _ver		3.1.92
%define         _snap		031014

%ifarch	sparc sparcv9 sparc64
%define		_with_esd	1
%define		_without_alsa	1
%endif

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		9
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:        http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	31e7deb9520a49d6fb34321e5468965c
Patch0:		%{name}-no_pedantic.patch
#Patch0:	%{name}-timidity.patch
#Patch1:	http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.1-video-20030316.patch
#Patch2:	http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.1-streaming-20030317.patch
#Patch2:	%{name}-streaming-fixed.patch
%{?_without_alsa:BuildConflicts:	alsa-driver-devel}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{?_with_nas:BuildRequires:	nas-devel >= 1.5}
%{?_with_esd:BuildRequires:     esound-devel}
BuildRequires:	Xaw3d-devel
BuildRequires:	cdparanoia-III
BuildRequires:	cdparanoia-III-devel
BuildRequires:	gettext-devel
# what for?
#BuildRequires:	gtk+-devel
BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires: 	libmusicbrainz-devel
BuildRequires:	libvorbis-devel
%{!?_without_xine:BuildRequires: xine-lib-devel >= 1.0b4}
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_chrpath		1

%description
KDE multimedia applications. Package includes:

 - Aktion - AVI player
 - Arts - arts tools
 - Kaboodle - a media player,
 - KMID - MIDI player,
 - KMIDI - software MIDI player,
 - KMIX - audio mixer,
 - KSCD - CD player,
 - Noatun - a media player.

%description -l pl
Multimedialne aplikacje KDE. Pakiet zawiera:

 - Aktion - odtwarzacz plik�w avi
 - Arts - narz�dzia arts
 - Kaboodle - odtwarzacz plik�w multimedialnych
 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD.
 - Noatun - odtwarzacz plik�w multimedialnych

%package devel
Summary:	kdemultimedia - headers
Summary(pl):	kdemultimedia - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}

%description devel
kdemultimedia - headers.

%description devel -l pl
kdemultimedia - pliki nag��wkowe.

%package static
Summary:	kdemultimedia - static libraries
Summary(pl):	kdemultimedia - biblioteki statyczne
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
kdemultimedia - static libraries.

%description static -l pl
kdemultimedia - biblioteki statyczne.

%package arts
Summary:	Arts Tools
Summary(pl):	Narz�dzia Arts
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description arts
Arts Tools.

%description arts -l pl
Narz�dzia Arts.

%package artsbuilder
Summary:	Arts Tools - builder
Summary(pl):	Narz�dzia Arts - builder
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-arts < 9:3.1.92.021012

%description artsbuilder
Arts Tools - builder.

%description artsbuilder -l pl
Narz�dzia Arts - builder.

%package artscontrol
Summary:	Arts Tools - control
Summary(pl):	Narz�dzia Arts - control
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-arts < 9:3.1.92.021012

%description artscontrol
Arts Tools - control.

%description artscontrol -l pl
Narz�dzia Arts - control.

%package artsplugin-audiofile
Summary:	Audiofile Plug-in
Summary(pl):	Wtyczka do Audiofile
Group:		X11/Applications
Requires:	audiofile
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-arts < 9:3.1.92.021012

%description artsplugin-audiofile
Audiofile Plug-in.

%description artsplugin-audiofile -l pl
Wtyczka do Audiofile.

%package artsplugin-xine
Summary:	Xine Plug-in
Summary(pl):	Wtyczka do Xine
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	xine-lib >= 1.0b4
Obsoletes:	%{name}-xine

%description artsplugin-xine
Xine Plug-in.

%description artsplugin-xine -l pl
Wtyczka do Xine.

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl):	Protok� audiocd dla konquerora
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	konqueror >= 9:%{version}
Obsoletes:	%{name}-kaudiocreator < 9:3.1.92.031014

%description audiocd
This package provides audiocd protocol for konqueror.

%description audiocd -l pl
Ten pakiet dostarcza protok� audiocd dla konquerora.

%package cddb
Summary:        cddb library for KDE
Summary(pl):    Biblioteka cddb pod KDE
Group:          X11/Applications
Requires:       kdebase-core >= 9:%{version}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libkcddb < 9:3.1.92.031014

%description cddb
CDDB control.

%description cddb -l pl
Sterowanie cddb.

%package juk
Summary:        A jukebox like program
Summary(pl):    Program spe�niaj�cy funkcje szafy graj�cej
Group:          X11/Applications
Requires:       id3lib
Requires:       kdebase-core >= 9:%{version}

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(r) or RealOne(r).

%description juk -l pl
Juk (czyt. d�uk, jak w Jukebox) to szafa graj�ca i zarz�dca muzyki
dla KDE podobny do iTunes(r) lub RealOne(r).

%package kaboodle
Summary:	Media player
Summary(pl):	Odtwarzacz multimedialny
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}

%description kaudiocreator
CD ripper and sound encoder frontend.

%description kaudiocreator -l pl
Nak�adka na CD ripper i enkoder d�wi�ku.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d�wi�kowych
Group:		X11/Development/Libraries
Requires:	konqueror >= %{version}
Obsoletes:	kdemultimedia < 8:3.0.8

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w�a�ciwo�ci pliku" konquerora
dodatkow� zak�adk� z rozszerzonymi informacjami o pliku.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntezator na karcie
muzycznej lub inne urz�dzenia MIDI przy��czone do niej.

#%package kmidi
#Summary:	KDE software MIDI Player
#Summary(pl):	Programowy odtwarzacz MIDI dla KDE
#Group:		X11/Applications
#Requires:       kdebase-core >= 9:%{version}
#
#%description kmidi
#Software MIDI player. It uses GUS patch files and CPU power to create
#high-quality sound.
#
#%description kmidi -l pl
#Programowy odtwarzacz MIDI. Wykorzystuje patche z GUSa i moc procesora
#do stworzenia dobrej jako�ci d�wi�ku.

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mixer audio dla KDE
Group:		X11/Applications
Requires:       kdebase-kicker >= 9:%{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d�wi�ku dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}
Requires:	%{name}-artscontrol = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}

%description krec
KDE sound recorder.

%description krec -l pl
Rejestrator d�wi�ku dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs�ug� CDDB. Automatycznie uaktualnia swoj� baz�
danych o p�ytach CD z Internetem. Potrafi tak�e wy�wietli� �adn�
graficzn� interpretacj� granych d�wi�k�w.

%package libkcddb
Summary:        A kcddb library
Summary(pl):    Biblioteka kcddb
Group:          X11/Libraries
Requires:       kdelibs >= 9:%{version}

%description libkcddb
A kcddb library.

%description libkcddb -l pl
Biblioteka kcddb.

%package libworkman
Summary:        A workman library
Summary(pl):    Biblioteka workman
Group:          X11/Libraries
Requires:       kdelibs >= 9:%{version}
Obsoletes:	%{name}-kscd < 9:3.1.92.031012

%description libworkman
A workman library.

%description libworkman -l pl
Biblioteka workman.

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description mpeglib
MPEG lib.

%description mpeglib -l pl
MPEG lib.

%package mpeglib-devel
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	%{name}-mpeglib-examples = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-mpeglib < 9:3.1.92.031012

%description mpeglib-devel
MPEG lib.

%description mpeglib-devel -l pl
MPEG lib.

%package mpeglib-examples
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-mpeglib < 9:3.1.92.031012

%description mpeglib-examples
MPEG lib.

%description mpeglib-examples -l pl
MPEG lib.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plik�w multimedialnych
Group:		X11/Applications
Requires:       kdebase-core >= 9:%{version}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plik�w multimedialnych.

%package noatun-libs
Summary:	KDE Media Player - shared libs
Summary(pl):	KDE Media Player - biblioteki wsp�dzielone
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-noatun < 9:3.1.92.031012

%description noatun-libs
KDE Media Player - shared libs.

%description noatun-libs -l pl
KDE Media Player - biblioteki wsp�dzielone.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build

for f in `find . -name *.desktop` ; do
	sed -i 's/\[nb\]/\[no\]/g' $f
done

AUDIO=""
%ifnarch sparc sparcv9 sparc64
AUDIO=oss,$AUDIO
%endif
%{?_with_esd:AUDIO=esd,$AUDIO}
%{?_with_nas:AUDIO=nas,$AUDIO}
AUDIO=${AUDIO%%,}

# kdemultimedia includes kernel headers which breaks thins, ugly workaround
rm -rf linux
mkdir linux
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
/usr/include/linux/cdrom.h > linux/cdrom.h

echo KDE_OPTIONS=nofinal >> juk/Makefile.am

%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-audio=$AUDIO \
	--enable-final \
%ifnarch sparc sparcv9 sparc64
	--with-alsa \
	--with-arts-alsa
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_docdir}/kde/HTML

#mv $RPM_BUILD_ROOT%{_bindir}/{timidity,ktimidity}

#cd $RPM_BUILD_ROOT%{_desktopdir}
#cat timidity.desktop |sed 's/Exec=timidity/Exec=ktimidity/' \
#    > ktimidity.desktop
#cd -

#cd $RPM_BUILD_ROOT%{_datadir}/apps/kmidi/config
#ln -s gravis.cfg GUSpatches
#cd -

%find_lang artsbuilder	--with-kde
%find_lang juk		--with-kde
%find_lang kaboodle	--with-kde
%find_lang kmid		--with-kde
%find_lang kmidi	--with-kde
%find_lang kmix		--with-kde
%find_lang kmixcfg	--with-kde
cat kmixcfg.lang >> kmix.lang
%find_lang krec		--with-kde
%find_lang kscd		--with-kde
%find_lang noatun	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	arts 			-p /sbin/ldconfig
%postun	arts			-p /sbin/ldconfig

%post	libkcddb		-p /sbin/ldconfig
%postun	libkcddb		-p /sbin/ldconfig

%post	libworkman		-p /sbin/ldconfig
%postun	libworkman		-p /sbin/ldconfig

%post	mpeglib			-p /sbin/ldconfig
%postun	mpeglib			-p /sbin/ldconfig

%post	mpeglib-examples	-p /sbin/ldconfig
%postun	mpeglib-examples	-p /sbin/ldconfig

%post	noatun-libs		-p /sbin/ldconfig
%postun	noatun-libs		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/arts/*
%{_includedir}/libkcddb
%{_includedir}/libwm
%{_includedir}/noatun
%{_libdir}/libartsbuilder.so
%{_libdir}/libartsgui.so
%{_libdir}/libartsgui_idl.so
%{_libdir}/libartsgui_kde.so
%{_libdir}/libartsmidi_idl.so
%{_libdir}/libartsmidi.so
%{_libdir}/libartsmodules*.so
%{_libdir}/libkcddb.so
%{_libdir}/libnoatun.so
%{_libdir}/libnoatuncontrols.so
%{_libdir}/libnoatuntags.so
%{_libdir}/libworkman.so
%{_libdir}/libyafcore.so
%{_libdir}/libyafxplayer.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libworkmanaudio.a

%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/midisend
%{_libdir}/libartsbuilder.la
%attr(755,root,root) %{_libdir}/libartsbuilder.so.*.*.*
%{_libdir}/libartscontrolapplet.la
%attr(755,root,root) %{_libdir}/libartscontrolapplet.so.*.*.*
%{_libdir}/libartscontrolsupport.la
%attr(755,root,root) %{_libdir}/libartscontrolsupport.so.*.*.*
%{_libdir}/libartseffects.la
%attr(755,root,root) %{_libdir}/libartseffects.so
%{_libdir}/libartsgui.la
%attr(755,root,root) %{_libdir}/libartsgui.so.*.*.*
%{_libdir}/libartsgui_idl.la
%attr(755,root,root) %{_libdir}/libartsgui_idl.so.*.*.*
%{_libdir}/libartsgui_kde.la
%attr(755,root,root) %{_libdir}/libartsgui_kde.so.*.*.*
%{_libdir}/libartsmidi.la
%attr(755,root,root) %{_libdir}/libartsmidi.so.*.*.*
%{_libdir}/libartsmidi_idl.la
%attr(755,root,root) %{_libdir}/libartsmidi_idl.so.*.*.*
%{_libdir}/libartsmodules.la
%attr(755,root,root) %{_libdir}/libartsmodules.so.*.*.*
%{_libdir}/libartsmodulescommon.la
%attr(755,root,root) %{_libdir}/libartsmodulescommon.so.*.*.*
%{_libdir}/libartsmoduleseffects.la
%attr(755,root,root) %{_libdir}/libartsmoduleseffects.so.*.*.*
%{_libdir}/libartsmodulesmixers.la
%attr(755,root,root) %{_libdir}/libartsmodulesmixers.so.*.*.*
%{_libdir}/libartsmodulessynth.la
%attr(755,root,root) %{_libdir}/libartsmodulessynth.so.*.*.*
%{_libdir}/mcop/Arts
%{_libdir}/mcop/artseffects.mcopclass
%{_libdir}/mcop/artseffects.mcoptype
%{_libdir}/mcop/artsgui.mcopclass
%{_libdir}/mcop/artsgui.mcoptype
%{_libdir}/mcop/artsmidi.mcopclass
%{_libdir}/mcop/artsmidi.mcoptype
%{_libdir}/mcop/artsmodules.mcopclass
%{_libdir}/mcop/artsmodules.mcoptype
%{_libdir}/mcop/artsmodulescommon.mcopclass
%{_libdir}/mcop/artsmodulescommon.mcoptype
%{_libdir}/mcop/artsmoduleseffects.mcopclass
%{_libdir}/mcop/artsmoduleseffects.mcoptype
%{_libdir}/mcop/artsmodulesmixers.mcopclass
%{_libdir}/mcop/artsmodulesmixers.mcoptype
%{_libdir}/mcop/artsmodulessynth.mcopclass
%{_libdir}/mcop/artsmodulessynth.mcoptype

%files artsbuilder -f artsbuilder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsbuilder
%{_libdir}/mcop/artsbuilder.mcopclass
%{_libdir}/mcop/artsbuilder.mcoptype
%{_datadir}/apps/artsbuilder
%{_datadir}/mimelnk/application/x-artsbuilder.desktop
%{_desktopdir}/kde/artsbuilder.desktop
%{_iconsdir}/crystalsvg/*/actions/artsbuilderexecute.png
%{_iconsdir}/crystalsvg/*/apps/artsbuilder.png

%files artscontrol
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscontrol
%{_datadir}/apps/artscontrol
%{_desktopdir}/kde/artscontrol.desktop
%{_iconsdir}/crystalsvg/*/apps/artscontrol.png

%files artsplugin-audiofile
%defattr(644,root,root,755)
%{_libdir}/libaudiofilearts.la
%attr(755,root,root) %{_libdir}/libaudiofilearts.so
%{_libdir}/mcop/audiofilearts.mcopclass
%{_libdir}/mcop/audiofilearts.mcoptype

%files artsplugin-xine
%defattr(644,root,root,755)
%{_libdir}/kde3/videothumbnail.la
%attr(755,root,root) %{_libdir}/kde3/videothumbnail.so
%{_libdir}/*_xine.la
%attr(755,root,root) %{_libdir}/*_xine.so
%{_libdir}/mcop/xinePlayObject.mcopclass
%{_datadir}/apps/videothumbnail
%{_datadir}/services/videothumbnail.desktop

%files audiocd
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%{_libdir}/kde3/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%{_datadir}/services/audiocd.protocol
%{_desktopdir}/kde/audiocd.desktop

%files cddb
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_cddb.la
%attr(755,root,root) %{_libdir}/kde3/kcm_cddb.so
%{_datadir}/config.kcfg/libkcddb.kcfg
%{_desktopdir}/kde/libkcddb.desktop

%files juk -f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_desktopdir}/kde/juk.desktop
%{_iconsdir}/*/*/*/juk*.png

%files kaboodle -f kaboodle.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaboodle
%{_libdir}/kaboodle.la
%attr(755,root,root) %{_libdir}/kaboodle.so
%{_libdir}/kde3/libkaboodlepart.la
%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_datadir}/services/kaboodleengine.desktop
%{_desktopdir}/kde/kaboodle.desktop
%{_iconsdir}/*/*/apps/kaboodle.*

%files kaudiocreator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_datadir}/apps/kaudiocreator
%{_desktopdir}/kde/kaudiocreator.desktop
%{_iconsdir}/[!l]*/*/*/kaudiocreator.png

%files kfile
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile_*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kmid -f kmid.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%{_libdir}/kde3/libkmidpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmidpart.so
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_desktopdir}/kde/kmid.desktop
%{_iconsdir}/*/*/*/kmid.png

#%files kmidi -f kmidi.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kmidi
#%attr(755,root,root) %{_bindir}/sf2cfg
#%attr(755,root,root) %{_bindir}/ktimidity
#%{_desktopdir}/kmidi.desktop
#%{_desktopdir}/ktimidity.desktop
#%{_datadir}/apps/kmidi
#%{_iconsdir}/*/*/*/kmidi.png

%files kmix -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%{_libdir}/libkdeinit_kmix.la
%attr(755,root,root) %{_libdir}/libkdeinit_kmix.so
%{_libdir}/libkdeinit_kmixctrl.la
%attr(755,root,root) %{_libdir}/libkdeinit_kmixctrl.so
%{_libdir}/kde3/kmix.la
%attr(755,root,root) %{_libdir}/kde3/kmix.so
%{_libdir}/kde3/kmixctrl.la
%attr(755,root,root) %{_libdir}/kde3/kmixctrl.so
%{_libdir}/kde3/kcm_kmix.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmix.so
%{_libdir}/kde3/kmix_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so
%{_desktopdir}/kde/kmix.desktop
%{_desktopdir}/kde/kmixcfg.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_datadir}/apps/kmix
%{_datadir}/apps/kicker/applets/*
%{_iconsdir}/*/*/*/kmix.png

%files kscd -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddaslave
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_desktopdir}/kde/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/apps/profiles/kscd.profile.xml
%{_datadir}/mimelnk/text/xmcd.desktop
%{_iconsdir}/*/*/*/kscd.png

%files krec -f krec.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krec
%{_libdir}/libkdeinit_krec.la
%attr(755,root,root) %{_libdir}/libkdeinit_krec.so
%{_libdir}/kde3/kcm_krec.la
%attr(755,root,root) %{_libdir}/kde3/kcm_krec.so
%{_libdir}/kde3/kcm_krec_files.la
%attr(755,root,root) %{_libdir}/kde3/kcm_krec_files.so
%{_libdir}/kde3/krec.la
%attr(755,root,root) %{_libdir}/kde3/krec.so
%{_libdir}/kde3/libkrecexport_mp3.la
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_mp3.so
%{_libdir}/kde3/libkrecexport_ogg.la
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_ogg.so
%{_libdir}/kde3/libkrecexport_wave.la
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_wave.so
%{_datadir}/apps/krec
%{_datadir}/services/kcm_krec.desktop
%{_datadir}/services/kcm_krec_files.desktop
%{_datadir}/services/krec_exportmp3.desktop
%{_datadir}/services/krec_exportogg.desktop
%{_datadir}/services/krec_exportwave.desktop
%{_datadir}/servicetypes/krec_exportitem.desktop
%{_desktopdir}/kde/krec.desktop
%{_iconsdir}/*/*/*/krec*

%files libkcddb
%defattr(644,root,root,755)
%{_libdir}/libkcddb.la
%attr(755,root,root) %{_libdir}/libkcddb.so.*.*.*

%files libworkman
%defattr(644,root,root,755)
%{_libdir}/libworkman.la
%attr(755,root,root) %{_libdir}/libworkman.so.*.*.*

%files mpeglib
%defattr(644,root,root,755)
# mpeglib part
%{_libdir}/libmpeg.la
%attr(755,root,root) %{_libdir}/libmpeg-0.3.0.so
# mpeglib_artsplug part
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%{_libdir}/libarts_mpeglib.la
%attr(755,root,root) %{_libdir}/libarts_mpeglib-0.3.0.so.*.*.*
%{_libdir}/libarts_splay.la
%attr(755,root,root) %{_libdir}/libarts_splay.so.*.*.*
%{_libdir}/mcop/CDDAPlayObject.mcopclass
%{_libdir}/mcop/MP3PlayObject.mcopclass
%{_libdir}/mcop/NULLPlayObject.mcopclass
%{_libdir}/mcop/OGGPlayObject.mcopclass
%{_libdir}/mcop/SplayPlayObject.mcopclass
%{_libdir}/mcop/WAVPlayObject.mcopclass

%files mpeglib-devel
%defattr(644,root,root,755)
%{_includedir}/mpeglib
%{_includedir}/mpeglib_artsplug
%{_libdir}/libarts_mpeglib.so
%{_libdir}/libarts_splay.so
%{_libdir}/libmpeg.so

%files mpeglib-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yaf-cdda
%attr(755,root,root) %{_bindir}/yaf-mpgplay
%attr(755,root,root) %{_bindir}/yaf-splay
%attr(755,root,root) %{_bindir}/yaf-tplay
%attr(755,root,root) %{_bindir}/yaf-vorbis
%attr(755,root,root) %{_bindir}/yaf-yuv
%{_libdir}/libyafcore.la
%attr(755,root,root) %{_libdir}/libyafcore.so.0.0.0
%{_libdir}/libyafxplayer.la
%attr(755,root,root) %{_libdir}/libyafxplayer.so.0.0.0

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/kde3/noatun*.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.so
%{_libdir}/mcop/Noatun
%{_libdir}/mcop/ExtraStereo.mcopclass
%{_libdir}/mcop/ExtraStereoGuiFactory.mcopclass
%{_libdir}/mcop/RawWriter.mcopclass
%{_libdir}/mcop/VoiceRemoval.mcopclass
%{_libdir}/mcop/noatunarts.mcopclass
%{_libdir}/mcop/noatunarts.mcoptype
%{_libdir}/mcop/winskinvis.mcopclass
%{_libdir}/mcop/winskinvis.mcoptype
%attr(755,root,root) %{_datadir}/apps/kconf_update/noatun20update
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/noatun*
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop
%{_desktopdir}/kde/noatun.desktop
%{_iconsdir}/*/*/*/noatun.png

%files noatun-libs
%defattr(644,root,root,755)
%{_libdir}/libnoatun.la
%attr(755,root,root) %{_libdir}/libnoatun.so.*.*.*
%{_libdir}/libnoatuncontrols.la
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so.*.*.*
%{_libdir}/libnoatuntags.la
%attr(755,root,root) %{_libdir}/libnoatuntags.so.*.*.*
%{_libdir}/libnoatunarts.la
%attr(755,root,root) %{_libdir}/libnoatunarts.so
%{_libdir}/libwinskinvis.la
%attr(755,root,root) %{_libdir}/libwinskinvis.so
