Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	1.1.2
Release:	1
Copyright:	GPL
Group:		X11/KDE/Multimedia
Group(pl):	X11/KDE/Multimedia
Vendor:		The KDE Team
Source:		ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	qt-devel >= 1.44
BuildRequires:	XFree86-devel
BuildRequires:	libstdc++-devel
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix	/usr/X11R6/

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

%package kmedia
Summary:	KDE Media Player
Summary(pl):	Odtwarzacz multimedialny dla KDE
Group:		X11/KDE/Multimedia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kmedia
This is a media player for KDE.
Currently it can be only used to play WAV files.

%description -l pl kmedia
Odtwarzacz multimedialny dla KDE.
W tej chwili obs³uguje tylko pliki WAV.

%package kmid
Summary:	KDE MIDI Player	
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/KDE/Multimedia
Requires:	qt >= 1.44
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
Group:		X11/KDE/Multimedia
Requires:	qt >= 1.44
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
Group:		X11/KDE/Multimedia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package kscd
Summary:	KDE CD Player	
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/KDE/Multimedia
Requires:	qt >= 1.44
Requires:	kdelibs = %{version} 

%description kscd
CD Player with CDDB support. It can automaticaly update its CD database with
the Internet and show graphical interpretation of played sounds.

%description kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê danych
o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn± graficzn±
interpretacjê granych d¼wiêków.

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-qt-dir=%{_prefix} \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

export KDEDIR=%{_prefix}
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

%find_lang kmedia
%find_lang kmix
%find_lang kscd
%find_lang kmid
%find_lang kmidi

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KMEDIA
#################################################

%files kmedia -f kmedia.lang
%defattr(644, root, root, 755)

%{_datadir}/kde/apps/kmedia

%lang(en) %{_datadir}/kde/doc/HTML/en/kmedia

%{_datadir}/kde/icons/mini/kmedia.xpm
%{_datadir}/kde/icons/kmedia.xpm

%config(missingok) /etc/X11/kde/applnk/Multimedia/KMedia.kdelnk

%attr(755,root,root) %{_bindir}/kmedia

#################################################
#             KMID
#################################################

%files kmid -f kmid.lang
%defattr(644, root, root, 755)

%config /etc/X11/kde/mimelnk/audio/x-karaoke.kdelnk

%config(missingok) /etc/X11/kde/applnk/Multimedia/kmid.kdelnk

%{_datadir}/kde/apps/kmid

%{_datadir}/kde/icons/mini/kmid.xpm
%{_datadir}/kde/icons/kmid.xpm

%lang(en) %{_datadir}/kde/doc/HTML/en/kmid
%lang(es) %{_datadir}/kde/doc/HTML/es/kmid

%attr(755,root,root) %{_bindir}/kmid

#################################################
#             KMIDI
#################################################

%files kmidi -f kmidi.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Multimedia/KMidi.kdelnk
%config %{_datadir}/kde/apps/kmidi/config/*.cfg

%attr(755,root,root) %{_bindir}/kmidi

%{_datadir}/kde/icons/mini/kmidi.xpm
%{_datadir}/kde/icons/kmidi.xpm

%dir %{_datadir}/kde/apps/kmidi
%dir %{_datadir}/kde/apps/kmidi/config

%{_datadir}/kde/apps/kmidi/config/chaos12-voices
%{_datadir}/kde/apps/kmidi/config/chaos8-voices
%{_datadir}/kde/apps/kmidi/config/megadrum
%{_datadir}/kde/apps/kmidi/config/megainst
%{_datadir}/kde/apps/kmidi/config/pila-voices
%{_datadir}/kde/apps/kmidi/config/sound-canvas-drums
%{_datadir}/kde/apps/kmidi/config/patch/
%{_datadir}/kde/apps/kmidi/pics/

%lang(en) %{_datadir}/kde/doc/HTML/en/kmidi
%lang(de) %{_datadir}/kde/doc/HTML/de/kmidi

#################################################
#             KMIX
#################################################

%files kmix -f kmix.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Multimedia/KMix.kdelnk

%attr(755,root,root) %{_bindir}/kmix

%{_datadir}/kde/icons/mini/kmix.xpm
%{_datadir}/kde/icons/kmix.xpm
%{_datadir}/kde/apps/kmix

%lang(en) %{_datadir}/kde/doc/HTML/en/kmix

#################################################
#             KSCD
#################################################

%files kscd -f kscd.lang
%defattr(644, root, root, 755)

%config(missingok) /etc/X11/kde/applnk/Multimedia/kscd.kdelnk
%config /etc/X11/kde/mimelnk/text/xmcd.kdelnk

%attr(755,root,root) %{_bindir}/kscdmagic
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/cddaslave
%attr(755,root,root) %{_bindir}/workman2cddb.pl

%{_datadir}/kde/apps/kscd

%{_datadir}/kde/icons/mini/kscd.xpm
%{_datadir}/kde/icons/kscd.xpm
%{_datadir}/kde/icons/cd.xpm

%lang(en) %{_datadir}/kde/doc/HTML/en/kscd
