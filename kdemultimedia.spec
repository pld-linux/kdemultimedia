
%bcond_without 	alsa	# disables ALSA support
%bcond_without  i18n    # dont build i18n subpackage

%ifarch	sparc sparcv9 sparc64
%undefine with_alsa
%endif

%define		_state		stable
%define		_ver		3.2.0
#%efine		_snap		040110

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}
Release:	0.1
Epoch:		9
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	caa8578190d032acd3c8fa996cf9585a
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	f7aeb11765cd23f1719c1d18762fbc47  
%endif
# Patch0:		%{name}-no_pedantic.patch
# Patch1:		%{name}-cdda_check.patch
BuildRequires:	Xaw3d-devel
%{?with_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	ed
BuildRequires:	gettext-devel
# what for?
#BuildRequires:	gtk+-devel
# No longer needed
#BuildRequires:	id3lib-devel
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libart_lgpl-devel
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
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcddb = %{epoch}:%{version}-%{release}
Requires:	%{name}-libworkman = %{epoch}:%{version}-%{release}
Requires:	%{name}-noatun-libs = %{epoch}:%{version}-%{release}

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
Summary:	Arts extensions
Summary(pl):	Rozszerzenia Arts
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-artsplugin-audiofile

%description arts
Arts extensions.

%description arts -l pl
Rozszerzenia Arts.

%package artsbuilder
Summary:	Arts Tools - builder
Summary(pl):	Narzêdzia Arts - builder
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-arts < 9:3.1.92.021012

%description artsbuilder
Arts Tools - builder.

%description artsbuilder -l pl
Narzêdzia Arts - builder.

%package artscontrol
Summary:	Arts Tools - control
Summary(pl):	Narzêdzia Arts - control
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-arts < 9:3.1.92.021012

%description artscontrol
Arts Tools - control.

%description artscontrol -l pl
Narzêdzia Arts - control.

#%package artsplugin-audiofile
#Summary:	Audiofile Plug-in
#Summary(pl):	Wtyczka do Audiofile
#Group:		X11/Applications
#Requires:	%{name}-arts = %{epoch}:%{version}-%{release}
#Obsoletes:	%{name}-arts < 9:3.1.92.021012

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
Nak³adka na CD ripper i enkoder d¼wiêku.

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
Summary(pl):	Mixer audio dla KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

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
Obsoletes:	%{name}-kscd < 9:3.1.92.031012

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
Obsoletes:	%{name}-mpeglib < 9:3.1.92.031012

%description mpeglib-devel
MPEG libraries - development files.

%description mpeglib-devel -l pl
Biblioteki obs³ugi MPEG - pliki dla programistów.

%package mpeglib-examples
Summary:	MPEG libraries - examples
Summary(pl):	Biblioteki obs³ugi MPEG - przyk³ady
Group:		X11/Applications
Requires:	%{name}-mpeglib = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-mpeglib < 9:3.1.92.031012

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
Obsoletes:	%{name}-noatun < 9:3.1.92.031012

%description noatun-libs
KDE Media Player - shared libs.

%description noatun-libs -l pl
KDE Media Player - biblioteki wspó³dzielone.

%package artsbuilder-i18n
Summary:	Internationalization and localization files for artsbuilder
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla artsbuilder
Group:	X11/Applications
Requires:	%{name}-artsbuilder = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description artsbuilder-i18n
Internationalization and localization files for artsbuilder.

%description -l pl artsbuilder-i18n
Pliki umiêdzynarodawiaj±ce dla artsbuilder.

%package juk-i18n
Summary:	Internationalization and localization files for juk
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla juk
Group:	X11/Applications
Requires:	%{name}-juk = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description juk-i18n
Internationalization and localization files for juk.

%description -l pl juk-i18n
Pliki umiêdzynarodawiaj±ce dla juk.

%package kaboodle-i18n
Summary:	Internationalization and localization files for kaboodle
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kaboodle
Group:	X11/Applications
Requires:	%{name}-kaboodle = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kaboodle-i18n
Internationalization and localization files for kaboodle.

%description -l pl kaboodle-i18n
Pliki umiêdzynarodawiaj±ce dla kaboodle.

%package kmid-i18n
Summary:	Internationalization and localization files for kmid
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmid
Group:	X11/Applications
Requires:	%{name}-kmid = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kmid-i18n
Internationalization and localization files for kmid.

%description -l pl kmid-i18n
Pliki umiêdzynarodawiaj±ce dla kmid.

%package kmix-i18n
Summary:	Internationalization and localization files for kmix
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmix
Group:	X11/Applications
Requires:	%{name}-kmix = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kmix-i18n
Internationalization and localization files for kmix.

%description -l pl kmix-i18n
Pliki umiêdzynarodawiaj±ce dla kmix.

%package kscd-i18n
Summary:	Internationalization and localization files for kscd
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kscd
Group:	X11/Applications
Requires:	%{name}-kscd = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description kscd-i18n
Internationalization and localization files for kscd.

%description -l pl kscd-i18n
Pliki umiêdzynarodawiaj±ce dla kscd.

%package krec-i18n
Summary:	Internationalization and localization files for krec
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla krec
Group:	X11/Applications
Requires:	%{name}-krec = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description krec-i18n
Internationalization and localization files for krec.

%description -l pl krec-i18n
Pliki umiêdzynarodawiaj±ce dla krec.

%package noatun-i18n
Summary:	Internationalization and localization files for noatun
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla noatun
Group:	X11/Applications
Requires:	%{name}-noatun = %{epoch}:%{version}-%{release}
Obsoletes:	kde-i18n-Affrikaans
Obsoletes:	kde-i18n-Afrikaans
Obsoletes:	kde-i18n-Arabic
Obsoletes:	kde-i18n-Azerbaijani
Obsoletes:	kde-i18n-Bulgarian
Obsoletes:	kde-i18n-Bosnian
Obsoletes:	kde-i18n-Catalan
Obsoletes:	kde-i18n-Czech
Obsoletes:	kde-i18n-Danish
Obsoletes:	kde-i18n-German
Obsoletes:	kde-i18n-Greek
Obsoletes:	kde-i18n-English_UK
Obsoletes:	kde-i18n-British
Obsoletes:	kde-i18n-Esperanto
Obsoletes:	kde-i18n-Spanish
Obsoletes:	kde-i18n-Estonian
Obsoletes:	kde-i18n-Finnish
Obsoletes:	kde-i18n-French
Obsoletes:	kde-i18n-Hebrew
Obsoletes:	kde-i18n-Hindi
Obsoletes:	kde-i18n-Croatian
Obsoletes:	kde-i18n-Hungarian
Obsoletes:	kde-i18n-Indonesian
Obsoletes:	kde-i18n-Icelandic
Obsoletes:	kde-i18n-Italian
Obsoletes:	kde-i18n-Japanese
Obsoletes:	kde-i18n-Korean
Obsoletes:	kde-i18n-Lithuanian
Obsoletes:	kde-i18n-Latvian
Obsoletes:	kde-i18n-Maltese
Obsoletes:	kde-i18n-Malay
Obsoletes:	kde-i18n-Mongolian
Obsoletes:	kde-i18n-Dutch
Obsoletes:	kde-i18n-Norwegian
Obsoletes:	kde-i18n-Norwegian_Bokmaal
Obsoletes:	kde-i18n-Norwegian_Bookmal
Obsoletes:	kde-i18n-Norwegian_Nynorsk
Obsoletes:	kde-i18n-Polish
Obsoletes:	kde-i18n-Portugnese
Obsoletes:	kde-i18n-Portuguese
Obsoletes:	kde-i18n-Brazil
Obsoletes:	kde-i18n-Brazil_Portugnese
Obsoletes:	kde-i18n-Brazil_Portuguese
Obsoletes:	kde-i18n-Romanian
Obsoletes:	kde-i18n-Russian
Obsoletes:	kde-i18n-Slovak
Obsoletes:	kde-i18n-Slovenian
Obsoletes:	kde-i18n-Serbian
Obsoletes:	kde-i18n-Swedish
Obsoletes:	kde-i18n-Tamil
Obsoletes:	kde-i18n-Thai
Obsoletes:	kde-i18n-Turkish
Obsoletes:	kde-i18n-Ukrainian
Obsoletes:	kde-i18n-Uzbek
Obsoletes:	kde-i18n-Venda
Obsoletes:	kde-i18n-Vietnamese
Obsoletes:	kde-i18n-Xhosa
Obsoletes:	kde-i18n-Simplified_Chinese
Obsoletes:	kde-i18n-Chinese
Obsoletes:	kde-i18n-Chinese-Big5
Obsoletes:	kde-i18n-Zulu
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-i18n

%description noatun-i18n
Internationalization and localization files for noatun.

%description -l pl noatun-i18n
Pliki umiêdzynarodawiaj±ce dla noatun.
%prep
%setup -q -n %{name}-%{version} 
#%%patch0 -p1
#%%patch1 -p1

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
	--with%{?without_alsa:out}-arts-alsa

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%if %{with i18n}
bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
        [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done
%endif
	

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

files="artsbuilder \
juk \
kaboodle \
kmid \
kmix \
krec \
kscd \
noatun"

for i in $files; do
        echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
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
%files juk-i18n -f juk.lang
%files kaboodle-i18n -f kaboodle.lang
%files kmid-i18n -f kmid.lang
%files kmix-i18n -f kmix.lang
%files kscd-i18n -f kscd.lang
%files krec-i18n -f krec.lang
%files noatun-i18n -f noatun.lang
%endif

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
