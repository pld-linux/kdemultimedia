# TODO:
# - enable gstreamer after making it selectable runtime
# - not sure about those unpackaged files:
#   /usr/share/desktop-directories/kde-multimedia-music.directory
#
# Conditional build:
%bcond_without	alsa			# build without ALSA support
%bcond_without	xine			# build without xine support
%bcond_with	tunepimp		# build with tunepimp support (needs old libtunepimp)
%bcond_with	gstreamer		# build with gstreamer support (needs old gstreamer)
%bcond_with	hidden_visibility	# gcc hidden visibility
#
%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	K Desktop Environment - multimedia applications
Summary(pl.UTF-8):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	3.5.9
Release:	3
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	fdfafe38d2c7e3019dafc80c177add15
#Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		kde-ac260-lt.patch
Patch2:		%{name}-bug-157891.patch
URL:		http://www.kde.org/
BuildRequires:	akode-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	arts-qt-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel >= alpha9.8-6
BuildRequires:	flac-devel >= 1.1.2
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gettext-devel
%if %{with gstreamer}
BuildRequires:	gstreamer08x-devel >= 0.8
%endif
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	lame-libs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel
BuildRequires:	libmusicbrainz-devel >= 1:2.1.1
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtheora-devel
%if %{with tunepimp}
BuildRequires:	libtunepimp-devel < 0.5
BuildRequires:	libtunepimp-devel >= 0.4.0
%endif
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	speex-devel
BuildRequires:	taglib-devel >= 0.95.031114
#BuildRequires:	unsermake >= 040511
%{?with_xine:BuildRequires:	xine-lib-devel >= 1:1.0}
BuildRequires:	zlib-devel
Obsoletes:	kdemultimedia-libworkman
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

%description -l pl.UTF-8
Multimedialne aplikacje KDE. Pakiet zawiera:

 - Arts - narzędzia arts,
 - Kaboodle - odtwarzacz plików multimedialnych,
 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD,
 - Noatun - odtwarzacz plików multimedialnych.

%package devel
Summary:	Header files for kdemultimedia libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek kdemultimedia
Group:		X11/Development/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	kdemultimedia-static

%description devel
Header files for kdemultimedia libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek kdemultimedia

%package akode
Summary:	A new generation arts plugin with high quality support for many formats
Summary(pl.UTF-8):	Wtyczka do arts nowej generacji z wysokiej jakości obsługą różnych formatów .
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}

%description akode
Arts plugin that supports high quality playback of the following
formats:
- Musepack (.MPC)
- mpeg (.MP3,.MP2, etc.)
- Ogg Vorbis (.ogg)
- FLAC
- speex
- WAV

%description akode -l pl.UTF-8
Wtyczka arts, która wspiera wysokiej jakości odtwarzanie następujących
formatów:
- Musepack (.MPC)
- mpeg (.MP3,.MP2, etc.)
- Ogg Vorbis (.ogg)
- FLAC
- speex
- WAV

%package arts
Summary:	Arts extensions
Summary(pl.UTF-8):	Rozszerzenia Arts
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdemultimedia-artsplugin-audiofile

%description arts
Arts extensions such as effect definitions, mixers presets and shared
libraries to access them.

%description arts -l pl.UTF-8
Rozszerzenia Arts takie jak definicje efektów, ustawienia mikserów
oraz biblioteki współdzielone dające do nich dostęp.

%package artsbuilder
Summary:	Arts Tools - builder
Summary(pl.UTF-8):	Narzędzia Arts - builder
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-arts < 9:3.1.92.021012

%description artsbuilder
A simple yet powerful effect and filter builder for arts.

%description artsbuilder -l pl.UTF-8
Prosty acz rozbudowany program do konstruowania efektów i filtrów w
arts.

%package artscontrol
Summary:	Arts Tools - control
Summary(pl.UTF-8):	Narzędzia Arts - control
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-arts < 9:3.1.92.021012

%description artscontrol
An advanced configuration tool for arts with FFT scope, media type
list, midi manager, client and environment manager and a server status
reporter

%description artscontrol -l pl.UTF-8
Zaawansowane narzędzie konfiguracyjne dla arts, zawiera: okno zakresu
FFT, listę obsługiwanych typów plików, moduły zarządzania klientami,
midi oraz środowiskiem, a także monitor stanu serwera dźwięku.

#%package artsplugin-audiofile
#Summary:	Audiofile Plug-in
#Summary(pl):	Wtyczka do Audiofile
#Group:		X11/Applications
#Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
#Obsoletes:	kdemultimedia-arts < 9:3.1.92.021012

#%description artsplugin-audiofile #Audiofile Plug-in.

#%description artsplugin-audiofile -l pl #Wtyczka do Audiofile.

%package artsplugin-xine
Summary:	Xine engine plugin for arts
Summary(pl.UTF-8):	Wtyczka silnika xine do arts
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	xine-lib >= 1:1.0
Obsoletes:	kdemultimedia-xine

%description artsplugin-xine
This plugin allows arts to play using xine engine. This plugin
supports more formats than akode, yet akode plays some of them with
better quality. For best quality use akode alongside this plugin, arts
will autodetect which plugin gives better quality. This plugin
supports:
- microsoft's windows media formats (asf,asx,wmv,wma)
- mpeg (vob,mpg,mpeg,m1v,m2v,m1s,m2s,m2p,MP4,MP3,MP2,mp1)
- divx and avi
- quicktime (qt,mov,moov)
- real.com formats (rv,ra,ram,rm)
- smil (.smi)
- FLAC
- speex
- ac3/aac/m4v/m4a
- Ogg Vorbis (ogg)

%description artsplugin-xine -l pl.UTF-8
Ta wtyczka umożliwia arts odtwarzanie dźwięku za pomocą silnika xine.
Wspiera ona więcej formatów niż akode, ale niektóre z nich akode
odtwarza w lepszej jakości. Dla najlepszej jakości należy używać tej
wtyczki wraz z akode, a arts sam wykryje, która z nich da lepszą
jakość przy konkretnym formacie. Wspierane formaty to:
- Microsoft Windows media (asf,asx,wmv,wma)
- mpeg (vob,mpg,mpeg,m1v,m2v,m1s,m2s,m2p,MP4,MP3,MP2,mp1)
- divx i avi
- quicktime (qt,mov,moov)
- real.com (rv,ra,ram,rm)
- smil (.smi)
- FLAC
- speex
- ac3/aac/m4v/m4a
- Ogg Vorbis (ogg)

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl.UTF-8):	Protokół audiocd dla konquerora
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	konqueror >= %{_minbaseevr}
Provides:	kdemultimedia(audiocd) = %{version}-%{release}
Conflicts:	kdemultimedia-kaudiocreator < 9:3.1.92.031014

%description audiocd
This package allows konqueror to play audiocd's without the need of an
external application. Just enter audiocd:/ in the location field.

%description audiocd -l pl.UTF-8
Ten pakiet pozwala konquerorowi odtwarzanie płyt z muzyką bez potrzeby
używania zewnętrznej aplikacji. Po prostu wpisz audiocd:/ w pole
adresu.

%package cddb
Summary:	CDDB library for KDE
Summary(pl.UTF-8):	Biblioteka CDDB pod KDE
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Conflicts:	kdemultimedia-libkcddb < 9:3.1.92.031014

%description cddb
Support for cd database (CDDB), which is the source for track data for
KDE apps (title, author, etc.) when the cd does not have CD-Text.

%description cddb -l pl.UTF-8
Wsparcie dla baz danych płyt CD (CDDB) z których program ściąga
informacje o odtwarzanym utworze (tytuł, autora itd.) jeśli płyta nie
ma CD-Text.

%package juk
Summary:	A jukebox like program
Summary(pl.UTF-8):	Program spełniający funkcję szafy grającej
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	taglib >= 0.95.031114

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists.
%if %{without gstreamer}

Gstreamer support in this version has been disabled. To reenable it
please repuild the source rpm with '--with gstreamer' option.
%endif

%description juk -l pl.UTF-8
Juk (czyt. dżuk, jak w Jukebox) to szafa grająca i zarządca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umożliwia modyfikowanie znaczników plików
dźwiękowych i zarządzanie kolekcją oraz playlistami.
%if %{without gstreamer}

Obsługa bibliotek gstreamer została wyłączona w tej wersji pakietu. Aby
ją uaktywnić, należy przebudować pakiet źródłowy (.src.rpm) z parametrem
'--with gstreamer'.
%endif

%package kaboodle
Summary:	Media player
Summary(pl.UTF-8):	Odtwarzacz multimedialny
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdemultimedia-aktion

%description kaboodle
A simple, embeddable, single file media player.

%description kaboodle -l pl.UTF-8
Prosty odtwarzacz pojedynczych plików.

%package kappfinder
Summary:	Kappfinder multimedia data
Summary(pl.UTF-8):	Dane o aplikacjach multimedialnych dla kappfindera
Group:		X11/Applications
Requires:	kdebase-kappfinder

%description kappfinder
Multimedia application data for the kappfinder program, which find
applications and adds them to the KDE menu.

%description kappfinder -l pl.UTF-8
Dane aplikacji multimedialnych dla kappfinder, aplikacji wyszukującej
inne aplikacje w systemie i dodającej je do menu KDE.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl.UTF-8):	Kreator audio
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	kdemultimedia-audiocd >= %{version}

%description kaudiocreator
CD ripper and sound encoder frontend.

%description kaudiocreator -l pl.UTF-8
Nakładka na CD ripper i koder dźwięku.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl.UTF-8):	Rozszerzone informacje o plikach dźwiękowych
Group:		X11/Development/Libraries
Requires:	konqueror >= %{version}
Obsoletes:	kdemultimedia < 8:3.0.8

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations for avi, au, FLAC, M3U, MP3, MPC, Ogg,
SID and WAV files.

%description kfile -l pl.UTF-8
Ten pakiet dodaje do okna dialogowego "właściwości pliku" konquerora
dodatkową zakładkę z rozszerzonymi informacjami o plikach avi, au,
FLAC, MP3, M3U, MPC, Ogg, SID i WAV.

%package kmid
Summary:	KDE MIDI Player
Summary(pl.UTF-8):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdemultimedia-kmidi

%description kmid
This is a MIDI player for KDE. It features:
- a nice interface to display karaoke lyrics
- a channel view to see what notes is each instrument playing
- supports external midi synths, AWE cards, FM output, and GUS
- powerful Midi Mapper
- can play broken midi

%description kmid -l pl.UTF-8
Odtwarzacz MIDI dla KDE. Oferuje:
- interfejs do wyświetlania tekstów w trybie karaoke
- tryb kanałów, wyświetlający nuty odtwarzane przez poszczególne
  instrumenty
- wsparcie dla zewnętrznych syntezatorów, kart AWE, wyjścia FM i GUS
- rozbudowany mapper MIDI
- odtwarzanie uszkodzony plików midi

%package kmix
Summary:	KDE audio mixer
Summary(pl.UTF-8):	Mikser dźwięku dla KDE
Group:		X11/Applications

%description kmix
Sound mixer application for KDE.

%description kmix -l pl.UTF-8
Mikser dźwięku dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl.UTF-8):	Rejestrator dźwięku dla KDE
Group:		X11/Applications
Requires:	%{name}-artscontrol = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}

%description krec
KDE sound recorder which supports MP3 and Ogg exporting and simple
effects and mixers.

%description krec -l pl.UTF-8
Rejestrator dźwięku dla KDE z obsługą eksportu do MP3 i Ogg oraz
prostymi efektami i mikserem.

%package kscd
Summary:	KDE CD Player
Summary(pl.UTF-8):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl.UTF-8
Odtwarzacz CD z obsługą CDDB. Automatycznie uaktualnia swoją bazę
danych o płytach CD z Internetem. Potrafi także wyświetlić ładną
graficzną interpretację granych dźwięków.

%package libkcddb
Summary:	CDDB accessing library
Summary(pl.UTF-8):	Biblioteka dostępu do baz CDDB
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkcddb
Library for accessing CDDB (cd track information databases) services.

%description libkcddb -l pl.UTF-8
Biblioteka dostępu do serwisów CDDB (baz danych z informacjami o
utworach).

%package mpeglib
Summary:	MPEG playback plugin for arts
Summary(pl.UTF-8):	Wtyczka z obsługą mpeg dla arts
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}

%description mpeglib
Plugin that adds support of MPEG audio and video formats to arts. It
give better quality than xine and worse than akode, yet it may be
beter for playing broken or low quality MP3 files than akode.

%description mpeglib -l pl.UTF-8
Wtyczka dodająca obsługę MPEG do arts daje jakość lepszą od wtyczki
xine i gorszą akode. Jedynie w przypadku uszkodzonych i niskiej
jakości MP3 jest lepsza od akode. Obsługuje zarówno dźwięk jak i obraz
zakodowany w MPEG.

%package mpeglib-devel
Summary:	MPEG libraries - development files
Summary(pl.UTF-8):	Biblioteki obsługi MPEG - pliki dla programistów
Group:		X11/Applications
Requires:	%{name}-mpeglib-examples = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Conflicts:	kdemultimedia-devel < 9:3.1.92.031012

%description mpeglib-devel
MPEG libraries - development files.

%description mpeglib-devel -l pl.UTF-8
Biblioteki obsługi MPEG - pliki dla programistów.

%package mpeglib-examples
Summary:	MPEG libraries - examples
Summary(pl.UTF-8):	Biblioteki obsługi MPEG - przykłady
Group:		X11/Applications
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-mpeglib < 9:3.1.92.031012

%description mpeglib-examples
MPEG libraries - examples.

%description mpeglib-examples -l pl.UTF-8
Biblioteki obsługi MPEG - przykłady.

%package noatun
Summary:	KDE Media Player
Summary(pl.UTF-8):	KDE Media Player - odtwarzacz plików multimedialnych
Group:		X11/Applications
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

# THIS NEEDS EXTENDING. noatun is a too powerful app to describe with
# one sentence.

%description noatun
KDE Media Player.

%description noatun -l pl.UTF-8
KDE Media Player - odtwarzacz plików multimedialnych.

%package noatun-libs
Summary:	KDE Media Player - shared libs
Summary(pl.UTF-8):	KDE Media Player - biblioteki współdzielone
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Conflicts:	kdemultimedia-noatun < 9:3.1.92.031012

%description noatun-libs
KDE Media Player - shared libs.

%description noatun-libs -l pl.UTF-8
KDE Media Player - biblioteki współdzielone.

%prep
%setup -q
#%patch100 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Player;/' \
	juk/juk.desktop \
	kscd/kscd.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Midi;Player;/' \
	kmid/kmid.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Audio;Midi;/' \
	kappfinder-data/meterbridge.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
	noatun/noatun.desktop \
	kaboodle/kaboodle.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Mixer;/' \
	kmix/kmix.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
	krec/krec.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
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
	arts/tools/artscontrol.desktop \
	arts/builder/artsbuilder.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

find . -type f -name '*.mcopclass' | xargs %{__sed} -i -e 's:\.la::'

cp %{_datadir}/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%build
export CDPARANOIA=%{_bindir}/cdparanoia

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with%{!?with_alsa:out}-arts-alsa \
	--with-extra-includes=%{_includedir}/speex \
	--with-qt-libraries=%{_libdir} \
	--with-distribution="PLD Linux Distribution" \
	--with-vorbis

%{__make}

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT \
		kde_htmldir=%{_kdedocdir}

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	# PLD doesn't have 'Multimedia/Music' submenu
	rm -f $RPM_BUILD_ROOT%{_sysconfdir}/xdg/menus/applications-merged/kde-multimedia-music.menu

	# locolor icons are deprecated (in PLD?)
	rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

	rm $RPM_BUILD_ROOT%{_libdir}/kde3/*.la
	rm $RPM_BUILD_ROOT%{_libdir}/libkdeinit_*.la

	touch installed.stamp
fi

rm -f *.lang
%find_lang artsbuilder		--with-kde
%find_lang juk			--with-kde
%find_lang kaudiocreator	--with-kde
%find_lang kaboodle		--with-kde
%find_lang kioslave		--with-kde
%find_lang kmid			--with-kde
%find_lang kmix			--with-kde
%find_lang krec			--with-kde
%find_lang kscd			--with-kde
%find_lang noatun		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	akode			-p /sbin/ldconfig
%postun	akode			-p /sbin/ldconfig

%post	artsplugin-xine		-p /sbin/ldconfig
%postun	artsplugin-xine		-p /sbin/ldconfig

%post	arts			-p /sbin/ldconfig
%postun	arts			-p /sbin/ldconfig

%post	audiocd			-p /sbin/ldconfig
%postun	audiocd			-p /sbin/ldconfig

%post	kmid			-p /sbin/ldconfig
%postun	kmid			-p /sbin/ldconfig

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
%{_includedir}/arts/*.h
%{_includedir}/arts/*.idl
%{_includedir}/libkcddb
%{_includedir}/noatun
%{_libdir}/libartsbuilder.la
%attr(755,root,root) %{_libdir}/libartsbuilder.so
%{_libdir}/libartscontrolapplet.la
%attr(755,root,root) %{_libdir}/libartscontrolapplet.so
%{_libdir}/libartscontrolsupport.la
%attr(755,root,root) %{_libdir}/libartscontrolsupport.so
%{_libdir}/libartseffects.la
%{_libdir}/libartsgui.la
%attr(755,root,root) %{_libdir}/libartsgui.so
%{_libdir}/libartsgui_idl.la
%attr(755,root,root) %{_libdir}/libartsgui_idl.so
%{_libdir}/libartsgui_kde.la
%attr(755,root,root) %{_libdir}/libartsgui_kde.so
%{_libdir}/libartsmidi.la
%attr(755,root,root) %{_libdir}/libartsmidi.so
%{_libdir}/libartsmidi_idl.la
%attr(755,root,root) %{_libdir}/libartsmidi_idl.so
%{_libdir}/libartsmodules.la
%attr(755,root,root) %{_libdir}/libartsmodules.so
%{_libdir}/libartsmodulescommon.la
%attr(755,root,root) %{_libdir}/libartsmodulescommon.so
%{_libdir}/libartsmoduleseffects.la
%attr(755,root,root) %{_libdir}/libartsmoduleseffects.so
%{_libdir}/libartsmodulesmixers.la
%attr(755,root,root) %{_libdir}/libartsmodulesmixers.so
%{_libdir}/libartsmodulessynth.la
%attr(755,root,root) %{_libdir}/libartsmodulessynth.so
%{_libdir}/libkcddb.la
%attr(755,root,root) %{_libdir}/libkcddb.so
%{_libdir}/libnoatun.la
%attr(755,root,root) %{_libdir}/libnoatun.so
%{_libdir}/libnoatunarts.la
%{_libdir}/libnoatuncontrols.la
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so
%{_libdir}/libnoatuntags.la
%attr(755,root,root) %{_libdir}/libnoatuntags.so
%{_libdir}/libwinskinvis.la
# nothing links with it
#%attr(755,root,root) %{_libdir}/libarts_akode.so
#%{_libdir}/libarts_akode.la
%attr(755,root,root) %{_libdir}/libarts_audiofile.so
%{_libdir}/libarts_audiofile.la
%if %{with xine}
#%attr(755,root,root) %{_libdir}/libarts_xine.so
#%{_libdir}/libarts_xine.la
%endif
#%attr(755,root,root) %{_libdir}/libaudiocdplugins.so
#%{_libdir}/libaudiocdplugins.la
#%attr(755,root,root) %{_libdir}/libkmidlib.so
#%{_libdir}/libkmidlib.la

%files akode
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarts_akode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarts_akode.so.0
%{_libdir}/mcop/akode*.mcop*

%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/midisend
%attr(755,root,root) %{_libdir}/libarts_audiofile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarts_audiofile.so.0
%attr(755,root,root) %{_libdir}/libartsbuilder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsbuilder.so.0
%attr(755,root,root) %{_libdir}/libartscontrolapplet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartscontrolapplet.so.1
%attr(755,root,root) %{_libdir}/libartscontrolsupport.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartscontrolsupport.so.1
%attr(755,root,root) %{_libdir}/libartseffects.so
%attr(755,root,root) %{_libdir}/libartsgui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsgui.so.0
%attr(755,root,root) %{_libdir}/libartsgui_idl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsgui_idl.so.0
%attr(755,root,root) %{_libdir}/libartsgui_kde.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsgui_kde.so.0
%attr(755,root,root) %{_libdir}/libartsmidi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmidi.so.0
%attr(755,root,root) %{_libdir}/libartsmidi_idl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmidi_idl.so.0
%attr(755,root,root) %{_libdir}/libartsmodules.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmodules.so.0
%attr(755,root,root) %{_libdir}/libartsmodulescommon.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmodulescommon.so.0
%attr(755,root,root) %{_libdir}/libartsmoduleseffects.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmoduleseffects.so.0
%attr(755,root,root) %{_libdir}/libartsmodulesmixers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmodulesmixers.so.0
%attr(755,root,root) %{_libdir}/libartsmodulessynth.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libartsmodulessynth.so.0
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
%{_libdir}/mcop/audiofilearts.mcopclass
%{_libdir}/mcop/audiofilearts.mcoptype
%{_iconsdir}/crystalsvg/*/actions/arts[!bc]*.*

%files artsbuilder -f artsbuilder.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artsbuilder
%{_libdir}/mcop/artsbuilder.mcopclass
%{_libdir}/mcop/artsbuilder.mcoptype
%{_datadir}/apps/artsbuilder
%{_datadir}/mimelnk/application/x-artsbuilder.desktop
%{_desktopdir}/kde/artsbuilder.desktop
%{_iconsdir}/crystalsvg/*/actions/artsbuilderexecute.*
%{_iconsdir}/hicolor/*/apps/artsbuilder.*

%files artscontrol
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/artscontrol
%{_datadir}/apps/artscontrol
%{_datadir}/apps/kicker/applets/artscontrolapplet.desktop
%{_desktopdir}/kde/artscontrol.desktop
%{_iconsdir}/hicolor/*/apps/artscontrol.*

%if %{with xine}
%files artsplugin-xine
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/videothumbnail.so
%attr(755,root,root) %{_libdir}/libarts_xine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarts_xine.so.0
%{_libdir}/mcop/xine*PlayObject.mcopclass
%{_datadir}/apps/videothumbnail
%{_datadir}/services/videothumbnail.desktop
%endif

%files audiocd -f kioslave.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%attr(755,root,root) %{_libdir}/kde3/libaudiocd_encoder*.so
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaudiocdplugins.so.1
%{_datadir}/apps/kconf_update/audiocd.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/apps/konqueror/servicemenus/audiocd_*.desktop
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%{_datadir}/services/audiocd.protocol
%{_desktopdir}/kde/audiocd.desktop

%files cddb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kcm_cddb.so
%{_datadir}/apps/kconf_update/kcmcddb-emailsettings.upd
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
%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_datadir}/services/kaboodleengine.desktop
%{_desktopdir}/kde/kaboodle.desktop
%{_iconsdir}/*/*/apps/kaboodle.*

%files kappfinder
%defattr(644,root,root,755)
%{_datadir}/apps/kappfinder/apps/Multimedia/*

%files kaudiocreator -f kaudiocreator.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_datadir}/apps/kaudiocreator
%{_datadir}/config.kcfg/kaudiocreator.kcfg
%{_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_datadir}/apps/kconf_update/kaudiocreator-libkcddb.upd
%{_datadir}/apps/kconf_update/kaudiocreator-meta.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-kaudiocreator-metadata.sh
%{_desktopdir}/kde/kaudiocreator.desktop
%{_iconsdir}/*/*/*/kaudiocreator.png

%files kfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kmid -f kmid.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%attr(755,root,root) %{_libdir}/kde3/libkmidpart.so
%attr(755,root,root) %{_libdir}/libkmidlib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkmidlib.so.0
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_desktopdir}/kde/kmid.desktop
%{_iconsdir}/*/*/*/kmid.png

%files kmix -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_libdir}/libkdeinit_kmix.so
%attr(755,root,root) %{_libdir}/libkdeinit_kmixctrl.so
%attr(755,root,root) %{_libdir}/kde3/kmix.so
%attr(755,root,root) %{_libdir}/kde3/kmixctrl.so
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so
%{_datadir}/apps/kicker/applets/kmixapplet.desktop
%{_datadir}/apps/kmix
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_desktopdir}/kde/kmix.desktop
%{_iconsdir}/*/*/*/kmix.png

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
%attr(755,root,root) %{_libdir}/libkdeinit_krec.so
%attr(755,root,root) %{_libdir}/kde3/kcm_krec.so
%attr(755,root,root) %{_libdir}/kde3/kcm_krec_files.so
%attr(755,root,root) %{_libdir}/kde3/krec.so
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_mp3.so
%attr(755,root,root) %{_libdir}/kde3/libkrecexport_ogg.so
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
%attr(755,root,root) %{_libdir}/libkcddb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkcddb.so.1

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_libdir}/libarts_mpeglib-*.*.*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarts_mpeglib-*.*.*.so.0
%attr(755,root,root) %{_libdir}/libarts_splay.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarts_splay.so.0
%attr(755,root,root) %{_libdir}/libmpeg-*.*.*.so
%attr(755,root,root) %{_libdir}/libyafcore.so
%attr(755,root,root) %{_libdir}/libyafxplayer.so
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
%{_libdir}/libarts_mpeglib.la
%attr(755,root,root) %{_libdir}/libarts_mpeglib.so
%{_libdir}/libarts_splay.la
%attr(755,root,root) %{_libdir}/libarts_splay.so
%{_libdir}/libmpeg.la
%attr(755,root,root) %{_libdir}/libmpeg.so
%{_libdir}/libyafcore.la
%{_libdir}/libyafxplayer.la

%files mpeglib-examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yaf-cdda
%attr(755,root,root) %{_bindir}/yaf-mpgplay
%attr(755,root,root) %{_bindir}/yaf-splay
%attr(755,root,root) %{_bindir}/yaf-tplay
%attr(755,root,root) %{_bindir}/yaf-vorbis
%attr(755,root,root) %{_bindir}/yaf-yuv

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%attr(755,root,root) %{_libdir}/libkdeinit_noatun.so
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
%{_datadir}/apps/kconf_update/noatun.upd
%attr(755,root,root) %{_libdir}/kconf_update_bin/noatun20update
%{_datadir}/apps/noatun*
%dir %{_datadir}/mimelnk/interface
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop
%{_desktopdir}/kde/noatun.desktop
%{_iconsdir}/*/*/*/noatun.png

%files noatun-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnoatun.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnoatun.so.1
%attr(755,root,root) %{_libdir}/libnoatunarts.so
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnoatuncontrols.so.1
%attr(755,root,root) %{_libdir}/libnoatuntags.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnoatuntags.so.1
%attr(755,root,root) %{_libdir}/libwinskinvis.so
