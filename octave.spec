Summary:	GNU Octave -- a high-level language for numerical computations
Summary(pl):	GNU Octave -- j�zyk programowania do oblicze� numerycznych
Name:		octave
Version:	2.0.14
Release:	1
Copyright:	GPL
Group:		Applications/Math
Group(pl):	Aplikacje/Matematyczne
Source:		ftp://ftp.che.wisc.edu/pub/octave/%{name}-%{version}.tar.bz2
Patch0:		octave-liboctave.info.patch
Patch1:		octave-Octave-FAQ.info.patch
URL:		http://www.che.wisc.edu/octave/
BuildPrereq:	libstdc++-devel
BuildPrereq:	ncurses-devel
BuildPrereq:	readline-devel
BuildPrereq:	flex
BuildPrereq:	bison
BuildPrereq:	egcs-g77
Requires:	gnuplot
BuildRoot:	/tmp/%{name}-%{version}-root

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for solving
linear and nonlinear problems numerically, and for performing other
numerical experiments using a language that is mostly compatible with
Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating ordinary
functions, manipulating polynomials, and integrating ordinary differential
and differential-algebraic equations. It is easily extensible and
customizable via user-defined functions written in Octave's own language, or
using dynamically loaded modules written in C++, C, Fortran, or other
languages.

%description -l pl
GNU Octave jest j�zykiem programowania wysokiego poziomu przeznaczonym
g��wnie do oblicze� numerycznych. Octave jest w du�ym stopniu kompatybilny z
j�zykiem Matlab. Pracowa� mo�na wprost z linii polece� lub uruchamia�
programy stworzone za pomoc� zewn�trznego edytora.



%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):    Pliki nag��wkowe i dodatkowa dokumentacja Octave 
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki                                                                        


%description -l pl devel
Pliki nag��wkowe i dodatkowa dokumentacja Octave


%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CFLAOCGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS" \
FFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr \
	--with-g77 \
	--enable-dl \
	--enable-shared \
	--enable-rpath \
	--enable-lite-kernel
make READLINE_DIR="" LIBREADLINE="-lreadline" octlibdir=/usr/lib

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr
	octlibdir=$RPM_BUILD_ROOT/usr/lib

strip --strip-unneeded $RPM_BUILD_ROOT/usr/lib/lib*so

install doc/liboctave/*.info* $RPM_BUILD_ROOT/usr/share/info
install doc/faq/*.info* $RPM_BUILD_ROOT/usr/share/info
gzip -9nf $RPM_BUILD_ROOT/usr/share/{info/*.info*,man/man1/*} \
	BUGS NEWS* PROJECTS README README.Linux ChangeLog* ROADMAP \
	SENDING-PATCHES THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info /usr/share/info/%{name}.info.gz /etc/info-dir
/sbin/install-info /usr/share/info/Octave-FAQ.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/share/info/%{name}.info.gz /etc/info-dir
	/sbin/install-info --delete /usr/share/info/Octave-FAQ.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig


%post devel
/sbin/install-info /usr/share/info/lib%{name}.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete /usr/share/info/lib%{name}.info.gz /etc/info-dir
fi


%files
%defattr(644,root,root,755)
%doc *.gz emacs examples doc/{interpreter,faq}/*.html
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/lib*so
%attr(755,root,root) /usr/libexec/octave
/usr/share/info/octave.info*
/usr/share/info/Octave-FAQ.info*
/usr/share/man/man1/*
/usr/share/octave

%files devel
%defattr(644,root,root,755)
%doc doc/refcard/refcard{-a4,}.* doc/liboctave/*.html
/usr/include/%{name}-%{version}
/usr/share/info/liboctave.info*
    
%changelog
* Tue May 11 1999 Rafa� Kleger-Rudomin <klakier@pg.gda.pl>
- added more html doc (I like it... :) )
- added a4 refcard to devel doc
- Octave-FAQ.info entry
- liboctave.info entry 
- divided into octave, octave-devel

* Sun May  9 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- now package is FHS 2.0 compliat,
- added passing $RPM_OPT_FLAGS to fortran compile options (FFLAGS),
- link with system readline instead static included with octave,
- added gzipping %doc and man pages,
- added using %%{_target} macro in ./configure parameters,
- added LDFLAGS="-s" to ./configure enviroment,
- install libraries in proper path (/usr/lib),
- changed permission to 755 on shared libraries,
- added stripping shared libs,
- added BuildPrereq: readline-devel, ncurses-devel, egcs-g77.

* Fri Apr 30 1999 Rafa� Kleger-Rudomin <klakier@pg.gda.pl>
  [2.0.14-1]
- Adapt for PLD.

* Thu Jun 11 1998 Andrew Veliath <andrewtv@usa.net>
- Add %attr, build as user.

* Mon Jun 1 1998 Andrew Veliath <andrewtv@usa.net>
- Add BuildRoot, installinfo, require gnuplot, description from
  Octave's web page, update to Octave 2.0.13.

- Adapt from existing spec file.
