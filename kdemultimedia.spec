#
# TODO:
#
# Conditional build:
%define         _state          unstable

%bcond_without	alsa	# build without ALSA support
%bcond_without	xine	# build without xine support
%bcond_with	gstreamer # build with gstreamer support
#
%define		_minlibsevr	9:3.4.89.050624
%define		_minbaseevr	9:3.4.89.050625

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	3.80.2
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
#% Source0-md5:	db69c9ab845c8295f095dc6394fba047
%{?with_alsa:BuildRequires:	alsa-lib-devel}
Patch0:		%{name}-taglib.patch
BuildRequires:	arts-qt-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdparanoia-III-devel
BuildRequires:	flac-devel >= 1.1.2
BuildRequires:	gettext-devel
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 0.8
BuildRequires:	gstreamer-plugins-devel >= 0.8
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
BuildRequires:	libtunepimp-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
BuildRequires:	polypaudio-devel
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
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	kdemultimedia-static

%description devel
Header files for kdemultimedia libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek kdemultimedia

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
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
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
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	taglib >= 0.95.031114

%description juk
JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists.
%if %{without gstreamer}

JuK (pronounced jook) is a jukebox and music manager for the KDE
desktop similar to jukebox software on other platforms such as
iTunes(R) or RealOne(R). As is typical with many jukebox applications,
JuK allows you to edit the "tags" of the audio files, and manage your
collection and playlists. Gstreamer support in this version has been
disabled. To reenable it please repuild the source rpm with '--with
gstreamer' option.
%endif

%description juk -l pl
Juk (czyt. d¿uk, jak w Jukebox) to szafa graj±ca i zarz±dca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umo¿liwia modyfikowanie znaczników plików
d¼wiêkowych i zarz±dzanie kolekcj± oraz playlistami.
%if %{without gstreamer}

Juk (czyt. d¿uk, jak w Jukebox) to szafa graj±ca i zarz±dca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umo¿liwia modyfikowanie znaczników plików
d¼wiêkowych i zarz±dzanie kolekcj± oraz playlistami. Obs³uga bibliotek
gstreamer zosta³a wy³±czona w tej wersji pakietu. Aby j± uaktywniæ,
nale¿y przebudowaæ pakiet ¼ród³owy (.src.rpm) z parametrem '--with
gstreamer'.
%endif

Juk (czyt. d¿uk, jak w Jukebox) to szafa graj±ca i zarz±dca muzyki dla
KDE podobny do iTunes(R) lub RealOne(R). Podobnie jak wiele innych
tego typu aplikacji, JuK umo¿liwia modyfikowanie znaczników plików
d¼wiêkowych i zarz±dzanie kolekcj± oraz playlistami. Obs³uga bibliotek
gstreamer zosta³a wy³±czona w tej wersji pakietu. Aby j± uaktywniæ,
nale¿y przebudowaæ pakiet ¼ród³owy (.src.rpm) z parametrem '--with
gstreamer'. #%package kaboodle #Summary: Media player #Summary(pl):
Odtwarzacz multimedialny #Group: X11/Applications #Requires:
kdebase-core >= %{_minbaseevr} #Obsoletes: kdemultimedia-aktion

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
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	kdemultimedia-audiocd >= %{_ver}

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
with file enhanced informations for avi, au, FLAC, M3U, MP3, MPC, Ogg,
SID and WAV files.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w³a¶ciwo¶ci pliku" konquerora
dodatkow± zak³adkê z rozszerzonymi informacjami o plikach avi, au,
FLAC, MP3, M3U, MPC, Ogg, SID i WAV.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
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

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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

%prep
%setup -q
%patch0 -p0

#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Player;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	juk/juk.desktop \
#	kscd/kscd.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Midi;Player;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kmid/kmid.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Audio;Midi;/' \
#	kappfinder-data/meterbridge.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;AudioVideo;Player;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	noatun/noatun.desktop \
#	kaboodle/kaboodle.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Mixer;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kmix/kmix.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
#	-e '/\[Desktop Entry\]/aEncoding=UTF-8' -e 's/Terminal=0/Terminal=false/' \
#	krec/krec.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;Recorder;/' \
#	-e '/\[Desktop Entry\]/aEncoding=UTF-8' -e 's/Terminal=0/Terminal=false/' \
#	kaudiocreator/kaudiocreator.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Audio;Recorder;/' \
#	kappfinder-data/galan.desktop \
#	kappfinder-data/mixxx.desktop \
#	kappfinder-data/rezound.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Audio;Sequencer;/' \
#	kappfinder-data/hydrogen.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Audio;/' \
#	kappfinder-data/ecamegapedal.desktop \
#	kappfinder-data/freebirth.desktop \
#	kappfinder-data/amsynth.desktop \
#	kappfinder-data/vkeybd.desktop \
#	kappfinder-data/jack-rack.desktop \
#	kappfinder-data/jamin.desktop \
#	kappfinder-data/ardour.desktop \
#	kappfinder-data/qsynth.desktop \
#	kappfinder-data/qjackctl.desktop \
#	kappfinder-data/muse.desktop \
#	kappfinder-data/freqtweak.desktop \
#	kappfinder-data/djplay.desktop \
#	kappfinder-data/ams.desktop \
#	kappfinder-data/zynaddsubfx.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Audio;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	arts/tools/artscontrol.desktop \
#	arts/builder/artsbuilder.desktop
#%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
#	libkcddb/kcmcddb/libkcddb.desktop
#for f in `find . -name \*.desktop`; do
#	if grep -q '^Categories=.*[^;]$' $f; then
#		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
#	fi
#	if grep -q '\[ven\]' $f; then
#		sed -i -e 's/\[ven\]/[ve]/' $f
#	fi
#done

%build
#export UNSERMAKE=%{_datadir}/unsermake/unsermake
export QTDIR=%{_prefix}
mkdir build
cd build
%cmake \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}
#	kde_libs_htmldir=%{_kdedocdir}

#%find_lang juk		--with-kde
#%find_lang kio_audiocd	--with-kde
#%find_lang kmid		--with-kde
#%find_lang kmix		--with-kde
#%find_lang kmixcfg	--with-kde
#cat kmixcfg.lang >> kmix.lang
#%find_lang kscd		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkcddb		-p /sbin/ldconfig
%postun	libkcddb		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/libkcddb
%{_includedir}/libkmid

%files audiocd
%defattr(644,root,root,755)
#-f kio_audiocd.lang
%defattr(644,root,root,755)
%{_libdir}/kde4/kcm_audiocd.la
%attr(755,root,root) %{_libdir}/kde4/kcm_audiocd.so
%{_libdir}/kde4/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde4/kio_audiocd.so
%{_libdir}/kde4/libaudiocd_encoder*.la
%attr(755,root,root) %{_libdir}/kde4/libaudiocd_encoder*.so
%attr(755,root,root) %{_libdir}/libaudiocdplugins.so*
%{_datadir}/apps/kconf_update/upgrade-metadata.sh
%{_datadir}/apps/konqueror/servicemenus/audiocd_play.desktop
%{_datadir}/config.kcfg/audiocd_*_encoder.kcfg
%{_datadir}/apps/kconf_update/audiocd.upd
%{_datadir}/services/audiocd.protocol
%{_datadir}/services/audiocd.desktop

%files cddb
%defattr(644,root,root,755)
%{_libdir}/kde4/kcm_cddb.la
%attr(755,root,root) %{_libdir}/kde4/kcm_cddb.so
%{_datadir}/config.kcfg/libkcddb.kcfg
%{_datadir}/apps/kconf_update/kcmcddb-emailsettings.upd
%{_datadir}/services/libkcddb.desktop

%files juk
%defattr(644,root,root,755)
#-f juk.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_desktopdir}/kde/juk.desktop
%{_iconsdir}/*/*/*/juk*.png
%{_datadir}/apps/juk/pics/*.png
%attr(755,root,root) %{_libdir}/libphononxineengine.so
%attr(755,root,root) %{_libdir}/libphononxineengine.so.*
%{_libdir}/kde4/phonon_xine.la
%attr(755,root,root) %{_libdir}/kde4/phonon_xine.so
%{_datadir}/services/phononbackends/xine.desktop
%{_libdir}/kde4/phonon_xineui.la
%attr(755,root,root) %{_libdir}/kde4/phonon_xineui.so

%files kappfinder
%defattr(644,root,root,755)
%{_datadir}/apps/kappfinder
%{_datadir}/desktop-directories/kde-multimedia-music.directory

%files kaudiocreator
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%{_datadir}/apps/kaudiocreator
%{_datadir}/config.kcfg/kaudiocreator.kcfg
%{_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_datadir}/apps/kconf_update/upgrade-kaudiocreator-metadata.sh
%{_datadir}/apps/kconf_update/kaudiocreator-*.upd
%{_desktopdir}/kde/kaudiocreator.desktop
%{_iconsdir}/[!l]*/*/*/kaudiocreator.png
%{_datadir}/apps/konqueror/servicemenus/audiocd_extract.desktop
%{_datadir}/apps/kaudiocreator/pics/check.png

%files kfile
%defattr(644,root,root,755)
%{_libdir}/kde4/kfile_*.la
%attr(755,root,root) %{_libdir}/kde4/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kmid
%defattr(644,root,root,755)
#-f kmid.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%{_libdir}/kde4/libkmidpart.la
%attr(755,root,root) %{_libdir}/kde4/libkmidpart.so
%attr(755,root,root) %{_libdir}/liblibkmid.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmidlib.so.*.*.*
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_desktopdir}/kde/kmid.desktop
%{_iconsdir}/*/*/*/kmid.png

%files kmix
%defattr(644,root,root,755)
#-f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_bindir}/kmixd
%attr(755,root,root) %{_libdir}/libkdeinit_kmix.so
%attr(755,root,root) %{_libdir}/libkdeinit_kmixd.so
%attr(755,root,root) %{_libdir}/libkdeinit_kmixctrl.so
%{_datadir}/apps/kmix
%{_datadir}/autostart/restore_kmix_volumes.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_desktopdir}/kde/kmix.desktop
%{_iconsdir}/*/*/*/kmix.png

%files kscd
%defattr(644,root,root,755)
#-f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_desktopdir}/kde/kscd.desktop
%{_datadir}/config.kcfg/kscd.kcfg
%{_datadir}/apps/profiles/kscd.profile.xml
%{_datadir}/mimelnk/text/xmcd.desktop
%{_iconsdir}/*/*/*/kscd.png
%{_iconsdir}/*/*/*/cdsmall.png

%files libkcddb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkcddb.so.*.*.*
