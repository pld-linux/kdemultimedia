Summary:     K Desktop Environment - multimedia applications
Summary(pl): K Desktop Environment - aplikacje multimedialne
Name:        kdemultimedia
Version:     1.1.1
Release:     2
Copyright:   GPL
Group:       X11/KDE/Multimedia
Group(pl):   X11/KDE/Multimedia
Vendor:	     The KDE Team
#ftp:	     ftp.kde.org
#patch:	     /pub/kde/stable/%{version}/distribution/tar/generic/source/
Source:      %{name}-%{version}.tar.bz2
Requires:    qt >= 1.44, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

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
  KMedia - Programik do odgrywania plików d¼wiêkowych
  KMID - Odgrywarka MIDI
  KMIDI - Programowa odgrywarka MIDI
  KMIX - Mixer audio
  KSCD - Odtwarzacz CD

%package kmedia
Summary:     KDE Media Player
Summary(pl): Odgrywarka multimedialna KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kmedia
This is a media player for KDE.
Currently it can be only used to play WAV files.

%description -l pl kmedia
Odgrywarka multimedialna dla KDE.
W tej chwili obs³uguje tylko pliki WAV.

%package kmid
Summary:     KDE MIDI Player	
Summary(pl): Odgrywarka MIDI dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kmid
This is a MIDI player for KDE.
It uses sound-card synthetizer or other hardware connected to MIDI to play MIDI
files.

%description kmid -l pl
Odgrywarka MIDI dla KDE.
Wykorzystuje tylko syntetyzator na karcie muzycznej lub inne urz±dzenia MIDI
po³±czone do niej.

%package kmidi
Summary:     KDE software MIDI Player	
Summary(pl): Programowa odgrywarka MIDI dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description kmidi -l pl
Programowa odgrywarka MIDI. Wykorzystuje patche z GUSa i moc procesora do
stworzenia dobrej jako¶ci d¼wiêku.

%package kmix 
Summary:     KDE audio mixer
Summary(pl): Mixer audio dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package kscd
Summary:     KDE CD Player	
Summary(pl): Odtwarzacz CD dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version} 

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
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti -fno-exceptions" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
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

%changelog
* Thu May 27 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [1.1.1-2]
- updates package to version 1.1.1,
- fixes problem with locala files,

* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sat Oct 10 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
