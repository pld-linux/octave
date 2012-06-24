Summary:	GNU Octave - a high-level language for numerical computations
Summary(cs):	GNU Octave - vy��� programovac� jazyk pro numerick� v�po�ty
Summary(da):	GNU Octave - et h�jniveausprog for numeriske beregninger
Summary(de):	GNU Octave - eine h�here Programmiersprache f�r nummerische Berechnungen
Summary(es):	GNU Octave - lenguaje de alto nivel para c�lculos num�ricos
Summary(fr):	GNU Octave - langage haut niveau pour les calculs num�riques
Summary(it):	GNU Octave - linguaggio di alto livello per calcoli numerici
Summary(ja):	GNU Octave ���ͷ׻��Ѥι�����
Summary(ko):	GNU Octave ��� ����� ���� ������ ��� 
Summary(no):	GNU Octave - et h�yniv�spr�k for numeriske beregninger
Summary(pl):	GNU Octave - j�zyk programowania do oblicze� numerycznych
Summary(pt):	GNU Octave - uma linguagem de alto n�vel para c�lculos num�ricos
Summary(pt_BR):	GNU Octave - um programa para c�lculo num�rico e matricial
Summary(ru):	GNU Octave - ���� �������� ������ ��� ���������� �������������� ��������
Summary(sv):	GNU Octave - ett h�gninv�spr�k f�r numeriska ber�kningar
Summary(zh_CN):	GNU Octave - �������ּ���ĸ߼����ԡ�
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
GNU Octave je vy��� programovac� jazyk, prim�rn� ur�en� pro numerick�
v�po�ty. Poskytuje pohodln� rozhran� p��kazov�ho ��dku pro numerick�
�e�en� line�rn�ch a neline�rn�ch probl�m� a pro prov�d�n� jin�ch
numerick�ch experiment� za pou��v�n� jazyku, kter� je t�m�� pln�
kompatibiln� s programem Matlab. M��e b�t pou��v�n i jako d�vkov�
jazyk.

Octave m� rozs�hl� n�stroje pro �e�en� obvykl�ch numerick�ch �loh v
line�rn� algeb�e, nalezen� ko�en� neline�rn�ch rovnic, integrov�n�
b�n�ch funkc�, polynomi�ln� manipulace, integrov�n� z�kladn�ch
diferenci�ln�ch a algebraicko-diferenci�ln�ch rovnic. Je jednodu�e
roz�i�iteln� a p�izp�sobiteln� pomoc� u�ivatelsky definovan�ch funkc�
napsan�ch v jeho vlastn�m jazyku. M��e pou��vat dynamicky zav�d�n�
moduly napsan� v jazyc�ch C++, C, Fortran a jin�ch.

%description -l da
GNU Octave er et h�gniveausprog, hovedsakligen beregnet til for
numeriska beregningar. Det har et bekv�mt kommandoradsgr�nseflade for
at l�sa linj�ra og ickelinj�ra problem numeriskt, og for at utf�ra
andra numeriske experiment med et sprog som i stora dele er
kompatibelt med Matlab. Det kan ogs� bruges som et sprog for satsvis
bearbejdning.

Octave har omfattende v�rkt�j for at l�sa almindelige problem inom
numerisk linj�r algebra, finde r�tter for ickelinj�ra ekvationer,
integrere normala funktioner, behandle polynom, og integrere ordin�re
differential og differentialalgebraiska ekvationer. Det er let at
utvidga og anpassa via brugerdefinierede funktioner skrivna i Octaves
eget sprog, og via dynamisk laddade moduler skriven i C++, C, Fortran,
eller andra sprog.

%description -l de
GNU Octave ist eine High-Level-Programmiersprache, die haupts�chlich
f�r nummerische Berechnungen vorgesehen ist. Sie verf�gt �ber eine
benutzerfreundliche Befehlszeilenoberfl�che zur nummerischen L�sung
von linearen und nichtlinearen Aufgaben und zum Ausf�hren weiterer
nummerischer Experimente unter Verwendung einer Programmiersprache,
die gr��tenteils mit Matlab kompatibel ist. Die Programmiersprache
kann auch als Batch-orientierte Sprache verwendet werden.

Octave verf�gt �ber umfangreiche Tools zum L�sen allgemeiner
nummerischer linearer algebraischer Aufgaben, zum Ermitteln der
L�sungen von nichtlinearen Gleichungen, zum Integrieren gew�hnlicher
Funktionen, zum Bearbeiten von Polynomen und zum Integrieren
gew�hnlicher Differential- und Differential-algebraischer Gleichungen.
Octave kann mit benutzerdefinierten Funktionen, die in der speziellen
Programmiersprache von Octave geschrieben sind, oder mit dynamisch
geladenen, in C++, C, Fortran oder einer anderen Programmiersprache
geschriebenen Modulen erweitert und angepasst werden.

%description -l es
GNU Octave lenguaje de alto nivel, pensado para c�lculos num�ricos.
Provee un interfaz de l�nea de comando para resolver problemas
lineales y no lineales num�ricamente, y para realizar otros
experimentos num�ricos usando un lenguaje casi compatible con Matlab.
Puede utilizarse tambi�n fuera de la l�nea de comandos.

Octave tiene herramientas para resolver problemas num�ricos de algebra
lineal com�n, encontrar raices de ecuaciones no-lineales, integraci�n
de funciones ordinarias, manipulaci�n de polinomios, e integrar
ecuaciones diferenciales ordinarias y algebra�cas diferenciales. Es
facilmente extensible y configurable via funciones de usuario escritas
en el lenguaje Octave, o usando m�dulos din�micos cargables escritos
en C++, C, Fortran u otros lenguajes.

%description -l fr
GNU Octave est un langage haut niveau con�u pour le calcul num�rique.
Il offre une interface de ligne de commande pratique permettant de
r�soudre num�riquement des probl�mes lin�aires et non lin�aires et
d'effectuer d'autres exp�riences num�riques � l'aide d'un langage
presque totalement compatible avec Matlab. Il peut �galement �tre
utilis� comme langage � orientation par lots.

Octave comporte des outils �tendus permettant de r�soudre des
probl�mes communs d'alg�bre lin�aire num�rique, en trouvant les
racines d'�quations non lin�aires, en int�grant des fonctions
ordinaires, en manipulant des polyn�mes et en int�grant des �quations
diff�rentielles ordinaires et diff�rentielles alg�briques. Il est
facilement extensible et personnalisable au moyen de fonctions
d�finies par l'utilisateur, �crites dans le langage d'Octave, ou �
l'aide de modules charg�s dynamiquement, �crits en C++, C, Fortran ou
autres langages.

%description -l it
GNU Octave � un linguaggio di alto livello per il calcolo numerico.
Fornisce una interfaccia basata sulla linea di comando per la
risoluzione numerica di problemi lineari e non lineari e per eseguire
altri esperimenti numerici usando un linguaggio per lo pi� compatibile
con Matlab. Pu� inoltre essere utilizzato come linguaggio orientato al
batch.

Octave possiede vari tool per risolvere problemi di algebra lineare,
per la ricerca di radici di equazioni non lineari, per il calcolo di
integrali di funzioni, per l'elaborazione di polinomi, per le
equazioni differenziali ordinarie e algebriche. Pu� essere facilmente
esteso e personalizzato tramite nuove funzioni definite dall'utente e
scritte nel linguaggio di Octave o tramite moduli caricati in modo
dinamico scritti in C, C++, Fortran o altri linguaggi.

%description -l ja
GNU Octave �ϡ���Ȥ��ƿ��ͷ׻�����Ū�Ȥ������٥����Ǥ���
GNU Octave �ϡ�����/��������������Ū�˲򤤤��ꡢMatlab 
�Ȥ�����ʬ�θߴ�������ä��������Ѥ��Ƥ���¾�ο���Ū�¸����
�ä��ꤹ�뤿��������ʥ��ޥ�ɥ饤�󥤥󥿡��ե��������󶡤��ޤ���
�Хå��ظ��θ���Ȥ��ƻ��Ѥ��뤳�Ȥ�Ǥ��ޤ���Octave �ϡ�
���̤ο���������������򤤤��ꡢ�������������κ��򸫤Ĥ����ꡢ
�̾�δؿ�����ʬ�����ꡢ¿�༰�������ꡢ����ʬ�����������
��ʬ����������ʬ�����ꤹ�뤿��ι��Ϥʥġ���������Ƥ��ޤ���Octave 
�ȼ��θ���ǽ񤫤줿�桼��������δؿ��䡢C++��C��Fortlan������¾��
����ǽ񤫤줿ưŪ�˥��ɤ����⥸�塼�����Ѥ���С��ưפ˳�ĥ
����ӥ������ޥ������뤳�Ȥ��Ǥ��ޤ���

%description -l pl
GNU Octave jest j�zykiem programowania wysokiego poziomu przeznaczonym
g��wnie do oblicze� numerycznych. Octave jest w du�ym stopniu
kompatybilny z j�zykiem Matlab. Pracowa� mo�na wprost z linii polece�
lub uruchamia� programy stworzone za pomoc� zewn�trznego edytora.

%description -l pt
O Octave da GNU � uma linguagem de alto n�vel, vocacionada
principalmente para o c�lculo num�rico. Oferece uma interface de linha
de comandos para resolver problemas lineares e n�o-lineares
numericamente, e para realizar outras experi�ncias num�ricas usando
uma linguagem que � relativamente compat�vel com o Matlab. Pode tamb�m
ser usado como uma linguagem orientada por lotes.

O Octave tem ferramentas extensivas para resolver problemas comuns de
�lgebra linear, descobrir as raizes de equa��es n�o-lineares, integrar
fun��es ordin�rias, manipular polin�mios e integrar equa��es
diferenciais ordin�rias e diferenciais alg�bricas. � facilmente
extens�vel e personaliz�vel atrav�s de fun��es definidas pelo
utilizador, escritas na pr�pria linguagem do Octave, ou usando m�dulos
carregados dinamicamente e feitos em C, C++, Fortran ou outras
linguagens."

%description -l pt_BR
GNU Octave - Um programa de c�lculo num�rico e matricial. Possui
linguagem de alto n�vel e ambiente interativo para computa��o num�rica
semelhantes ao do Matlab.

%description -l ru
GNU Octave - ��� ���� �������� ������, ��������������� ��� ����������
�������������� ����������. �� ������������� ������� ����������
��������� ��� ������� �������� � ���������� �������������� ����� � ���
���������� ������ �������������� �������������, ��������� ����, �
����������� ������� ����������� � Mathlab.

����� ����, Octave ����� �������������� ��� �������� ��������� � �����
�������� ���������� ��� ������� �������� �������������� �����,
���������� ������ ���������� ���������, �������������� �������, ������
� ���������� � ������� ��������� ���������������� ���������. ����
����� ����� ��������� ��� ������ ���������� ����� Octave ��� ���������
����������� ����������� ������, ���������� �� ������ C, C++, ������� �
��.

%description -l sv
GNU Octave �r ett h�gniv�spr�k, huvudsakligen avsett f�r numeriska
ber�kningar. Det har ett bekv�mt kommandoradsgr�nssnitt f�r att l�sa
linj�ra och ickelinj�ra problem numeriskt, och f�r att utf�ra andra
numeriska experiment med ett spr�k som i stora delar �r kompatibelt
med Matlab. Det kan ocks� anv�ndas som ett spr�k f�r satsvis
bearbetning.

Octave har omfattande verktyg f�r att l�sa vanliga problem inom
numerisk linj�r algebra, hitta r�tter f�r ickelinj�ra ekvationer,
integrera normala funktioner, hantera polynom, och integrera ordin�ra
differential och differentialalgebraiska ekvationer. Det �r l�tt att
utvidga och anpassa via anv�ndardefinierade funktioner skrivna i
Octaves eget spr�k, och via dynamiskt laddade moduler skrivan i C++,
C, Fortran, eller andra spr�k.

%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):	Pliki nag��wkowe i dodatkowa dokumentacja Octave
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and devel docs for Octave.

%description devel -l pl
Pliki nag��wkowe i dodatkowa dokumentacja Octave.

%package -n xemacs-octave-mode-pkg
Summary:	XEmacs mode for Octave
Summary(pl):	Tryb edycji plik�w Octave dla XEmacsa
Group:		Applications/Editors/Emacs
Requires:	xemacs

%description -n xemacs-octave-mode-pkg
XEmacs mode for Octave.

%description -n xemacs-octave-mode-pkg -l pl
Tryb edycji plik�w Octave dla XEmacsa.

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
