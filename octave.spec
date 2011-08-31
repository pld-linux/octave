Summary:	GNU Octave - a high-level language for numerical computations
Summary(cs.UTF-8):	GNU Octave - vyšší programovací jazyk pro numerické výpočty
Summary(da.UTF-8):	GNU Octave - et højniveausprog for numeriske beregninger
Summary(de.UTF-8):	GNU Octave - eine höhere Programmiersprache für nummerische Berechnungen
Summary(es.UTF-8):	GNU Octave - lenguaje de alto nivel para cálculos numéricos
Summary(fr.UTF-8):	GNU Octave - langage haut niveau pour les calculs numériques
Summary(it.UTF-8):	GNU Octave - linguaggio di alto livello per calcoli numerici
Summary(ja.UTF-8):	GNU Octave 数値計算用の高級言語
Summary(ko.UTF-8):	GNU Octave 산술 계산을 위한 고차원 언어
Summary(nb.UTF-8):	GNU Octave - et høynivåspråk for numeriske beregninger
Summary(pl.UTF-8):	GNU Octave - język programowania do obliczeń numerycznych
Summary(pt.UTF-8):	GNU Octave - uma linguagem de alto nível para cálculos numéricos
Summary(pt_BR.UTF-8):	GNU Octave - um programa para cálculo numérico e matricial
Summary(ru.UTF-8):	GNU Octave - Язык высокого уровня для выполнения математических расчетов
Summary(sv.UTF-8):	GNU Octave - ett högninvåspråk för numeriska beräkningar
Summary(zh_CN.UTF-8):	GNU Octave - 用于数字计算的高级语言。
Name:		octave
Version:	3.4.2
Release:	2
Epoch:		2
License:	GPL v3+
Group:		Applications/Math
Source0:	http://ftp.gnu.org/gnu/octave/%{name}-%{version}.tar.bz2
# Source0-md5:	31c744ab4555a2bf04d5e644b93f9b51
Source1:	%{name}.desktop
Patch0:		%{name}-info.patch
Patch1:		%{name}-build.patch
URL:		http://www.octave.org/
BuildRequires:	AMD-devel
BuildRequires:	CAMD-devel
BuildRequires:	CCOLAMD-devel
BuildRequires:	CHOLMOD-devel
BuildRequires:	COLAMD-devel
BuildRequires:	CXSparse-devel
BuildRequires:	GraphicsMagick-c++-devel
BuildRequires:	UMFPACK-devel
BuildRequires:	arpack-devel >= 2.1-8
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
#BuildRequires:	bison >= 1.31
BuildRequires:	blas-devel
BuildRequires:	curl-devel
BuildRequires:	fftw3-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	flex >= 2.5.4
BuildRequires:	fltk-gl-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gcc-fortran >= 6:4.0
BuildRequires:	glpk-devel >= 4.14
#BuildRequires:	gperf >= 3.0.1
BuildRequires:	hdf5-devel >= 1.6.0
BuildRequires:	lapack-devel >= 3.1.1-3
BuildRequires:	libstdc++-devel >= 6:4.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pcre-devel
BuildRequires:	qhull-devel >= 2011.1
BuildRequires:	qrupdate-devel
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo-texi2dvi
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
Requires:	gnuplot
Suggests:	GraphicsMagick
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

%description -l cs.UTF-8
GNU Octave je vyšší programovací jazyk, primárně určený pro numerické
výpočty. Poskytuje pohodlné rozhraní příkazového řádku pro numerické
řešení lineárních a nelineárních problémů a pro provádění jiných
numerických experimentů za používání jazyku, který je téměř plně
kompatibilní s programem Matlab. Může být používán i jako dávkový
jazyk.

Octave má rozsáhlé nástroje pro řešení obvyklých numerických úloh v
lineární algebře, nalezení kořenů nelineárních rovnic, integrování
běžných funkcí, polynomiální manipulace, integrování základních
diferenciálních a algebraicko-diferenciálních rovnic. Je jednoduše
rozšiřitelný a přizpůsobitelný pomocí uživatelsky definovaných funkcí
napsaných v jeho vlastním jazyku. Může používat dynamicky zaváděné
moduly napsané v jazycích C++, C, Fortran a jiných.

%description -l da.UTF-8
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

%description -l de.UTF-8
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

%description -l es.UTF-8
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

%description -l fr.UTF-8
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

%description -l it.UTF-8
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

%description -l ja.UTF-8
GNU Octave は、主として数値計算を目的とした高レベル言語です。
GNU Octave は、線型/非線型問題を数値的に解いたり、Matlab
との大部分の互換性を持った言語を使用してその他の数値的実験を行
ったりするための便利なコマンドラインインターフェイスを提供します。
バッチ指向の言語として使用することもできます。Octave は、
共通の数値線型代数問題を解いたり、非線型方程式の根を見つけたり、
通常の関数を積分したり、多項式を操作したり、常微分方程式や代数
微分方程式を積分したりするための広範なツールを備えています。Octave
独自の言語で書かれたユーザー定義の関数や、C++、C、Fortlan、その他の
言語で書かれた動的にロードされるモジュールを使用すれば、容易に拡張
およびカスタマイズすることができます。

%description -l pl.UTF-8
GNU Octave jest językiem programowania wysokiego poziomu przeznaczonym
głównie do obliczeń numerycznych. Octave jest w dużym stopniu
kompatybilny z językiem Matlab. Pracować można wprost z linii poleceń
lub uruchamiać programy stworzone za pomocą zewnętrznego edytora.

%description -l pt.UTF-8
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

%description -l pt_BR.UTF-8
GNU Octave - Um programa de cálculo numérico e matricial. Possui
linguagem de alto nível e ambiente interativo para computação numérica
semelhantes ao do Matlab.

%description -l ru.UTF-8
GNU Octave - это язык высокого уровня, предназначенный для выполнения
математических вычислений. Он предоставляет удобный коммандный
интерфейс для решения линейных и нелинейных математических задач и для
проведения других арифметических экспериментов, используя язык, в
большенстве случаев совместимый с Mathlab.

Кроме того, Octave может использоваться для пакетной обработки и имеет
средства расширения для решения линейных алгебраических задач,
нахождения корней нелинейных уравнений, интегрирование функций, работу
с полиномами и решение различных дифференциальных уравнений. Язык
можно легко расширить при помощи собственно языка Octave или используя
динамически загружаемые модули, написанные на языках C, C++, Фортран и
др.

%description -l sv.UTF-8
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
Summary(pl.UTF-8):	Pliki nagłówkowe i dodatkowa dokumentacja Octave
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	hdf5-devel >= 1.6.0

%description devel
Header files and devel docs for Octave.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dodatkowa dokumentacja Octave.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-amd-includedir=%{_includedir}/amd \
	--with-camd-includedir=%{_includedir}/camd \
	--with-cholmod-includedir=%{_includedir}/cholmod \
	--with-colamd-includedir=%{_includedir}/colamd \
	--with-ccolamd-includedir=%{_includedir}/ccolamd \
	--with-cxsparse-includedir=%{_includedir}/cxsparse \
	--with-umfpack-includedir=%{_includedir}/umfpack \
	--enable-dl \
	--enable-shared \
	--enable-static=no \
	--enable-rpath=no

%{__make} \
	octincludedir=%{_includedir}/octave \
	octlibdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	octincludedir=%{_includedir}/octave \
	octlibdir=%{_libdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

# Create directory for add-on packages
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/packages
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/packages
touch $RPM_BUILD_ROOT%{_datadir}/%{name}/octave_packages

%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/www.octave.org-octave.desktop
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
/sbin/ldconfig
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README
%doc examples doc/{faq,interpreter}/*.{html,pdf} doc/refcard/refcard-a4.pdf
%attr(755,root,root) %{_bindir}/mkoctfile
%attr(755,root,root) %{_bindir}/mkoctfile-%{version}
%attr(755,root,root) %{_bindir}/octave
%attr(755,root,root) %{_bindir}/octave-%{version}
%attr(755,root,root) %{_libdir}/libcruft.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcruft.so.0
%attr(755,root,root) %{_libdir}/liboctave.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboctave.so.0
%attr(755,root,root) %{_libdir}/liboctinterp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboctinterp.so.0
%{_libdir}/octave
%{_infodir}/octave.info*
%{_infodir}/OctaveFAQ.info*
%{_mandir}/man1/mkoctfile.1*
%{_mandir}/man1/octave.1*
%{_datadir}/octave
%{_desktopdir}/octave.desktop

%files devel
%defattr(644,root,root,755)
%doc doc/liboctave/liboctave.{html,pdf}
%attr(755,root,root) %{_bindir}/octave-config
%attr(755,root,root) %{_bindir}/octave-config-%{version}
%attr(755,root,root) %{_libdir}/libcruft.so
%attr(755,root,root) %{_libdir}/liboctave.so
%attr(755,root,root) %{_libdir}/liboctinterp.so
%{_includedir}/%{name}*
%{_mandir}/man1/octave-config.1*
%{_infodir}/liboctave.info*
