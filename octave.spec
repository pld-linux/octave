Summary:	GNU Octave -- a high-level language for numerical computations
Summary(pl):	GNU Octave -- jêzyk programowania do obliczeñ numerycznych
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
GNU Octave jest jêzykiem programowania wysokiego poziomu przeznaczonym
g³ównie do obliczeñ numerycznych. Octave jest w du¿ym stopniu kompatybilny z
jêzykiem Matlab. Pracowaæ mo¿na wprost z linii poleceñ lub uruchamiaæ
programy stworzone za pomoc± zewnêtrznego edytora.


%package devel
Summary:	Header files and devel docs for Octave
Summary(pl):    Pliki nag³ówkowe i dodatkowa dokumentacja Octave 
Group:          Development/Libraries
Group(pl):      Programowanie/Biblioteki                                                                        

%description -l pl devel
Pliki nag³ówkowe i dodatkowa dokumentacja Octave


%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
autoconf
CFLAOCGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS" \
FFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr \
	--with-g77 \
	--enable-dl \
	--enable-shared \
	--enable-rpath \
	--enable-lite-kernel

make octlibdir=%{_libdir} octincludedir=%{_includedir}/octave
make -C doc/faq Octave-FAQ.info
make -C doc/liboctave liboctave.info

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	octlibdir=$RPM_BUILD_ROOT%{_libdir}
	octincludedir=$RPM_BUILD_ROOT%{_includedir}/octave

mv -f $RPM_BUILD_ROOT%{_bindir}/octave-%{version} $RPM_BUILD_ROOT/usr/bin/octave

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*so

install doc/liboctave/*.info* $RPM_BUILD_ROOT%{_infodir}
install doc/faq/*.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf $RPM_BUILD_ROOT%{_datadir}/{info/*.info*,man/man1/*} \
	BUGS NEWS* PROJECTS README README.Linux ChangeLog* ROADMAP \
	SENDING-PATCHES THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/install-info %{_infodir}/%{name}.info.gz /etc/info-dir
/sbin/install-info %{_infodir}/Octave-FAQ.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/%{name}.info.gz /etc/info-dir
	/sbin/install-info --delete %{_infodir}/Octave-FAQ.info.gz /etc/info-dir
fi

%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/lib%{name}.info.gz /etc/info-dir

%preun devel
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/lib%{name}.info.gz /etc/info-dir
fi


%files
%defattr(644,root,root,755)
%doc *.gz emacs examples doc/{interpreter,faq}/*.html
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*so
%attr(755,root,root) /usr/libexec/octave
%{_infodir}/octave.info*
%{_infodir}/Octave-FAQ.info*
%{_mandir}/man1/*
%{_datadir}/octave

%files devel
%defattr(644,root,root,755)
%doc doc/refcard/refcard{-a4,}.* doc/liboctave/*.html
%{_includedir}/%{name}-%{version}
%{_infodir}/liboctave.info*
    
%changelog
* Wed May 12 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- added rebuilding additional info files from patched .texi
- removed READLINE_DIR="" LIBREADLINE="-lreadline" from make.
 
* Tue May 11 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
- added more html doc (I like it... :) )
- added a4 refcard to devel doc
- Octave-FAQ.info entry
- liboctave.info entry 
- divided into octave, octave-devel

* Sun May  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- now package is FHS 2.0 compliant,
- added passing $RPM_OPT_FLAGS to fortran compile options (FFLAGS),
- link with system readline instead static included with octave,
- added gzipping %doc and man pages,
- added using %%{_target_platform} macro in ./configure parameters,
- added LDFLAGS="-s" to ./configure enviroment,
- install libraries in proper path (/usr/lib),
- changed permission to 755 on shared libraries,
- added stripping shared libs,
- added BuildPrereq: readline-devel, ncurses-devel, egcs-g77.

* Fri Apr 30 1999 Rafa³ Kleger-Rudomin <klakier@pg.gda.pl>
  [2.0.14-1]
- Adapt for PLD.

* Thu Jun 11 1998 Andrew Veliath <andrewtv@usa.net>
- Add %attr, build as user.

* Mon Jun 1 1998 Andrew Veliath <andrewtv@usa.net>
- Add BuildRoot, installinfo, require gnuplot, description from
  Octave's web page, update to Octave 2.0.13.

- Adapt from existing spec file.
