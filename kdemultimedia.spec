#
# Conditional build:
# _without_xine	Set this option in case You haven't
#		xine-lib to ommit xine plug-in building.
#
# _without_alsa	Set this option in case you dont want alsa.
#
# _with_esd	Set this option in case you want esd support.
#
# _with_nas 	Set this option if you want nas support.
#

%define         _state          stable
%define         _ver		3.1.1

%define		_without_alsa	1
%ifarch	sparc sparcv9 sparc64
%define		_with_esd	1
%endif

Summary:	K Desktop Environment - multimedia applications
Summary(pl):	K Desktop Environment - aplikacje multimedialne
Name:		kdemultimedia
Version:	%{_ver}
Release:	3
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	bdd53d23d13adf2419554e995417178e
# generated from kde-i18n
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	83b0712b82e44be9bfedd9d78ddaf4f1
Patch0:		%{name}-timidity.patch
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_alsa:BuildRequires:	alsa-driver-devel}
BuildRequires:	arts-devel
BuildRequires:	arts-kde-devel
BuildRequires:	cdparanoia-III
BuildRequires:	cdparanoia-III-devel
%{?_with_esd:BuildRequires:     esound-devel}
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	kdelibs-devel >= 8:%{version}
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
%{?_with_nas:BuildRequires:	nas-devel >= 1.5}
BuildRequires:	perl
%{!?_without_xine:BuildRequires: xine-lib-devel}
BuildRequires:	zlib-devel
Requires:	kdelibs = 8:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

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

 - Aktion - odtwarzacz plik�w avi
 - Arts - narz�dzia arts
 - Kaboodle - odtwarzacz plik�w multimedialnych
 - KMID - odtwarzacz MIDI,
 - KMIDI - programowy odtwarzacz MIDI,
 - KMIX - mikser audio,
 - KSCD - odtwarzacz CD.
 - Noatun - odtwarzacz plik�w multimedialnych

%package devel
Summary:	kdemultimedia - headers
Summary(pl):	kdemultimedia - pliki nag��wkowe
Group:		X11/Development/Libraries
Requires:	arts-devel >= 1.0.3
Requires:	kdelibs-devel >= 8:%{version}
Requires:	%{name}-arts = %{epoch}:%{version}
Requires:	%{name}-mpeglib = %{epoch}:%{version}
Requires:	%{name}-noatun = %{epoch}:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description devel
kdemultimedia - headers.

%description devel -l pl
kdemultimedia - pliki nag��wkowe.

%package aktion
Summary:	KDE Media Player
Summary(pl):	Odtwarzacz multimedialny dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	aktion

%description aktion
This is a media player for KDE. Currently it can be only used to play
WAV files.

%description aktion -l pl
Odtwarzacz multimedialny dla KDE. W tej chwili obs�uguje tylko pliki
WAV.

%package arts
Summary:	Arts Tools
Summary(pl):	Narz�dzia Arts
Group:		X11/Applications
Requires(post):	/sbin/ldconfig
Requires:	kdelibs >= 8:%{version}
Requires:	%{name}-mpeglib = %{epoch}:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description arts
Arts Tools.

%description arts -l pl
Narz�dzia Arts.

%package kaboodle
Summary:	Media player
Summary(pl):	Odtwarzacz multimedialny
Group:		X11/Applications
Obsoletes:	kdemultimedia < 3.0.8

%description kaboodle
Media player.

%description kaboodle -l pl
Odtwarzacz multimedialny.

%package kaudiocreator
Summary:	Audio Creator
Summary(pl):	Kreator audio
Group:		X11/Applications
Obsoletes:	kdemultimedia < 3.0.8

%description kaudiocreator
CD ripper and sound encoder frontend. Already provides audiocd
protocol for konqueror.

%description kaudiocreator -l pl
Nak�adka na CD ripper i enkoder d�wi�ku. Dostarcza r�wnie� protok�
audiocd do konquerora.

%package kfile
Summary:	Audio file formats enhanced information
Summary(pl):	Rozszerzone informacje o plikach d�wi�kowych
Group:		X11/Development/Libraries
Obsoletes:	kdemultimedia < 3.0.8

%description kfile
This package adds a fold to konqueror "file properties" dialog window
with file enhanced informations.

%description kfile -l pl
Ten pakiet dodaje do okna dialogowego "w�asciwo�ci pliku" konquerora
dodatkow� zak�adk� z rozszerzonymi informacjami o pliku.

%package kmid
Summary:	KDE MIDI Player
Summary(pl):	Odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description kmid
This is a MIDI player for KDE. It uses sound-card synthetizer or other
hardware connected to MIDI to play MIDI files.

%description kmid -l pl
Odtwarzacz MIDI dla KDE. Wykorzystuje tylko syntezator na karcie
muzycznej lub inne urz�dzenia MIDI przy��czone do niej.

%package kmidi
Summary:	KDE software MIDI Player
Summary(pl):	Programowy odtwarzacz MIDI dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description kmidi
Software MIDI player. It uses GUS patch files and CPU power to create
high-quality sound.

%description kmidi -l pl
Programowy odtwarzacz MIDI. Wykorzystuje patche z GUSa i moc procesora
do stworzenia dobrej jako�ci d�wi�ku.

%package kmix
Summary:	KDE audio mixer
Summary(pl):	Mixer audio dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description kmix
Sound mixer application for KDE.

%description kmix -l pl
Mikser audio dla KDE.

%package krec
Summary:	KDE sound recorder
Summary(pl):	Rejestrator d�wi�ku dla KDE
Group:		X11/Applications
Requires:	%{name}-arts = %{epoch}:%{version}
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description krec
KDE sound recorder.

%description krec -l pl
Rejestrator d�wi�ku dla KDE.

%package kscd
Summary:	KDE CD Player
Summary(pl):	Odtwarzacz CD dla KDE
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Obsoletes:	kdemultimedia < 3.0.8

%description kscd
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description kscd -l pl
Odtwarzacz CD z obs�ug� CDDB. Automatycznie uaktualnia swoj� baz�
danych o p�ytach CD z Internetem. Potrafi tak�e wy�wietli� �adn�
graficzn� interpretacj� granych d�wi�k�w.

%package mpeglib
Summary:	MPEG lib
Summary(pl):	MPEG lib
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Requires:	arts >= 12:1.0.0
Obsoletes:	kdemultimedia < 3.0.8

%description mpeglib
MPEG lib.

%description mpeglib -l pl
MPEG lib.

%package noatun
Summary:	KDE Media Player
Summary(pl):	KDE Media Player - odtwarzacz plik�w multimedialnych
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Requires:	arts >= 12:1.0.0
Obsoletes:	kdemultimedia < 3.0.8

%description noatun
KDE Media Player.

%description noatun -l pl
KDE Media Player - odtwarzacz plik�w multimedialnych.

%package xine
Summary:	Xine Plug-in
Summary(pl):	Wtyczka do Xine
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}
Requires:	arts >= 12:1.0.0
Requires:	xine-lib
Obsoletes:	kdemultimedia < 3.0.8

%description xine
Xine Plug-in.

%description xine -l pl
Wtyczka do Xine.

%prep
%setup -q
%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags} -I%{_includedir}"

AUDIO=""
%ifnarch sparc sparcv9 sparc64
AUDIO=oss,$AUDIO
%endif
%{!?_without_alsa:AUDIO=alsa,$AUDIO}
%{?_with_nas:AUDIO=nas,$AUDIO}
%{?_with_esd:AUDIO=esd,$AUDIO}
AUDIO=${AUDIO%%,}

# kdemultimedia includes kernel headers which breaks things
# with PLD kernels 2.4.x, below workaround  by misiek
mkdir linux
sed -e 's#slots\[CDROM_MAX_SLOTS\]#kde_slots\[CDROM_MAX_SLOTS\]#g' \
/usr/include/linux/cdrom.h > linux/cdrom.h

for plik in `find ./ -name \*.desktop` ; do
	echo $plik
	perl -pi -e "s/\[nb\]/\[no\]/g" $plik
done

%configure \
 	--with-pam="yes" \
	--enable-final \
	--enable-audio=$AUDIO

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/{timidity,ktimidity}

ALD=$RPM_BUILD_ROOT%{_applnkdir}
install -d $ALD/{Settings/KDE,Multimedia/ArtsTools}
mv -f $ALD/{Multimedia/More/*.desktop,Multimedia}
mv -f $ALD/{Multimedia/arts*.desktop,Multimedia/ArtsTools}
mv -f $ALD/{Settings/[!K]*,Settings/KDE}

echo "[Desktop Entry]\nName=Arts Tools\nIcon=arts\nType=Directory" \
    > $ALD/Multimedia/ArtsTools/.directory

cat $ALD/Multimedia/timidity.desktop |sed 's/Exec=timidity/Exec=ktimidity/' \
    > $ALD/Multimedia/ktimidity.desktop

cd $RPM_BUILD_ROOT%{_datadir}/apps/kmidi/config
ln -s gravis.cfg GUSpatches
cd -

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for i in /usr/X11R6/share/locale/*/LC_MESSAGES/*.mo ; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

:> kfile.lang
programs="kfile_au kfile_avi kfile_m3u kfile_mp3 kfile_ogg kfile_wav"
for i in $programs; do
        %find_lang $i --with-kde
        cat $i.lang >> kfile.lang
done

:> arts.lang
programs="artsbuilder artscontrol artsmodules desktop_kdemultimedia"
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> arts.lang
done

%find_lang kmix			--with-kde
%find_lang kmixcfg		--with-kde
%find_lang kcmkmix		--with-kde
cat {kmixcfg,kcmkmix}.lang >> kmix.lang

%find_lang kaudiocreator	--with-kde
%find_lang kcmaudiocd		--with-kde
%find_lang kio_audiocd		--with-kde
cat {kcmaudiocd,kio_audiocd}.lang >> kaudiocreator.lang

%find_lang kaboodle		--with-kde
%find_lang kmid			--with-kde
%find_lang kmidi		--with-kde
%find_lang krec			--with-kde
%find_lang kscd			--with-kde
%find_lang noatun		--with-kde
%find_lang aktion		--with-kde
#%find_lang kmyapp		--with-kde
#%find_lang koncd		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	aktion	-p /sbin/ldconfig
%postun	aktion	-p /sbin/ldconfig

%post arts
/sbin/ldconfig
echo "Remember to restart artsd!"

%postun	arts	-p /sbin/ldconfig

%post	kscd	-p /sbin/ldconfig
%postun	kscd	-p /sbin/ldconfig

%post   mpeglib -p /sbin/ldconfig
%postun mpeglib -p /sbin/ldconfig

%post	noatun	-p /sbin/ldconfig
%postun	noatun	-p /sbin/ldconfig


%files devel
%defattr(644,root,root,755)
# shared libraries
%attr(755,root,root) %{_libdir}/libnoatuncontrols.so
%attr(755,root,root) %{_libdir}/libnoatun.so
%attr(755,root,root) %{_libdir}/libnoatuntags.so
%attr(755,root,root) %{_libdir}/libworkman.so
# shared, possibly (lt_)dlopened libraries
%attr(755,root,root) %{_libdir}/libaktion.so
%attr(755,root,root) %{_libdir}/libartsbuilder.so
%attr(755,root,root) %{_libdir}/libartsgui_idl.so
%attr(755,root,root) %{_libdir}/libartsgui_kde.so
%attr(755,root,root) %{_libdir}/libartsgui.so
%attr(755,root,root) %{_libdir}/libartsmidi_idl.so
%attr(755,root,root) %{_libdir}/libartsmidi.so
%attr(755,root,root) %{_libdir}/libartsmodules.so
%attr(755,root,root) %{_libdir}/libarts_mpeglib.so
%attr(755,root,root) %{_libdir}/libarts_splay.so
%attr(755,root,root) %{_libdir}/libmpeg.so
%attr(755,root,root) %{_libdir}/libyafcore.so
%attr(755,root,root) %{_libdir}/libyafxplayer.so
%{_includedir}/*.h
%{_includedir}/arts/*
%{_includedir}/mpeglib*
%{_includedir}/noatun

%files aktion -f aktion.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aktion*
%attr(755,root,root) %{_libdir}/libaktion.so.*
%{_libdir}/libaktion.la
%{_datadir}/apps/aktion
%{_datadir}/config/aktionrc
%{_applnkdir}/Multimedia/aktion.desktop
%{_pixmapsdir}/*/*/apps/aktion.png

%files arts -f arts.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/arts*
%attr(755,root,root) %{_bindir}/midisend
%attr(755,root,root) %{_libdir}/libaudiofilearts.so
%{_libdir}/libaudiofilearts.la
%attr(755,root,root) %{_libdir}/libartseffects.so
%attr(755,root,root) %{_libdir}/libarts[!_]*.so.*
%{_libdir}/libarts[!_]*.la
%attr(755,root,root) %{_libdir}/libarts_[!m]*.so.*
%{_libdir}/libarts_[!mx]*.la
%{_libdir}/mcop/audiofilearts*
%{_libdir}/mcop/arts*
%{_libdir}/mcop/Splay*
%{_libdir}/mcop/Arts/*
%{_libdir}/mcop/ExtraStereo.mcopclass
%{_libdir}/mcop/ExtraStereoGuiFactory.mcopclass
%{_libdir}/mcop/VoiceRemoval.mcopclass
%{_libdir}/mcop/RawWriter.mcopclass
%{_datadir}/apps/artsbuilder
%{_datadir}/apps/artscontrol
%{_datadir}/mimelnk/application/*arts*
%dir %{_applnkdir}/Multimedia/ArtsTools
%{_applnkdir}/Multimedia/ArtsTools/.directory
%{_applnkdir}/Multimedia/ArtsTools/arts*.desktop
%{_pixmapsdir}/*/*/*/arts*

%files kaboodle -f kaboodle.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaboodle
%attr(755,root,root) %{_libdir}/kaboodle.so
%{_libdir}/kaboodle.la
%attr(755,root,root) %{_libdir}/kde3/libkaboodlepart.so
%{_libdir}/kde3/libkaboodlepart.la
%{_datadir}/apps/kaboodle
%{_datadir}/services/kaboodle_component.desktop
%{_applnkdir}/Multimedia/kaboodle.desktop
%{_pixmapsdir}/*/*/apps/kaboodle.*

%files kaudiocreator -f kaudiocreator.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaudiocreator
%attr(755,root,root) %{_libdir}/kde3/kcm_audiocd.so
%{_libdir}/kde3/kio_audiocd.la
%attr(755,root,root) %{_libdir}/kde3/kio_audiocd.so
%{_libdir}/kde3/kcm_audiocd.la
%{_datadir}/apps/kaudiocreator
%{_datadir}/services/audiocd.protocol
%{_applnkdir}/Multimedia/kaudiocreator.desktop
%{_applnkdir}/Settings/KDE/Sound/audiocd.desktop
%{_pixmapsdir}/[!l]*/*/*/kaudiocreator.png

%files kfile -f kfile.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kfile_*.so
%{_libdir}/kde3/kfile_*.la
%{_datadir}/services/kfile_*.desktop

%files kmid -f kmid.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmid
%attr(755,root,root) %{_libdir}/kde3/libkmidpart.so
%{_libdir}/kde3/libkmidpart.la
%{_datadir}/apps/kmid
%{_datadir}/mimelnk/audio/x-karaoke.desktop
%{_datadir}/servicetypes/*midi*.desktop
%{_applnkdir}/Multimedia/kmid.desktop
%{_pixmapsdir}/*/*/*/kmid.png

%files kmidi -f kmidi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmidi
%attr(755,root,root) %{_bindir}/sf2cfg
%attr(755,root,root) %{_bindir}/ktimidity
%{_applnkdir}/Multimedia/kmidi.desktop
%{_applnkdir}/Multimedia/ktimidity.desktop
%{_datadir}/apps/kmidi
%{_pixmapsdir}/*/*/*/kmidi.png

%files kmix -f kmix.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmix
%attr(755,root,root) %{_bindir}/kmixctrl
%attr(755,root,root) %{_libdir}/kmix.so
%{_libdir}/kmix.la
%attr(755,root,root) %{_libdir}/kmixctrl.so
%{_libdir}/kmixctrl.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmix.so
%{_libdir}/kde3/kcm_kmix.la
%attr(755,root,root) %{_libdir}/kde3/kmix_panelapplet.so
%{_libdir}/kde3/kmix_panelapplet.la
%{_applnkdir}/Multimedia/kmix.desktop
%{_applnkdir}/.hidden/kmixcfg.desktop
%{_datadir}/services/kmixctrl_restore.desktop
%{_datadir}/apps/kmix
%{_datadir}/apps/kicker/applets/*
%{_pixmapsdir}/*/*/*/kmix.png

%files kscd -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%attr(755,root,root) %{_bindir}/workman2cddb.pl
%attr(755,root,root) %{_libdir}/libworkman.so.*
%{_libdir}/libworkman.la
%{_applnkdir}/Multimedia/kscd.desktop
%{_datadir}/apps/kscd
%{_datadir}/mimelnk/text/xmcd.desktop
%{_pixmapsdir}/*/*/*/kscd.png

%files krec -f krec.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/krec
%attr(755,root,root) %{_libdir}/krec.so
%{_libdir}/krec.la
%{_datadir}/apps/krec
%{_applnkdir}/Multimedia/krec.desktop
%{_pixmapsdir}/*/*/*/krec*

%files mpeglib
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeglibartsplay
%attr(755,root,root) %{_bindir}/yaf*
%attr(755,root,root) %{_libdir}/libyaf*.so.*
%{_libdir}/libyaf*.la
%attr(755,root,root) %{_libdir}/libarts_mpeglib*.so.*
%{_libdir}/libarts_mpeglib.la
%attr(755,root,root) %{_libdir}/libmpeg-*.so
%{_libdir}/libmpeg.la
# Note that SplayPlayObject.mopclass is *not* here.
#%%{_libdir}/mcop/VCDPlayObject.mcopclass
%{_libdir}/mcop/WAVPlayObject.mcopclass
%{_libdir}/mcop/OGGPlayObject.mcopclass
%{_libdir}/mcop/NULLPlayObject.mcopclass
%{_libdir}/mcop/MP3PlayObject.mcopclass
%{_libdir}/mcop/CDDAPlayObject.mcopclass
#%%{_libdir}/mcop/MPGPlayObject.mcopclass

%files noatun -f noatun.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/noatun*
%attr(755,root,root) %{_libdir}/libnoatun*.so.*
%attr(755,root,root) %{_libdir}/libnoatunarts.so
%{_libdir}/libnoatun*.la
%attr(755,root,root) %{_libdir}/libwinskinvis.so
%{_libdir}/libwinskinvis.la
%attr(755,root,root) %{_libdir}/kde3/noatun*.so
%{_libdir}/kde3/noatun*.la
%{_libdir}/mcop/Noatun
%{_libdir}/mcop/noatun*
%{_libdir}/mcop/winskinvis*
%attr(755,root,root) %{_datadir}/apps/kconf_update/noatun20update
%{_datadir}/apps/kconf_update/*.upd
%{_datadir}/apps/noatun*
%{_datadir}/mimelnk/interface/x-winamp-skin.desktop
%{_applnkdir}/Multimedia/noatun.desktop
%{_pixmapsdir}/*/*/*/noatun.png

%if %{?_without_xine:0}%{!?_without_xine:1}
%files xine
%defattr(644,root,root,755)
#%{_libdir}/kde3/videothumbnail.la
#%attr(755,root,root) %{_libdir}/kde3/videothumbnail.so
%attr(755,root,root) %{_libdir}/*_xine.so
%{_libdir}/*_xine.la
%{_libdir}/mcop/xinePlayObject.mcopclass
#%{_datadir}/apps/videothumbnail
#%{_datadir}/services/videothumbnail.desktop
%endif
