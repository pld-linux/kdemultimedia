Summary:     K Desktop Environment - multimedia applications
Summary(pl): K Desktop Environment - aplikacje multimedialne
Name:        kdemultimedia
Version:     1.0
Release:     7
Copyright:   GPL
Group:       X11/KDE/Multimedia
Vendor:	     The KDE Team
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

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

%package -n kmedia
Summary:     KDE Media Player
Summary(pl): Odgrywarka multimedialna KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmedia
This is a media player for KDE.
Currently it can be only used to play WAV files.

%description -l pl -n kmedia
Odgrywarka multimedialna dla KDE.
W tej chwili obs³uguje tylko pliki WAV.

%package -n kmid
Summary:     KDE MIDI Player	
Summary(pl): Odgrywarka MIDI dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmid
This is a MIDI player for KDE.
It uses sound-card synthetizer or other hardware connected to MIDI to play MIDI
files.

%description -n kmid -l pl
Odgrywarka MIDI dla KDE.
Wykorzystuje tylko syntetyzator na karcie muzycznej lub inne urz±dzenia MIDI
po³±czone do niej.

%package -n kmidi
Summary:     KDE software MIDI Player	
Summary(pl): Programowa odgrywarka MIDI dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description -n kmidi -l pl
Programowa odgrywarka MIDI. Wykorzystuje patche z GUSa i moc procesora do
stworzenia dobrej jako¶ci d¼wiêku.

%package -n kmix 
Summary:     KDE audio mixer
Summary(pl): Mixer audio dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmix
Sound mixer application for KDE.

%description -n kmix -l pl
Mikser audio dla KDE.

%package -n kscd
Summary:     KDE CD Player	
Summary(pl): Odtwarzacz CD dla KDE
Group:       X11/KDE/Multimedia
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n kscd
CD Player with CDDB support. It can automaticaly update its CD database with
the Internet and show graphical interpretation of played sounds.

%description -n kscd -l pl
Odtwarzacz CD z obs³ug± CDDB. Automatycznie uaktualnia swoj± bazê danych
o p³ytach CD z Internetem. Potrafi tak¿e wy¶wietliæ ³adn± graficzn±
interpretacjê granych d¼wiêków.

%prep
%setup -q

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done
cd $DIR

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KMEDIA
#################################################

%files -n kmedia
%defattr(644,root,root,755)
/usr/X11R6/share/kde/apps/kmedia
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmedia
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmedia.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmedia.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kmedia.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmedia.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmedia.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmedia.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kmedia.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kmedia.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmedia.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kmedia.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmedia.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmedia.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kmedia.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmedia.mo
%lang(pt) /usr/X11R6/share/locale/pt_*/LC_MESSAGES/kmedia.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kmedia.mo

/usr/X11R6/share/kde/icons/mini/kmedia.xpm
/usr/X11R6/share/kde/icons/kmedia.xpm

%config(missingok) /etc/X11/kde/applnk/Multimedia/KMedia.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKMedia
%attr(755,root,root) /usr/X11R6/bin/kmedia

#################################################
#             KMID
#################################################

%files -n kmid
%defattr(644,root,root,755)
%config /etc/X11/kde/mimelnk/audio/x-karaoke.kdelnk
%config(missingok) /etc/X11/kde/applnk/Multimedia/kmid.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekmid
/usr/X11R6/share/kde/apps/kmid
/usr/X11R6/share/kde/icons/mini/kmid.xpm
/usr/X11R6/share/kde/icons/kmid.xpm
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmid
%lang(es) /usr/X11R6/share/kde/doc/HTML/es/kmid
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmid.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmid.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmid.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmid.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kmid.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kmid.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmid.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmid.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmid.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kmid.mo
%attr(755,root,root) /usr/X11R6/bin/kmid

#################################################
#             KMIDI
#################################################

%files -n kmidi
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Multimedia/KMidi.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKMidi
%config /usr/X11R6/share/kde/apps/kmidi/config/*.cfg
%attr(755,root,root) /usr/X11R6/bin/kmidi
/usr/X11R6/share/kde/icons/mini/kmidi.xpm
/usr/X11R6/share/kde/icons/kmidi.xpm
%dir /usr/X11R6/share/kde/apps/kmidi
%dir /usr/X11R6/share/kde/apps/kmidi/config
/usr/X11R6/share/kde/apps/kmidi/config/chaos12-voices
/usr/X11R6/share/kde/apps/kmidi/config/chaos8-voices
/usr/X11R6/share/kde/apps/kmidi/config/megadrum
/usr/X11R6/share/kde/apps/kmidi/config/megainst
/usr/X11R6/share/kde/apps/kmidi/config/pila-voices
/usr/X11R6/share/kde/apps/kmidi/config/sound-canvas-drums
/usr/X11R6/share/kde/apps/kmidi/config/patch/
/usr/X11R6/share/kde/apps/kmidi/pics/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmidi
%lang(de) /usr/X11R6/share/kde/doc/HTML/de/kmidi

#################################################
#             KMIX
#################################################

%files -n kmix
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Multimedia/KMix.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeKMix
%attr(755,root,root) /usr/X11R6/bin/kmix
/usr/X11R6/share/kde/icons/mini/kmix.xpm
/usr/X11R6/share/kde/icons/kmix.xpm
/usr/X11R6/share/kde/apps/kmix
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmix
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmix.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmix.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmix.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmix.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmix.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kmix.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kmix.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmix.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kmix.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmix.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmix.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmix.mo
%lang(pt) /usr/X11R6/share/locale/pt_*/LC_MESSAGES/kmix.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/kmix.mo

#################################################
#             KSCD
#################################################

%files -n kscd
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Multimedia/kscd.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekscd
%config /etc/X11/kde/mimelnk/text/xmcd.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kscdmagic
%attr(755,root,root) /usr/X11R6/bin/kscd
%attr(755,root,root) /usr/X11R6/bin/cddaslave
%attr(755,root,root) /usr/X11R6/bin/workman2cddb.pl
/usr/X11R6/share/kde/apps/kscd
/usr/X11R6/share/kde/icons/mini/kscd.xpm
/usr/X11R6/share/kde/icons/kscd.xpm
/usr/X11R6/share/kde/icons/cd.xpm
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kscd
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kscd.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kscd.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kscd.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kscd.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/kscd.mo
%lang(zh) /usr/X11R6/share/locale/zh_*/LC_MESSAGES/kscd.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kscd.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kscd.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kscd.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kscd.mo

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Sat Oct 10 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- created new spec based on kdebase.spec.
