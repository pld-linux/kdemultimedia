#
# Conditional build:
%bcond_without	alsa	# build without ALSA support
%bcond_without	xine	# build without xine support

%define		_state		stable
%define		_ver		3.3.1

%define		_minlibsevr	9:3.3.1
%define		_minbaseevr	9:3.3.1

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}
Release:	1
Epoch:		9
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	4a3462ba7b37e0057eadd24541908f95
# Source0-size:	5362949
Patch100:	%{name}-branch.diff
Patch0:		%{name}-llh.patch
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	arts-qt-devel
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libmusicbrainz-devel >= 1:2.1.1
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel >= 0.95.031114
BuildRequires:	unsermake >= 040511
%{?with_xine:BuildRequires:	xine-lib-devel >= 1:1.0}
BuildRequires:	speex-devel
BuildRequires:	flac-devel
BuildRequires:	libmad-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE multimedia applications. Package includes:

 - Arts - arts tools
 - Kaboodle - a media player,
 - KMID - MIDI player,
 - KMIDI - software MIDI player,
 - KMIX - audio mixer,
 - KSCD - CD player,
 - Noatun - a media player.

%description -l pl
Multimedialne aplikacje KDE. Pakiet zawiera:

 - Arts - narzêdzia arts,
 - Kaboodle - odtwarzacz plików multimedialnych,
 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD,
 - Noatun - odtwarzacz plików multimedialnych.

%package devel
Summary:	Header files for kdemultimedia libraries
Summary(pl):	Pliki nag³ówkowe bibliotek kdemultimedia
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{_minlibsevr}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-static

%description devel
Header files for kdemultimedia libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek kdemultimedia

%package akode
Summary:	A new generation arts plugin with high quality support for many formats.
Summary(pl):	Wtyczka do arts nowej generacji z wysokiej jako¶ci obs³ug± ró¿nych formatów .
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}

%description akode
Arts plugin that supports high quality playback of the following
formats:
- musepack (.mpc)
- mpeg (.MP3,.MP2, etc.)
- ogg vorbis (.ogg)
- flac
- speex
- WAV


%description akode -l pl
Wtyczka arts, która wspiera wysokiej jako¶ci odtwarzanie nastêpuj±cych
formatów:
- musepack (.mpc)
- mpeg (.MP3,.MP2, etc.)
- ogg vorbis (.ogg)
- flac
- speex
- WAV


%package arts
Summary:	Arts extensions
Summary(pl):	Rozszerzenia Arts
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdemultimedia-artsplugin-audiofile

%description arts
Arts extensions such as effect definitions, mixers presets and shared
libraries to access them.

%description arts -l pl
Rozszerzenia Arts takie jak definicje efektów, ustawienia mikserów
oraz biblioteki wspó³dzielone daj±ce do nich dostêp.

%package artsbuilder
Summary:	Arts Tools - builder
Summary(pl):	Narzêdzia Arts - builder
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-arts < 9:3.1.92.021012

%description artsbuilder
A simple yet powerful effect and filter builder for arts.

%description artsbuilder -l pl
Prosty acz rozbudowany program do konstruowania efektów i filtrów w
arts.

%package artscontrol
Summary:	Arts Tools - control
Summary(pl):	Narzêdzia Arts - control
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-arts < 9:3.1.92.021012

%description artscontrol
An advanced configuration tool for arts with FFT scope, media type
list, midi manager, client and environment manager and a server status
reporter

%description artscontrol -l pl
Zaawansowane narzêdzie konfiguracyjne dla arts, zawiera: okno zakresu
FFT, listê obs³ugiwanych typów plików, modu³y zarz±dzania klientami,
midi oraz ¶rodowiskiem, a tak¿e monitor stanu serwera d¼wiêku.

#%package artsplugin-audiofile 
#Summary: Audiofile Plug-in
#Summary(pl): Wtyczka do Audiofile 
#Group: X11/Applications 
#Requires: %{name}-arts = %{epoch}:%{version}-%{release} 
#Obsoletes:kdemultimedia-arts < 9:3.1.92.021012

#%description artsplugin-audiofile #Audiofile Plug-in.

#%description artsplugin-audiofile -l pl #Wtyczka do Audiofile.

%package artsplugin-xine
Summary:	Xine engine plugin for arts
Summary(pl):	Wtyczka silnika xine do arts
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	xine-lib >= 1:1.0
Obsoletes:	kdemultimedia-xine

%description artsplugin-xine
This plugin allows arts to play using xine engine. This plugin
supports more formats then akode, yet akode plays some of them with
better quality. For best quality use akode alongside this plugin, arts
will autodetect which plugin gives better quality. This plugin
supports:
- microsoft's windows media formats (asf,asx,wmv,wma)
- mpeg (vob,mpg,mpeg,m1v,m2v,m1s,m2s,m2p,MP4,MP3,MP2,mp1)
- divx and avi
- quicktime (qt,mov,moov)
- real.com formats (rv,ra,ram,rm)
- smil (.smi)
- flac
- speex
- ac3/aac/m4v/m4a
- ogg vorbis (ogg)

%description artsplugin-xine -l pl
Ta wtyczka umo¿liwia arts odtwarzanie d¼wiêku za pomoc± silnika xine.
Wspiera ona wiêcej formatów ni¿ akode, ale niektóre z nich akode
odtwarza w lepszej jako¶ci. Dla najlepszej jako¶ci nale¿y u¿ywaæ tej
wtyczki wraz z akode, a arts sam wykryje, która z nich da lepsz±
jako¶æ przy konkretnym formacie. Wspierane formaty to:
- Microsoft Windows media (asf,asx,wmv,wma)
- mpeg (vob,mpg,mpeg,m1v,m2v,m1s,m2s,m2p,MP4,MP3,MP2,mp1)
- divx i avi
- quicktime (qt,mov,moov)
- real.com (rv,ra,ram,rm)
- smil (.smi)
- flac
- speex
- ac3/aac/m4v/m4a
- ogg vorbis (ogg)

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl):	Protokó³ audiocd dla konquerora
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	konqueror >= %{_minbaseevr}
Conflicts:	kdemultimedia-kaudiocreator < 9:3.1.92.031014

%description audiocd
This package allows konqueror to play audiocd's without the need of an
external application. Just enter audiocd:/ in the location field.

%description audiocd -l pl
Ten pakiet pozwala konquerorowi odtwarzanie p³yt z muzyk± bez potrzeby
u¿ywania zewnêtrznej aplikacji. Po prostu wpisz audiocd:/ w pole
adresu.

%package cddb
Summary:	CDDB library for KDE
Summary(pl):	Biblioteka CDDB pod KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-libkcddb < 9:3.1.92.031014

%description cddb
Support for cd database (CDDB), which is the source for track data for
KDE apps (title, author, etc.) when the cd does not have CD-Text.

%description cddb -l pl
Wsparcie dla baz danych p³yt CD (CDDB) z których program ¶ci±ga
informacje o odtwarzanym utworze (tytu³, autora itd.) je¶li p³yta nie
ma CD-Text.

%package juk
Summary:	A jukebox like program
Summary(pl):	Program spe³niaj±cy funkcjê szafy graj±cej
Group:		X11/Applications
Requires:	taglib >= 0.95.031114
Requires:	kdebase-core >= %{_minbaseevr}

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists.

%description juk -l pl
Juk (czyt. d¿uk, jak w Jukebox) to szafa graj±ca i zarz±dca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umo¿liwia modyfikowanie znaczników plików
d¼wiêkowych i zarz±dzanie kolekcj± oraz playlistami.

%package kaboodle
Summary:	Media player
Summary(pl):	Odtwarzacz multimedialny
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kaboodle
A simple, embeddable, single file media player.

%description kaboodle -l pl
Prosty odtwarzacz pojedynczych plików.

%package kappfinder
Summary:	Kappfinder multimedia data
Summary(pl):	Dane o aplikacjach multimedialnych dla kappfindera
Group:		X11/Applications
Requires:	kdebase-kappfinder

%description kappfinder
Multimedia application data for the kappfinder program, which find
applications and adds them to the KDE menu.

%description kappfinder -l pl
Dane aplikacji multimedialnych dla kappfinder, aplikacji wyszukuj±cej
inne aplikacje w systemie i dodaj±cej je do menu KDE.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}

%description kaudiocreator
CD ripper and sound encoder frontend.

%description kaudiocreator -l pl
Nak³adka na CD ripper i koder d¼wiêku.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d¼wiêkowych
Group:		X11/Development/Libraries
Requires:	konqueror >= %{_ver}
Obsoletes:	kdemultimedia < 8:3.0.8

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations for avi, au, flac, m3u, MP3, mpc, ogg,
sid and WAV files.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" konquerora
dodatkow± zak³adkê z rozszerzonymi informacjami o plikach avi, au,
flac, MP3, m3u, mpc, ogg, sid and WAV.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmid
This is a MIDI player for KDE. It features:
- a nice interface to display karaoke lyrics
- a channel view to see what notes is each instrument playing
- supports external midi synths, AWE cards, FM output, and GUS
- powerful Midi Mapper
- can play broken midi

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Oferuje:
- interfejs do wy¶wietlania tekstów w trybie karaoke
- tryb kana³ów, wy¶wietlaj±cy nuty odtwarzane przez poszczególne
  instrumenty
- wsparcie dla zewnêtrznych syntezatorów, kart AWE, wyj¶cia FM i GUS
- rozbudowany mapper MIDI
- odtwarzanie uszkodzony plików midi

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mikser d¼wiêku dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser d¼wiêku dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d¼wiêku dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-artscontrol = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}

%description krec
KDE sound recorder which supports MP3 and ogg exporting and simple
effects and mixers.

%description krec -l pl
Rejestrator d¼wiêku dla KDE z obs³ug± eksportu do MP3 i ogg oraz
prostymi efektami i mikserem.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê
danych o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn±
graficzn± interpretacjê granych d¼wiêków.

%package libkcddb
Summary:	CDDB accessing library
Summary(pl):	Biblioteka dostêpu do baz CDDB
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkcddb
Library for accessing CDDB (cd track information databases) services.

%description libkcddb -l pl
Biblioteka dostêpu do serwisów CDDB (baz danych z informacjami o
utworach).

%package mpeglib
Summary:	MPEG playback plugin for arts
Summary(pl):	Wtyczka z obs³ug± mpeg dla arts
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}

%description mpeglib
Plugin that adds support of MPEG audio and video formats to arts. It
give better quality than xine and worse than akode, yet it may be
beter for playing broken or low quality MP3 files than akode.

%description mpeglib -l pl
Wtyczka dodaj±ca obs³ugê MPEG do arts daje jako¶æ lepsz± od wtyczki
xine i gorsz± akode. Jedynie w przypadku uszkodzonych i niskiej
jako¶ci MP3 jest lepsza od akode. Obs³uguje zarówno d¼wiêk jak i obraz
zakodowany w MPEG.

%package mpeglib-devel
Summary:	MPEG libraries - development files
Summary(pl):	Biblioteki obs³ugi MPEG - pliki dla programistów
Group:		X11/Applications
Requires:	kdelibs-devel >= %{_minlibsevr}
Requires:	%{name}-mpeglib-examples = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-devel < 9:3.1.92.031012

%description mpeglib-devel
MPEG libraries - development files.

%description mpeglib-devel -l pl
Biblioteki obs³ugi MPEG - pliki dla programistów.

%package mpeglib-examples
Summary:	MPEG libraries - examples
Summary(pl):	Biblioteki obs³ugi MPEG - przyk³ady
Group:		X11/Applications
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-mpeglib < 9:3.1.92.031012

%description mpeglib-examples
MPEG libraries - examples.

%description mpeglib-examples -l pl
Biblioteki obs³ugi MPEG - przyk³ady.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plików multimedialnych
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}

# THIS NEEDS EXTENDING. noatun is a too powerful app to describe with
# one sentence.

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plików multimedialnych.

%package noatun-libs
Summary:	KDE Media Player - shared libs
Summary(pl):	KDE Media Player - biblioteki wspó³dzielone
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-noatun < 9:3.1.92.031012

%description noatun-libs
KDE Media Player - shared libs.

%description noatun-libs -l pl
KDE Media Player - biblioteki wspó³dzielone.

%prep
%setup -q 
#%patch100 -p1
%patch0 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Player;/' \
	-e 's/Terminal=0/Terminal=false/' \
	juk/juk.desktop \
	kscd/kscd.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Midi;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kmid/kmid.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Midi;/' \
	kappfinder-data/meterbridge.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
	-e 's/Terminal=0/Terminal=false/' \
	noatun/noatun.desktop \
	kaboodle/kaboodle.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Mixer;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kmix/kmix.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
	-e '/\[Desktop Entry\]/aEncoding=UTF-8' -e 's/Terminal=0/Terminal=false/' \
	krec/krec.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
	-e '/\[Desktop Entry\]/aEncoding=UTF-8' -e 's/Terminal=0/Terminal=false/' \
	kaudiocreator/kaudiocreator.desktop 
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Recorder;/' \
	kappfinder-data/galan.desktop \
	kappfinder-data/mixxx.desktop \
	kappfinder-data/rezound.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Sequencer;/' \
	kappfinder-data/hydrogen.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;/' \
	kappfinder-data/ecamegapedal.desktop \
	kappfinder-data/freebirth.desktop \
	kappfinder-data/amsynth.desktop \
	kappfinder-data/vkeybd.desktop \
	kappfinder-data/jack-rack.desktop \
	kappfinder-data/jamin.desktop \
	kappfinder-data/ardour.desktop \
	kappfinder-data/qsynth.desktop \
	kappfinder-data/qjackctl.desktop \
	kappfinder-data/muse.desktop \
	kappfinder-data/freqtweak.desktop \
	kappfinder-data/djplay.desktop \
	kappfinder-data/ams.desktop \
	kappfinder-data/zynaddsubfx.desktop  
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;/' \
	-e 's/Terminal=0/Terminal=false/' \
	arts/tools/artscontrol.desktop \
	arts/builder/artsbuilder.desktop
%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	libkcddb/kcmcddb/libkcddb.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
done

for i in `find ./mpeglib/ -name Makefile.am`; do echo KDE_OPTIONS=nofinal >> ${i} ; done

%build
cp %{_datadir}/automake/config.sub admin

export UNSERMAKE=%{_datadir}/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

export CDPARANOIA=%{_bindir}/cdparanoia

%configure \
	--disable-rpath \
	--enable-final \
	--with%{?without_alsa:out}-arts-alsa \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang artsbuilder	--with-kde
%find_lang juk		--with-kde
%find_lang kaboodle	--with-kde
%find_lang kmid		--with-kde
%find_lang kmix		--with-kde
%find_lang kmixcfg	--with-kde
cat kmixcfg.lang >> kmix.lang
%find_lang krec		--with-kde
%find_lang kscd		--with-kde
%find_lang noatun	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	arts			-p /sbin/ldconfig
%postun	arts			-p /sbin/ldconfig

%post	libkcddb		-p /sbin/ldconfig
%postun	libkcddb		-p /sbin/ldconfig

%post	mpeglib			-p /sbin/ldconfig
%postun	mpeglib			-p /sbin/ldconfig

%post	mpeglib-examples	-p /sbin/ldconfig
%postun	mpeglib-examples	-p /sbin/ldconfig

%post	noatun-libs		-p /sbin/ldconfig
%postun	noatun-libs		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/akode
%{_includedir}/arts/*.h
%{_includedir}/arts/*.idl
%{_includedir}/libkcddb
%{_includedir}/noatun
%{_libdir}/libakode.so
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

%files akode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakode.la
%attr(755,root,root) %{_libdir}/libakode.so.*.*.*
%{_libdir}/libarts_akode.la
%attr(755,root,root) %{_libdir}/libarts_akode.so
%{_libdir}/libakode_*.la
%attr(755,root,root) %{_libdir}/libakode_*.so
%{_libdir}/mcop/akode*PlayObject.mcopclass
%{_libdir}/mcop/akodearts.mcop*

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
# artsplugin-audiofile files - arts crashes
# without libaudiofilearts.so installed - so
# separating them has no sense at this moment
%{_libdir}/libaudiofilearts.la
%attr(755,root,root) %{_libdir}/libaudiofilearts.so
%{_libdir}/mcop/audiofilearts.mcopclass
%{_libdir}/mcop/audiofilearts.mcoptype
%{_iconsdir}/crystalsvg/*/actions/arts[!bc]*.png
%{_iconsdir}/crystalsvg/*/actions/arts[!bc]*.svg

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
%{_datadir}/apps/kicker/applets/artscontrolapplet.desktop
%{_desktopdir}/kde/artscontrol.desktop
%{_iconsdir}/crystalsvg/*/apps/artscontrol.png
%{_iconsdir}/crystalsvg/*/apps/artscontrol.svg

%if %{with xine}
%files artsplugin-xine
%defattr(644,root,root,755)
%{_libdir}/kde3/videothumbnail.la
%attr(755,root,root) %{_libdir}/kde3/videothumbnail.so
%{_libdir}/*_xine.la
%attr(755,root,root) %{_libdir}/*_xine.so
%{_libdir}/mcop/xine*PlayObject.mcopclass
%{_datadir}/apps/videothumbnail
%{_datadir}/services/videothumbnail.desktop
%endif

%files audiocd
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%{_libdir}/kde3/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%{_libdir}/kde3/libaudiocd_encoder*.la
%attr(755,root,root) %{_libdir}/kde3/libaudiocd_encoder*.so
%{_libdir}/libaudiocdplugins.la
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so*
%{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
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
%{_libdir}/kde3/libkaboodlepart.la
%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_datadir}/services/kaboodleengine.desktop
%{_desktopdir}/kde/kaboodle.desktop
%{_iconsdir}/*/*/apps/kaboodle.*

%files kappfinder
%defattr(644,root,root,755)
%{_datadir}/apps/kappfinder/apps/Multimedia/*

%files kaudiocreator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_datadir}/apps/kaudiocreator
#%{_datadir}/config/kaudiocreatorrc
%{_datadir}/config.kcfg/kaudiocreator.kcfg
%{_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_datadir}/apps/kconf_update/upgrade-kaudiocreator-metadata.sh
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
%{_libdir}/libkmidlib.la
%attr(755,root,root) %{_libdir}/libkmidlib.so*
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_desktopdir}/kde/kmid.desktop
%{_iconsdir}/*/*/*/kmid.png
%{_libdir}/libkmidlib.la
%attr(755,root,root) %{_libdir}/libkmidlib.so.0.0.0

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
%{_libdir}/kde3/kmix_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so
%{_datadir}/apps/kicker/applets/kmixapplet.desktop
%{_datadir}/apps/kmix
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_desktopdir}/kde/kmix.desktop
%{_iconsdir}/*/*/*/kmix.png
%{_kdedocdir}/en/kcontrol/kmixcfg

%files kscd -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_desktopdir}/kde/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/config.kcfg/kscd.kcfg
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
%attr(755,root,root) %{_libdir}/libarts_mpeglib.so
%attr(755,root,root) %{_libdir}/libarts_splay.so
%attr(755,root,root) %{_libdir}/libmpeg.so
%attr(755,root,root) %{_libdir}/libyafcore.so
%attr(755,root,root) %{_libdir}/libyafxplayer.so
%{_includedir}/mpeglib
%{_includedir}/mpeglib_artsplug

%files mpeglib-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yaf-cdda
%attr(755,root,root) %{_bindir}/yaf-mpgplay
%attr(755,root,root) %{_bindir}/yaf-splay
%attr(755,root,root) %{_bindir}/yaf-tplay
%attr(755,root,root) %{_bindir}/yaf-vorbis
%attr(755,root,root) %{_bindir}/yaf-yuv
%{_libdir}/libyafcore.la
%attr(755,root,root) %{_libdir}/libyafcore.so.*.*.*
%{_libdir}/libyafxplayer.la
%attr(755,root,root) %{_libdir}/libyafxplayer.so.*.*.*

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%{_libdir}/libkdeinit_noatun.la
%attr(755,root,root) %{_libdir}/libkdeinit_noatun.so
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
