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
%define         _ver		3.1.91
%define         _snap		030918

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
# Source0-md5:	35ad2e12dec6a0dadc0c57b3dbe79b08
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

 - Aktion - odtwarzacz plików avi
 - Arts - narzêdzia arts
 - Kaboodle - odtwarzacz plików multimedialnych
 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD.
 - Noatun - odtwarzacz plików multimedialnych

%package devel
Summary:	kdemultimedia - headers
Summary(pl):	kdemultimedia - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-kscd = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun = %{epoch}:%{version}-%{release}

%description devel
kdemultimedia - headers.

%description devel -l pl
kdemultimedia - pliki nag³ówkowe.

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
Summary(pl):	Narzêdzia Arts
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-aktion

%description arts
Arts Tools.

%description arts -l pl
Narzêdzia Arts.

%package juk
Summary:        A jukebox like program
Summary(pl):    Program spe³niaj±cy funkcje szafy graj±cej
Group:          X11/Applications
Requires:       id3lib
Requires:       kdebase-core >= %{version}
Requires:       %{name}-mpeglib = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-aktion

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(r) or RealOne(r).

%description juk -l pl
Juk (czyt. d¿uk, jak w Jukebox) to szafa graj±ca i zarz±dca muzyki
dla KDE podobny do iTunes(r) lub RealOne(r).

%package kaboodle
Summary:	Media player
Summary(pl):	Odtwarzacz multimedialny
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description kaudiocreator
CD ripper and sound encoder frontend. Already provides audiocd
protocol for konqueror.

%description kaudiocreator -l pl
Nak³adka na CD ripper i enkoder d¼wiêku. Dostarcza równie¿ protokó³
audiocd do konquerora.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d¼wiêkowych
Group:		X11/Development/Libraries
Requires:	konqueror >= %{version}
Obsoletes:	kdemultimedia < 8:3.0.8
Obsoletes:	%{name}-aktion

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" konquerora
dodatkow± zak³adkê z rozszerzonymi informacjami o pliku.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntezator na karcie
muzycznej lub inne urz±dzenia MIDI przy³±czone do niej.

%package kmidi
Summary:	KDE software MIDI Player
Summary(pl):	Programowy odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description kmidi -l pl
Programowy odtwarzacz MIDI. Wykorzystuje patche z GUSa i moc procesora
do stworzenia dobrej jako¶ci d¼wiêku.

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mixer audio dla KDE
Group:		X11/Applications
Requires:       kdebase-kicker >= %{version}
Obsoletes:	%{name}-aktion

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d¼wiêku dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-aktion

%description krec
KDE sound recorder.

%description krec -l pl
Rejestrator d¼wiêku dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê
danych o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn±
graficzn± interpretacjê granych d¼wiêków.

%package libkcddb
Summary:        cddb library for KDE
Summary(pl):    Biblioteka cddb pod KDE
Group:          X11/Libraries
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description libkcddb
cddb library for KDE.

%description libkcddb -l pl
Biblioteka cddb pod KDE.

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	%{name}-aktion

%description mpeglib
MPEG lib.

%description mpeglib -l pl
MPEG lib.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plików multimedialnych
Group:		X11/Applications
Requires:       kdebase-core >= %{version}
Obsoletes:	%{name}-aktion

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plików multimedialnych.

%package xine
Summary:	Xine Plug-in
Summary(pl):	Wtyczka do Xine
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Requires:	xine-lib >= 1.0b4
Obsoletes:	%{name}-aktion

%description xine
Xine Plug-in.

%description xine -l pl
Wtyczka do Xine.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e "s/\[nb\]/\[no\]/g" $plik
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

%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-audio=$AUDIO

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
cat artsbuilder.lang > arts.lang
%find_lang juk		--with-kde
#%find_lang kaboodle	--with-kde
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

%post	arts 		-p /sbin/ldconfig
%postun	arts		-p /sbin/ldconfig

%post	kscd		-p /sbin/ldconfig
%postun	kscd		-p /sbin/ldconfig

%post	mpeglib		-p /sbin/ldconfig
%postun	mpeglib		-p /sbin/ldconfig

%post	libkcddb	-p /sbin/ldconfig
%postun	libkcddb	-p /sbin/ldconfig

%post	noatun		-p /sbin/ldconfig
%postun	noatun		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
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
%{_includedir}/libwm
%{_includedir}/mpeglib*
%{_includedir}/noatun

%files static
%defattr(644,root,root,755)
%{_libdir}/libworkmanaudio.a

%files arts -f arts.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arts*
%attr(755,root,root) %{_bindir}/midisend
%{_libdir}/libaudiofilearts.la
%attr(755,root,root) %{_libdir}/libaudiofilearts.so
%{_libdir}/libarts[!_]*.la
%attr(755,root,root) %{_libdir}/libartseffects.so
%attr(755,root,root) %{_libdir}/libarts[!_]*.so.*.*.*
%{_libdir}/libarts_splay.la
%attr(755,root,root) %{_libdir}/libarts_splay.so.*.*.*
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
%{_desktopdir}/kde/arts*.desktop
%{_iconsdir}/*/*/*/arts*

%files juk -f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_desktopdir}/kde/juk.desktop
%{_iconsdir}/*/*/*/juk*.png


#%files kaboodle -f kaboodle.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kaboodle
#%{_libdir}/kaboodle.la
#%attr(755,root,root) %{_libdir}/kaboodle.so
#%{_libdir}/kde3/libkaboodlepart.la
#%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
#%{_datadir}/apps/kaboodle
#%{_datadir}/services/kaboodle_component.desktop
#%{_datadir}/services/kaboodleengine.desktop
#%{_desktopdir}/kde/kaboodle.desktop
#%{_iconsdir}/*/*/apps/kaboodle.*

%files kaudiocreator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_libdir}/kde3/kcm_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%{_libdir}/kde3/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%{_datadir}/apps/kaudiocreator
%{_datadir}/services/audiocd.protocol
%{_desktopdir}/kde/kaudiocreator.desktop
%{_desktopdir}/kde/audiocd.desktop
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
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_libdir}/libworkman.la
%attr(755,root,root) %{_libdir}/libworkman.so.*.*.*
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
%{_libdir}/kde3/libkrecexport_ogg.la
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_ogg.so
%{_libdir}/kde3/libkrecexport_wave.la
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_wave.so
%{_datadir}/apps/krec
%{_datadir}/services/kcm_krec.desktop
%{_datadir}/services/kcm_krec_files.desktop
%{_datadir}/services/krec_exportogg.desktop
%{_datadir}/services/krec_exportwave.desktop
%{_datadir}/servicetypes/krec_exportitem.desktop
%{_desktopdir}/kde/krec.desktop
%{_iconsdir}/*/*/*/krec*

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_bindir}/yaf*
%{_libdir}/libyaf*.la
%attr(755,root,root) %{_libdir}/libyaf*.so.*.*.*
%{_libdir}/libarts_mpeglib.la
%attr(755,root,root) %{_libdir}/libarts_mpeglib-0.3.0.so.*.*.*
%{_libdir}/libmpeg.la
%attr(755,root,root) %{_libdir}/libmpeg-0.3.0.so
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
%{_libdir}/libkcddb.la
%attr(755,root,root) %{_libdir}/libkcddb.so.*.*.*
%{_libdir}/kde3/kcm_cddb.la
%attr(755,root,root) %{_libdir}/kde3/kcm_cddb.so
%{_desktopdir}/kde/libkcddb.desktop

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/libnoatun.la
%attr(755,root,root) %{_libdir}/libnoatun.so.*.*.*
%{_libdir}/libnoatunarts.la
%attr(755,root,root) %{_libdir}/libnoatunarts.so
%{_libdir}/libnoatuncontrols.la
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so.*.*.*
%{_libdir}/libnoatuntags.la
%attr(755,root,root) %{_libdir}/libnoatuntags.so.*.*.*
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
%{_desktopdir}/kde/noatun.desktop
%{_iconsdir}/*/*/*/noatun.png

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
