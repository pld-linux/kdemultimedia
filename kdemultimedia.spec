#
# Conditional build:
%bcond_without	alsa	# build without ALSA support
%bcond_without	i18n	# don't build i18n per module subpackages
#
%define		_state		stable
%define		_ver		3.2.2

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}
Release:	2
Epoch:		9
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	062249563cbf66d77e61b41e5126f806
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
%if %{with i18n}
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	70b3e8e15eea6e5c40df1b35c62aa8a5
%endif
# Patch0:		%{name}-3.2branch.diff
# Patch0:		%{name}-no_pedantic.patch
# Patch1:		%{name}-cdda_check.patch
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires: 	libmusicbrainz-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	taglib-devel >= 0.95.031114
BuildRequires:	xine-lib-devel >= 1:1.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

 - Aktion - odtwarzacz plików avi,
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
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-static

%description devel
Header files for kdemultimedia libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek kdemultimedia

%package arts
Summary:	Arts extensions
Summary(pl):	Rozszerzenia Arts
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdemultimedia-artsplugin-audiofile

%description arts
Arts extensions.

%description arts -l pl
Rozszerzenia Arts.

%package artsbuilder
Summary:	Arts Tools - builder
Summary(pl):	Narzêdzia Arts - builder
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-arts < 9:3.1.92.021012

%description artsbuilder
Arts Tools - builder.

%description artsbuilder -l pl
Narzêdzia Arts - builder.

%package artscontrol
Summary:	Arts Tools - control
Summary(pl):	Narzêdzia Arts - control
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-arts < 9:3.1.92.021012

%description artscontrol
Arts Tools - control.

%description artscontrol -l pl
Narzêdzia Arts - control.

#%package artsplugin-audiofile
#Summary:	Audiofile Plug-in
#Summary(pl):	Wtyczka do Audiofile
#Group:		X11/Applications
#Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
#Obsoletes:	kdemultimedia-arts < 9:3.1.92.021012

#%description artsplugin-audiofile
#Audiofile Plug-in.

#%description artsplugin-audiofile -l pl
#Wtyczka do Audiofile.

%package artsplugin-xine
Summary:	Xine Plug-in
Summary(pl):	Wtyczka do Xine
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	xine-lib >= 1:1.0
Obsoletes:	%{name}-xine

%description artsplugin-xine
Xine Plug-in.

%description artsplugin-xine -l pl
Wtyczka do Xine.

%package audiocd
Summary:	Audiocd protocol for konqueror
Summary(pl):	Protokó³ audiocd dla konquerora
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	konqueror >= 9:%{version}
Obsoletes:	%{name}-kaudiocreator < 9:3.1.92.031014

%description audiocd
This package provides audiocd protocol for konqueror.

%description audiocd -l pl
Ten pakiet dostarcza protokó³ audiocd dla konquerora.

%package cddb
Summary:	cddb library for KDE
Summary(pl):	Biblioteka cddb pod KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libkcddb < 9:3.1.92.031014

%description cddb
CDDB control.

%description cddb -l pl
Sterowanie cddb.

%package juk
Summary:	A jukebox like program
Summary(pl):	Program spe³niaj±cy funkcjê szafy graj±cej
Group:		X11/Applications
Requires:	taglib >= 0.95.031114
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}

%description kaudiocreator
CD ripper and sound encoder frontend.

%description kaudiocreator -l pl
Nak³adka na CD ripper i koder d¼wiêku.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d¼wiêkowych
Group:		X11/Development/Libraries
Requires:	konqueror >= %{version}
Obsoletes:	kdemultimedia < 8:3.0.8

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
Requires:	kdebase-core >= 9:%{version}

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntezator na karcie
muzycznej lub inne urz±dzenia MIDI przy³±czone do niej.

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mikser d¼wiêku dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser d¼wiêku dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d¼wiêku dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-artscontrol = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}

%description krec
KDE sound recorder.

%description krec -l pl
Rejestrator d¼wiêku dla KDE.

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
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê
danych o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn±
graficzn± interpretacjê granych d¼wiêków.

%package libkcddb
Summary:	kcddb library
Summary(pl):	Biblioteka kcddb
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libkcddb
kcddb library.

%description libkcddb -l pl
Biblioteka kcddb.

%package libworkman
Summary:	workman library
Summary(pl):	Biblioteka workman
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdemultimedia-kscd < 9:3.1.92.031012

%description libworkman
workman library.

%description libworkman -l pl
Biblioteka workman.

%package mpeglib
Summary:	MPEG libraries
Summary(pl):	Biblioteki obs³ugi MPEG
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}

%description mpeglib
MPEG libraries.

%description mpeglib -l pl
Biblioteki obs³ugi MPEG.

%package mpeglib-devel
Summary:	MPEG libraries - development files
Summary(pl):	Biblioteki obs³ugi MPEG - pliki dla programistów
Group:		X11/Applications
Requires:	%{name}-mpeglib-examples = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-mpeglib < 9:3.1.92.031012

%description mpeglib-devel
MPEG libraries - development files.

%description mpeglib-devel -l pl
Biblioteki obs³ugi MPEG - pliki dla programistów.

%package mpeglib-examples
Summary:	MPEG libraries - examples
Summary(pl):	Biblioteki obs³ugi MPEG - przyk³ady
Group:		X11/Applications
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-mpeglib < 9:3.1.92.031012

%description mpeglib-examples
MPEG libraries - examples.

%description mpeglib-examples -l pl
Biblioteki obs³ugi MPEG - przyk³ady.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plików multimedialnych
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plików multimedialnych.

%package noatun-libs
Summary:	KDE Media Player - shared libs
Summary(pl):	KDE Media Player - biblioteki wspó³dzielone
Group:		X11/Libraries
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	kdemultimedia-noatun < 9:3.1.92.031012

%description noatun-libs
KDE Media Player - shared libs.

%description noatun-libs -l pl
KDE Media Player - biblioteki wspó³dzielone.

%package i18n
Summary:	Common internationalization and localization files for kdemultimedia
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdemultimedia
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdemultimedia.

%description i18n -l pl
Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdemultimedia.

%package artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artsbuildera
Group:		X11/Applications
Requires:	%{name}-artsbuilder = %{epoch}:%{version}-%{release}
Requires:	%{name}-arts-i18n = %{epoch}:%{version}-%{release}

%description artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description artsbuilder-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artsbuildera.

%package artscontrol-i18n
Summary:	Internationalization and localization files for artscontrol
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artscontrol
Group:		X11/Applications
Requires:	%{name}-artscontrol = %{epoch}:%{version}-%{release}
Requires:	%{name}-arts-i18n = %{epoch}:%{version}-%{release}

%description artscontrol-i18n
Internationalization and localization files for artscontrol.

%description artscontrol-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla artscontrol.

%package arts-i18n
Summary:	Internationalization and localization files for arts
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla arts
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}

%description arts-i18n
Internationalization and localization files for arts.

%description arts-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla arts.

%package juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla juk
Group:		X11/Applications
Requires:	%{name}-juk = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description juk-i18n
Internationalization and localization files for juk.

%description juk-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla juk.

%package kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaboodle
Group:		X11/Applications
Requires:	%{name}-kaboodle = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kaboodle-i18n
Internationalization and localization files for kaboodle.

%description kaboodle-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaboodle.

%package kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmid
Group:		X11/Applications
Requires:	%{name}-kmid = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmid-i18n
Internationalization and localization files for kmid.

%description kmid-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmid.

%package kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmix
Group:		X11/Applications
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmix-i18n
Internationalization and localization files for kmix.

%description kmix-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmix.

%package kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kscd
Group:		X11/Applications
Requires:	%{name}-kscd = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kscd-i18n
Internationalization and localization files for kscd.

%description kscd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kscd.

%package krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krec
Group:		X11/Applications
Requires:	%{name}-krec = %{epoch}:%{version}-%{release}
Requires:	%{name}-artscontrol-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-kmix-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description krec-i18n
Internationalization and localization files for krec.

%description krec-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla krec.

%package noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:		X11/Applications
Requires:	%{name}-noatun = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description noatun-i18n
Internationalization and localization files for noatun.

%description noatun-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla noatun.

%package kfile-i18n
Summary:	Internationalization and localization files for kfile
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kfile
Group:		X11/Applications
Requires:	%{name}-kfile = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n >= 9:%{version}

%description kfile-i18n
Internationalization and localization files for kfile.

%description kfile-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kfile.

%package audiocd-i18n
Summary:	Internationalization and localization files for audiocd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla audiocd
Group:		X11/Applications
Requires:	%{name}-audiocd = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb-i18n = %{epoch}:%{version}-%{release}
Requires:	konqueror-i18n >= 9:%{version}

%description audiocd-i18n
Internationalization and localization files for audiocd.

%description audiocd-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla audiocd.

%package libkcddb-i18n
Summary:	Internationalization and localization files for libkcddb
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla libkcddb
Group:		X11/Applications
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}

%description libkcddb-i18n
Internationalization and localization files for libkcddb.

%description libkcddb-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla libkcddb.

%package kaudiocreator-i18n
Summary:	Internationalization and localization files for kaudiocreator
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaudiocreatora
Group:		X11/Applications
Requires:	%{name}-kaudiocreator = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb-i18n = %{epoch}:%{version}-%{release}

%description kaudiocreator-i18n
Internationalization and localization files for kaudiocreator.

%description kaudiocreator-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kaudiocreatora.

%prep
%setup -q -n %{name}-%{version} 

%build
cp /usr/share/automake/config.sub admin

fix="kfile-plugins/ogg/configure.in.in \
	mpeglib_artsplug/configure.in.in"

for i in $fix;
do
	grep -v AC_REQUIRE $i >> $i.1
	mv $i{.1,}
done

%{__make} -f admin/Makefile.common cvs

export CDPARANOIA=%{_bindir}/cdparanoia

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \
	--with%{!?with_alsa:out}-arts-alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang artsbuilder	--with-kde
%find_lang juk		--with-kde
%find_lang kaboodle	--with-kde
%find_lang kmid		--with-kde
# No kmidi
# %find_lang kmidi	--with-kde
%find_lang kmix		--with-kde
%find_lang kmixcfg	--with-kde
cat kmixcfg.lang >> kmix.lang
%find_lang krec		--with-kde
%find_lang kscd		--with-kde
%find_lang noatun	--with-kde

%if %{with i18n}

%find_lang libkcddb	--with-kde
%find_lang kcmcddb	--with-kde
cat kcmcddb.lang >> libkcddb.lang

%find_lang kio_audiocd	--with-kde
%find_lang kcmaudiocd	--with-kde
cat kcmaudiocd.lang >> kio_audiocd.lang

%find_lang kaudiocreator --with-kde
%find_lang artscontrol	--with-kde
%find_lang artsmodules	--with-kde
mv artsmodules.lang arts.lang

%find_lang kcmkmix	--with-kde
cat kcmkmix.lang >> kmix.lang

kfile="au \
avi \
flac \
m3u \
mp3 \
ogg \
wav"
> kfile.lang

for i in $kfile;
do
	%find_lang kfile_${i} --with-kde
	cat kfile_${i}.lang >> kfile.lang
done
%endif

files="artsbuilder \
juk \
kaboodle \
kmid \
kmix \
krec \
kscd \
noatun"

for i in $files; do
	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done

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

%if %{with i18n}
%files artsbuilder-i18n -f artsbuilder.lang
%files artscontrol-i18n -f artscontrol.lang
%files arts-i18n -f arts.lang
%files juk-i18n -f juk.lang
%files kaboodle-i18n -f kaboodle.lang
%files kmid-i18n -f kmid.lang
%files kmix-i18n -f kmix.lang
%files kscd-i18n -f kscd.lang
%files krec-i18n -f krec.lang
%files noatun-i18n -f noatun.lang
%files kfile-i18n -f kfile.lang
%files audiocd-i18n -f kio_audiocd.lang
%files kaudiocreator-i18n -f kaudiocreator.lang
%files libkcddb-i18n -f libkcddb.lang
%endif

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libartsbuilder.so
%attr(755,root,root) %{_libdir}/libartsgui.so
%attr(755,root,root) %{_libdir}/libartsgui_idl.so
%attr(755,root,root) %{_libdir}/libartsgui_kde.so
%attr(755,root,root) %{_libdir}/libartsmidi_idl.so
%attr(755,root,root) %{_libdir}/libartsmidi.so
%attr(755,root,root) %{_libdir}/libartsmodules*.so
%attr(755,root,root) %{_libdir}/libkcddb.so
%attr(755,root,root) %{_libdir}/libnoatun.so
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so
%attr(755,root,root) %{_libdir}/libnoatuntags.so
%attr(755,root,root) %{_libdir}/libworkman.so
# static-only library, no shared version - so here
#%{_libdir}/libworkmanaudio.a
%{_includedir}/*.h
%{_includedir}/arts/*.h
%{_includedir}/arts/*.idl
%{_includedir}/libkcddb
%{_includedir}/libwm
%{_includedir}/noatun

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

%files artsbuilder -f artsbuilder_en.lang
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

%files juk -f juk_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/juk
%{_datadir}/apps/juk
%{_datadir}/apps/konqueror/servicemenus/jukservicemenu.desktop
%{_desktopdir}/kde/juk.desktop
%{_iconsdir}/*/*/*/juk*.png

%files kaboodle -f kaboodle_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaboodle
#%{_libdir}/kaboodle.la
#%attr(755,root,root) %{_libdir}/kaboodle.so
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
%{_datadir}/config.kcfg/kaudiocreator.kcfg
%{_datadir}/config.kcfg/kaudiocreator_encoders.kcfg
%{_desktopdir}/kde/kaudiocreator.desktop
%{_iconsdir}/[!l]*/*/*/kaudiocreator.png

%files kfile
%defattr(644,root,root,755)
%{_libdir}/kde3/kfile_*.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_datadir}/services/kfile_*.desktop

%files kmid -f kmid_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%{_libdir}/kde3/libkmidpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmidpart.so
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_desktopdir}/kde/kmid.desktop
%{_iconsdir}/*/*/*/kmid.png
%{_libdir}/libkmidlib.la
%{_libdir}/libkmidlib.so.0.0.0

%files kmix -f kmix_en.lang
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
%{_datadir}/apps/kicker/applets/kmixapplet.desktop
%{_iconsdir}/*/*/*/kmix.png

%files kscd -f kscd_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cddaslave
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%{_desktopdir}/kde/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/apps/profiles/kscd.profile.xml
%{_datadir}/mimelnk/text/xmcd.desktop
%{_iconsdir}/*/*/*/kscd.png

%files krec -f krec_en.lang
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
%attr(755,root,root) %{_libdir}/libyafcore.so.0.0.0
%{_libdir}/libyafxplayer.la
%attr(755,root,root) %{_libdir}/libyafxplayer.so.0.0.0

%files noatun -f noatun_en.lang
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
