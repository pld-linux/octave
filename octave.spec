Summary:	GNU Octave - a high-level language for numerical computations
Summary(cs):	GNU Octave - vy¹¹í programovací jazyk pro numerické vıpoèty
Summary(da):	GNU Octave - et højniveausprog for numeriske beregninger
Summary(de):	GNU Octave - eine höhere Programmiersprache für nummerische Berechnungen
Summary(es):	GNU Octave - lenguaje de alto nivel para cálculos numéricos
Summary(fr):	GNU Octave - langage haut niveau pour les calculs numériques
Summary(it):	GNU Octave - linguaggio di alto livello per calcoli numerici
Summary(ja):	GNU Octave ¿ôÃÍ·×»»ÍÑ¤Î¹âµé¸À¸ì
Summary(ko):	GNU Octave »ê¼ú °è»êÀ» À§ÇÑ °íÂ÷¿ø ¾ğ¾î 
Summary(no):	GNU Octave - et høynivåspråk for numeriske beregninger
Summary(pl):	GNU Octave - jêzyk programowania do obliczeñ numerycznych
Summary(pt):	GNU Octave - uma linguagem de alto nível para cálculos numéricos
Summary(pt_BR):	GNU Octave - um programa para cálculo numérico e matricial
Summary(ru):	GNU Octave - ñÚÙË ×ÙÓÏËÏÇÏ ÕÒÏ×ÎÑ ÄÌÑ ×ÙĞÏÌÎÅÎÉÑ ÍÁÔÅÍÁÔÉŞÅÓËÉÈ ÒÁÓŞÅÔÏ×
Summary(sv):	GNU Octave - ett högninvåspråk för numeriska beräkningar
Summary(zh_CN):	GNU Octave - ÓÃÓÚÊı×Ö¼ÆËãµÄ¸ß¼¶ÓïÑÔ¡£
Name:		octave
Version:	2.1.46
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.che.wisc.edu/pub/octave/bleeding-edge/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www.che.wisc.edu/octave/
BuildRequires:	bison
BuildRequires:	blas-devel
BuildRequires:	fftw-devel
BuildRequires:	flex
BuildRequires:	gcc-g77
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	gnuplot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description -l cs
GNU Octave je vy¹¹í programovací jazyk, primárnì urèenı pro numerické
vıpoèty. Poskytuje pohodlné rozhraní pøíkazového øádku pro numerické
øe¹ení lineárních a nelineárních problémù a pro provádìní jinıch
numerickıch experimentù za pou¾ívání jazyku, kterı je témìø plnì
kompatibilní s programem Matlab. Mù¾e bıt pou¾íván i jako dávkovı
jazyk.

Octave má rozsáhlé nástroje pro øe¹ení obvyklıch numerickıch úloh v
lineární algebøe, nalezení koøenù nelineárních rovnic, integrování
bì¾nıch funkcí, polynomiální manipulace, integrování základních
diferenciálních a algebraicko-diferenciálních rovnic. Je jednodu¹e
roz¹iøitelnı a pøizpùsobitelnı pomocí u¾ivatelsky definovanıch funkcí
napsanıch v jeho vlastním jazyku. Mù¾e pou¾ívat dynamicky zavádìné
moduly napsané v jazycích C++, C, Fortran a jinıch.

%description -l da
GNU Octave er et høgniveausprog, hovedsakligen beregnet til for
numeriska beregningar. Det har et bekvæmt kommandoradsgrænseflade for
at løsa linjæra og ickelinjæra problem numeriskt, og for at utføra
andra numeriske experiment med et sprog som i stora dele er
kompatibelt med Matlab. Det kan også bruges som et sprog for satsvis
bearbejdning.

Octave har omfattende værktøj for at løsa almindelige problem inom
numerisk linjær algebra, finde røtter for ickelinjæra ekvationer,
integrere normala funktioner, behandle polynom, og integrere ordinære
differential og differentialalgebraiska ekvationer. Det er let at
utvidga og anpassa via brugerdefinierede funktioner skrivna i Octaves
eget sprog, og via dynamisk laddade moduler skriven i C++, C, Fortran,
eller andra sprog.

%description -l de
GNU Octave ist eine High-Level-Programmiersprache, die hauptsächlich
für nummerische Berechnungen vorgesehen ist. Sie verfügt über eine
benutzerfreundliche Befehlszeilenoberfläche zur nummerischen Lösung
von linearen und nichtlinearen Aufgaben und zum Ausführen weiterer
nummerischer Experimente unter Verwendung einer Programmiersprache,
die größtenteils mit Matlab kompatibel ist. Die Programmiersprache
kann auch als Batch-orientierte Sprache verwendet werden.

Octave verfügt über umfangreiche Tools zum Lösen allgemeiner
nummerischer linearer algebraischer Aufgaben, zum Ermitteln der
Lösungen von nichtlinearen Gleichungen, zum Integrieren gewöhnlicher
Funktionen, zum Bearbeiten von Polynomen und zum Integrieren
gewöhnlicher Differential- und Differential-algebraischer Gleichungen.
Octave kann mit benutzerdefinierten Funktionen, die in der speziellen
Programmiersprache von Octave geschrieben sind, oder mit dynamisch
geladenen, in C++, C, Fortran oder einer anderen Programmiersprache
geschriebenen Modulen erweitert und angepasst werden.

%description -l es
GNU Octave lenguaje de alto nivel, pensado para cálculos numéricos.
Provee un interfaz de línea de comando para resolver problemas
lineales y no lineales numéricamente, y para realizar otros
experimentos numéricos usando un lenguaje casi compatible con Matlab.
Puede utilizarse también fuera de la línea de comandos.

Octave tiene herramientas para resolver problemas numéricos de algebra
lineal común, encontrar raices de ecuaciones no-lineales, integración
de funciones ordinarias, manipulación de polinomios, e integrar
ecuaciones diferenciales ordinarias y algebraícas diferenciales. Es
facilmente extensible y configurable via funciones de usuario escritas
en el lenguaje Octave, o usando módulos dinámicos cargables escritos
en C++, C, Fortran u otros lenguajes.

%description -l fr
GNU Octave est un langage haut niveau conçu pour le calcul numérique.
Il offre une interface de ligne de commande pratique permettant de
résoudre numériquement des problèmes linéaires et non linéaires et
d'effectuer d'autres expériences numériques à l'aide d'un langage
presque totalement compatible avec Matlab. Il peut également être
utilisé comme langage à orientation par lots.

Octave comporte des outils étendus permettant de résoudre des
problèmes communs d'algèbre linéaire numérique, en trouvant les
racines d'équations non linéaires, en intégrant des fonctions
ordinaires, en manipulant des polynômes et en intégrant des équations
différentielles ordinaires et différentielles algébriques. Il est
facilement extensible et personnalisable au moyen de fonctions
définies par l'utilisateur, écrites dans le langage d'Octave, ou à
l'aide de modules chargés dynamiquement, écrits en C++, C, Fortran ou
autres langages.

%description -l it
GNU Octave è un linguaggio di alto livello per il calcolo numerico.
Fornisce una interfaccia basata sulla linea di comando per la
risoluzione numerica di problemi lineari e non lineari e per eseguire
altri esperimenti numerici usando un linguaggio per lo più compatibile
con Matlab. Può inoltre essere utilizzato come linguaggio orientato al
batch.

Octave possiede vari tool per risolvere problemi di algebra lineare,
per la ricerca di radici di equazioni non lineari, per il calcolo di
integrali di funzioni, per l'elaborazione di polinomi, per le
equazioni differenziali ordinarie e algebriche. Può essere facilmente
esteso e personalizzato tramite nuove funzioni definite dall'utente e
scritte nel linguaggio di Octave o tramite moduli caricati in modo
dinamico scritti in C, C++, Fortran o altri linguaggi.

%description -l ja
GNU Octave ¤Ï¡¢¼ç¤È¤·¤Æ¿ôÃÍ·×»»¤òÌÜÅª¤È¤·¤¿¹â¥ì¥Ù¥ë¸À¸ì¤Ç¤¹¡£
GNU Octave ¤Ï¡¢Àş·¿/ÈóÀş·¿ÌäÂê¤ò¿ôÃÍÅª¤Ë²ò¤¤¤¿¤ê¡¢Matlab 
¤È¤ÎÂçÉôÊ¬¤Î¸ß´¹À­¤ò»ı¤Ã¤¿¸À¸ì¤ò»ÈÍÑ¤·¤Æ¤½¤ÎÂ¾¤Î¿ôÃÍÅª¼Â¸³¤ò¹Ô
¤Ã¤¿¤ê¤¹¤ë¤¿¤á¤ÎÊØÍø¤Ê¥³¥Ş¥ó¥É¥é¥¤¥ó¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òÄó¶¡¤·¤Ş¤¹¡£
¥Ğ¥Ã¥Á»Ø¸ş¤Î¸À¸ì¤È¤·¤Æ»ÈÍÑ¤¹¤ë¤³¤È¤â¤Ç¤­¤Ş¤¹¡£Octave ¤Ï¡¢
¶¦ÄÌ¤Î¿ôÃÍÀş·¿Âå¿ôÌäÂê¤ò²ò¤¤¤¿¤ê¡¢ÈóÀş·¿ÊıÄø¼°¤Îº¬¤ò¸«¤Ä¤±¤¿¤ê¡¢
ÄÌ¾ï¤Î´Ø¿ô¤òÀÑÊ¬¤·¤¿¤ê¡¢Â¿¹à¼°¤òÁàºî¤·¤¿¤ê¡¢¾ïÈùÊ¬ÊıÄø¼°¤äÂå¿ô
ÈùÊ¬ÊıÄø¼°¤òÀÑÊ¬¤·¤¿¤ê¤¹¤ë¤¿¤á¤Î¹­ÈÏ¤Ê¥Ä¡¼¥ë¤òÈ÷¤¨¤Æ¤¤¤Ş¤¹¡£Octave 
ÆÈ¼«¤Î¸À¸ì¤Ç½ñ¤«¤ì¤¿¥æ¡¼¥¶¡¼ÄêµÁ¤Î´Ø¿ô¤ä¡¢C++¡¢C¡¢Fortlan¡¢¤½¤ÎÂ¾¤Î
¸À¸ì¤Ç½ñ¤«¤ì¤¿Æ°Åª¤Ë¥í¡¼¥É¤µ¤ì¤ë¥â¥¸¥å¡¼¥ë¤ò»ÈÍÑ¤¹¤ì¤Ğ¡¢ÍÆ°×¤Ë³ÈÄ¥
¤ª¤è¤Ó¥«¥¹¥¿¥Ş¥¤¥º¤¹¤ë¤³¤È¤¬¤Ç¤­¤Ş¤¹¡£

%description -l pl
GNU Octave jest jêzykiem programowania wysokiego poziomu przeznaczonym
g³ównie do obliczeñ numerycznych. Octave jest w du¿ym stopniu
kompatybilny z jêzykiem Matlab. Pracowaæ mo¿na wprost z linii poleceñ
lub uruchamiaæ programy stworzone za pomoc± zewnêtrznego edytora.

%description -l pt
O Octave da GNU é uma linguagem de alto nível, vocacionada
principalmente para o cálculo numérico. Oferece uma interface de linha
de comandos para resolver problemas lineares e não-lineares
numericamente, e para realizar outras experiências numéricas usando
uma linguagem que é relativamente compatível com o Matlab. Pode também
ser usado como uma linguagem orientada por lotes.

O Octave tem ferramentas extensivas para resolver problemas comuns de
álgebra linear, descobrir as raizes de equações não-lineares, integrar
funções ordinárias, manipular polinómios e integrar equações
diferenciais ordinárias e diferenciais algébricas. É facilmente
extensível e personalizável através de funções definidas pelo
utilizador, escritas na própria linguagem do Octave, ou usando módulos
carregados dinamicamente e feitos em C, C++, Fortran ou outras
linguagens."

%description -l pt_BR
GNU Octave - Um programa de cálculo numérico e matricial. Possui
linguagem de alto nível e ambiente interativo para computação numérica
semelhantes ao do Matlab.

%description -l ru
GNU Octave - ÜÔÏ ÑÚÙË ×ÙÓÏËÏÇÏ ÕÒÏ×ÎÑ, ĞÒÅÄÎÁÚÎÁŞÅÎÎÙÊ ÄÌÑ ×ÙĞÏÌÎÅÎÉÑ
ÍÁÔÅÍÁÔÉŞÅÓËÉÈ ×ÙŞÉÓÌÅÎÉÊ. ïÎ ĞÒÅÄÏÓÔÁ×ÌÑÅÔ ÕÄÏÂÎÙÊ ËÏÍÍÁÎÄÎÙÊ
ÉÎÔÅÒÆÅÊÓ ÄÌÑ ÒÅÛÅÎÉÑ ÌÉÎÅÊÎÙÈ É ÎÅÌÉÎÅÊÎÙÈ ÍÁÔÅÍÁÔÉŞÅÓËÉÈ ÚÁÄÁŞ É ÄÌÑ
ĞÒÏ×ÅÄÅÎÉÑ ÄÒÕÇÉÈ ÁÒÉÆÍÅÔÉŞÅÓËÉÈ ÜËÓĞÅÒÉÍÅÎÔÏ×, ÉÓĞÏÌØÚÕÑ ÑÚÙË, ×
ÂÏÌØÛÅÎÓÔ×Å ÓÌÕŞÁÅ× ÓÏ×ÍÅÓÔÉÍÙÊ Ó Mathlab.

ëÒÏÍÅ ÔÏÇÏ, Octave ÍÏÖÅÔ ÉÓĞÏÌØÚÏ×ÁÔØÓÑ ÄÌÑ ĞÁËÅÔÎÏÊ ÏÂÒÁÂÏÔËÉ É ÉÍÅÅÔ
ÓÒÅÄÓÔ×Á ÒÁÓÛÉÒÅÎÉÑ ÄÌÑ ÒÅÛÅÎÉÑ ÌÉÎÅÊÎÙÈ ÁÌÇÅÂÒÁÉŞÅÓËÉÈ ÚÁÄÁŞ,
ÎÁÈÏÖÄÅÎÉÑ ËÏÒÎÅÊ ÎÅÌÉÎÅÊÎÙÈ ÕÒÁ×ÎÅÎÉÊ, ÉÎÔÅÇÒÉÒÏ×ÁÎÉÅ ÆÕÎËÃÉÊ, ÒÁÂÏÔÕ
Ó ĞÏÌÉÎÏÍÁÍÉ É ÒÅÛÅÎÉÅ ÒÁÚÌÉŞÎÙÈ ÄÉÆÆÅÒÅÎÃÉÁÌØÎÙÈ ÕÒÁ×ÎÅÎÉÊ. ñÚÙË
ÍÏÖÎÏ ÌÅÇËÏ ÒÁÓÛÉÒÉÔØ ĞÒÉ ĞÏÍÏİÉ ÓÏÂÓÔ×ÅÎÎÏ ÑÚÙËÁ Octave ÉÌÉ ÉÓĞÏÌØÚÕÑ
ÄÉÎÁÍÉŞÅÓËÉ ÚÁÇÒÕÖÁÅÍÙÅ ÍÏÄÕÌÉ, ÎÁĞÉÓÁÎÎÙÅ ÎÁ ÑÚÙËÁÈ C, C++, æÏÒÔÒÁÎ É
ÄÒ.

%description -l sv
GNU Octave är ett högnivåspråk, huvudsakligen avsett för numeriska
beräkningar. Det har ett bekvämt kommandoradsgränssnitt för att lösa
linjära och ickelinjära problem numeriskt, och för att utföra andra
numeriska experiment med ett språk som i stora delar är kompatibelt
med Matlab. Det kan också användas som ett språk för satsvis
bearbetning.

Octave har omfattande verktyg för att lösa vanliga problem inom
numerisk linjär algebra, hitta rötter för ickelinjära ekvationer,
integrera normala funktioner, hantera polynom, och integrera ordinära
differential och differentialalgebraiska ekvationer. Det är lätt att
utvidga och anpassa via användardefinierade funktioner skrivna i
Octaves eget språk, och via dynamiskt laddade moduler skrivan i C++,
C, Fortran, eller andra språk.

%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):	Pliki nag³ówkowe i dodatkowa dokumentacja Octave
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and devel docs for Octave.

%description devel -l pl
Pliki nag³ówkowe i dodatkowa dokumentacja Octave.

%package -n xemacs-octave-mode-pkg
Summary:	XEmacs mode for Octave
Summary(pl):	Tryb edycji plików Octave dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-octave-mode-pkg
XEmacs mode for Octave.

%description -n xemacs-octave-mode-pkg -l pl
Tryb edycji plików Octave dla XEmacsa.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure \
	--with-g77 \
	--enable-dl \
	--enable-shared \
	--enable-static=no \
	--enable-rpath \
	--enable-lite-kernel

%{__make}
%{__make} -C doc/faq Octave-FAQ.info
%{__make} -C doc/liboctave liboctave.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	octincludedir=$RPM_BUILD_ROOT%{_includedir} \
	octlibdir=$RPM_BUILD_ROOT%{_libdir}

ln -sf %{_includedir}/%{name} $RPM_BUILD_ROOT%{_includedir}/%{name}-%{version}

install doc/liboctave/*.info* $RPM_BUILD_ROOT%{_infodir}
install doc/faq/*.info* $RPM_BUILD_ROOT%{_infodir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Numerics/%{name}.desktop

## xemacs-octave-mode-pkg
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
cp -a emacs/*.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode
# add otags script or not (additional Requires: ctags)???
#cp -a emacs/otags $RPM_BUILD_ROOT%{_bindir}
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/octave-mode/auto-autoloads.el
(autoload 'run-octave "octave-inf" nil t)
(autoload 'octave-help "octave-hlp" nil t)
(autoload 'octave-mode "octave-mod" nil t)
(setq auto-mode-alist
      (cons '("\\\\.m$" . octave-mode) auto-mode-alist))
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS THANKS PROJECTS
%doc emacs examples doc/{interpreter,faq}/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/octave
%{_infodir}/octave.info*
%{_infodir}/Octave-FAQ.info*
%{_mandir}/man1/*
%{_datadir}/octave
%{_applnkdir}/Scientific/Numerics/*

%files devel
%defattr(644,root,root,755)
%doc doc/refcard/refcard{-a4,}.* doc/liboctave/*.html
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}*
%{_infodir}/liboctave.info*

%files -n xemacs-octave-mode-pkg
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/lisp/*
