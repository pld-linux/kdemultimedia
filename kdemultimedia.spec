Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	2.0.1
Release:	1
Copyright:	GPL
Group:		X11/Applications
Vendor:		The KDE Team
Source:		ftp://ftp.kde.org/pub/kde/snapshost/current/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel >= 2.2.2
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/
%define         _fontdir        /usr/share/fonts
%define         _sharedir       %{_prefix}/share
%define         _htmldir        %{_sharedir}/doc/kde/HTML

%description
KDE multimedia applications.
Package includes:
  KMedia - Media player
  KMID - MIDI player
  KMIDI - software MIDI player
  KMIX - audio mixer
  KSCD - CD Player

%description -l pl
Multimedialne aplikacje KDE.
Pakiet zawiera:
  KMedia - Program do odtwarzania plików d¼wiêkowych
  KMID - Odtwarzacz MIDI
  KMIDI - Programowy odtwarzacz MIDI
  KMIX - Mixer audio
  KSCD - Odtwarzacz CD

%package arts
Summary:	Arts
Summary(pl):	Arts
Group:		X11/Applications
Requires:	kdelibs = %{version} 

%description arts

%description -l pl arts

%package aktion
Summary:	KDE Media Player
Summary(pl):	Odtwarzacz multimedialny dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description aktion
This is a media player for KDE.
Currently it can be only used to play WAV files.

%description -l pl aktion
Odtwarzacz multimedialny dla KDE.
W tej chwili obs³uguje tylko pliki WAV.

%package kmid
Summary:	KDE MIDI Player	
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kmid
This is a MIDI player for KDE.
It uses sound-card synthetizer or other hardware connected to MIDI to play MIDI
files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE.
Wykorzystuje tylko syntetyzator na karcie muzycznej lub inne urz±dzenia MIDI
przy³±czone do niej.

%package kmidi
Summary:	KDE software MIDI Player	
Summary(pl):	Programowy odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description kmidi -l pl
Programowy odtwarzacz MIDI. Wykorzystuje patche z GUSa i moc procesora do
stworzenia dobrej jako¶ci d¼wiêku.

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
CD Player with CDDB support. It can automaticaly update its CD database with
the Internet and show graphical interpretation of played sounds.

%description kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê danych
o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn± graficzn±
interpretacjê granych d¼wiêków.

%package kaiman
Summary:	KDE Media Player
Summary(pl):	KDE Media Player
Group:		X11/Applications
Requires:	kdelibs = %{version} 

%description kaiman

%description -l pl kaiman

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs = %{version} 

%description mpeglib

%description -l pl mpeglib

%prep
%setup -q
%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
 	--with-pam="yes"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT


%post mpeglib -p /sbin/ldconfig
%postun mpeglib -p /sbin/ldconfig

%post aktion -p /sbin/ldconfig
%postun aktion -p /sbin/ldconfig

%post arts -p /sbin/ldconfig
%postun arts -p /sbin/ldconfig

%post kmid -p /sbin/ldconfig
%postun kmid -p /sbin/ldconfig

%post kmix -p /sbin/ldconfig
%postun kmix -p /sbin/ldconfig

%post kscd -p /sbin/ldconfig
%postun kscd -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_bindir}/yaf*
%attr(755,root,root) %{_libdir}/libyaf*.so.*.*.*
%attr(755,root,root) %{_libdir}/libarts_mpeglib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libmpeg-*.so.*.*.*
%{_libdir}/libmpeg.so
%{_libdir}/libmpeg.la
%{_libdir}/libyaf*.so
%{_libdir}/libyaf*.la
%{_libdir}/libarts_mpeglib*.so
%{_libdir}/libarts_mpeglib*.la
%{_includedir}/mpeglib_artsplug
%{_includedir}/mpeglib

%files aktion
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aktion*
%attr(755,root,root) %{_libdir}/libaktion.so.*.*.*
%{_libdir}/libaktion.so
%{_libdir}/libaktion.la
%{_applnkdir}/Multimedia/aktion.desktop
%{_datadir}/apps/aktion
%{_datadir}/config/aktionrc
%{_pixmapsdir}/locolor/*x*/apps/aktion.png

%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arts*
%attr(755,root,root) %{_bindir}/midisend
%attr(755,root,root) %{_libdir}/libartsbuilder.so.*.*.*
%attr(755,root,root) %{_libdir}/libartsmodules.so.*.*.*
%{_libdir}/mcop/artsmodules.*
%{_libdir}/mcop/Arts/*
%{_libdir}/libartsbuilder.so
%{_libdir}/libartsbuilder.la
%{_libdir}/libartsmodules.so
%{_libdir}/libartsmodules.la
%{_applnkdir}/Multimedia/arts*.desktop
%{_datadir}/apps/artsbuilder
%{_datadir}/apps/artscontrol
%{_datadir}/doc/kde/HTML/en/artsbuilder

%files kaiman
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaiman
%{_applnkdir}/Multimedia/kaiman.desktop
%{_datadir}/apps/kaiman
%{_pixmapsdir}/locolor/*x*/apps/kaiman.png
%{_pixmapsdir}/hicolor/*x*/apps/kaiman.png

%files kmid
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%attr(755,root,root) %{_libdir}/libkmidpart.so.*.*.*
%{_libdir}/libkmidpart.so
%{_applnkdir}/Multimedia/kmid.desktop
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/doc/kde/HTML/en/kmid
%{_pixmapsdir}/locolor/*x*/apps/kmid.png
%{_pixmapsdir}/hicolor/*x*/apps/kmid.png

%files kmidi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmidi
%attr(755,root,root) %{_bindir}/sf2cfg
%attr(755,root,root) %{_bindir}/timidity
%{_applnkdir}/Multimedia/kmidi.desktop
%{_applnkdir}/Multimedia/timidity.desktop
%{_datadir}/apps/kmidi
%{_datadir}/doc/kde/HTML/en/kmidi
%{_pixmapsdir}/locolor/*x*/apps/kmidi.png
%{_pixmapsdir}/hicolor/*x*/apps/kmidi.png

%files kmix
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_libdir}/kmixctrl.*
%attr(755,root,root) %{_libdir}/libkcm_kmix.*
%attr(755,root,root) %{_libdir}/libkmixapplet.so.*.*.*
%{_libdir}/libkmixapplet.so
%{_applnkdir}/Multimedia/kmix.desktop
%{_applnkdir}/Settings/Sound/kmix.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_datadir}/apps/kmix
%{_datadir}/apps/kicker/applets/*
%{_datadir}/doc/kde/HTML/en/kmix
%{_pixmapsdir}/locolor/*x*/apps/kmix.png
%{_pixmapsdir}/hicolor/*x*/apps/kmix.png

%files kscd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%attr(755,root,root) %{_libdir}/libworkman.so.*.*.*
%{_libdir}/libworkman.so
%{_libdir}/libworkman.la
%{_applnkdir}/Multimedia/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/mimelnk/text/xmcd.desktop
%{_datadir}/doc/kde/HTML/en/kscd
%{_pixmapsdir}/locolor/*x*/apps/kscd.png
%{_pixmapsdir}/hicolor/*x*/apps/kscd.png
