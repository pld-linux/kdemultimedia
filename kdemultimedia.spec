%define		_ver		3.0
#define		_sub_ver
%define		_rel		2

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_version}
Release:	%{_release}
Epoch:		6
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-kmidi-alsa.patch
%ifnarch sparc sparc64
BuildRequires:	alsa-lib-devel
%endif
BuildRequires:	arts-devel
BuildRequires:	arts-kde-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _fontdir        /usr/share/fonts
%define         _sharedir       %{_prefix}/share
%define         _htmldir        /usr/share/doc/kde/HTML

%description
KDE multimedia applications. Package includes:
 - KMedia - Media player,
 - KMID - MIDI player,
 - KMIDI - software MIDI player,
 - KMIX - audio mixer,
 - KSCD - CD Player.

%description -l pl
Multimedialne aplikacje KDE. Pakiet zawiera:
 - KMedia - Program do odtwarzania plików d¼wiêkowych,
 - KMID - Odtwarzacz MIDI,
 - KMIDI - Programowy odtwarzacz MIDI,
 - KMIX - Mixer audio,
 - KSCD - Odtwarzacz CD.

%package arts
Summary:	Arts
Summary(pl):	Arts
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description arts
Arts.

%description arts -l pl
Arts.

%package aktion
Summary:	KDE Media Player
Summary(pl):	Odtwarzacz multimedialny dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}
Obsoletes:	aktion

%description aktion
This is a media player for KDE. Currently it can be only used to play
WAV files.

%description aktion -l pl
Odtwarzacz multimedialny dla KDE. W tej chwili obs³uguje tylko pliki
WAV.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntetyzator na karcie
muzycznej lub inne urz±dzenia MIDI przy³±czone do niej.

%package kmidi
Summary:	KDE software MIDI Player
Summary(pl):	Programowy odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

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
Requires:	kdelibs = %{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kscd
CD Player with CDDB support. It can automaticaly update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê
danych o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn±
graficzn± interpretacjê granych d¼wiêków.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player
Group:		X11/Applications
Requires:	kdelibs = %{version}
Requires:	arts >= 1.0.0

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player.

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs = %{version}
Requires:	arts >= 1.0.0

%description mpeglib
MPEG lib.

%description mpeglib -l pl
MPEG lib.

%package devel
Summary:	kdemultimedia - headers
Summary(pl):	kdemultimedia - pliki nag³ówkowe
Group:		X11/Development/Libraries
Requires:	kdemultimedia-mpeglib = %{version}
Requires:	kdemultimedia-noatun = %{version}
Requires:	kdelibs-devel = %{version}

%description devel
kdemultimedia - headers.

%description devel -l pl
kdemultimedia - pliki nag³ówkowe.

%package kaboodle
Summary:	Media player
Summary(pl):	Odtwarzacz multimedialny
Group:		X11/Applications

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
CFLAGS="%{rpmcflags} -I%{_includedir}"

%configure CPPFLAGS="$CPPFLAGS" \
 	--with-pam="yes" \
	--enable-audio=oss,alsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/Settings/KDE
mv $ALD/{Settings/Sound,Settings/KDE}

%find_lang aktion --with-kde
%find_lang noatun --with-kde

%post   mpeglib -p /sbin/ldconfig
%postun mpeglib -p /sbin/ldconfig

%post   aktion -p /sbin/ldconfig
%postun aktion -p /sbin/ldconfig

%post   arts -p /sbin/ldconfig
%postun arts -p /sbin/ldconfig

%post   kmid -p /sbin/ldconfig
%postun kmid -p /sbin/ldconfig

%post   kmix -p /sbin/ldconfig
%postun kmix -p /sbin/ldconfig

%post   kscd -p /sbin/ldconfig
%postun kscd -p /sbin/ldconfig

%post   noatun -p /sbin/ldconfig
%postun noatun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdummy.so.*.*.*
%attr(755,root,root) %{_libdir}/libdummy.la
%attr(755,root,root) %{_libdir}/kde3/kfile_*.??
%{_datadir}/services/kfile_*.desktop

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_bindir}/yaf*
%attr(755,root,root) %{_libdir}/libyaf*.so.*.*.*
%attr(755,root,root) %{_libdir}/libarts_mpeglib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libmpeg-*.so
%{_libdir}/libmpeg.la
%{_libdir}/libyaf*.la
%{_libdir}/libarts_mpeglib*.la
# Note that SplayPlayObject.mopclass is *not* here.
%{_libdir}/mcop/VCDPlayObject.mcopclass
%{_libdir}/mcop/WAVPlayObject.mcopclass
%{_libdir}/mcop/OGGPlayObject.mcopclass
%{_libdir}/mcop/NULLPlayObject.mcopclass
%{_libdir}/mcop/MP3PlayObject.mcopclass
%{_libdir}/mcop/CDDAPlayObject.mcopclass
%{_libdir}/mcop/MPGPlayObject.mcopclass

%files aktion -f aktion.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aktion*
%attr(755,root,root) %{_libdir}/libaktion.so.*.*.*
%{_libdir}/libaktion.la
%{_applnkdir}/Multimedia/aktion.desktop
%{_datadir}/apps/aktion
%{_datadir}/config/aktionrc
%{_pixmapsdir}/*/*/apps/aktion.png

%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arts*
%attr(755,root,root) %{_bindir}/midisend
%attr(755,root,root) %{_libdir}/libaudiofilearts.??
%attr(755,root,root) %{_libdir}/libarts[!_]*.so.*.*.*
%attr(755,root,root) %{_libdir}/libarts[!_]*.la
%attr(755,root,root) %{_libdir}/libarts_[!m]*.so.*.*.*
%attr(755,root,root) %{_libdir}/libarts_[!m]*.la
%attr(755,root,root) %{_libdir}/libarts[!_mgb]*.so
%{_libdir}/mcop/audiofilearts*
%{_libdir}/mcop/arts*
%{_libdir}/mcop/Splay*
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/ExtraStereo.mcopclass
%{_libdir}/mcop/ExtraStereoGuiFactory.mcopclass
%{_libdir}/mcop/VoiceRemoval.mcopclass
%{_libdir}/mcop/RawWriter.mcopclass
%{_applnkdir}/Multimedia/arts*.desktop
%{_pixmapsdir}/*/*/apps/arts*
%{_pixmapsdir}/*/*/actions/artsbuilder*
%{_datadir}/apps/artsbuilder
%{_datadir}/apps/artscontrol
%{_htmldir}/en/artsbuilder
%{_datadir}/mimelnk/application/*arts*

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%attr(755,root,root) %{_libdir}/libnoatun*.so.*.*.*
%attr(755,root,root) %{_libdir}/libnoatun[!.c]*so
%attr(755,root,root) %{_libdir}/libwinskinvis.??
%{_libdir}/libnoatun*.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.??
%{_libdir}/mcop/Noatun
%{_libdir}/mcop/noatun*
%{_libdir}/mcop/winskinvis*
%{_applnkdir}/Multimedia/noatun.desktop
%{_datadir}/apps/noatun*
%{_datadir}/apps/kconf_update/noatun*
%{_pixmapsdir}/*/*/apps/noatun.png

%files kmid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%attr(755,root,root) %{_libdir}/libkmidpart.so.*.*.*
%{_libdir}/libkmidpart.la
%{_applnkdir}/Multimedia/kmid.desktop
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_htmldir}/en/kmid
%{_datadir}/servicetypes/*midi*.desktop
%{_pixmapsdir}/*/*/apps/kmid.png

%files kmidi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmidi
%attr(755,root,root) %{_bindir}/sf2cfg
%attr(755,root,root) %{_bindir}/timidity
%{_applnkdir}/Multimedia/kmidi.desktop
%{_applnkdir}/Multimedia/timidity.desktop
%{_datadir}/apps/kmidi
%{_htmldir}/en/kmidi
%{_pixmapsdir}/*/*/apps/kmidi.png

%files kmix
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_libdir}/kmix.??
%attr(755,root,root) %{_libdir}/kmixctrl.*
%attr(755,root,root) %{_libdir}/kde3/kcm_kmix.??
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so.*.*.*
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.la
%{_applnkdir}/Multimedia/kmix.desktop
%{_applnkdir}/Settings/KDE/Sound/kmixcfg.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_datadir}/apps/kmix
%{_datadir}/apps/kicker/applets/*
%{_htmldir}/en/kmix
%{_pixmapsdir}/*/*/apps/kmix.png

%files kscd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%attr(755,root,root) %{_libdir}/libworkman.so.*.*.*
%{_libdir}/libworkman.la
%{_applnkdir}/Multimedia/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/mimelnk/text/xmcd.desktop
%{_htmldir}/en/kscd
%{_pixmapsdir}/*/*/apps/kscd.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libarts_mpeglib.so
%{_libdir}/libnoatuncontrols.so
%{_libdir}/libartsmidi_idl.so
%{_libdir}/libartsmodules.so
%{_libdir}/libartsgui_kde.so
%{_libdir}/libartsgui_idl.so
%{_libdir}/libartsbuilder.so
%{_libdir}/libyafxplayer.so
%{_libdir}/libmpeg.so
%{_libdir}/libarts_splay.so
%{_libdir}/libkmidpart.so
%{_libdir}/libartsmidi.so
%{_libdir}/libyafcore.so
%{_libdir}/libworkman.so
%{_libdir}/libartsgui.so
%{_libdir}/libnoatun.so
%{_libdir}/libaktion.so
%{_libdir}/libdummy.so
%{_libdir}/kde3/kmix_panelapplet.so

%files kaboodle
%defattr(644,root,root,755)
%{_bindir}/kaboodle
%{_libdir}/kaboodle.??
%{_libdir}/libkaboodlepart.??
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_applnkdir}/Multimedia/kaboodle.desktop
%{_pixmapsdir}/*/*/apps/kaboodle.*
