#
# Conditional build:
# --without	alsa	Set this option in case you don't want alsa.
#
# --with	esd	Set this option in case you want esd support.
#
# --with	nas 	Set this option if you want nas support.
#
# --without	xine	Set this option in case You haven't
#			xine-lib to ommit xine plug-in building.
#

%define         _state          snapshots
%define         _ver		3.2
%define         _snap		030406

%ifarch	sparc sparcv9 sparc64
%define		_with_esd	1
%define		_without_alsa	1
%endif

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:        http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-timidity.patch
Patch1:		http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.1-video-20030316.patch
#Patch2:	http://rambo.its.tudelft.nl/~ewald/xine/%{name}-3.1.1-streaming-20030317.patch
Patch2:		%{name}-streaming-fixed.patch 
%{?_without_alsa:BuildConflicts:	alsa-driver-devel}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{?_with_nas:BuildRequires:	nas-devel >= 1.5}
%{?_with_esd:BuildRequires:     esound-devel}
BuildRequires:	Xaw3d-devel
BuildRequires:	arts-devel
BuildRequires:	arts-kde-devel
BuildRequires:	cdparanoia-III
BuildRequires:	cdparanoia-III-devel
BuildRequires:	gettext-devel
# what for?
#BuildRequires:	gtk+-devel
BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
%{!?_without_xine:BuildRequires: xine-lib-devel >= 1.0b4}
BuildRequires:	zlib-devel
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

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
Requires:	arts-devel >= 1.0.3
Requires:	kdelibs-devel >= %{version}
Requires:	%{name}-aktion = %{version}
Requires:	%{name}-arts = %{version}
Requires:	%{name}-kscd = %{version}
Requires:	%{name}-libkcddb = %{version}
Requires:	%{name}-mpeglib = %{version}
Requires:	%{name}-noatun = %{version}

%description devel
kdemultimedia - headers.

%description devel -l pl
kdemultimedia - pliki nag��wkowe.

%package static
Summary:	kdemultimedia - static libraries
Summary(pl):	kdemultimedia - biblioteki statyczne
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
kdemultimedia - static libraries.

%description static -l pl
kdemultimedia - biblioteki statyczne.

%package aktion
Summary:	KDE Media Player
Summary(pl):	Odtwarzacz multimedialny dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	aktion

%description aktion
This is a media player for KDE. Currently it can be only used to play
WAV files.

%description aktion -l pl
Odtwarzacz multimedialny dla KDE. W tej chwili obs�uguje tylko pliki
WAV.

%package arts
Summary:	Arts Tools
Summary(pl):	Narz�dzia Arts
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	%{name}-mpeglib = %{version}

%description arts
Arts Tools.

%description arts -l pl
Narz�dzia Arts.

%package juk
Summary:        A jukebox like program
Summary(pl):    Program spe�niaj�cy funkcje szafy graj�cej
Group:          X11/Applications
Requires:       kdelibs >= %{version}
Requires:       %{name}-mpeglib = %{version}

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

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications

%description kaudiocreator
CD ripper and sound encoder frontend. Already provides audiocd
protocol for konqueror.

%description kaudiocreator -l pl
Nak�adka na CD ripper i enkoder d�wi�ku. Dostarcza r�wnie� protok�
audiocd do konquerora.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d�wi�kowych
Group:		X11/Development/Libraries
Obsoletes:	kdemultimedia < 3.0.8

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
Requires:	kdelibs >= %{version}

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntezator na karcie
muzycznej lub inne urz�dzenia MIDI przy��czone do niej.

%package kmidi
Summary:	KDE software MIDI Player
Summary(pl):	Programowy odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description kmidi -l pl
Programowy odtwarzacz MIDI. Wykorzystuje patche z GUSa i moc procesora
do stworzenia dobrej jako�ci d�wi�ku.

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mixer audio dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d�wi�ku dla KDE
Group:		X11/Applications
Requires:	%{name}-arts = %{version}
Requires:	kdelibs >= %{version}

%description krec
KDE sound recorder.

%description krec -l pl
Rejestrator d�wi�ku dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	kdelibs >= %{version}

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs�ug� CDDB. Automatycznie uaktualnia swoj� baz�
danych o p�ytach CD z Internetem. Potrafi tak�e wy�wietli� �adn�
graficzn� interpretacj� granych d�wi�k�w.

%package libkcddb
Summary:        cddb library for KDE
Summary(pl):    Biblioteka cddb pod KDE
Group:          X11/Libraries
Requires:       kdelibs >= %{version}
Requires:       arts >= 1.0.0

%description libkcddb
cddb library for KDE.

%description libkcddb -l pl
Biblioteka cddb pod KDE.

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	arts >= 1.0.0

%description mpeglib
MPEG lib.

%description mpeglib -l pl
MPEG lib.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plik�w multimedialnych
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	arts >= 1.0.0

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plik�w multimedialnych.

%package xine
Summary:	Xine Plug-in
Summary(pl):	Wtyczka do Xine
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	arts >= 1.0.0
Requires:	xine-lib >= 1.0b4

%description xine
Xine Plug-in.

%description xine -l pl
Wtyczka do Xine.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        PNGCFLAGS=" `pkg-config libpng12 --cflags`"
fi
	

CFLAGS="%{rpmcflags} -I%{_includedir}"

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

%{__make} -f Makefile.cvs

%configure \
 	--with-pam="yes" \
	--enable-final \
	--enable-audio=$AUDIO
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/{timidity,ktimidity}    

install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE
mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Settings/Sound,Settings/KDE/}

cd $RPM_BUILD_ROOT%{_desktopdir}
cat timidity.desktop |sed 's/Exec=timidity/Exec=ktimidity/' \
    > ktimidity.desktop
cd -

cd $RPM_BUILD_ROOT%{_datadir}/apps/kmidi/config
ln -s gravis.cfg GUSpatches
cd -

%find_lang aktion	--with-kde
%find_lang artsbuilder	--with-kde
cat artsbuilder.lang > arts.lang
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

%post arts
echo "Remember to restart artsd !"

%post   mpeglib -p /sbin/ldconfig
%postun mpeglib -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_libdir}/libaktion.so
%{_libdir}/libarts_mpeglib.so
%{_libdir}/libarts_splay.so
%{_libdir}/libartsbuilder.so
%{_libdir}/libartsgui.so
%{_libdir}/libartsgui_idl.so
%{_libdir}/libartsgui_kde.so
%{_libdir}/libartsmidi_idl.so
%{_libdir}/libartsmidi.so
%{_libdir}/libartsmodules*.so
%{_libdir}/libkcddb.so
%{_libdir}/libmpeg.so
%{_libdir}/libnoatun.so
%{_libdir}/libnoatuncontrols.so
%{_libdir}/libnoatuntags.so
%{_libdir}/libworkman.so
%{_libdir}/libyafcore.so
%{_libdir}/libyafxplayer.so
%{_includedir}/*.h
%{_includedir}/arts/*
%{_includedir}/libkcddb/*
%{_includedir}/mpeglib*
%{_includedir}/noatun

%files static
%defattr(644,root,root,755)
%{_libdir}/libworkmanaudio.a

%files aktion -f aktion.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aktion*
%{_libdir}/libaktion.la
%attr(755,root,root) %{_libdir}/libaktion.so.*
%{_datadir}/apps/aktion
%{_datadir}/config/aktionrc
%{_desktopdir}/aktion.desktop
%{_pixmapsdir}/*/*/apps/aktion.png

%files arts -f arts.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arts*
%attr(755,root,root) %{_bindir}/midisend
%{_libdir}/libaudiofilearts.la
%attr(755,root,root) %{_libdir}/libaudiofilearts.so
%{_libdir}/libarts[!_]*.la
%attr(755,root,root) %{_libdir}/libartseffects.so
%attr(755,root,root) %{_libdir}/libarts[!_]*.so.*
%{_libdir}/libarts_[!mx]*.la
%attr(755,root,root) %{_libdir}/libarts_[!m]*.so.*
%{_libdir}/mcop/audiofilearts*
%{_libdir}/mcop/arts*
%{_libdir}/mcop/Splay*
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/ExtraStereo.mcopclass
%{_libdir}/mcop/ExtraStereoGuiFactory.mcopclass
%{_libdir}/mcop/VoiceRemoval.mcopclass
%{_libdir}/mcop/RawWriter.mcopclass
%{_datadir}/apps/artsbuilder
%{_datadir}/apps/artscontrol
%{_datadir}/mimelnk/application/*arts*
%{_desktopdir}/arts*.desktop
%{_pixmapsdir}/*/*/*/arts*

%files juk -f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_desktopdir}/juk.desktop
%{_pixmapsdir}/*/*/*/juk.png


%files kaboodle -f kaboodle.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaboodle
%{_libdir}/kaboodle.la
%attr(755,root,root) %{_libdir}/kaboodle.so
%{_libdir}/kde3/libkaboodlepart.la
%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_desktopdir}/kaboodle.desktop
%{_pixmapsdir}/*/*/apps/kaboodle.*

%files kaudiocreator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_libdir}/kde3/kcm_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%{_libdir}/kde3/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%{_datadir}/apps/kaudiocreator
%{_datadir}/services/audiocd.protocol
%{_desktopdir}/kaudiocreator.desktop
%{_applnkdir}/Settings/KDE/Sound/audiocd.desktop
%{_pixmapsdir}/[!l]*/*/*/kaudiocreator.png

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
%{_desktopdir}/kmid.desktop
%{_pixmapsdir}/*/*/*/kmid.png

%files kmidi -f kmidi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmidi
%attr(755,root,root) %{_bindir}/sf2cfg
%attr(755,root,root) %{_bindir}/ktimidity
%{_desktopdir}/kmidi.desktop
%{_desktopdir}/ktimidity.desktop
%{_datadir}/apps/kmidi
%{_pixmapsdir}/*/*/*/kmidi.png

%files kmix -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%{_libdir}/kmix.la
%attr(755,root,root) %{_libdir}/kmix.so
%{_libdir}/kmixctrl.la
%attr(755,root,root) %{_libdir}/kmixctrl.so
%{_libdir}/kde3/kcm_kmix.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmix.so
%{_libdir}/kde3/kmix_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so
%{_desktopdir}/kmix.desktop
%{_applnkdir}/.hidden/kmixcfg.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_datadir}/apps/kmix
%{_datadir}/apps/kicker/applets/*
%{_pixmapsdir}/*/*/*/kmix.png

%files kscd -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_libdir}/libworkman.la
%attr(755,root,root) %{_libdir}/libworkman.so.*
%{_desktopdir}/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/mimelnk/text/xmcd.desktop
%{_pixmapsdir}/*/*/*/kscd.png

%files krec -f krec.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krec
%{_libdir}/krec.la
%attr(755,root,root) %{_libdir}/krec.so
%{_datadir}/apps/krec
%{_desktopdir}/krec.desktop
%{_pixmapsdir}/*/*/*/krec*

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_bindir}/yaf*
%{_libdir}/libyaf*.la
%attr(755,root,root) %{_libdir}/libyaf*.so.*
%{_libdir}/libarts_mpeglib.la
%attr(755,root,root) %{_libdir}/libarts_mpeglib*.so.*
%{_libdir}/libmpeg.la
%attr(755,root,root) %{_libdir}/libmpeg-*.so
# Note that SplayPlayObject.mopclass is *not* here.
#%%{_libdir}/mcop/VCDPlayObject.mcopclass
%{_libdir}/mcop/WAVPlayObject.mcopclass
%{_libdir}/mcop/OGGPlayObject.mcopclass
%{_libdir}/mcop/NULLPlayObject.mcopclass
%{_libdir}/mcop/MP3PlayObject.mcopclass
%{_libdir}/mcop/CDDAPlayObject.mcopclass
#%%{_libdir}/mcop/MPGPlayObject.mcopclass

%files libkcddb 
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcddb.so.1.0.0
%{_libdir}/libkcddb.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_cddb_config.so
%{_libdir}/kde3/libkcm_cddb_config.la
%{_applnkdir}/Settings/KDE/Sound/cddb.desktop

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/libnoatun*.la
%attr(755,root,root) %{_libdir}/libnoatun*.so.*
%attr(755,root,root) %{_libdir}/libnoatunarts.so
%{_libdir}/libwinskinvis.la
%attr(755,root,root) %{_libdir}/libwinskinvis.so
%{_libdir}/kde3/noatun*.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.so
%{_libdir}/mcop/Noatun
%{_libdir}/mcop/noatun*
%{_libdir}/mcop/winskinvis*
%attr(755,root,root) %{_datadir}/apps/kconf_update/noatun20update
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/noatun*
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop
%{_desktopdir}/noatun.desktop
%{_pixmapsdir}/*/*/*/noatun.png

%if %{?_without_xine:0}%{!?_without_xine:1}
%files xine
%defattr(644,root,root,755)
%{_libdir}/kde3/videothumbnail.la
%attr(755,root,root) %{_libdir}/kde3/videothumbnail.so
%{_libdir}/*_xine.la
%attr(755,root,root) %{_libdir}/*_xine.so
%{_libdir}/mcop/xinePlayObject.mcopclass
%{_datadir}/apps/videothumbnail
%{_datadir}/services/videothumbnail.desktop
%endif
